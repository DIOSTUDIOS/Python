from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from logic import *

import os


class Gui:
    def __init__(self):
        self.gui = Tk()
        self.window()

    def window(self):
        windowWidth = 580
        windowHeight = 390

        screenWidth = self.gui.winfo_screenwidth()
        screenHeight = self.gui.winfo_screenheight()

        self.gui.geometry('%dx%d+%d+%d' % (windowWidth, windowHeight, (screenWidth-windowWidth)/2, (screenHeight-windowHeight)/2))
        self.gui.resizable(0, 0)

        self.gui.title('业务链流程版本升级程序')
        self.gui.iconbitmap(os.getcwd() + '\process.ico')

        Label(self.gui, text='流程名称', anchor='center', font=('黑体', 16)).place(x=20, y=20, width=100, height=30)
        self.gui.processName = Entry(self.gui, font=('黑体', 14))
        self.gui.processName.place(x=140, y=20, width=300, height=30)
        self.gui.check = Button(self.gui, text='查询', command=self.check)
        self.gui.check.place(x=460, y=20, width=100, height=30)

        Label(self.gui, text='流程标识', anchor='center', font=('黑体', 16)).place(x=20, y=70, width=100, height=30)
        self.gui.processID = Combobox(self.gui, font=('黑体', 10))
        self.gui.processID.place(x=140, y=70, width=300, height=30)
        self.gui.processID.bind('<<ComboboxSelected>>', self.show)

        self.gui.text = Text(self.gui, font=('黑体', 12))
        self.gui.text.place(x=20, y=120, width=540, height=200)

        Label(self.gui, text='流程版本', anchor='center', font=('黑体', 16)).place(x=20, y=340, width=100, height=30)
        self.gui.processVersion = Entry(self.gui, font=('黑体', 14))
        self.gui.processVersion.place(x=140, y=340, width=300, height=30)
        self.gui.update = Button(self.gui, text='升级', command=self.update)
        self.gui.update.place(x=460, y=340, width=100, height=30)

        self.gui.mainloop()
        pass

    def check(self):
        processName = self.gui.processName.get()

        if processName == '':
            messagebox.showerror(message='请填写流程名称！')
        else:
            if is_exist_process(processName):
                ids = show_process_id(processName)

                self.gui.processID['value'] = ids
            else:
                messagebox.showerror(message='流程名称不存在，请检查并重新输入！')
        pass

    def show(self, event):
        self.gui.text.delete(1.0, END)

        processID = self.gui.processID.get()

        details = show_process_info(processID)

        for item in details:
            self.gui.text.insert(INSERT, item)
            self.gui.text.insert(INSERT, '\n')
        pass

    def update(self):
        processName = self.gui.processName.get()
        processID = self.gui.processID.get()
        processVersion = self.gui.processVersion.get()

        if processName == '':
            messagebox.showerror(message='请输入流程名称！')
        elif processID == '':
            messagebox.showerror(message='请选择流程标识！')
        elif processVersion == '':
            messagebox.showerror(message='请输入流程版本！')
        else:
            if is_newest_version(processID, processVersion):
                update_phase_process(processName, processID, processVersion)
                update_pre_process(processName, processID, processVersion)
                update_next_process(processName, processID, processVersion)

                messagebox.showinfo(message='流程升级完成，请查看日志！')
            else:
                messagebox.showerror(message='输入的流程版本错误！')
        pass


if __name__ == '__main__':
    Gui()
