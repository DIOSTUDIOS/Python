import flet as ft
from flet import Colors, Icons


def card(page):
    page.title = "卡片示例"
    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.ALBUM),
                            title=ft.Text("魔法夜莺"),
                            subtitle=ft.Text("朱莉·盖布尔作曲，西德尼·斯坦作词。"),
                        ),
                        ft.Row(
                            [ft.TextButton(text="购票"), ft.TextButton("试听")],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            ),
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            color=ft.colors.BLUE,
            elevation=1,
            margin=ft.margin.all(20),
            shadow_color=Colors.BLUE,
            surface_tint_color=Colors.RED,
        )
    )

ft.app(target=card)
