# 源码归档范围

按原Flutter模板的忽略规则归档 **139个文件**。初始审计复制145项，其中以下6项为可再生的构建辅助文件，不强制加入Git：

- Android `GeneratedPluginRegistrant.java`。
- iOS `GeneratedPluginRegistrant.h`、`GeneratedPluginRegistrant.m`。
- Android `gradlew`、`gradlew.bat`、`gradle-wrapper.jar`。

保留平台构建设置、Gradle配置和Wrapper properties。Flutter在插件解析或Android构建阶段生成相应胶水与辅助文件，普通使用者从README的Flutter命令进入。此文件本身增加一项说明，最终提交文件数以Git文件清单为准。

源项目是默认计数器初始化骨架；本机未装可用Flutter SDK，未声称完成本机原生打包或真机验证。GitHub工作流的真实分析、原widget测试、Web构建和浏览器截图结果待远端执行后记录。
