import time
import sys, os
import main as rm


class Settings():
    def __init__(self):
        self.config_file = open("cgf.csv", 'a+')

    def set_code_menu(self):
        self.choices = {
            "1": self.check_code,
            "2": self.set_code,
            "3": self.del_code,
            "0": self.re_menu
        }
        os.system('cls')
        print("""
        设置基金代码与金额:
        1. 【查询】基金代码和持有金额
        2. 【添加】基金代码和持有金额
        3. 【删除】基金代码和持有金额
        0. 返回【主菜单】
        """)
        choice = input("请输入一个序号： ")
        action = self.choices.get(choice)
        if action:
            action()
        else:
            print("{0} 不能作为合法输入！".format(choice))
            command = input("\n" + "输入任意键返回！")


    def check_code(self):
        os.system('cls')
        print("您持有的基金：" + "\n")
        f = open("cgf.csv", 'r')
        lines = f.readlines()
        for line in lines:
            name, amount = line.split(",")
            name = name.strip()
            amount = amount.strip()
            print("基金代码: ", name, ", 持有金额: ", amount, "元" + "\n")
        f.close()
        command = input("\n" + "输入任意键返回！")

    def set_code(self):
        os.system('cls')
        print("您持有的基金：")
        f = open("cgf.csv", 'a+')
        content = input("请输入代码和金额，用空格隔开:")
        name, amount = content.split(" ")
        name = name.strip()
        amount = amount.strip()
        amount_judge = amount
        if name.isdigit() and len(name) == 6 and amount_judge.replace(".", "").isdigit():
            f.write('\n' + name + "," + amount)
            f.close()
            print("成功添加基金代码: ", name, ", 金额: ", amount, "元")
        else:
            print("基金代码或金额输入错误！")
        command = input("\n" + "输入任意键返回！")

    def del_code(self):
        os.system('cls')
        print("您持有的基金：" + "\n")
        f = open("cgf.csv", 'r')
        lines = f.readlines()
        for line in lines:
            name, amount = line.split(",")
            name = name.strip()
            amount = amount.strip()
            print("基金代码: ", name, ", 持有金额: ", amount, "元" + "\n")
        f.close()
        content = input("请输入想要删除的基金代码:")
        code = content.strip()
        f = open("cgf.csv", 'w')
        for line in lines:
            name, amount = line.split(",")
            if code != name:
                f.write((name + "," + amount).strip())
        print("\n" + "成功删除基金代码: ", code)
        f.close()
        command = input("\n" + "输入任意键返回！")


    def re_menu(self):
        os.system('cls')
        pass



class Menu():
    def __init__(self):
        self.Settings = Settings()
        self.rm = rm.Main()
        self.choices = {
            "1": self.rm.run,
            "2": self.Settings.set_code_menu,
            "0": self.quit
        }

    def display_menu(self):
        os.system('cls')
        print("""
        Yuan的实时基金监控系统:
        1. 基金实时监控程序
        2. 设置基金代码与持有金额
        0. 退出
        """)

    def run(self):
        while True:
            self.display_menu()
            try:
                choice = input("请输入一个序号： ")
            except Exception as e:
                print("请输入合理数字序号！")
                command = input("\n" + "输入任意键返回！");continue


            choice = str(choice).strip()
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} 不能作为合理输入！".format(choice))

    def quit(self):
        os.system('cls')
        print("\n您已安全退出设置程序！\n")
        sys.exit(0)


if __name__ == '__main__':
    Menu().run()
