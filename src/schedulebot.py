import os

import discord
from discord.ext import commands
import config
from admins import admin_list

class ScheduleBot():

    def __init__(self, client, admins):
        self.config = config
        self.admins = admins
        self.client = client
        self.on_ready = self.client.event(self.on_ready)

    def start_bot(self):
        self.client.run(config.bot_token)

    def load_cogs(self):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                print("Loaded Cog: ", f'cogs.{filename[:-3]}')
                self.client.load_extension(f'cogs.{filename[:-3]}')

    #admin only bool function
    def is_admin(ctx):
        is_admin = False
        for admin in self.admins:
            if ctx.message.author.id == admin:
                is_admin = True
        return is_admin

    #ready prompt
    async def on_ready(self):
        print("Scheduler Bot is ready.")
        print("Logged in as: ", self.client.user)
        print("ID: ", self.client.user.id)

    #load commands
    @commands.command()
    @commands.check(is_admin)
    async def load(ctx, extension):
        self.client.load_extension(f'cogs.{extension}')

    #unload commands
    @commands.command()
    @commands.check(is_admin)
    async def unload(ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')

    #reload commands
    @commands.command()
    @commands.check(is_admin)
    async def reload(ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')
        self.client.load_extension(f'cogs.{extension}')

def main():
    client = commands.Bot(command_prefix = config.command_prefix)
    bot = ScheduleBot(client, admin_list)
    bot.load_cogs() # load cogs before starting the bot
    bot.start_bot()

if __name__ == '__main__':
    main()
