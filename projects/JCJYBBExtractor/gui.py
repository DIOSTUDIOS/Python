import os
import threading

from tkinter import *
from tkinter import messagebox, scrolledtext
from tkinter.ttk import Combobox
from logic import generate_excel


class Gui:
    def __init__(self):
        self.root = Tk()

        windowWidth = 500
        windowHeight = 400
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()
        self.root.geometry('%dx%d+%d+%d' % (windowWidth, windowHeight, (screenWidth - windowWidth) / 2, (screenHeight - windowHeight) / 2))

        self.root.resizable(width=False, height=False)

        self.root.iconbitmap(os.getcwd() + '/datasheet.ico')
        self.root.title('热力经营报表导出工具')

        self.label = Label(self.root, text='报表名称', anchor='center', font=('黑体', 16))
        self.label.place(x=20, y=20, width=100, height=40)

        self.comboBox = Combobox(self.root, font=('黑体', 16))
        self.comboBox.place(x=140, y=20, width=220, height=40)
        self.comboBox['values'] = ('出库明细', '产品明细', '订单明细', '合同明细', '装配收入',
                                   '研发利润', '分配收入', '利润明细', '利润汇总')

        self.button = Button(self.root, text='导出', font=('黑体', 16), command=self.export)
        self.button.place(x=380, y=20, width=100, height=40)

        self.log = scrolledtext.ScrolledText(self.root, font=('黑体', 12))
        self.log.place(x=20, y=80, width=460, height=280)

    def export(self):
        reportNames = {
            '出库明细': 'ckmx',
            '产品明细': 'cpmx',
            '订单明细': 'ddmx',
            '合同明细': 'htmx',
            '装配收入': 'zpsr',
            '研发利润': 'yflr',
            '分配收入': 'fpsr',
            '利润明细': 'lrmx',
        }

        reportName = self.comboBox.get()

        if reportName in reportNames:
            self.log.insert(END, f'{reportName} 报表数据获取中……' + '\n')

            thread = threading.Thread(target=generate_excel, args=(reportNames[reportName], reportName))
            thread.start()
            # thread.join()
            # self.log.insert(END, f'报表 {reportName}.xlsx 已生成！' + '\n')
        else:
            messagebox.showerror(title='错误', message='请选择报表名称')

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    pass
