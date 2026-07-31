from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from rich import print 


@tool
def get_text_length(text: str) -> int:
    """Returns the length of the text"""
    return len(text)

tools = {
    "get_text_length": get_text_length
}

llm = ChatMistralAI(model="mistral-small-2603")
llm_with_tool = llm.bind_tools([get_text_length])

messages = []
prompt = input("You: ")
query = HumanMessage(prompt)
messages.append(query)

result = llm_with_tool.invoke(messages)

messages.append(result)

if result.tool_calls:
    tool_name = result.tool_calls[0]["name"]
    tool_message = tools[tool_name].invoke(result.tool_calls[0])
    messages.append(tool_message)

result = llm_with_tool.invoke(messages)

print(result.content)