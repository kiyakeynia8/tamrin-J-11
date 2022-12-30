class Fraction:
    def __init__(self,ss,mm):
        self.s = ss
        self.m = mm

    def sum(self,f2):
        s = self.s * f2.m + self.m * f2.s
        m = self.m * f2.m
        x = Fraction(s,m)
        return x
        
    def mul(self,f1):
        result_s = f1.s * self.s
        result_m = f1.m * self.m
        x = Fraction(result_s, result_m)
        return x

    def sub(self,f2):
        s = self.s * f2.m - self.m * f2.s
        m = self.m * f2.m
        x = Fraction(s,m)
        return x

    def div(self,f1):
        s = f1.s * self.m
        m = self.s * f1.m
        x = Fraction(s, m)
        return x

    def show(self):
        print(self.s,"/",self.m)

    def f_t_n(self,f1): 
        x = self.s / self.m
        c = f1.s / f1.m
        x_c = Fraction(x, c)
        return x_c

    def sim(self,f1):
        for i in range(2,f1.m):
            if f1.s % i == 0 and f1.m % i == 0:
                x = Fraction(int(f1.s / i),int(f1.m / i))
                return x
        else:
            x = Fraction(f1.s,f1.m) 
        return x
            

a = Fraction(25,15)
a.show()

b = Fraction(10,3)
b.show()

z = b.mul(a)
z.show()

d = a.sum(b)
d.show()

w = a.sub(b)
w.show()

e = b.div(a)
e.show()

q= b.f_t_n(a)
q.show()

t = b.sim(a)
t.show()

