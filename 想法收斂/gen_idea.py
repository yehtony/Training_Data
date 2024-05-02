import requests

api_url = "http://ml.hsueh.tw/callapi/"


def call_api_nlp(messages):
    payload = {
        "engine": "gpt-35-turbo-16k",
        "temperature": 0,
        "max_tokens": 2000,
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
        "content": "你具有台灣108課綱國小自然科學科目的專業知識，同時你具有進行小組合作及探究活動的專業經驗。現在你要做的事是根據國小自然科探究問題及對應單元知識，模擬出國小學生在進行自然科小組探究活動的討論過程以及內容，並且加入討論離題等現實會發生的情況，內容不要太過深奧，以國小中年級學生的具有的知識水平為準。總共需根據探究問題列出25句討論對話，每一句對話須包含1.想法標題 2.回覆內容，對話格式為[{'想法標題':'回覆內容'},...]。範例：[{'生活中的聲音如何產生'：'請發表你們的想法', '物體震動':'【💡我的想法】聲音是透過震動產生', '請舉例'：'【❓我想知道】為什麼？'}]。想法標題為回覆內容的重點，回覆內容以【💡我的想法】、【🧐我覺得更好的想法】、【❓我想知道】、【🙅🏻這個想法不能解釋】、【📄舉例和參考來源】、【✍🏻我的總結】作為起始句。",
    },
]


def gen_idea(inquiry: str, knowledge: str) -> str:
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
