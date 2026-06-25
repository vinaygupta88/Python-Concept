class Vinay:
    def fun(self):
        print("Vinay fun karne VGI gaya")

class Shivang:
    def fun(self):
        print("Shivang fun karne VGI gaya")

class Friends(Vinay, Shivang):
    pass

f = Friends()
f.fun()
