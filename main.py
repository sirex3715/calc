import tkinter as tk

# ボタン表示を分かりやすくするためリストで格納
BUTTON_TEXT = ["7", "8", "9", "+", "AC",
               "6", "5", "4", "-", "BS",
               "3", "2", "1", "*", "Undo",
               "00", "0", ".", "/", "="]

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("電卓")

        # 表示盤を表現
        self.upper_frame = tk.Frame(self, bg="black")
        self.text = tk.StringVar()
        self.text.set("")
        self.Label = tk.Label(self.upper_frame, textvariable=self.text, width=20,
                              background="black", foreground="white").pack(fill=tk.X)
        self.upper_frame.pack(padx=10, pady=10)

        # ボタンを表現
        self.lower_frame = tk.Frame(self, bg="black")

        for i, t in zip(range(20), BUTTON_TEXT):
            button = tk.Button(self.lower_frame, text=t, width=4, font=("", 12))
            button.grid(row=i//5, column=i%5, padx=5, pady=5)
            button.bind("<Button-1>", self.clicked)

        self.lower_frame.pack(padx=10, pady=10)

        # 計算結果保持のための変数を用意
        self.output_strings = ""
        self.most_recent_strings = ""

    def clicked(self, event):
        text = event.widget["text"]

        # 受け取ったボタンのtextに応じた処理を行う
        if text == "AC":  # 全文字を消去する
            self.most_recent_strings = self.output_strings
            self.output_strings = ""
            self.text.set("")

        elif text == "BS":  # 右端の桁を削除する
            self.most_recent_strings = self.output_strings
            self.output_strings = self.output_strings[:-1]
            self.text.set(self.output_strings)

        elif text == "=":  # 計算結果を表示する
            self.most_recent_strings = self.output_strings
            self.output_strings = str(eval(self.output_strings))
            self.text.set(self.output_strings)

        elif text == "Undo":  # 一動作前の表示に戻す
            self.output_strings = self.most_recent_strings
            self.text.set(self.output_strings)

        else:  # 入力された数字、算術記号を表示させる
            self.most_recent_strings = self.output_strings
            self.output_strings += text
            self.text.set(self.output_strings)


if __name__ == "__main__":
    app = App()
    app.mainloop()