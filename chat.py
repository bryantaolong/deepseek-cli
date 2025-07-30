import os

from colorama import Fore
from openai import OpenAI

# 从环境变量中读取 API Key 和 Base URL
API_KEY = os.getenv("DEEPSEEK_API_KEY")
BASE_URL = "https://api.deepseek.com"

if not API_KEY:
    raise EnvironmentError("环境变量 DEEPSEEK_API_KEY 未设置，请设置后重试。")

# 初始化 OpenAI 客户端
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# 初始化对话历史
messages = [{"role": "system", "content": "You are a helpful assistant"}]

def chat(model="deepseek-chat"):
    while True:
        print(Fore.BLUE + f"[当前模型: {model}]")
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("对话结束。")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=messages,
                stream=False
            )

            assistant_reply = response.choices[0].message.content
            print(f"DeepSeek: {assistant_reply}")

            messages.append({"role": "assistant", "content": assistant_reply})

            print(f"[本次对话使用的 tokens: {response.usage.total_tokens}]")

        except Exception as e:
            print(f"发生错误: {e}")
            break
