# BrainBoost Flutter · 初始化计数器骨架

**这是处于初始化阶段的 Flutter 模板项目，尚未实现脑训练功能。** 它与另一个 [BrainBoost React/Vite 网页小游戏](https://github.com/yangwei251003/brainboost) 是不同工程，不能互相替代。

[计数器示例预览](https://yangwei251003.github.io/brainboost-flutter/) · [新增自有内容MIT](LICENSE) · [模板/字体/第三方协议](THIRD_PARTY_NOTICES.md)

![由CI实际运行Web导出后生成的计数器截图](https://yangwei251003.github.io/brainboost-flutter/preview.png)

图片由发布流程实际打开Flutter构建后生成。首次CI及Pages部署成功前，预览与图片尚不可用；不以静态设计稿替代运行截图。

## 当前具备什么

- 原Flutter计数器界面：点击“+”增加计数，状态保存在当前页面内存中，刷新重置。
- Android、iOS、Linux、macOS、Windows、Web平台工程骨架。
- 原有1个widget测试，验证0 → 点击 → 1的计数行为。
- 新增明确阶段标记、本地Roboto字体、固定官方SDK的Web构建/检查与Pages流程。

**没有**记忆/反应训练游戏、AI模型、登录、账号、积分、支付、云数据库或长期历史统计；本仓库不宣传这些能力已完成。

## 最简运行

安装 [Flutter官方稳定SDK](https://docs.flutter.dev/install/archive)，本项目与CI固定使用 **Flutter3.38.7 / Dart3.10.7**。确认`flutter --version`和`flutter doctor`，并安装Chrome。

```bash
git clone https://github.com/yangwei251003/brainboost-flutter.git
cd brainboost-flutter
flutter pub get --enforce-lockfile
flutter run -d chrome
```

不需要`.env`、模型密钥、账号或数据库。需要其他平台时运行`flutter devices`后选择目标；Android另需Android SDK/JDK，Windows另需Visual Studio C++桌面工具链，iOS/macOS需对应Apple环境。它们的安装包和真机行为本轮没有验收。

## 测试与Web导出

```bash
flutter analyze
flutter test
flutter build web --release --base-href /brainboost-flutter/ --no-web-resources-cdn
```

`build/web`是部署成品，由CI构建后作为Pages制品保存；源码仓库保留Dart、平台工程、锁文件与必要资产，不提交SDK、依赖缓存、签名文件或构建临时目录。若部署在域名根路径，将`--base-href`改为`/`，使用HTTP服务器打开构建结果。

`.github/workflows/pages.yml`从官方Flutter仓库获取固定版本并核对提交SHA，执行依赖锁定安装、分析、原widget测试与Web构建，再用真实Chromium检查加载并生成桌面/手机截图。该流程需要成功运行后才能将CI状态记为已通过，单有工作流文件不代表测试已执行。

## 目录

```text
lib/main.dart       明确标注为骨架的计数器
test/               原widget测试
android/ ios/       移动平台工程
linux/ macos/ windows/ 桌面平台工程
web/                Web宿主与默认图标
assets/fonts/       本地OFL字体
third_party/        完整来源许可文本
scripts/            CI浏览器加载与真实截图检查
```

## 本轮记录与计划

2026-10-26：从本地独立Flutter目录归档，核对当前实际为默认计数器；过滤IDE、SDK个人路径、生成配置、缓存和临时构建输出，保留完整平台骨架及锁文件，补全来源说明。原文件保持只读。

**本机限制：** flutter/dart不在PATH；原缓存指向的SDK目录现已不存在，也没有可核对的Web导出。因此本轮没有在本机运行Flutter分析、widget测试、Web或原生编译，不编造本机运行结果；CI将承担可复现验证并产出真实截图。新增浏览器脚本只有在CI执行后才有运行结果。

后续先明确Flutter产品需求，再逐项实现功能与测试。当前项目应分类为“开发中 / 初始化骨架”；没有原生平台打包、签名或发布记录，暂不列入本地可删除清单。


## CI锁文件与字体复现记录

2026-10-27：原Windows镜像锁文件与固定SDK不兼容，首次严格安装明确失败；没有把失败记作通过。随后在[隔离恢复分支的实际Ubuntu CI](https://github.com/yangwei251003/brainboost-flutter/actions/runs/40357307684)用同一个官方SDK生成锁，依赖解析、分析、原widget测试、Web构建、桌面/手机渲染和0→1点击均通过。本机仍未安装Flutter；这些是CI结果。

24个hosted依赖的完整包SHA256已与[pub.dev](https://pub.dev/)官方元数据逐项核对，完整许可随源码保存。使用镜像环境时请注意锁定来源为pub.dev；[Dart官方锁文件说明](https://dart.dev/tools/pub/cmd/pub-get)解释了严格锁的作用。正式工作流继续使用`--enforce-lockfile`，不会每次静默重新选版。

首次恢复实测仍有一次默认Roboto外部下载。依据[该固定Flutter版本的CanvasKit源码](https://github.com/flutter/flutter/blob/3.38.7/engine/src/flutter/lib/web_ui/lib/src/engine/canvaskit/fonts.dart#L89-L107)，引擎按字体族名`Roboto`判断本地默认字体是否存在；本次将本地OFL字体注册名改为该名字，并把真实浏览器检查收紧为外部请求必须为零。这项字体修正已由[正式CI](https://github.com/yangwei251003/brainboost-flutter/actions/runs/40360380365)及[匿名Windows Chrome记录](docs/ONLINE_VERIFIED.json)确认：桌面/手机渲染、计数0→1、0页面错误、0失败资源、0外部请求。[当前发布浏览器记录](https://yangwei251003.github.io/brainboost-flutter/ci-browser-check.json)继续随正式部署生成。细节见[CI_RECOVERY.json](docs/CI_RECOVERY.json)。


网页制品通过`copy_web_licenses.py`一并保存全部原许可/字体OFL，逐文件核对原字节；公开入口为[网页完整许可目录](https://yangwei251003.github.io/brainboost-flutter/licenses/)。源码、24份Dart包许可与字体文件保留在Git，SDK/依赖缓存和编译临时目录不上传。
