import tkinter as tk
from tkinter import messagebox

class Index(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.grid()
        
        # create widgets
        self.author = tk.Label(self, text="作者：赵家乐")
        self.text = tk.Label(self, text='请输入您的身高：(单位：cm)')
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text='确认', command=self.check)

        # layout widgets
        self.author.grid(row=0, column=0)
        self.text.grid(row=1, column=0)
        self.entry.grid(row=2, column=0)
        self.button.grid(row=2, column=1)
        
    def calculate(self):
        self.value = self.entry.get()
        try:
            self.float_value = float(self.value)
            return True
        except:
            pass
        return False


    def check(self):
        if self.calculate() == True:
            tk.Label(self, text='经计算，您的身高为：'+str(self.float_value)+'cm').grid(row=3, column=0)
        else:
            messagebox.showerror('Err', '请输入正确数字！')

if __name__ == '__main__':
    root = tk.Tk()
    root.title('身高计算器')
    root.geometry('400x200')
    root.resizable(0, 0)

    Index()
    root.mainloop()

