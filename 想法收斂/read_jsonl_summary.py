import json
import ast

file_path = "./dataset/InquiryQuestion/Idea/refine/summary/ideawall_summarize.jsonl"
file_path_two = "./dataset/ideawall_summarize.jsonl"
# 读取 JSONL 文件并处理每一行
with open(file_path, "r", encoding="utf-8-sig") as f:
    lines = f.readlines()

# 处理每一行数据
for i, line in enumerate(lines):
    # 将 JSON 数据加载为 Python 字典
    data = json.loads(line)
    text_list = ast.literal_eval(data["idea"])

    # print(text_list)
    # 將列表轉換為字串
    formatted_str = "小組想法-自然科學探究活動：\n"
    for idx, item in enumerate(text_list):
        for key, value in item.items():
            formatted_str += f"{idx+1}. {key}: {value},\n"
    # 移除最後一個逗號
    formatted_str = formatted_str.rstrip(",\n")
    formatted_summary = "小組想法摘要-自然科學探究活動：\n" + data["summary"].replace(
        "\r", ""
    )
    data["idea"] = formatted_str
    data["summary"] = formatted_summary
    new_json_data = json.dumps(data, ensure_ascii=False)

    # 将修改后的数据写回文件
    lines[i] = new_json_data + "\n"
    print(lines[i])

# 将修改后的数据写回文件
with open(file_path_two, "w", encoding="utf-8-sig") as f:
    f.writelines(lines)
