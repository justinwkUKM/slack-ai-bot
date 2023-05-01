# Ben: The AI Writing Assistant

Ben is a slack bot that helps you write various types of content using AI. Whether you need a cold email, a sales pitch, an Instagram caption, a summary, an AIDA model, a media campaign, or a code interpretation, Ben can help you draft, edit, or optimize your requests in a conversational way. Ben will use natural language processing and machine learning to generate professional and effective content for you.

![Screen Shot 2023-05-01 at 9 24 23 PM](https://user-images.githubusercontent.com/20006026/235457904-ac21d04b-e6bc-4e6b-a39f-2330a71a47ab.png)
## Part 1 — Slack Setup

#### 1. Create a new Slack app

- Choose an existing Slack workspace or create a new one.
- Go to [https://api.slack.com/apps](https://api.slack.com/apps) and sign in with your Slack account.
- Click "Create New App" and provide an app name and select your workspace as the development workspace. Click "Create App".

#### 2. Set up your bot

- Under the "Add features and functionality" section, click on "Bots".
- Click "Add a Bot User" and fill in the display name and default username. Save your changes.

#### 3. Add permissions to your bot

- In the left sidebar menu, click on "OAuth & Permissions".
- Scroll down to "Scopes" and add the required bot token scopes. For this example, you'll need at least `app_mentions:read`, `chat:write`, and `channels:history`.

#### 4. Install the bot to your workspace

- In the left sidebar menu, click on "Install App".
- Click "Install App to Workspace" and authorize the app.

#### 5. Retrieve the bot token

- After installation, you'll be redirected to the "OAuth & Permissions" page.
- Copy the "Bot User OAuth Access Token" (it starts with `xoxb-`). You'll need it for your Python script.

## Part 2 — Python Setup

#### 1. Set up your Python environment

- Install Python 3.6 or later (if you haven't already).
- Install the required packages: `slack-sdk`, `slack-bolt`, and `Flask`. You can do this using pip:

```other
pip install slack-sdk slack-bolt Flask
```

In addition to the steps you provided, you can also create a virtual environment to isolate the dependencies of your Python app from other projects on your machine. Here are the steps to create a virtual environment using `venv` or `conda` and install the required packages:

Using `venv`:

```bash
python3 -m venv myenv
source myenv/bin/activate
pip install slack-sdk slack-bolt Flask
```

Using `conda`:

```other
conda create --name myenv python=3.8
conda activate myenv
pip install slack-sdk slack-bolt Flask
```

#### 2. Create the Python script with Flask

- Create a new Python file (e.g., `app.py`) and insert the code from [`app.py`](https://github.com/daveebbelaar/langchain-experiments/blob/main/slack/app.py) in this repository.
- If you want to use a free version, you can explore the others supported [LangChain's Model](https://python.langchain.com/en/latest/modules/models/llms/integrations.html).

#### 3. Set the environment variable in the .env file

- Create a .env file in your project directory and add the following keys:

```yaml
SLACK_BOT_TOKEN = "xoxb-your-token"
SLACK_SIGNING_SECRET = "your-secret"
SLACK_BOT_USER_ID = "your-bot-id"
```

#### 4. Start your local FastAPI server

- Run the Python script in the terminal (macOS/Linux) or Command Prompt (Windows): `uvicorn app:api --reload --port 8000 --log-level warning` The server should start, and you'll see output indicating that it's running on [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Part 3 — Server Setup (Local)

#### 1. Expose your local server using ngrok

- If you haven't installed ngrok, you can download it from [https://ngrok.com/download](https://ngrok.com/download) or, on macOS, install it via Homebrew by running: `brew install ngrok`
- In a new terminal (macOS/Linux) or Command Prompt (Windows), start ngrok by running the following command: `ngrok http 5000`
- Note the HTTPS URL provided by ngrok (e.g., [https://yoursubdomain.ngrok.io](https://yoursubdomain.ngrok.io/)). You'll need it for the next step.

Remember that if you installed ngrok via Homebrew, you can run `ngrok http 5000` from any directory in the terminal. If you downloaded it from the website, navigate to the directory where ngrok is installed before running the command.

#### 2. Configure your Slack app with the ngrok URL

- Go back to your Slack app settings at [https://api.slack.com/apps](https://api.slack.com/apps).
- Click on "Event Subscriptions" in the left sidebar menu.
- Enable events and enter your ngrok URL followed by `/slack/events` (e.g., [https://yoursubdomain.ngrok.io/slack/events](https://yoursubdomain.ngrok.io/slack/events)).
- Scroll down to "Subscribe to bot events" and click "Add Bot User Event". Add the `app_mention` event and save your changes.

>**Note**
> Please note that every time you restart ngrok in the terminal, you have to update the URL in Slack — this is just for testing.

#### 3. Reinstall your Slack app to update the permissions

- In the left sidebar menu, click on "Install App".
- Click "Reinstall App to Workspace" and authorize the app.

#### 4. Add your bot to a Slack channel

- Type `/invite @bot-name` in the channel.

## Part 4 — Add Custom Functions

#### 1. Create a function to draft cold emails

- Create a new file called `functions.py` and insert the code from [`functions.py`](https://github.com/daveebbelaar/langchain-experiments/blob/main/slack/functions.py)
- Import the function in your `app.py` file with `from functions import draft_email`.
- And update the `handle_mentions` function.

## How to use Ben

To use Ben, you need to install the slack app from [here](https://slack.com/apps/A01U8RZLZJQ-ben-the-ai-writing-assistant). Once you have installed the app, you can invite Ben to any channel or direct message by typing `/invite @Ben`. You can also start a conversation with Ben by typing `@Ben` in any channel or direct message.

To request Ben to write something for you, you need to follow this format:

`Ben advertise: a new type of energy drink targeting young adults aged 18-30. The name of the drink is "Wolf"`

For example:

`@Ben cold_email: web design services`

`@Ben instagaram: write an Instagram caption about my new book called 'the game of prawns'`

`@Ben write a summary of this article`

## Features of Ben

Ben can write various types of content for different purposes and platforms. Here are some examples of what Ben can do:

- Cold emails: Ben can help you write personalized and engaging emails to potential customers or clients. Ben will use best practices and proven templates to craft your email. You can also ask Ben to optimize your email for open rate, click rate, or reply rate.
- Email Replies: You can ask Ben to draft, edit, or optimize your emails in a conversational way. Ben will use natural language processing and machine learning to generate professional and effective emails for you. 
- Sales pitch: Ben can help you write persuasive and compelling pitches to sell your product or service. Ben will use the AIDA model (Attention, Interest, Desire, Action) to structure your pitch. You can also ask Ben to optimize your pitch for clarity, urgency, or value proposition.
- Instagram captions: Ben can help you write catchy and creative captions for your Instagram posts. Ben will use hashtags, emojis, and keywords to make your captions stand out. You can also ask Ben to optimize your captions for engagement, reach, or conversions.
- Summaries: Ben can help you write concise and informative summaries of any text. Ben will use natural language understanding and summarization techniques to extract the main points and key details from your text. You can also ask Ben to optimize your summaries for length, readability, or relevance.
- AIDA models: Ben can help you write AIDA models for any product or service. AIDA stands for Attention, Interest, Desire, Action, and it is a framework for writing persuasive copy. Ben will generate each component of the AIDA model based on your input. You can also ask Ben to optimize your AIDA models for specificity, emotion, or credibility.
- Media campaigns: Ben can help you write media campaigns for any platform or channel. Media campaigns are strategic plans for delivering a message to a target audience. Ben will generate the objectives, strategies, tactics, and metrics for your media campaign based on your input. You can also ask Ben to optimize your media campaigns for impact, efficiency, or alignment.
- Code interpretations: Ben can help you write code interpretations for any programming language or framework. Code interpretations are explanations of what the code does and how it works. Ben will use natural language generation and code analysis to generate clear and accurate code interpretations based on your input. You can also ask Ben to optimize your code interpretations for simplicity, accuracy, or completeness.

## Why choose Ben

Ben is more than just a writing tool. He is an AI writing assistant that can interact with you in a natural and friendly way. He can understand your needs and preferences and adapt his writing style accordingly. He can also give you feedback and suggestions to improve your writing skills.

Ben is fast and reliable. He can generate high-quality content in seconds and deliver it to you in slack. He can also handle multiple requests at the same time and work with different types of content.

Ben is affordable and accessible. He is free to use for up to 10 requests per month.
