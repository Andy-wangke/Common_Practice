
class Calendar():
    months_days = (31,28,31,30,31,30,31,31,30,31,30,31)

    def __init__(self,day=1,month=1,year=1900):
        self.day=day
        self.month=month
        self.year=year

    def leapyear(self,year):
        if year % 4:
            #not a leap year
            return 0
        else:
            if year%100:
                return 0
            else:
                if year% 400:
                    return 0
                else:
                    return 1

    def set(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year

    def get():
        return (self,self.day,self.month,self.year)
    def advance(self):
        months=Calendar.months_days
        max_days=months[self.month-1]
        if self.month ==2:
            max_days+=self.leapyear(self.year)
        if self.day==max_days:
            self.day=1
            if self.month==12:
                self.month=1
                self.year+=1
            else:
                self.month+=1
        else:
            self.day+=1

    def __str__(self):
        return str(self.day)+'/'+str(self.month)+'/'+str(self.year)

    
if __name__=='__main__':
    calendar=Calendar()
    print(calendar)
    calendar.advance()
    print(calendar)

        
