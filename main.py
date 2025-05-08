import streamlit as st
from utils import generate_script

st.title("📽️视频脚本生成器")

subject = st.text_input("💡请输入主题：")
video_length = st.number_input("🗒️请输入视频大致时长（单位：分钟）：", min_value=0.1, step=0.1)

with st.sidebar:
    api_key = st.text_input("请输入DeepSeek API密钥：", type="password")
    st.write("[获取DeepSeek密钥](https://api-docs.deepseek.com/zh-cn/)")

creativity =st.slider("✨请输入视频脚本的创造力（数字越小则越严谨， 越大则越多样）：", min_value=0.0, max_value=1.0,
          step=0.1, value=0.2)

submit = st.button("生成脚本")

if submit and not api_key:
    st.info("请输入API密钥")
    st.stop()
if submit and not subject:
    st.info("请输入视频的主题")
    st.stop()
if submit and not video_length >= 0.1:
    st.info("视频长度要大于或等于0.1")
    st.stop()
if submit:
    with st.spinner("AI正在思考中， 请稍后..."):
        title, script = generate_script(subject, video_length, creativity, api_key)
    st.success("视频脚本已生成！")
    st.subheader("🔥标题：")
    st.write(title)
    st.subheader("🗒️视频脚本")
    st.write(script)