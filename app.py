import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_bolt.adapter.flask import SlackRequestHandler
from slack_bolt import App
from dotenv import find_dotenv, load_dotenv
from flask import Flask, request
from functions import draft_email, summary, pythonify, javascript, linux, advertise, instagram, aida, media_campaign, sales_pitch, cold_email

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Set Slack API credentials
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_SIGNING_SECRET = os.environ["SLACK_SIGNING_SECRET"]
SLACK_BOT_USER_ID = os.environ["SLACK_BOT_USER_ID"]

# Initialize the Slack app
app = App(token=SLACK_BOT_TOKEN)

# Initialize the Flask app
# Flask is a web application framework written in Python
flask_app = Flask(__name__)
handler = SlackRequestHandler(app)


def get_bot_user_id():
    """
    Get the bot user ID using the Slack API.
    Returns:
        str: The bot user ID.
    """
    try:
        # Initialize the Slack client with your bot token
        slack_client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
        response = slack_client.auth_test()
        return response["user_id"]
    except SlackApiError as e:
        print(f"Error: {e}")


def my_function(text):
    """
    Custom function to process the text and return a response.
    In this example, the function converts the input text to uppercase.

    Args:
        text (str): The input text to process.

    Returns:
        str: The processed text.
    """
    response = text.upper()
    return response


@app.event("app_mention")
def handle_mentions(body, say):
    """
    Event listener for mentions in Slack.
    When the bot is mentioned, this function processes the text and sends a response.

    Args:
        body (dict): The event data received from Slack.
        say (callable): A function for sending a response to the channel.
    """
    text = body["event"]["text"]

    mention = f"<@{SLACK_BOT_USER_ID}>"
    text = text.replace(mention, "").strip()

    say("Sure, I'll get right on that!")
    if text.lower().startswith('translate:'):
        print('translate')
        response = my_function(text)
    elif text.lower().startswith('outline:'):
        print('outline')
        response = my_function(text)
    elif text.lower().startswith('blog:'):
        print('blog')
        response = my_function(text)
    elif text.lower().startswith('timeoff:'):
        print('timeoff')
        response = my_function(text)
    elif text.lower().startswith('complaint:'):
        print('complaint')
        response = my_function(text)
    elif text.lower().startswith('creative:'):
        print('creative')
        response = my_function(text)
    elif text.lower().startswith('summarize:'):
        text = text.replace("summarize:", "").strip()
        print('summarize')
        response = summary(text)
    elif text.lower().startswith('python:'):
        text = text.replace("python:", "").strip()
        print('python')
        response = pythonify(text)
    elif text.lower().startswith('javascript:'):
        text = text.replace("javascript:", "").strip()
        print('javascript')
        response = javascript(text)
    elif text.lower().startswith('linux:'):
        text = text.replace("linux:", "").strip()
        print('linux')
        response = linux(text)
    elif text.lower().startswith('advertise:'):
        text = text.replace("advertise:", "").strip()
        print('advertise')
        response = advertise(text)
    elif text.lower().startswith('aida:'):
        text = text.replace("aida:", "").strip()
        print('aida')
        response = aida(text)
    elif text.lower().startswith('instagram:'):
        text = text.replace("instagram:", "").strip()
        print('instagram')
        response = instagram(text)
    elif text.lower().startswith('sales_pitch:'):
        text = text.replace("sales_pitch:", "").strip()
        print('sales_pitch')
        response = sales_pitch(text)
    elif text.lower().startswith('cold_email:'):
        text = text.replace("cold_email:", "").strip()
        print('cold_email')
        response = cold_email(text)
    elif text.lower().startswith('media_campaign:'):
        text = text.replace("media_campaign:", "").strip()
        print('media_campaign')
        response = media_campaign(text)
    else:
      response = draft_email(text)
    say(response)


@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    """
    Route for handling Slack events.
    This function passes the incoming HTTP request to the SlackRequestHandler for processing.

    Returns:
        Response: The result of handling the request.
    """
    return handler.handle(request)


# Run the Flask app
if __name__ == "__main__":
    flask_app.run(port=8000)