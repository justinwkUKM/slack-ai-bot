from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import find_dotenv, load_dotenv
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

load_dotenv(find_dotenv())


def draft_email(user_input, name="Waqas"):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1)

    template = """
    
    You are Ben, a helpful assistant that drafts an email reply based on provided input, either email or user input or both.
    
    Your goal is to help the user quickly create a perfect email reply.
    
    Keep your reply short and to the point and mimic the style of the email so you reply in a similar manner to match the tone.
    
    Start your reply by saying: "Hi {name}, here's a draft for your reply:". And then proceed with the reply on a new line.
    
    Make sure to sign of with {signature}.
    
    """

    signature = f"Kind regards, \n\{name}"
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = "Here's the email to reply to and consider any other comments from the user for reply as well: {user_input}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(user_input=user_input, signature=signature, name=name)

    return response

def summary(user_input):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1)

    template = """
    
    You are Ben, a helpful assistant that Summarize the following content {user_input}
    
    Your goal is to help the user quickly create a perfect summary.
    
    """

    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = ""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(user_input=user_input)

    return response

def pythonify(user_input):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1)

    template = """
    
    I want you to act like a Python interpreter. I will give you Python code, and you will execute it. Do not provide any explanations. 
    Do not respond with anything except the output of the code. The code is: “{user_input}”. 
    If you dont understand the code, then express your yourself. 
    Highlght the error if any.
    
    """

    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = ""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(user_input=user_input)

    return response

def javascript(user_input):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1)

    template = """
    
    I want you to act as a javascript console. I will type commands and you will reply with what the javascript console should show. 
    I want you to only reply with the terminal output inside one unique code block, and nothing else. do not write explanations. 
    Do not respond with anything except the output of the code. The code is: “{user_input}”.
    do not type commands unless I instruct you to do so. when I need to tell you something in English, I will do so by putting text inside curly brackets after the code. 
    If you dont understand the code, then express your yourself. 

    """

    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = ""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(user_input=user_input)

    return response

def linux(user_input):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1)

    template = """
    
    I want you to act as a Linux terminal. I will type commands and you will reply with what the terminal should show. I want you to only reply with the terminal output inside one unique code block, and nothing else. do not write explanations. do not type commands unless I instruct you to do so. when I need to tell you something in English, I will do so by putting text inside curly brackets. 
    my first command is : {user_input}
    If you dont understand the command, then express your yourself. 

    
    """

    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = ""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(user_input=user_input)

    return response

def advertise(user_input):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1)

    template = """
    
    I want you to act as an advertiser. You will create a campaign to promote a product or service of your choice. 
    You will choose a target audience, develop key messages and slogans, select the media channels for promotion, and decide on any additional activities needed to reach your goals. 
    My first suggestion request is : {user_input}
    Everything you suggest should be SEO optimized
    """

    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = ""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(user_input=user_input)

    return response

def aida(user_input):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1)

    template = """
    
    I want you to act as an marketing expert. 
    Write an AIDA for : {user_input}
    Add some emojis to make your reply interesting.
    
    """

    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = ""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(user_input=user_input)

    return response

def instagram(user_input):
    chat = ChatOpenAI(model_name="gpt-4", temperature=1)

    template = """
    
    I want you to act as an content creation expert. 
    Write an attractive SEO Optimized Instagram Caption for : {user_input}
    Add some emojis to make your reply interesting.

    
    """

    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = ""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(user_input=user_input)

    return response

def media_campaign(user_input):
    chat = ChatOpenAI(model_name="gpt-4", temperature=1)

    template = """
    
    Create a 3-month social media campaign calendar for our product with the goal to {user_input} and mention the channels we should focus on.
    Add some emojis to make your reply interesting.
   
    """

    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = ""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(user_input=user_input)

    return response

def cold_email(user_input, name='Waqas'):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1)

    template = """
    
    You are Ben, a helpful assistant that is an exprt in drafting cold emails based on provided input.
    
    Your goal is to help the user quickly create a perfect influencing cold email.    
    
    Start your reply by saying: "Hi {name}, here's a draft for your cold email:". And then proceed with the reply on a new line.
    
    Make sure to sign of with {signature}.

    
    """
    signature = f"Kind regards, \n\{name}"
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = ""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(user_input=user_input, signature=signature, name=name)

    return response

def sales_pitch(user_input):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1)

    template = """
    
    Write a creative sales pitch about {user_input}.
    Add some emojis to make your reply interesting.
    
    
    """

    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = ""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(user_input=user_input)

    return response