import flet as ft


def main(page: ft.Page):
    page.window.center()
    page.window.maximizable = False
    page.window.resizable = False
    page.title = "业务流程升级程序"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    procesName = ft.TextField(hint_text='请输入流程名称，然后点击查询按钮', width=900),
    page.add(
        ft.Column(
            width=960,
            # spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    width=960,
                    spacing=0,
                    controls=[
                        # ft.Container(
                        #     content=ft.TextField(hint_text='请输入流程名称，然后点击查询按钮', width=900),
                        #     # margin=5,
                        #     # padding=5,
                        #     alignment=ft.alignment.center,
                        #     # bgcolor=ft.Colors.AMBER,
                        #     width=900,
                        #     height=60,
                        #     # border_radius=10,
                        # ),
                        # ft.Container(
                        #     content=ft.IconButton(icon='search', width=60),
                        #     # margin=5,
                        #     # padding=5,
                        #     alignment=ft.alignment.center,
                        #     # bgcolor=ft.Colors.RED,
                        #     width=60,
                        #     height=60,
                        #     # border_radius=10,
                        # )
                        procesName,
                        ft.IconButton(icon='search', width=60),
                    ],
                )],
        ),
        ft.Text(value=page.window.width),
        ft.Text(value=page.window.height),
    )


ft.app(target=main)
