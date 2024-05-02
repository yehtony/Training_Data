import pandas as pd
import os
from gen_idea import gen_idea
from gen_summary import gen_summary
from gen_summary_llama import gen_summary_llama
from gen_message import gen_message


def process_gen_idea(inquiry, knowledge):
    # gen_idea(inquiry, knowledge)
    return gen_idea(inquiry, knowledge)


def process_gen_summary(inquiry, idea):
    # gen_idea(inquiry, knowledge)
    return gen_summary(inquiry, idea)


def process_gen_summary_llama(inquiry, idea):
    # gen_idea(inquiry, knowledge)
    return gen_summary_llama(inquiry, idea)


def process_gen_message(inquiry, knowledge):
    # gen_idea(inquiry, knowledge)
    return gen_message(inquiry, knowledge)


# 指定目錄
directory = "./dataset/InquiryQuestion/Idea/refine"

# 創建一個空的DataFrame來儲存所有文件的數據
# all_data = pd.DataFrame()

# # 遍歷目錄下的所有文件
# for filename in os.listdir(directory):
#     all_data = pd.DataFrame()
#     if filename.endswith(".csv"):
#         # 完整的文件路徑
#         file_path = os.path.join(directory, filename)

#         # 讀取CSV文件
#         data = pd.read_csv(file_path)

#         # 確保CSV文件包含所需的欄位
#         if all(column in data.columns for column in ["inquiry", "knowledge", "idea"]):
#             # 處理數據並存儲結果到'idea'欄位
#             data["idea"] = data.apply(
#                 lambda row: process_gen_idea(row["inquiry"], row["knowledge"]), axis=1
#             )

#             # 將處理後的數據追加到all_data DataFrame中
#             all_data = pd.concat([all_data, data], ignore_index=True)
#             all_data.to_csv(f"{directory}/Idea/{filename}", index=False, encoding='utf_8_sig')

#             # 查看合併後的數據
#             print(all_data)
#         else:
#             print(f"File {filename} does not contain the required columns.")
#     else:
#         continue
# # all_data.to_csv(f"{directory}/idea_{filename}", index=False)
# # # 儲存處理後的所有數據到一個新的CSV文件
# # all_data.to_csv(f"./{file_path}/{filename}", index=False)


for filename in os.listdir(directory):
    all_data = pd.DataFrame()
    if filename.endswith(".csv"):
        # 完整的文件路徑
        file_path = os.path.join(directory, filename)
        print(filename)
        # 讀取CSV文件
        data = pd.read_csv(file_path)

        # 確保CSV文件包含所需的欄位
        if all(column in data.columns for column in ["inquiry", "knowledge", "idea"]):
            # 處理數據並存儲結果到'idea'欄位
            data["summary"] = data.apply(
                lambda row: process_gen_summary_llama(
                    row["inquiry"], eval(row["idea"])
                ),
                axis=1,
            )
            # 將處理後的數據追加到all_data DataFrame中
            all_data = pd.concat([all_data, data], ignore_index=True)
            all_data.to_csv(
                f"{directory}/summary/llama/{filename}",
                index=False,
                encoding="utf_8_sig",
            )

            # 查看合併後的數據
            print(all_data)
        else:
            print(f"File {filename} does not contain the required columns.")
    else:
        continue
# all_data.to_csv(f"{directory}/idea_{filename}", index=False)
# # 儲存處理後的所有數據到一個新的CSV文件
# all_data.to_csv(f"./{file_path}/{filename}", index=False)

# for filename in os.listdir(directory):
#     all_data = pd.DataFrame()
#     if filename.endswith(".csv"):
#         # 完整的文件路徑
#         file_path = os.path.join(directory, filename)

#         # 讀取CSV文件
#         data = pd.read_csv(file_path)

#         # 確保CSV文件包含所需的欄位
#         if all(column in data.columns for column in ["inquiry", "knowledge", "idea"]):
#             # 處理數據並存儲結果到'idea'欄位
#             data["message"] = data.apply(
#                 lambda row: process_gen_message(row["inquiry"], row["knowledge"]),
#                 axis=1,
#             )

#             # 將處理後的數據追加到all_data DataFrame中
#             all_data = pd.concat([all_data, data], ignore_index=True)
#             all_data.to_csv(
#                 f"{directory}/message/{filename}", index=False, encoding="utf_8_sig"
#             )

#             # 查看合併後的數據
#             print(all_data)
#         else:
#             print(f"File {filename} does not contain the required columns.")
#     else:
#         continue

# import ast

# for filename in os.listdir(directory):
#     all_data = pd.DataFrame()
#     if filename.endswith(".csv"):
#         # 完整的文件路徑
#         file_path = os.path.join(directory, filename)

#         # 讀取CSV文件
#         data = pd.read_csv(file_path)
#         print(filename)

#         # 確保CSV文件包含所需的欄位
#         if all(column in data.columns for column in ["inquiry", "knowledge", "idea"]):
#             # 處理數據並存儲結果到'idea'欄位
#             # 将 messages 列中的每个 set 拆分为一行
#             data["messages"] = (
#                 data["messages"].replace("\n", "").apply(ast.literal_eval)
#             )
#             data = data.explode("messages")

#             print(data["messages"])

#             # 重置索引以保持与 inquiry 列对应
#             data = data.reset_index(drop=True)

#             # 分割字典中的键值对为两列
#             data[["message", "relevant"]] = pd.DataFrame(
#                 data["messages"]
#                 .apply(lambda x: (list(x.keys())[0], list(x.values())[0]))
#                 .tolist(),
#                 index=data.index,
#             )

#             # 將處理後的數據追加到all_data DataFrame中
#             all_data = pd.concat([all_data, data], ignore_index=True)
#             all_data.to_csv(
#                 f"{directory}/relevant/{filename}",
#                 index=False,
#                 encoding="utf_8_sig",
#             )

#             # 查看合併後的數據
#             print(all_data)
#         else:
#             print(f"File {filename} does not contain the required columns.")
#     else:
#         continue
