import streamlit as st
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

#response = agent.invoke(
#    {
#        "input": "What is the FULL ADDRESS  of company !BIG IMPACT GRAPHICS LIMITED?"
#    }
#)

def get_response(prompt_input):
        chat_completion = agent.invoke (
             {
                "input": prompt_input
             }
        )
        response = chat_completion.get("output")
        print(response)
        return response



# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Streamlit app layout
st.title("Companies House Chatbot")
user_input = st.text_input("You:", key="input")

if user_input:
    # Append user input to chat history
    st.session_state.chat_history = []
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Generate response from Groq model
    response = get_response(user_input)
    st.session_state.chat_history.append({"role": "assistant", "content": response})

# Display chat history
for message in st.session_state.chat_history:
    st.write(f"{message['role'].capitalize()}: {message['content']}")


#print(response)
