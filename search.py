import pandas as pd
import eel


# 検索対象取得
df=pd.read_csv("./source.csv")
source=list(df["name"])

### デスクトップアプリ作成課題
def kimetsu_search(word, csv_path):
    # 検索
    if word in source:
        print("『{}』はあります".format(word))
        eel.view_log_js("『{}』はあります\n".format(word))
    else:
        print("『{}』はありません".format(word))
        eel.view_log_js("『{}』はありません\n".format(word))
        # 追加
        #add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        #if add_flg=="1":
        source.append(word)

    # CSV書き込み
    df=pd.DataFrame(source,columns=["name"])
    df.to_csv(csv_path ,encoding="utf_8-sig")
    print(source)