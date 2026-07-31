from langchain.tools import tool

@tool
def get_greeting(name:str):
    """Greets the person with the given name"""
    return f"Hello {name}"

@tool
def add_number(a:int , b:int):
    """Adds two numbers"""
    return a + b

result = get_greeting.invoke({"name": "Aman"})

print(result)

print(get_greeting.description)
print(get_greeting.name)
print(get_greeting.args)
print(type(get_greeting))