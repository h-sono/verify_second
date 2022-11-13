# Tkinterライブラリをインポートする
import tkinter
from tkinter import messagebox

# Tkinterインスタンスの生成
# 変数を使ってウィンドウの設定を行う
root = tkinter.Tk()
# ウィンドウのタイトルを指定する
root.title("GUI検証")
# ウィンドウサイズを指定する。横×縦
root.geometry("500x400")

# 入力欄の作成はEntryを使用する。widthで幅を指定。
input_field = tkinter.Entry(width=40)
# placeプロパティにて配置箇所をX,Y座標で指定する
input_field.place(x=20, y=100)
# ボタンクリック時に呼び出す関数を定義
def click_botton():
    """
    入力欄の値をget()にて取得。
    入力値をダイアログに表示する。
    """
    input_value = input_field.get()
    messagebox.showinfo("イベント",input_value + "が入力されました。")

# ボタンの作成はButtonを使用する。commandにて実行関数を指定する。
button = tkinter.Button(text="実行", command=click_botton)
# placeプロパティにて配置箇所をX,Y座標で指定する
button.place(x=20, y=140)

# ウィンドウの描画
root.mainloop()

