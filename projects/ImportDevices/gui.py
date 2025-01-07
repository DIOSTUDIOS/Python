from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from logic import import_simcard_info, create_devices_file, create_simcard_file

import os


class Gui:
    def __init__(self):
        self.window = None
        self.gui()

    def gui(self):
        self.window = Tk()

        windowWidth = 510
        windowHeight = 270

        screenWidth = self.window.winfo_screenwidth()
        screenHeight = self.window.winfo_screenheight()

        self.window.geometry('%dx%d+%d+%d' % (windowWidth, windowHeight, (screenWidth-windowWidth)/2, (screenHeight-windowHeight)/2))
        self.window.resizable(0, 0)

        self.window.title('二网文件生成器')
        self.window.iconbitmap(os.getcwd() + '\icon.ico')
        # 文件路径
        Label(self.window, text='文件路径', anchor='center', font=('黑体', 18)).place(x=20, y=20, width=100, height=30)
        # 文件显示框
        self.window.file = Entry(self.window)
        self.window.file.place(x=140, y=20, width=300, height=30)
        # 文件选择按钮
        img = ImageTk.PhotoImage(Image.open('.\open.png').resize((20, 20)))
        Button(self.window, image=img, command=self.select_file).place(x=460, y=20, width=30, height=30)

        Label(self.window, text='设备年限', anchor='center', font=('黑体', 18)).place(x=20, y=70, width=100, height=30)
        # 设备承诺年限选择框
        self.window.deviceYear = Combobox(self.window, value=['1', '2', '3', '4', '5'])
        self.window.deviceYear.current(2)
        self.window.deviceYear.place(x=140, y=70, width=300, height=30)
        # 通讯卡基本信息导入按钮
        self.window.importSimcardInfo = Button(self.window, text='导入卡片年限信息', command=self.import_simcard_info)
        self.window.importSimcardInfo.place(x=290, y=120, width=200, height=30)
        # 设备导入文件生成按钮
        self.window.createDevicesFile = Button(self.window, text='生成设备导入文件', command=self.create_devices_file)
        self.window.createDevicesFile.place(x=290, y=170, width=200, height=30)
        # 卡片导入文件生成按钮
        self.window.createSimcardFile = Button(self.window, text='生成卡片导入文件', command=self.create_simcard_file)
        self.window.createSimcardFile.place(x=290, y=220, width=200, height=30)

        self.window.mainloop()
        pass

    def select_file(self):
        document = filedialog.askopenfilename(initialdir=os.getcwd(),
                                              title="选择文件",
                                              filetypes=(("Excel files", "*.xlsx"), ("Excel files", "*.xls"))
                                              )

        self.window.file.insert(INSERT, document)
        pass

    def import_simcard_info(self):
        file = self.window.file.get()

        if file == '':
            messagebox.showinfo(title='提示', message='请选择文件')
        else:
            result = import_simcard_info(file)

            if result:
                messagebox.showinfo(title='提示', message='信息导入成功！')
                self.window.quit()
            else:
                pass
        pass

    def create_devices_file(self):
        file = self.window.file.get()

        if file == '':
            messagebox.showinfo(title='提示', message='请选择文件')
        else:
            result = create_devices_file(file)

            if result:
                messagebox.showinfo(title='提示', message='文件生成成功！')
                # self.window.quit()
            else:
                pass
        pass

    def create_simcard_file(self):
        file = self.window.file.get()
        year = self.window.deviceYear.get()

        # messagebox.showinfo(message=year)

        if file == '':
            messagebox.showinfo(title='提示', message='请选择文件')
        else:
            result = create_simcard_file(file, year)

            if result:
                messagebox.showinfo(title='提示', message='文件生成成功！')
                # self.window.quit()
            else:
                pass
        pass
