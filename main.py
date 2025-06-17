import os
from pathlib import Path
import platform


#检测启动器
def check_file_existence(file_path: str) -> None:
    """检查文件是否存在并输出结果"""
    # 处理用户主目录缩写 ~
    expanded_path = os.path.expanduser(file_path)
    
    # 检查文件是否存在
    if os.path.exists(expanded_path):
        if os.path.isfile(expanded_path):
            print(f"✅ 文件 '{expanded_path}' 存在")
            # 输出文件详细信息
            file_size = os.path.getsize(expanded_path)
            print(f"   - 文件大小: {file_size} 字节")
            print(f"   - 绝对路径: {Path(expanded_path).resolve()}")
        else:
            print(f"❌ '{expanded_path}' 存在，但它是一个目录")
    else:
        print(f"❌ 文件 '{expanded_path}' 不存在")
        exit()

def command(command = ""):
    os.system(command)
    return 0
def gpf():
    print("0.退出")
    print("1.查看可以安装的版本")
    print("2.安装版本")
    print("3.启动游戏")
    print("4.删除配置文件")
    print("5.补全资源、依赖库或原生依赖库")
    print("6.删除版本")
    print("7.自定义指令，输入':qw'退出")
    print("8.删除.minecraft文件夹")
    print("9.更多")
def start():
    game = "True"
    while game == "True":
        command("cls")
        gpf()              
        input1 = input(">")
        if input1 == "0":
            exit()
        if input1 == "1":
            command("cls")
            command("cmcl install --show=all")
            input1 = input("请按任意键。")
        if input1 == "2":
            command("cls")
            command("cmcl install --show=all")
            version = input("请输入版本:")
            command("cmcl install " + version)
            input1 = input("请按任意键。")
        if input1 == "3":
            command("cls")
            command("cmcl -l")
            input1 = input("输入版本:")
            command("cls")
            command("cmcl " + input1)
            input1 = input("请按任意键。")
        if input1 == "4":
            command("del cmcl.json")
            print("已删除")
            input1 = input("请按任意键。")
        if input1 =="5":
            command("cls")
            command("cmcl -l")
            input1 = input("输入版本:")
            command("cmcl version "+input1+" --complete=assets")
            command("cmcl version "+input1+" --complete=libraries")
            command("cmcl version "+input1+" --complete=natives")
            print("成功")
            input1 = input("请按任意键。")
        if input1 =="6":
            command("cls")            
            command("cmcl -l")
            input1 = input("输入版本:")
            command("cmcl version "+input1+" -d")
            print("成功")
            input1 = input("请按任意键。")
        if input1 =="7":
            command("cls")    
            command_True = "true"
            while command_True =="true":
                input1 = input("$cmcl/:>")
                if input1 ==":qw":
                    command_True = "false"
                else:
                    print("正在执行中。。。")
                    command("cmcl "+input1)
                    print("执行完毕。")
            print("已退出")
        if input1 =="8":
            command("cls")
            input1 = input("你确认删除吗？(Y/N)")
            if input1 == "y"or"Y":
                command("rd /s .minecraft")
                print("OK!!!")
                input1 = input("请按任意键。")
            else:
                if input1 == "n"or"N":
                    input1 = input("请按任意键。")
                else:
                    input1 = input("请按任意键。")
        if input1 =="9":
            command("cls")
            print(
                "            版本：1.0.0"+"\n                  "+
                "           cmcl of pycmd 我的世界启动器        "
            )
            input1 = input("请按任意键。")

# 执行检查
if platform.system() =="Windows":
    check_file_existence("cmcl.com") 
    start()
else:
    print("必须是Windows系统，否则命令无法运行。")
    input("请按任意键。")
