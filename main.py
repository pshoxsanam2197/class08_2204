# 7-m
class Kitob:
    def och(self):
        print( "Kitob ochildi")

    def oqi(self):
        self.och()
        print( "Kitob o‘qilmoqda")

    def yop(self):
        self.oqi()
        print(  "Kitob yopildi")

h1 = Kitob()
h1.och()
print("---------")
h1.oqi()
print("---------")
h1.yop()
