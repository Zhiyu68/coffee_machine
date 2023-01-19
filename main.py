from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 根据*()蓝图 得到一个具体的 *
money_machine = MoneyMachine()
coffee_maker= CoffeeMaker()
menu = Menu()
# turn on
is_on = True

# 打开程序
while is_on:
    # 设置菜单变量
    # Object . Method
    options = menu.get_items()
    # options = "lette/espresso/capucchino"
    # 问问顾客要什么？（并列出菜单）
    choice = input(f"what would you like?({options}):")

    # 只有管理者才知道的string
    # 输入off,结束程序
    if choice == "off":
        is_on = False
    # 1. print report
    #  只有管理者才知道的string
    # 这里的report指的是administrator 知道的特定的string.可以随意命名。
    elif choice=="report":
        # Object . Method
        # Method:report() 指的是打印所有原材料
        money_machine.report()
        coffee_maker.report()
    else:
        # 顾客和管理者都可以操作
        # drink = 饮品名
        drink = menu.find_drink(choice)

        # 2. check resource_sufficient?
        # 检查是否足够的资源来制作当前的饮料,返回 True / None
        if coffee_maker.is_resource_sufficient(drink):

            # 通过一种method 实现两个需求：3. process coins & 4. check transaction successful?
            # make_payment function 已经包含了运行process_coins function
            # 比较机器 收到的钱 >= 应收钱
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
