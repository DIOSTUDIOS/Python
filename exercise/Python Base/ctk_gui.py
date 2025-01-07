import customtkinter as ctk

ctk.set_appearance_mode("Light")  # 设置外观模式为系统模式（可以是 "Light", "Dark", "System"）
ctk.set_default_color_theme("blue")  # 设置默认颜色主题

root = ctk.CTk()
root.title("CTk 示例")
# root.iconbitmap('icon.ico')
root.minsize(300, 200)
root.maxsize(600, 400)
root.geometry('300x200+100+100')
root.state('zoomed')
# root.attributes('-alpha', 0.5)
root.attributes('-topmost', 1)
# root.attributes('-disabled', 1)
# root.attributes('-fullscreen', 1)
# root.attributes('-type', 'dialog')
# root.bgcolor('red')
root.resizable(False, False)

button = ctk.CTkButton(root, text="点击我")
button.pack()

label = ctk.CTkLabel(root, text="Hello, CTk!", font=("Arial", 16))
label.pack()

text = ctk.CTkTextbox(root, width=200, height=100, font=("Consolas, Arial, 仿宋", 12))
text.pack()

checkBox = ctk.CTkCheckBox(root, text="复选框", font=("黑体", 28), onvalue=1, offvalue=0)
checkBox.pack()
print(checkBox.get())

root.mainloop()
