import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")

# 设置主题，例如'clam', 'alt', 'default'等
style = ttk.Style(root)
style.theme_use('clam')

# 创建一个按钮
button = ttk.Button(root, text="点击我")
button.pack()

root.mainloop()
