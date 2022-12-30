class Mixed_number:
    def __init__(self,c_n,ss,mm):
        self.complete_number = c_n
        self.sorat = ss
        self.makhraj = mm
        self.fix()

    def show(self):
        print(self.complete_number,self.sorat,"/",self.makhraj)

    def fix(self):
        if self.sorat > self.makhraj:
            self.sorat-=self.makhraj
            self.complete_number+=1

    def sum(self,b):
        sorat = self.sorat * b.makhraj + self.makhraj * b.sorat
        makhraj = self.makhraj * b.makhraj
        complete_number = self.complete_number + b.complete_number
        if sorat > makhraj:
            sorat-=makhraj
            complete_number+=1
        x = Mixed_number(complete_number, sorat, makhraj)
        return x

    def mul(self,b):
        complete_number = 0
        c_2_s = (self.complete_number*self.makhraj)+self.sorat
        c_1_s = (b.complete_number*b.makhraj)+b.sorat
        multiplication_s = c_1_s * c_2_s
        multiplication_m = self.makhraj * b.makhraj
        complete_number = multiplication_s // multiplication_m
        multiplication_s = multiplication_s % multiplication_m

        x = Mixed_number(complete_number,multiplication_s, multiplication_m)
        return x

    def sub(self,b):
        c_1_s = self.sorat * b.makhraj
        c_1_m = self.makhraj * b.makhraj
        c_2_s = b.sorat * self.makhraj
        c_2_m = c_1_m

        if c_1_s >= c_1_m:
            c_1_s-=c_1_m
            self.complete_number+=1
        if c_2_s >= c_2_m:
            c_2_s-=c_2_m
            b.complete_number+=1

        complete_number = self.complete_number - b.complete_number
        sub_s = c_1_s - c_2_s
        sub_m = c_1_m

        x = Mixed_number(complete_number, sub_s, sub_m)
        return x


a  = Mixed_number(3, 5, 4)
a.show()

b = Mixed_number(4, 3, 8)
b.show()

c = b.sum(a)
c.show()

d = b.mul(a)
d.show()

e = b.sub(a)
e.show()