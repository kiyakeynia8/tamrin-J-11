class Time:
    def __init__(self,hh,mm,ss):

        self.hour = hh
        self.minute = mm
        self.secound = ss
        self.fix()

    def show(self):
        print(self.hour,":",self.minute,":",self.secound)

    def sum(self,other):
        s_new = self.secound + other.secound
        m_new = self.minute + other.minute
        h_new = self.hour + other.hour
        result = Time(h_new, m_new, s_new)
        return result
    
    def seb(self,other):
        s_new = self.secound - other.secound
        m_new = self.minute - other.minute
        h_new = self.hour - other.hour
        result = Time(h_new, m_new, s_new)
        return result

    def fix(self):
        if self.secound >= 60:
            self.secound -= 60
            self.minute += 1

        if self.minute >= 60:
            self.minute-= 60
            self.hour+= 1

        if self.secound < 0:
            self.secound+=60
            self.minute-=1

        if self.minute < 0:
            self.minute += 60
            self.hour -= 1

    def t_to_s(self,other):
        minute1 = (self.hour * 60) + self.minute
        secound1 = (minute1 * 60+self.secound)
        minute2 = (other.hour * 60) + other.minute
        secound2 = (minute2 * 60 + other.secound)
        return secound1 , "and" , secound2

    def s_to_t(self):
        hour = self.secound // 3600
        minute = (self.secound % 3600) // 60
        secound = (self.secound % 3600) % 60
        x = Time(hour, minute, secound)
        return x

t_t = Time(0, 0, 7342)

t1 = Time(3, 75, 17)
t1.show()

t2 = Time(3, 50, 26)
t2.show()

t3 = t1.sum(t2)
t3.show()

t4 = t1.seb(t2)
t4.show() 

t5 = t1.t_to_s(t2)
print(t5)

t6 = t_t.s_to_t()
t6.show()