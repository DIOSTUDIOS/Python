from flet import Page, app
from src.views import carrier


def main(page: Page):
    page.window.center()
    page.window.resizable = False
    page.window.maximizable = False
    page.title = 'ToolsKit'
    page.expand = True
    page.add(carrier)


if __name__ == '__main__':
    app(target=main, assets_dir='assets')
