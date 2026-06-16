# %%
import os
from dotenv import load_dotenv
load_dotenv()
from typing_extensions import TypedDict
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages
from typing import Annotated
from IPython.display import Image, display
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition
from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI


# %%
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# %%
class ChatState(TypedDict):
    messages: Annotated[list[str], add_messages]

llm = ChatOpenAI(model="gpt-4o")


# %%
def default_grpah():

    # Node definition
    def call_llm(state:ChatState):
        return {"messages":[llm.invoke(state["messages"])]}

    graph_workflow= StateGraph(ChatState)

    graph_workflow.add_node("agent", call_llm)

    graph_workflow.add_edge(START, "agent")
    graph_workflow.add_edge("agent", END)

    agent=graph_workflow.compile()

    return agent

agent =default_grpah()



