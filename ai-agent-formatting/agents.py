from scrapper import get_text_from_url
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_openai import AzureChatOpenAI
from langchain.tools import tool
import os
from dotenv import load_dotenv

load_dotenv()

def get_response_from_openai(message):

    llm = AzureChatOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_API_BASE"),
        deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        temperature=0.0,
        max_tokens=1000
    )

    response = llm.invoke(message)
    return response

@tool
def documentation_tool (url: str, question: str) -> str:
    """
    This tool takes a URL and a question, retrieves the text from the URL,
    and returns an answer to the question based on the retrieved text.
    """

    context = get_text_from_url(url)

    messages = [
        SystemMessage(content="You are a helpful programming assistant that must explain programming library documentation to the user."),
        HumanMessage(content=f"Documentarion: {context} \n\n {question}")
    ]

    response = get_response_from_openai(messages)
    return response

@tool
def black_formatter(path: str) -> str:
    """
    This tool receives as input a file system path to a python script file and runs black formatter to format the file's.
    """

    try:
        os.system(f"black {path}")
        return "Done!"
    except Exception as e:
        return "Did not work!"
    

toolkit = [documentation_tool, black_formatter]

llm = AzureChatOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_API_BASE"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    temperature=0.0,
    max_tokens=1000
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """
         You are programing assistant. Use your tools to answer the user's questions.
         If you don not have a tool to answer the question, just say so.

         Return only the answer.
         """),
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ]
)

agent = create_openai_tools_agent(
    llm=llm,
    tools=toolkit,
    prompt=prompt
)

AgentExecutor = AgentExecutor(
    agent=agent,
    tools=toolkit,
    verbose=True,
    return_intermediate_steps=True
)

result = AgentExecutor.invoke(
    {
        #"input": "Hello",
        #"input": "Gostaria que você formatasse o arquivo path .\\file_example.py.",
        #"input": "Quais os modulos do roteiro de aprendizagem de acordo com essa documentação da url https://learn.microsoft.com/en-us/credentials/applied-skills/create-agents-in-microsoft-copilot-studio/",
        "input": "Gostaria que você formatasse o arquivo path .\\scrapper.py. e depois liste os modulos do roteiro de aprendizagem de acordo com essa documentação da url https://learn.microsoft.com/en-us/credentials/applied-skills/create-agents-in-microsoft-copilot-studio/",
        "chat_history": []
    }
)

print(result['output'])