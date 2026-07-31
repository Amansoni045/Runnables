from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI 
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser 

# prompt = ChatPromptTemplate.from_template(
#     "Explain {topic} in simple words"
# )

# model = ChatMistralAI(model = "mistral-small-2506")

# parser = StrOutputParser()

# formatted_prompt = prompt.format_messages(topic="Machine Learning")

# response = model.invoke(formatted_prompt)

# final_output = parser.parse(response.content)

# print(final_output)


prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words"
)

model = ChatMistralAI(model="mistral-small-2603")

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"topic":"Machine Learning"})
print(result)