from dotenv import load_dotenv
import pandas as pd
from llama_index.llms.groq import Groq
import os
from llama_index.experimental.query_engine import PandasQueryEngine
from llama_index.core import Settings
from llama_index.core import PromptTemplate

_ = load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

Settings.llm = Groq(model="llama-3.3-70b-versatile", api_key=api_key)

# load data to the pandas df agent
company_data_df = pd.read_csv('./data/company_data_min.csv')
query_engine = PandasQueryEngine(df=company_data_df, verbose=True)


query = " list all the details about the company name NNOVATION LAB LTD"

response = query_engine.query(
    query,
)

print(response)