# Python Learning

从零开始学习 Python 的练习项目集合。覆盖知识点：基础语法、函数与模块、核心数据结构、面向对象、异常处理、HTTP请求、NumPy、项目工程化、日志与测试、CLI 工具。

## 项目列表

| 文件 | 知识点 | 说明 |
|---|---|---|
| `hello.py` | 变量、输入输出、类型转换、条件判断 | 第一个 Python 程序，输入姓名年龄输出欢迎语 |
| `stats.py` + `main.py` | 函数定义、模块导入、字典统计、文件读写 | 单词频率统计器，读取文本文件输出 Top10 |
| `grades.py` | 字典/列表增删查、排序、lambda | 学生成绩管理系统，7 个功能菜单 |
| `calc.py` | 异常处理、文件追加写入 | 交互式计算器，结果追加到 result.txt |
| `fib.py` | 递归函数 | 斐波那契数列递归实现 |
| `library.py` | 类与对象、`__init__`、`__str__` | 图书馆借书系统，Book + Library 类 |
| `weather.py` | HTTP 请求、API 调用、JSON | 天气查询工具，调用 wttr.in 免费 API |
| `numpy_demo.py` | NumPy 数组、矩阵运算、速度对比 | 纯 Python 与 NumPy 性能对比演示 |
| `test_grades.py` | 单元测试、unittest | 学生成绩系统的核心函数测试 |
| `library_project/` | 项目工程化、src 布局、pyproject.toml | 图书馆项目打包为可安装包 |
| `todo_project/` | argparse CLI、JSON 持久化、完整测试 | 待办清单命令行工具 |

## 环境要求

- Python 3.10+
- 第三方依赖：`requests`、`numpy`（按需安装）

```bash
pip install requests numpy
```
