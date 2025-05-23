import os

from langchain.prompts import ChatPromptTemplate
from langchain_deepseek import ChatDeepSeek

def generate_script(subject, video_length, creativity,
                    api_key):
    title_template = ChatPromptTemplate.from_messages(
        [
            ("human", """请为{subject}这个主题想一个吸引人的标题。
            只需要给出1个标题就可以了，不要输出额外内容。""")
        ]
    )

    script_template = ChatPromptTemplate.from_messages(
        [
            ("human",
             """你是一位短视频频道的博主。根据以下标题和相关信息，为短视频频道写一个视频脚本。
             视频标题：{title}，视频时长：{duration}分钟，生成的脚本的长度尽量遵循视频时长的要求。
             要求开头抓住限球，中间提供干货内容，结尾有惊喜，脚本格式也请按照【开头、中间，结尾】分隔。
             整体内容的表达方式要尽量轻松有趣，吸引年轻人。""")
        ]
    )

    model = ChatDeepSeek(model="deepseek-chat", api_key=api_key, temperature=creativity,
                         base_url="https://api.deepseek.com")

    title_chain = title_template | model
    script_chain = script_template | model

    title = title_chain.invoke({"subject":subject}).content
    script = script_chain.invoke({"title":title, "duration":video_length}).content

    return title, script

# print(generate_script("sora模型", 1, 0.6, os.getenv("DEEPSEEK_API_KEY")))