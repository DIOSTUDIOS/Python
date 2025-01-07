import tkinter as tk
from tkinter import ttk


def close_window():
    root.destroy()


root = tk.Tk()
root.title("我的优美窗口")
root.geometry("300x200")
root.configure(bg="#E0FFFF")

# 使用clam主题（还有其他主题如'vista'、'xpnative'等可尝试）
style = ttk.Style()
style.theme_use('clam')
# 自定义按钮样式
style.configure('TButton', foreground='white', background='#4CAF50',  # 前景色为白色，背景色为绿色
                font=('Arial', 12),
                borderwidth=2,  # 边框宽度
                relief='raised',  # 按钮的立体效果样式
                padding=(5, 3, 5, 3))  # 按钮内容的内边距

label = tk.Label(root, text="欢迎来到这个优美的窗口", font=("Arial", 14), bg="#E0FFFF")
label.pack(pady=30)

close_btn = ttk.Button(root, text="关闭窗口", command=close_window, style='TButton')
close_btn.pack()

root.mainloop()