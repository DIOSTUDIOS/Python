import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPalette


class BeautifulWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题
        self.setWindowTitle('优美的 PyQt 窗口')

        # 设置窗口背景颜色
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(240, 240, 240))
        self.setPalette(palette)

        # 主布局
        main_layout = QVBoxLayout()

        # 标题栏
        title_bar = QFrame()
        title_bar.setFrameShape(QFrame.NoFrame)
        title_layout = QHBoxLayout()
        title_label = QLabel('我的应用')
        title_label.setFont(QFont('微软雅黑', 16, QFont.Bold))
        title_layout.addWidget(title_label)
        title_bar.setLayout(title_layout)
        main_layout.addWidget(title_bar)

        # 内容区域
        content_layout = QVBoxLayout()
        content_label = QLabel('欢迎使用本应用，这里可以展示一些信息或者图片等。')
        content_label.setAlignment(Qt.AlignCenter)
        content_label.setFont(QFont('宋体', 12))
        content_layout.addWidget(content_label)

        # 按钮布局
        button_layout = QHBoxLayout()
        button1 = QPushButton('按钮 1')
        button1.setStyleSheet('QPushButton { background-color: #4CAF50; color: white; border-radius: 5px; padding: 5px 10px; }'
                              'QPushButton:hover { background-color: #45a049; }')
        button1.clicked.connect(self.button1Clicked)
        button_layout.addWidget(button1)

        button2 = QPushButton('按钮 2')
        button2.setStyleSheet('QPushButton { background-color: #03A9F4; color: white; border-radius: 5px; padding: 5px 10px; }'
                              'QPushButton:hover { background-color: #0288D1; }')
        button2.clicked.connect(self.button2Clicked)
        button_layout.addWidget(button2)

        content_layout.addLayout(button_layout)
        main_layout.addLayout(content_layout)

        self.setLayout(main_layout)

        # 设置窗口大小和位置
        self.setGeometry(300, 300, 400, 250)

        # 显示窗口
        self.show()

    def button1Clicked(self):
        print('按钮 1 被点击了')

    def button2Clicked(self):
        print('按钮 2 被点击了')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = BeautifulWindow()
    sys.exit(app.exec_())