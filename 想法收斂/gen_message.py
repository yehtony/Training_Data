import requests

api_url = "http://ml.hsueh.tw/callapi/"


def call_api_nlp(messages):
    payload = {
        "engine": "gpt-35-turbo-16k",
        "temperature": 0,
        "max_tokens": 1000,
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
        "content": "你具有台灣108課綱國小自然科學科目的專業知識，同時你具有進行小組合作及探究活動的專業經驗。現在你要做的事是根據國小自然科探究問題及對應單元知識，模擬出國小學生在進行自然科小組探究活動的討論過程以及內容，並且加入討論偏離主題的情況，內容不要太過深奧，以國小中年級學生的具有的知識水平為準。總共列出20句對話。根據探究問題列出10句與探究問題有關的對話，同時列出10句不屬於自然科學領域並且與探究問題「毫不相關」的對話，每一句對話須包含回覆內容與相關性，無關內容標記為0，有關內容標記為1，對話格式為[{'回覆內容'：'相關性'},...]。範例：假設探究問題是「怎麼讓物質溫度上升呢?」，輸出[{'我們可以使用溫度計來測量物質的溫度': 1}, {我昨天去遊樂園玩，好好玩': 0}, {'我喜歡看電影，最近看了一部很好笑的喜劇': 0}, {'太陽照射物體會使物體溫度上升': 1}]。",
    },
]


def gen_message(inquiry: str, knowledge: str) -> str:
    messages = message_system_summarize.copy()
    messages.extend(
        [
            {
                "role": "user",
                "content": f"'探究問題：{inquiry}' '單元知識：{knowledge}'",
            },
        ]
    )
    response = call_api_nlp(messages)
    print(response)
    return response


# inquiry = "怎麼讓物質溫度上升呢?"
# knowledge = "1. 溫度計的使用方法 2. 太陽照射、物質燃燒和摩擦等可以使溫度升高，運用測量的方法可知溫度高低。"

# gen_message(inquiry, knowledge)
