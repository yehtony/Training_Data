import requests
from pydantic import BaseModel

api_url = "http://ml.hsueh.tw/callapi/"


def call_api_nlp(messages):
    payload = {
        "engine": "taide-llama-3",
        "temperature": 0.1,
        "max_tokens": 200,
        "top_p": 0.95,
        "roles": messages,
        "frequency_penalty": 0,
        "repetition_penalty": 1.03,
        "presence_penalty": 0,
        "stop": "",
        "past_messages": 1,
        "purpose": "dev",
    }

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    # 發送 POST 請求
    response = requests.post(api_url, json=payload, headers=headers)

    # 取得回應內容
    result = response.json()
    reply = result["choices"][0]["message"]["content"]
    return reply


# System Background
message_system_summarize = [
    {
        "role": "system",
        "content": "你具有台灣108課綱國小自然科學科目的專業知識。現在你要做的事是根據國小自然科探究問題，對國小學生的小組討論內容進行判斷，如果討論內容與探究問題無關輸出'0'，如果與問題有關輸出'1'，除此之外不要回覆其他訊息。",
    },
]


# class Message(BaseModel):
#     message: list


def gen_summary_llama(inquiry: str, idea:str) -> str:
    messages = message_system_summarize.copy()
    # print(inquiry)
    # idea_list = [f"{index}.{element}" for index, element in enumerate(idea)]
    # idea_string = " ".join(idea_list)
    # print(idea_string)
    messages.extend(
        [
            {
                "role": "user",
                "content": f"'探究問題：{inquiry}' '討論內容：{idea}'",
            },
        ]
    )
    response = call_api_nlp(messages)
    print(response)
    return response


inquiry = "怎麼讓物質溫度上升呢?"
idea = "我昨天去遊樂園玩，好好玩"

gen_summary_llama(inquiry, idea)