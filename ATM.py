class NecobishiBank():

    # 口座の残高
    balance = 0

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        print(self.balance)
        print("100万引き出せた！")

    def send(self, amount):
        print("1円送金した！")

    def deposit(self, amount):
        print("5円預金した！")


shounandai_atm = NecobishiBank(100)
print("湘南台ATM: " + str(shounandai_atm.balance))


yokohama_atm = NecobishiBank(1000)
print("横浜ATM: " + str(yokohama_atm.balance))
