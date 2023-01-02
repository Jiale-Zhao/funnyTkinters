import tkinter as tk
from tkinter import messagebox

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.grid()

        # create widgets
        self.author = tk.Label(self, text='作者：赵家乐')
        self.text = tk.Label(self, text='请输入您的体重（单位：斤）：')
        self.entry = tk.Entry(self)
        self.commitbutton = tk.Button(self, text='确认', command=self.calculateresult)
        self.resultlabel = tk.Label(self)

        # layout widgets
        self.author.grid(row=0, column=0)
        self.text.grid(row=1, column=0)
        self.entry.grid(row=2, column=0)
        self.commitbutton.grid(row=2, column=1)
        self.resultlabel.grid(row=3, column=0, columnspan=2)

    def commitCheck(self):
        self.weight = self.entry.get()
        try:
            self.intweight = int(self.weight)
            return True
        except:
            pass
        return False

    def calculateresult(self):
        self.resultlabel.grid_forget()
        if self.commitCheck() == True:
            self.strweight = str(self.intweight)
            self.length = len(self.strweight)
            if self.strweight[0]+self.calculatezero() == self.strweight:
                self.resultlabel = tk.Label(self, text='恭喜您！你的体重为'+self.strweight+'斤')
            else:
                self.resultlabel = tk.Label(self, text='恭喜您！您的体重为'+self.strweight[0]+self.calculatezero()+'多斤')
            self.resultlabel.grid(row=3, column=0, columnspan=2)
        else:
            messagebox.showerror('Err', '请输入正确数字！')


    def calculatezero(self):
        self.resultlength = self.length - 1
        self.listresult = [] * self.resultlength
        self.result = ''
        for i in range(self.resultlength):
            self.listresult.append('0')
            self.result = ''.join(self.listresult)
        return self.result


if __name__ == '__main__':
    root = tk.Tk()
    
    root.title('体重计算器')

    App(root)
    root.mainloop()
        
