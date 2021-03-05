import tkinter as tk

BUTTON_TEXT = ["7", "8", "9", "+", "AC",
               "6", "5", "4", "-", "BS",
               "3", "2", "1", "*", "Undo",
               "00", "0", ".", "/", "="]

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("電卓")
        self.upper_frame = tk.Frame(self, bg="black")
        self.text = tk.StringVar()
        self.text.set("")
        self.Label = tk.Label(self.upper_frame, textvariable=self.text, width=20,
                              background="black", foreground="white").pack(fill=tk.X)
        self.upper_frame.pack(padx=10, pady=10)

        self.output_strings = ""
        self.most_recent_strings = ""

        self.lower_frame = tk.Frame(self, bg="black")

        for i, t in zip(range(20), BUTTON_TEXT):
            button = tk.Button(self.lower_frame, text=t, width=4, font=("", 12))
            button.grid(row=i//5, column=i%5, padx=5, pady=5)
            button.bind("<Button-1>", self.clicked)

        self.lower_frame.pack(padx=10, pady=10)

    def clicked(self, event):
        text = event.widget["text"]

        if text == "AC":
            self.most_recent_strings = self.output_strings
            self.output_strings = ""
            self.text.set("")

        elif text == "BS":
            self.most_recent_strings = self.output_strings
            self.output_strings = self.output_strings[:-1]
            self.text.set(self.output_strings)

        elif text == "=":
            self.most_recent_strings = self.output_strings
            self.output_strings = str(eval(self.output_strings))
            self.text.set(self.output_strings)

        elif text == "Undo":
            self.output_strings = self.most_recent_strings
            self.text.set(self.output_strings)

        else:
            self.most_recent_strings = self.output_strings
            self.output_strings += text
            self.text.set(self.output_strings)


if __name__ == "__main__":
    app = App()
    app.mainloop()