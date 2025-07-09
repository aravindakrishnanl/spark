import os
import pandas as pd
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage
from langchain.tools import tool
from langchain_groq import ChatGroq
from email_setup import send_email

import pandas as pd

data = {
    "email_id": [
        "aravindhnov05@gmail.com",
        "gokulrajtvm05@gmail.com",
        "madhavan07vk@gmail.com",
        "madhavan86776@gmail.com",
        "siddharth.sulur@gmail.com",
        "siddharthsridhar2006@gmail.com"
    ],
    "product_name": [
        "Detergent Powder",
        "Shampoo, Hand Sanitizer",
        "Face Wash, Detergent Bar",
        "Toothpaste",
        "Soap, Toothbrush, Hair Oil",
        "Comb, Sanitary Napkins"
    ],
    "quantity": [
        [53],
        [51, 51],
        [57, 52],
        [53],
        [52, 54, 55],
        [51, 58]
    ]
}

df = pd.DataFrame(data)

llm = ChatGroq(
    api_key= os.getenv("GROQ_API_KEY"),
    model= "deepseek-r1-distill-llama-70b",
    temperature= 0
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an inventory assistant. Use the tool to send emails for product restocking."),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

tools = [send_email]

agent = create_openai_functions_agent(llm=llm, tools=tools, prompt=prompt)

executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

for _, row in df.iterrows():
    products = [p.strip() for p in row['product_name'].split(',')]
    quantities = eval(row['quantity']) if isinstance(row['quantity'], str) else row['quantity']

    product_lines = [
        f"- {prod}: {qty} units"
        for prod, qty in zip(products, quantities)
    ]
    product_list_str = "\n".join(product_lines)

    instruction = (
        f"Send an email to {row['email_id']} with subject 'Product Restock Request' and body:\n\n"
        f"Dear Supplier,\n\n"
        f"We would like to order the following products:\n"
        f"{product_list_str}\n\n"
        f"Please confirm availability and delivery timeline.\n\n"
        f"Thanks,\nInventory Team"
    )

    executor.invoke({"input": instruction})
