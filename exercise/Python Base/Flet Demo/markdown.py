import flet as ft

md1 = """
# Markdown 示例
Markdown 允许您轻松地在应用程序中包含格式化文本、图像和格式化 Dart 代码。

## 标题

Setext 风格

这是 H1
=============

这是 H2
-------------

Atx 风格

# 这是 H1

## 这是 H2

###### 这是 H6

选择有效的标题：

- [x] `# hello`
- [ ] `#hello`

## 链接

[内联风格](https://www.google.com)

## 图像

![来自 Flet 资产的图像](/icons/icon-192.png)

![测试图像](https://picsum.photos/200/300)

## 表格

|语法                                 |结果                               |
|---------------------------------------|-------------------------------------|
|`*italic 1*`                           |*italic 1*                           |
|`_italic 2_`                           | _italic 2_                          |
|`**bold 1**`                           |**bold 1**                           |
|`__bold 2__`                           |__bold 2__                           |
|`This is a ~~strikethrough~~`          |This is a ~~strikethrough~~          |
|`***italic bold 1***`                  |***italic bold 1***                  |
|`___italic bold 2___`                  |___italic bold 2___                  |
|`***~~italic bold strikethrough 1~~***`|***~~italic bold strikethrough 1~~***|
|`~~***italic bold strikethrough 2***~~`|~~***italic bold strikethrough 2***~~|

## 样式

将文本样式设置为 _italic_、__bold__、~~strikethrough~~ 或 `内联代码`。

- 使用 bulleted 列表
-  better clarify
- 您的要点

## 代码块

格式化的 Dart 代码看起来也非常漂亮：

```
void main() {
  runApp(MaterialApp(
    home: Scaffold(
      body: ft.Markdown(data: markdownData),
    ),
  ));
}
```
"""


def main(page: ft.Page):
    page.scroll = "auto"
    page.add(
        ft.Markdown(
            md1,
            selectable=True,
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
            on_tap_link=lambda e: page.launch_url(e.data),
        )
    )

ft.app(target=main)