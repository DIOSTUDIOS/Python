from src.views.elements import *


class ProcessUpdater(Column):
    def __init__(self):
        super().__init__()
        self.adaptive = True
        self.alignment = MainAxisAlignment.CENTER
        self.horizontal_alignment = CrossAxisAlignment.CENTER
        self.expand = True
        self.width = 900
        self.controls = [
            TextButtonBox(title='流程名称', tip='请输入流程名称', icon=Icons.SEARCH, tooltip='根据流程名称查询系统中的流程标识', action='search'),
            TextDropedBox(title='流程标识'),
            TextListedBox(title='使用列表'),
            TextButtonBox(title='流程版本', tip='请输入流程版本', icon=Icons.UPDATE, tooltip='升级业务链中的流程到最新版', action='update')
        ]


class DevicesInfoExporter(Column):
    def __init__(self):
        super().__init__()
        self.adaptive = True
        self.alignment = MainAxisAlignment.CENTER
        self.horizontal_alignment = CrossAxisAlignment.CENTER
        self.expand = True
        self.width = 900
        self.controls = [
            Placeholder(color=Colors.GREEN_900, expand=True)
        ]


class StatementExporter(Column):
    def __init__(self):
        super().__init__()
        self.adaptive = True
        self.alignment = MainAxisAlignment.CENTER
        self.horizontal_alignment = CrossAxisAlignment.CENTER
        self.expand = True
        self.width = 900
        self.controls = [
            Placeholder(color=Colors.RED_900, expand=True)
        ]
