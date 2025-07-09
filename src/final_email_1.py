import os
import pandas as pd
from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_structured_chat_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
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
def automate_email(df):
    for _, row in df.iterrows():
        products = [p.strip() for p in row['product_name'].split(',')]
        quantities = eval(row['quantity']) if isinstance(row['quantity'], str) else row['quantity']

        product_lines = [
            f"- {prod}: {qty} units"
            for prod, qty in zip(products, quantities)
        ]
        product_list_str = "\n".join(product_lines)

        instruction = (
            f"""Send an email to {row['email_id']} with subject 'Product Restock Request' and body: as like these Dear Supplier, We would like to order the following products:
            We would like to order the following products: {product_list_str}Please confirm availability and delivery timeline. Make sure that this is formated and send to 
            send_email function.. the params are 'recipient_name', 'subject', 'body' """
        )

        executor.invoke({"input": instruction})
