## pythonでソフトウェア開発
注意：windowsで動くソフトウェアを開発するにはwindows環境下で行う。

### 環境準備
- windows本体にpythonをインストール。
- 環境変数にpythonのパスを通す。
- 作業場所がVsCodeの場合、拡張機能でPythonをインストール。
⇒import元に飛べないため。
- 仮想環境を使う場合は以下を実施。
  - 仮想環境作成。
  $ python -m venv {仮想環境名}
  - 仮想環境へ切り替え。仮想環境実行用ファイルのあるディレクトリへ移動。
  $ .\{仮想環境名}\Script\activate.bat
  - 仮想環境終了。
  $ deactivate
- 作成したファイルの例。
以下はtkinterを使用。

```python
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

# ウィンドウの描画　※最後にmainloopが必要
root.mainloop()
```

- コマンドプロンプトにて以下コマンドを実行し、動作確認。
$ python {pyファイル名}
- 正常に動作することを確認。
- windowsで配布できるよう.exeファイルを作成する。pyinstallerが必要であるためインストール。
$ pip install pyinstaller
- pyinstallerで.exeファイルを作成。
$ pyinstaller {pyファイル名} --noconsole --onefile
※1 --onefileオプションをつけると配布ファイルが一つにまとまる。
※2 --noconsoleオプションをつけると配布ファイルを実行したときにコンソールが非表示となる。
- distフォルダ内に.exeファイルが生成されるのでこれを配布。
