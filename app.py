import streamlit as st
from pathlib import Path
from urllib.parse import quote_plus
from langchain_groq import ChatGroq
from sqlalchemy import create_engine
from langchain_community.utilities import SQLDatabase
from langchain_classic.agents import create_sql_agent
from langchain_classic.agents.agent_types import AgentType
from langchain_classic.agents.agent_toolkits import SQLDatabaseToolkit
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()

st.title('LANGCHAIN: CHAT WITH SQL DB')

LOCALDB='USE_LOCALDB'
MYSQLDB='USE_MYSQL'

radio_option=['Use SQLite3 Database(student.db)','Connect to MySQL Database']
selected_option=st.sidebar.radio("Choose the Database",options=radio_option)

if selected_option == 'Connect to MySQL Database':
    db_uri=MYSQLDB
    mysql_host=st.sidebar.text_input('Provide MYSQL Hostname',value='localhost')
    mysql_user=st.sidebar.text_input('Provide MYSQL Username',value='root')
    mysql_password=st.sidebar.text_input('Provide MYSQL Password',type='password')
    mysql_db=st.sidebar.text_input('Provide MYSQL Database name')

else:
    db_uri=LOCALDB

groq_api=st.sidebar.text_input('Enter the Groq Api Key',type='password')
if not groq_api:
    st.info('Provide your groq API Key to Continue')
    st.stop()

model=ChatGroq(model='llama-3.3-70b-versatile',groq_api_key=groq_api,streaming=True)

@st.cache_resource(ttl=7200)

def configure_db(db_uri,mysql_host=None,mysql_user=None,mysql_password=None,mysql_db=None):
    if db_uri==LOCALDB:
        dbfilepath=(Path(__file__).parent/"student.db").absolute()
        creator=lambda: sqlite3.connect(f"file:{dbfilepath}?mode=ro",uri=True)
        return SQLDatabase(create_engine("sqlite:///",creator=creator))

    elif db_uri==MYSQLDB:
        if not(mysql_host and mysql_user and mysql_password and mysql_db):
            st.error("please provide all MySQL connection details")
            st.stop()

        encoded_password=quote_plus(mysql_password)
        connection_str=f"mysql+mysqlconnector://{mysql_user}:{encoded_password}@{mysql_host}/{mysql_db}"

        try:
            db=SQLDatabase(create_engine(connection_str))
            st.success('Succesfully Connected to MySQL DataBase !')
            return db
        
        except Exception as e:
            st.error(f"Failed to connect to MySQL:{e}")
            st.stop()

if db_uri==MYSQLDB:
    db=configure_db(db_uri,mysql_host,mysql_user,mysql_password,mysql_db)
else:
    db=configure_db(db_uri)


## ---------- AGENT ----- TOOLKIT ----------- ##

toolkit=SQLDatabaseToolkit(db=db,llm=model)
agent=create_sql_agent(llm=model,toolkit=toolkit,verbose=True,agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

if  "messages" not in st.session_state or st.sidebar.button("clear message history"):
    st.session_state['messages']=[{"role":"Assistant","content":"How can i help you ?"}]
    for msg in st.session_state['messages']:
        st.chat_message(msg['role']).write(msg['content'])


user_query=st.chat_input(placeholder='Ask anything from the Database...')

if user_query:
    st.session_state['messages'].append({'role':'user','content':user_query})
    st.chat_message('user').write(user_query)

    with st.chat_message("Assistant"):
        streamlit_callback=StreamlitCallbackHandler(st.container())
        response=agent.run(user_query,callbacks=[streamlit_callback])
        st.session_state['messages'].append({'role':'Assistant','content':response})
        st.write(response)