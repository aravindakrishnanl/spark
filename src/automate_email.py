import os
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_structured_chat_agent
from langchain_core.tools import Tool
from langchain_groq import ChatGroq
from email_setup import send_email

load_dotenv()

# tools = [
#     Tool(
#     name="Email",
#     func=send_email,
#     description=(
#         "Use this to send an email. "
#         "Input should include: recipient email, subject, and body of the email. "
#         "Format: recipient_name, subject, body"
#         "The function contains three parameters 'recipient_name', 'subject', 'body'"
#     )
# )
# ]

tools = [send_email]

prompt = hub.pull("hwchase17/structured-chat-agent")


llm = ChatGroq(
    api_key= os.getenv("GROQ_API_KEY"),
    model= "deepseek-r1-distill-llama-70b",
    temperature= 0
)

agent = create_structured_chat_agent(
    llm = llm,
    tools = tools,
    prompt= prompt,
)

agent_executor = AgentExecutor(
    agent= agent, 
    tools= tools,
    verbose = True,
    handle_parsing_errors= True
)

# a = the sender mail id

def agent_sending_email(a):
    response = agent_executor.invoke({    
        "input": f"Send an email to {a} with subject 'Hello' and body 'Hi Arav, hope you're well.'"
    })
    print("Success")

# agent_sending_email("arav302005@gmail.com")