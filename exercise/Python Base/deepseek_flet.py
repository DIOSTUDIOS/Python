import flet as ft
from flet import icons


def main(page: ft.Page):
    # 页面基础设置
    page.title = "Flet 多视图应用"
    page.window_width = 800
    page.window_height = 600

    # 定义右侧内容容器
    right_content = ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        spacing=20,
        controls=[
            ft.Text("请选择左侧菜单功能", size=20)
        ]
    )

    # 菜单按钮点击处理函数
    def menu_click(e, section_name):
        right_content.controls.clear()
        right_content.controls.append(
            ft.Text(f"{section_name} 功能区域", size=24, weight=ft.FontWeight.BOLD)
        )

        # 添加占位控件（可根据后续需求替换为实际内容）
        right_content.controls.extend([
            ft.Divider(),
            ft.Text("功能开发中...", size=16),
            ft.ProgressRing(),
            ft.Text("这是一个占位区域，可替换为实际功能组件", color=ft.colors.GREY)
        ])
        page.update()

    # 创建左侧导航菜单
    left_nav = ft.Column(
        width=100,
        spacing=10,
        controls=[
            ft.IconButton(
                icon=icons.HOME,
                icon_size=30,
                tooltip="主页",
                on_click=lambda e: menu_click(e, "主页")
            ),
            ft.IconButton(
                icon=icons.BAR_CHART,
                icon_size=30,
                tooltip="数据分析",
                on_click=lambda e: menu_click(e, "数据分析")
            ),
            ft.IconButton(
                icon=icons.SETTINGS,
                icon_size=30,
                tooltip="系统设置",
                on_click=lambda e: menu_click(e, "系统设置")
            ),
            ft.IconButton(
                icon=icons.CLOUD_UPLOAD,
                icon_size=30,
                tooltip="数据同步",
                on_click=lambda e: menu_click(e, "数据同步")
            ),
            ft.VerticalDivider(),
            ft.IconButton(
                icon=icons.HELP_OUTLINE,
                icon_size=30,
                tooltip="帮助文档",
                on_click=lambda e: menu_click(e, "帮助文档")
            )
        ]
    )

    # 构建主布局
    page.add(
        ft.Row(
            [
                # 左侧导航
                ft.Container(
                    left_nav,
                    padding=10,
                    bgcolor=ft.colors.BLUE_GREY_100,
                    border_radius=ft.border_radius.all(10)
                ),

                # 垂直分隔线
                ft.VerticalDivider(width=1),

                # 右侧内容区
                ft.Container(
                    right_content,
                    padding=20,
                    expand=True
                )
            ],
            expand=True
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
