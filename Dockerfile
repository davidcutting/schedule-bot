FROM python:3.8
WORKDIR /schedule-bot

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY src/ .

CMD [ "python3", "./schedulebot.py" ]
