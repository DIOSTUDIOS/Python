from flet import *


class MenuButton(IconButton):
    def __init__(self, icon=None, tooltip=None, action=None):
        super().__init__()
        self.adaptive = True
        self.alignment = alignment.center
        self.mouse_cursor = MouseCursor.CLICK
        self.icon = icon
        self.tooltip = tooltip
        self.action = action
        self.on_click = self.action_handler

    def action_handler(self, e):
        if self.action == 'ProcessUpdater':
            from src.views import carrier
            from src.views.windows import FunctionsBar
            from src.views.modules import ProcessUpdater
            carrier.controls.pop()
            carrier.controls.append(FunctionsBar(ProcessUpdater()))
            carrier.update()

        if self.action == 'DevicesInfoExporter':
            from src.views import carrier
            from src.views.windows import FunctionsBar
            from src.views.modules import DevicesInfoExporter

            carrier.controls.pop()
            carrier.controls.append(FunctionsBar(DevicesInfoExporter()))
            carrier.update()

        if self.action == 'StatementExporter':
            from src.views import carrier
            from src.views.windows import FunctionsBar
            from src.views.modules import StatementExporter

            carrier.controls.pop()
            carrier.controls.append(FunctionsBar(StatementExporter()))
            carrier.update()


class TextButtonBox(Row):
    def __init__(self, title=None, tip=None, icon=None, tooltip=None, action=None):
        super().__init__()
        self.adaptive = True
        self.alignment = MainAxisAlignment.START
        super().__init__()
        self.alignment = MainAxisAlignment.START
        self.vertical_alignment = CrossAxisAlignment.CENTER
        self.textField = TextField(hint_text=tip, width=750)
        self.action = action
        self.controls = [
            Text(value=title, width=100),
            self.textField,
            IconButton(icon=icon, width=50, height=50, tooltip=tooltip, on_click=self.action_handler)
        ]

    def action_handler(self, e):
        print(self.textField.value)


class TextDropedBox(Row):
    def __init__(self, title=None):
        super().__init__()
        self.alignment = MainAxisAlignment.START
        self.vertical_alignment = CrossAxisAlignment.CENTER
        self.controls = [
            Text(value=title, width=100),
            Dropdown(width=750, options=[
                dropdown.Option('1'),
                dropdown.Option('2'),
                dropdown.Option('3'),
            ]),
        ]


class TextListedBox(Row):
    def __init__(self, title=None):
        super().__init__()
        self.alignment = MainAxisAlignment.START
        self.vertical_alignment = CrossAxisAlignment.CENTER
        self.controls = [
            Text(value=title, width=100),
            Column(
                controls=[
                    Row(controls=[Text(value='1')]),
                    Row(controls=[Text(value='2')]),
                    Row(controls=[Text(value='3')]),
                    Row(controls=[Text(value='4')]),
                    Row(controls=[Text(value='5')]),
                    Row(controls=[Text(value='6')]),
                    Row(controls=[Text(value='7')])
                ]
            )
        ]
