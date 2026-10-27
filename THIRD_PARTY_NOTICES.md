# Third-party notices / 第三方说明

本目录目前主要由Flutter生成的应用模板组成。不要把模板、平台Runner、Flutter默认图标和第三方资产声明为用户原创。根MIT仅授予本项目新增的说明、工作流、检查脚本与自有改动，不改变以下来源的原有权利。

| 材料 | 来源与许可 |
|---|---|
| Flutter 3.38.7 应用/平台模板、Material Icons、默认Flutter图标与运行时 | Flutter Authors，BSD-3-Clause；保留 `third_party/flutter/LICENSE` 和 `PATENT_GRANT`。Flutter名称/标志仍受相应商标规则约束，不表示官方背书。 |
| Cupertino Icons 1.0.9 | 使用原包随附MIT许可，完整文本位于 `third_party/cupertino_icons/LICENSE`。 |
| Gradle 8.14 wrapper与构建工具 | 发行版使用Apache-2.0及原文件记载的第三方条款，完整原根许可文件位于 `third_party/gradle/LICENSE`。 |
| Roboto Variable 字体 | Google Fonts / Roboto，SIL OFL 1.1；完整文本 `third_party/roboto/OFL.txt`，资源 `assets/fonts/Roboto-Variable.ttf`。仅用于让示例的英文UI使用本地字体。 |

Flutter固定版本源码： https://github.com/flutter/flutter/tree/3.38.7 ，提交 `3b62efc2a3da49882f43c372e0bc53daef7295a6`。
Roboto来源： https://github.com/google/fonts/tree/main/ofl/roboto ，字体SHA256 `d7598e12c5dbef095ff8272cfc55da0250bd07fbdecbac8a530b9b277872a134`。运行时导出继续保留Flutter生成的NOTICES，不以本文件代替包内许可证。


2026-10-27：依赖锁由上述固定官方SDK的真实Ubuntu CI生成，24个hosted包的官方pub.dev元数据与完整压缩包SHA256全部核对；逐包完整原LICENSE保存在`third_party/dart-packages/`，版本、来源、哈希与许可证路径见[inventory](third_party/dart-packages/inventory.json)。其中开发/测试依赖也保留许可，不将其称为应用自有代码；SDK组件由原Flutter许可覆盖。下载缓存和包源码不进入Git。
