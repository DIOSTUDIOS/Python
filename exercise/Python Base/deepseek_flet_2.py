import flet as ft


# 左侧菜单栏封装类（保持不变）
class MenuSidebar(ft.Column):
    def __init__(self, on_menu_changed):
        super().__init__()
        self.width = 80
        self.alignment = ft.MainAxisAlignment.START
        self.spacing = 10
        self.on_menu_changed = on_menu_changed
        self.selected_index = 0

    def add_menu_button(self, icon, tooltip):
        index = len(self.controls)
        btn = ft.IconButton(
            icon=icon,
            selected=False,
            tooltip=tooltip,
            on_click=lambda e, idx=index: self._button_clicked(idx),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),icon_size=24,
            )
        )
        self.controls.append(btn)
        if len(self.controls) == 1:
            self._set_selected(0)

    def _button_clicked(self, index):
        self._set_selected(index)
        if self.on_menu_changed:
            self.on_menu_changed(index)

    def _set_selected(self, index):
        for i, btn in enumerate(self.controls):
            btn.selected = (i == index)
        self.selected_index = index
        self.update()


# 右侧功能区封装类（保持不变）
class ContentArea(ft.Container):
    def __init__(self):
        super().__init__(expand=True)
        self.content = ft.Column()
        self.modules = {}
        self.current_module = None

    def register_module(self, index, module):
        self.modules[index] = module

    def show_module(self, index):
        if index in self.modules:
            self.content.controls = [self.modules[index]]
            self.update()


# 修正后的基础功能模块类（不再继承 UserControl）
class BaseModule(ft.Column):
    def __init__(self, title):
        super().__init__()
        self.title = title
        self.spacing = 20
        self.controls = [
            ft.Text(title, size=24, weight=ft.FontWeight.BOLD),
            ft.Divider(height=10),
            self.create_content()
        ]

    def create_content(self):
        # 子类必须实现此方法
        return ft.Text("功能模块内容占位", size=16)


# 示例功能模块（调整为直接构建控件）
class HomeModule(BaseModule):
    def __init__(self):
        super().__init__("首页")

    def create_content(self):
        return ft.Column([
            ft.Text("欢迎使用本应用程序！", size=18),
            ft.FilledButton("示例按钮")
        ])


class SettingsModule(BaseModule):
    def __init__(self):
        super().__init__("系统设置")

    def create_content(self):
        return ft.Column([
            ft.Switch(label="启用通知"),
            ft.Slider(min=0, max=100, divisions=10, label="音量调节")
        ])


def main(page: ft.Page):
    # 页面设置（保持不变）
    page.title = "模块化应用示例"
    page.window_width = 1200
    page.window_height = 800
    page.theme_mode = ft.ThemeMode.LIGHT

    def menu_changed(index):
        content_area.show_module(index)

    menu = MenuSidebar(on_menu_changed=menu_changed)
    content_area = ContentArea()  # 提前创建内容区域

    # 先注册模块再添加按钮
    content_area.register_module(0, HomeModule())
    content_area.register_module(1, SettingsModule())

    # 最后添加菜单按钮
    menu.add_menu_button(ft.Icons.HOME, "首页")
    menu.add_menu_button(ft.Icons.SETTINGS, "设置")

    # 构建布局后再设置初始模块
    layout = ft.Row([
        ft.Container(menu, width=80, padding=10, bgcolor=ft.colors.SURFACE_VARIANT),
        ft.VerticalDivider(width=1),
        ft.Container(content_area, padding=20, expand=True)
    ], expand=True)

    page.add(layout)
    # 在控件添加到页面后设置初始选中
    menu._set_selected(0)  # 直接调用内部方法设置初始状态
    content_area.show_module(0)


if __name__ == "__main__":
    ft.app(target=main)
