import openai
from openai import OpenAI

messages=[
    {"role": "system", "content": "You are a language translator,the user will provide you with the language to translate to and the message to translate"},
]

client = OpenAI(api_key="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")

def translate(message: str, language: str = "Spanish"):
    messages.append(
        {
            "role": "user",
            "content": "Convert the below message to " + language
        }
    )
    messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    completion = client.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=messages,
        max_tokens=100
    )

    return completion.choices[0].message.content

