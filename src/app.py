import streamlit as st
from streamlit_chat import message
import openai

st.header("🤖 GPT-3 Chat Demo")

# st.title("🤖 GPT-3 Chat Demo ")
# st.sidebar.title("Data Sources")

# open ai Key
st.sidebar.header("📚 先设置好openAI Api key")
key_input = st.sidebar.text_input(
    "输入Key", placeholder="st-", key="key"
)

if key_input:
    openai.api_key = key_input


def generate_response(content):
    prompt = "你是 ChatGPT, 一个由 OpenAI 训练的大型语言模型, 你旨在回答并解决人们的任何问题，并且可以使用多种语言与人交流。\n请回答我下面的问题\nQ: " + content + "\nA: "
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.9,
    )

    message = completions.choices[0].text
    return message


if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


def get_text():
    input_text = st.text_input("输入你的问题:", "", key="input")
    return input_text


user_input = get_text()

if user_input:
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i],
                is_user=True, key=str(i) + '_user')
