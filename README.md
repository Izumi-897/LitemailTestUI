# 电商系统 UI 自动化测试实战 (Mobile Web)

本仓库基于 **Python + Selenium + Pytest** 框架，针对全栈电商系统的移动端 H5 核心业务流程实现了 UI 自动化测试。项目旨在通过 **Page Object Model (POM)** 设计模式提升脚本复用性，并解决移动端组件库（Vant UI）在异步渲染下的交互稳定性问题。

---

## 🛠️ 技术栈
- **测试框架**: Pytest (支持参数化及 Fixture 管理)
- **自动化工具**: Selenium WebDriver
- **页面模型**: Page Object Model (POM)
- **仿真配置**: Chrome Mobile Emulation (模拟 iPhone 12 Pro)
- **测试报告**: Allure Report
- **持续集成思路**: 遵循 Git 版本控制及标准化脚本迭代流程

---

## 🌟 项目核心设计
- **POM 深度实践**: 将页面元素定位与业务操作解耦，封装了 BasePage 通用基类，大幅降低后期维护成本。
- **异步交互优化**: 针对 Vue + Vant UI 框架导致的元素陈旧（StaleElementReferenceException）及 UI 遮罩层问题，封装了基于 JavaScript 的事件分发（Event Dispatching）与显式等待逻辑，确保测试稳定性。
- **移动端仿真**: 通过 WebDriver 配置移动端仿真模式，真实复现 H5 端的触摸交互行为。
- **失败现场溯源**: 集成 Pytest Hook 钩子函数，实现在测试失败时自动捕获页面快照并嵌入 Allure 报告，快速定位故障根源。

---

## 📂 项目结构
```text
.
├── pages/                  # Page Object 表现层
│   ├── base_page.py        # 基础封装：JS 注入、显式等待、异常重试
│   ├── login_page.py       # 登录模块：账号鉴权与状态校验
│   ├── address_page.py     # 地址模块：复杂表单填充与弹出层处理
│   └── search_page.py      # 商品模块：搜索入口跳转与结果匹配
├── tests/                  # 测试执行层
│   ├── test_login.py       # 登录功能场景化测试
│   ├── test_address.py     # 地址簿全链路增删改查测试
│   └── test_search.py      # 商品检索与列表刷新验证
├── report/                 # 测试报告工件
├── conftest.py             # Pytest 全局配置：Driver 初始化、截图钩子
├── main.py                 # 项目一键运行入口
└── pytest.ini              # Pytest 运行参数配置
```

## 📊 测试结果展示 (Allure Report)

> **报告存放说明**：本项目生成的 Allure 原始数据存放在 `report/` 目录下。

#### 测试概览
以下为自动化测试执行的 Dashboard 统计：
![Allure Dashboard](report/screenshots/首页概览.png)

#### 详细执行轨迹
报告详细记录了接口的 Request 参数、Response 返回以及每一步的业务逻辑断言。
![Allure Detail](report/screenshots/用例详情.png)

### 项目声明：本仓库代码仅用于个人测试开发技能的实践与展示。