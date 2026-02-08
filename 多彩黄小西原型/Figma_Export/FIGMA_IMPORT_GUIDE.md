# 如何将多彩黄小西原型导入 Figma

由于 `.fig` 是 Figma 的私有二进制格式，我们为您准备了**行业标准的设计交付包**。请按照以下步骤操作，即可完美还原设计稿。

## 📁 交付包内容 (`Figma_Export/`)
1.  **`index.html`**: 包含完整布局和样式的网页文件。
2.  **`design_tokens.json`**: 包含颜色、字体规范的令牌文件（可用于 Tokens Studio）。
3.  **资源图片**: 如 `honyifu.png`。

## 🚀 导入方法 A：使用 "html.to.design" 插件 (推荐)
这是最快还原页面布局的方法。

1.  打开 **Figma**。
2.  点击顶部工具栏的 **"Resources"** (图标为方块+菱形)，选择 **"Plugins"**。
3.  搜索并运行 **"html.to.design"** 插件。
4.  在插件界面中，选择 **"Import via Chrome extension"** 或者直接拖拽 `index.html` 文件（部分版本支持本地文件）。
    *   *提示：如果插件需要 URL，您可以双击打开 `index.html`，然后将浏览器地址栏的 `file:///...` 链接复制进去。*
5.  点击 **"Import"**。
6.  设计稿将自动在 Figma 中生成，且图层结构清晰（Auto Layout 可能需要微调）。

## 🎨 导入方法 B：导入设计规范 (Tokens)
如果您使用 **Tokens Studio for Figma** 插件，可以直接导入配色方案。

1.  运行 **Tokens Studio** 插件。
2.  点击 **"Tools"** -> **"Load from JSON"**。
3.  选择本文件夹中的 `design_tokens.json`。
4.  此时所有的颜色变量（如 `primary-color` #5E6E82, `accent-color` #FF7157）都会自动创建为 Figma 的 Color Styles。

## 📝 手动还原要点
如果您需要手动绘制，请参考以下核心参数：

*   **画布尺寸**: iPhone 14/15 Pro (393x852)
*   **安全区域**: 顶部 44px (Dynamic Island), 底部 34px (Home Indicator)
*   **主色 (Miao Silver)**: `#5E6E82`
*   **强调色 (Embroidery Red)**: `#FF7157`
*   **字体**: PingFang SC / San Francisco
