from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv
import pandas as pd
import os
from langchain_openai import ChatOpenAI

_ = load_dotenv()

df = pd.read_csv('./data/company_data_min.csv')

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    verbose=True
)

agent = create_pandas_dataframe_agent(
    llm, df, agent_type="openai-tools", verbose=True, allow_dangerous_code=True
)

response = agent.invoke(
    {
        "input": "list all the details about the company name !BIG IMPACT GRAPHICS LIMITED?"
    }
)

print(response)