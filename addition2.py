class Addition:
    def add(self,a=0,b=0,c=0,d=0):
        print("Sum =",(a+b+c+d))

a = Addition()
a.add()
a.add(10)
a.add(10,20)
a.add(10,20,30)
a.add(10,20,30,40)