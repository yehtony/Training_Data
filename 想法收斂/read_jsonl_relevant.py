import json

file_path = (
    "./dataset/InquiryQuestion/Idea/refine/message/relevant/bert/idea_relevant.jsonl"
)
file_path_two = "./dataset/idea_relevant.jsonl"
# 读取 JSONL 文件并处理每一行
with open(file_path, "r", encoding="utf-8-sig") as f:
    lines = f.readlines()

# 处理每一行数据
for i, line in enumerate(lines):
    # 将 JSON 数据加载为 Python 字典
    data = json.loads(line)
    text_list = json.loads(data["text"])
    # print(text_list)
    # # 修改文本格式
    # data["text"][0] = "探究問題：{}".format(data["text"][0])
    # data["text"][1] = "學生想法：{}".format(data["text"][1])
    # 修改文本格式
    text_list[0] = "探究問題：{}".format(text_list[0])
    text_list[1] = "學生想法：{}".format(text_list[1])
    # print(text_list)

    # 将修改后的文本列表转换回字符串
    # data["text"] = json.dumps(text_list, ensure_ascii=False)
    data["text"] = formatted_text = "\n".join(text_list)
    if data["label"] == 0:
        data["label"] = "無關：學生「無」針對探究問題提出想法"
    elif data["label"] == 1:
        data["label"] = "有關：學生「有」針對探究問題提出想法"
    # 将修改后的数据转换回 JSON 格式
    new_json_data = json.dumps(data, ensure_ascii=False)

    # print(data)

    # 将修改后的数据写回文件
    lines[i] = new_json_data + "\n"
    print(lines[i])

# 将修改后的数据写回文件
with open(file_path_two, "w", encoding="utf-8-sig") as f:
    f.writelines(lines)
