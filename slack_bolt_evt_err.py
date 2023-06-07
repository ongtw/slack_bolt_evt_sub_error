import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler

#
# Code taken from https://api.slack.com/start/building/bolt-python
# - added dotenv to load secrets
#

# Load env vars
load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_SECRET = os.getenv("SLACK_SECRET")
PORT = 3000

# Init Slack app
bolt_app = App(token=SLACK_BOT_TOKEN, signing_secret=SLACK_SECRET)


# Start
if __name__ == "__main__":
    bolt_app.start(port=PORT)
