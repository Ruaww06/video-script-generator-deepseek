from langchain.prompts import ChatPromptTemplate
from prompt_template import system_template_text, user_template_text
from langchain_deepseek import ChatDeepSeek
from langchain.output_parsers import PydanticOutputParser
from Xiaohongshu_model import Xiaohongshu

# import os

def generate_xiaohongshu(theme, deepseek_api_key):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template_text),
        ("human", user_template_text)
    ])

    model = ChatDeepSeek(model="deepseek-chat",api_key=deepseek_api_key,base_url="https://api.deepseek.com")


    output_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)
    chain = prompt | model | output_parser
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "theme": theme
    })

    return result

# print(generate_xiaohongshu("深圳景点", os.getenv("DEEPSEEK_API_KEY")))