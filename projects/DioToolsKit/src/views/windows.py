from src.views.modules import *


class Carrier(Row):
    def __init__(self):
        super().__init__()
        self.adaptive = True
        self.alignment = MainAxisAlignment.START
        self.vertical_alignment = CrossAxisAlignment.CENTER
        self.expand = True
        self.controls = [
            ToolsBar(),
            VerticalDivider(width=10, color=Colors.BLACK),
            FunctionsBar(ProcessUpdater())
        ]


class ToolsBar(Column):
    def __init__(self):
        super().__init__()
        self.adaptive = True
        self.alignment = MainAxisAlignment.START
        self.horizontal_alignment = CrossAxisAlignment.CENTER
        self.controls = [
            MenuButton(icon=Icons.UPDATE, tooltip='无需停办流程而升级业务链流程版本', action='ProcessUpdater'),
            MenuButton(icon=Icons.BAR_CHART, tooltip='从数据库导出热力经营报表相关数据', action='DevicesInfoExporter'),
            MenuButton(icon=Icons.DEVICES, tooltip='生成二网平台设备、通讯卡信息导入文件', action='StatementExporter'),
        ]


class FunctionsBar(Column):
    def __init__(self, control):
        super().__init__()
        self.adaptive = True
        self.alignment = MainAxisAlignment.CENTER
        self.horizontal_alignment = CrossAxisAlignment.CENTER
        self.expand = True
        self.controls.append(control)


if __name__ == '__main__':
    pass
