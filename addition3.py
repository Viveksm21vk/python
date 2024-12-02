class Addition:
    def add(self,*args):
        print("Sum =",sum(args))

a = Addition()
a.add()
a.add(10)
a.add(10,20)
a.add(10,20,30)
a.add(10,20,30,40)