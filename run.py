import os
import pytest
import shutil

if __name__ == '__main__':
    # 配置测试结果原始数据 (Results) 与最终报告 (Report) 的存放路径
    results_dir = 'report/allure-results'
    report_dir = 'report/html'

    # 环境预处理：清理历史执行产生的测试工件，确保报告数据唯一性
    if os.path.exists(results_dir):
        shutil.rmtree(results_dir)
    if os.path.exists(report_dir):
        shutil.rmtree(report_dir)

    # 启动 Pytest 执行引擎，运行全量测试用例并持久化原始测试数据
    print("🚀 开始执行自动化测试...")
    pytest.main([
        "-s", "-v",
        "./tests",
        f"--alluredir={results_dir}",
        "--clean-alluredir"
    ])

    # 调用 Allure 命令行工具，将原始 JSON 数据编译为静态 HTML 可视化报告
    print("\n📊 正在生成测试报告...")
    os.system(f"allure generate {results_dir} -o {report_dir} --clean")

    print(f"\n✅ 全部完成！")
    print(f"👉 报告所在路径: {os.path.abspath(report_dir)}")
    print(f"👉 如果要预览报告，请运行: allure serve {results_dir}")