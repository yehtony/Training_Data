import requests
from pydantic import BaseModel

api_url = "http://ml.hsueh.tw/callapi/"


def call_api_nlp(messages):
    payload = {
        "engine": "gpt-35-turbo-16k",
        "temperature": 0,
        "max_tokens": 200,
        "top_p": 0.95,
        "top_k": 1,
        "roles": messages,
        "frequency_penalty": 0,
        "repetition_penalty": 1.03,
        "presence_penalty": 0,
        "stop": "",
        "past_messages": 0,
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
        "content": "你具有台灣108課綱國小自然科學科目的專業知識。現在你要做的事是根據國小自然科探究問題，對國小學生的小組討論內容進行想法摘要，摘要出4~6個重點並用數字分行列點，僅進行摘要動作，並且僅摘要與探究問題有關的內容，切記不要對使用者的討論內容提出任何評論、糾正、回覆、想法猜測，回覆不要帶有人稱主詞，回覆字數在75字以內。",
    },
]


class Message(BaseModel):
    message: list


def gen_summary(inquiry: str, idea: Message) -> str:
    messages = message_system_summarize.copy()
    idea_list = [f"{index}.{element}" for index, element in enumerate(idea)]
    idea_string = " ".join(idea_list)
    messages.extend(
        [
            {
                "role": "user",
                "content": f"'探究問題：{inquiry}' '討論內容：{idea_string}'",
            },
        ]
    )
    response = call_api_nlp(messages)
    print(response)
    return response


# inquiry = "怎麼讓物質溫度上升呢?"
# idea = [
#     {"怎麼讓物質溫度上升呢？": "請發表你們的想法"},
#     {"太陽照射": "【💡我的想法】太陽照射物體會使物體溫度上升"},
#     {"為什麼？": "【❓我想知道】為什麼太陽照射會使物體溫度上升？"},
#     {"物體吸收太陽能": "【💡我的想法】物體吸收太陽能會使分子運動加快，溫度上升"},
#     {
#         "那為什麼黑色物體比白色物體溫度高呢？": "【❓我想知道】為什麼黑色物體比白色物體溫度高？"
#     },
#     {"黑色物體吸收光熱": "【💡我的想法】黑色物體吸收光熱多，所以溫度較高"},
#     {"那為什麼物質燃燒會使溫度上升呢？": "【❓我想知道】為什麼物質燃燒會使溫度上升？"},
#     {"燃燒釋放熱能": "【💡我的想法】物質燃燒時會釋放熱能，使溫度上升"},
#     {"那摩擦呢？": "【❓我想知道】摩擦是如何使溫度上升的？"},
#     {"分子運動加快": "【💡我的想法】摩擦會使物體分子運動加快，溫度上升"},
#     {"那溫度計是如何測量溫度的呢？": "【❓我想知道】溫度計是如何測量溫度的？"},
#     {"溫度計的液體膨脹": "【💡我的想法】溫度計的液體會因為溫度上升而膨脹"},
#     {"那溫度計的刻度是怎麼來的呢？": "【❓我想知道】溫度計的刻度是怎麼來的？"},
#     {"攝氏溫標": "【💡我的想法】溫度計的刻度是根據攝氏溫標來的"},
#     {"那溫度計的使用方法是什麼呢？": "【❓我想知道】溫度計的使用方法是什麼呢？"},
#     {"放在物體上": "【💡我的想法】溫度計要放在物體上，等待一段時間後讀取溫度"},
#     {"那溫度計的單位是什麼呢？": "【❓我想知道】溫度計的單位是什麼呢？"},
#     {"攝氏度": "【💡我的想法】溫度計的單位是攝氏度"},
#     {"那溫度計的範圍是多少呢？": "【❓我想知道】溫度計的範圍是多少呢？"},
#     {"攝氏-10度到100度": "【💡我的想法】溫度計的範圍是攝氏-10度到100度"},
#     {"那溫度計的讀數是如何表示的呢？": "【❓我想知道】溫度計的讀數是如何表示的呢？"},
#     {"數字加上°C": "【💡我的想法】溫度計的讀數是數字加上°C"},
#     {"那溫度計的讀數有什麼意義呢？": "【❓我想知道】溫度計的讀數有什麼意義呢？"},
#     {"表示物體的溫度": "【💡我的想法】溫度計的讀數可以表示物體的溫度"},
#     {
#         "那溫度計的讀數可以用來做什麼呢？": "【❓我想知道】溫度計的讀數可以用來做什麼呢？"
#     },
#     {"判斷物體的熱度": "【💡我的想法】溫度計的讀數可以用來判斷物體的熱度"},
#     {
#         "✍🏻我的總結": "物質溫度上升可以透過太陽照射、物質燃燒和摩擦等方式，而溫度計可以用來測量和判斷物體的溫度。"
#     },
# ]
