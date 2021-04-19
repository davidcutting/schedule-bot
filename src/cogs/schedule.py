import discord
from discord.ext import commands
import config

import csv
from datetime import datetime
from datetime import timedelta
import threading

class Schedule(commands.Cog):

    def __init__(self, client):
        self.client = client
        now = datetime.now()
        self.notif_at = now.replace(day=now.day, hour=now.hour, minute=now.minute+1, second=0, microsecond=0)
        delay = (self.notif_at - datetime.now()).total_seconds()
        self.timer = threading.Timer(delay, self.notify)
        self.timer.start()

    async def notify(self):
        chan = bot.get_channel(config.notif_channel)
        await chan.send('<@!{}> Reminder notification!'.format(config.notif_group))

def setup(client):
    client.add_cog(Schedule(client))
