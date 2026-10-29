# 第一段代码：和 AI 说你好
# 运行方式：python hello_ai.py

from openai import OpenAI
import os
from dotenv import load_dotenv

# 从 .env 文件读取 API Key（不要把 key 直接写在代码里，这是行业惯例）
load_dotenv()

client = OpenAI(
    api_key=os.getenv("SILICONFLOW_API_KEY"),   # 读取 .env 里的密钥
    base_url="https://api.siliconflow.cn/v1",   # SiliconFlow 的接口地址（兼容 OpenAI 格式）
)

# 发起一次对话请求
response = client.chat.completions.create(
    model="Qwen/Qwen2.5-7B-Instruct",  # SiliconFlow 上的免费模型
    messages=[
        # system：给 AI 设定人设/规则，用户看不到
        {"role": "system", "content": "你是一个友好的AI助手，用简洁的中文回答"},
        # user：就是你说的话
        {"role": "user", "content": "你好！请用一句话介绍你自己"},
    ],
)

# 从返回结果里取出 AI 的回答并打印
print(response.choices[0].message.content)
