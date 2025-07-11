import os
import pandas as pd
from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_structured_chat_agent
from langchain.tools import tool
from langchain_groq import ChatGroq
from email_setup import send_email
from langchain import hub

import pandas as pd

load_dotenv()

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

executor = AgentExecutor(
    agent= agent, 
    tools= tools,
    verbose = True,
    handle_parsing_errors= True
)
from collections import defaultdict

grouped = defaultdict(list)

def automate_email(df):
    for _, row in df.iterrows():
        grouped[row['email_id']].append((row['product_name'], row['quantity']))

    # Generate and invoke clear instructions per email
    for email, items in grouped.items():
        body_lines = "\n".join([f"- {product}: {qty} units" for product, qty in items])
        
        prompt = (
            f"Send an email to {email} with subject 'Product Restock Request' and body:\n"
            f"Dear Supplier,\n\n"
            f"We would like to order the following products:\n\n"
            f"{body_lines}\n\n"
            f"Please confirm availability and delivery timeline.\n\n"
            f"Pass the parameters to the `send_email` function as:\n"
            f"- recipient_name (if identifiable)\n"
            f"- subject\n"
            f"- body"
        )

        executor.invoke({"input": prompt})