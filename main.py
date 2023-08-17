from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents.agent_types import AgentType

from fastapi import FastAPI

app = FastAPI()

llm = OpenAI(temperature=0)

db = SQLDatabase.from_uri("postgresql://app:@localhost/db")
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)


@app.get("/query")
def read_root(query: str):
    out = agent_executor.run(query)
    return {"response": out}
