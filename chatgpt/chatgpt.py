# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
# 请先安装openai的库
# pip install openai
import openai

# api key可能已经失效了，请换成自己的有效api key
openai.api_key = "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"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "钢铁侠的演员是谁?"},
        {
            "content": "'钢铁侠在漫威电影宇宙中的扮演者是罗伯特·唐尼（Robert Downey Jr.）。'",
            "role": "assistant"
        },
        {"role": "user", "content": "他还参演过哪些作品?"},
    ]
)

print(response)
