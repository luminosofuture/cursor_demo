# 测试Python脚本：输出系统信息与目录文件
import time
import platform
import os

# 输出欢迎语
print("=== 测试脚本运行结果 ===")
print(f"欢迎语：Hello from Ubuntu & VS Code")
print(f"当前时间：{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
print(f"Ubuntu主机名：{platform.node()}")
# 遍历当前目录文件
print("\n当前目录下的文件：")
for file_name in os.listdir("./"):
    print(f"- {file_name}")