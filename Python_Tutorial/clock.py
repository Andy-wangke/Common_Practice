class Clock():

    def __init__(self,hours=0,minutes=0,seconds=0):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds

    def set(self,hours,minutes,seconds=0):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds

    def tick(self):
        """Time will be advanced by one second"""
        if self.seconds==59:
            self.seconds=0
            if self.minutes==59:
                self.minutes=0
                self.hours=0 if self.hours==23 else self.hours
            else:
                self.minutes+=1
        else:
            self.seconds+=1

            
    def display(self):
        print('%d:%d:%d' % (self.hours,self.minutes,self.seconds))

    def __str__(self):
        return "%2d:%2d:%2d" % (self.hours,self.minutes,self.seconds)

clock=Clock()
print(clock)

seconds=10001
for i in range(seconds):
    clock.tick()
print(seconds,' equals ',clock)
                
