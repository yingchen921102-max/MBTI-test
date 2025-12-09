# -*- coding: utf-8 -*-

from google.colab import files
import csv

# ====== 題庫（你原本的題目） ======
questions = [
    { "question": "你在社交場合更喜歡？", "dimension": "EI", "a": "與多人互動", "b": "獨處或與少數人相處" },
    { "question": "你更依賴什麼來做決定？", "dimension": "TF", "a": "邏輯與分析", "b": "感受與價值觀" },
    { "question": "你處理事情時更傾向？", "dimension": "JP", "a": "按計畫行事", "b": "隨機應變" },
    { "question": "你偏好哪種資訊處理方式？", "dimension": "SN", "a": "實際經驗", "b": "直覺靈感" },
    { "question": "你做事時較像哪種人？", "dimension": "JP", "a": "喜歡提前安排計畫", "b": "喜歡保持彈性與自由" },
    { "question": "遇到問題時你傾向依賴什麼？", "dimension": "TF", "a": "客觀事實與邏輯", "b": "情緒與他人感受" },
    { "question": "你更容易從哪裡獲得能量？", "dimension": "EI", "a": "和人互動、聊天", "b": "自己獨處、思考" },
    { "question": "你學習新事物時偏好哪種方式？", "dimension": "SN", "a": "透過實作、具體例子", "b": "靠直覺與靈感理解" }
]

# ====== 回饋文字 ======
feedback_text = {
    "E": "你喜歡與人互動，常常能從社交活動中獲得能量，也擅長在團隊中發揮影響力。",
    "I": "你傾向在獨處或小圈子中充電，喜歡深度思考與自我反省，觀察力敏銳。",
    "S": "你注重現實與細節，做決策時會考慮實際可行性，擅長掌握眼前的事物。",
    "N": "你喜歡從大局觀察事物，善於發現潛在可能性，喜歡創新與未來導向的想法。",
    "T": "你偏向理性分析，重視邏輯與客觀判斷，在做決策時會以事實為依據。",
    "F": "你重視他人感受與人際關係，做決策時會考慮情感因素，善於理解他人的需求。",
    "J": "你喜歡有計畫、有結構的生活，做事有條理且善於安排時間，重視目標與規劃。",
    "P": "你彈性高，喜歡保持選擇空間，能隨機應變，面對突發狀況也能適應自如。"
}


# ====== 測驗流程 ======
def conduct_test(questions):
    scores = {"EI": 0, "SN": 0, "TF": 0, "JP": 0}

    for q in questions:
        print("\n" + q["question"])
        print("A.", q["a"])
        print("B.", q["b"])

        while True:
            answer = input("請輸入 A 或 B：").strip().upper()
            if answer in ["A", "B"]:
                break
            print("輸入錯誤，請輸入 A 或 B")

        if answer == "A":
            scores[q["dimension"]] += 1
        else:
            scores[q["dimension"]] -= 1

    return scores


def get_mbti(scores):
    result = ""
    result += "E" if scores["EI"] > 0 else "I"
    result += "S" if scores["SN"] > 0 else "N"
    result += "T" if scores["TF"] > 0 else "F"
    result += "J" if scores["JP"] > 0 else "P"
    return result


# ====== 產生 CSV 檔案 ======
def save_to_csv(result, feedback_output):
    filename = "mbti_result.csv"
    header = ["MBTI", "E/I 回饋", "S/N 回饋", "T/F 回饋", "J/P 回饋"]

    data = [
        result,
        feedback_output["EI"],
        feedback_output["SN"],
        feedback_output["TF"],
        feedback_output["JP"]
    ]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)

    files.download(filename)


# ====== 主程式 ======
def main():
    print("歡迎來到 MBTI 心理測驗！請誠實作答。\n")

    scores = conduct_test(questions)
    result = get_mbti(scores)

    # 個別維度分析
    dims = {
        "EI": result[0],
        "SN": result[1],
        "TF": result[2],
        "JP": result[3]
    }

    feedback_output = {
        "EI": feedback_text[dims["EI"]],
        "SN": feedback_text[dims["SN"]],
        "TF": feedback_text[dims["TF"]],
        "JP": feedback_text[dims["JP"]]
    }

    print("\n========================")
    print("你的 MBTI 結果是：", result)
    print("========================\n")

    # 印出每個維度回饋
    print("📌 個別維度分析：\n")
    print("外向 / 內向 (E/I)：", feedback_output["EI"])
    print("感覺 / 直覺 (S/N)：", feedback_output["SN"])
    print("思考 / 情感 (T/F)：", feedback_output["TF"])
    print("判斷 / 知覺 (J/P)：", feedback_output["JP"])

    # 產生 CSV
    save_to_csv(result, feedback_output)


main()
