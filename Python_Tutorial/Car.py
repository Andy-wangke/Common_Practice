#
class Car():
    '''
    this is description

    '''
    def __init__(self,make,model,year,odometer_reading=0):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=odometer_reading

    def get_description_name(self):
         long_name=str(self.year)+' '+self.make+' '+self.model
         return long_name.title() #title()

    def reading_odometer(self):
        print("this car has "+ str(self.odometer_reading)+' miles on it.')
        
    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print('You cannot roll back an odometer. Inserted:'+mileage)
    def increase_odometer(self,miles=0):
        self.odometer_reading+=miles

new_Car=Car('audi','a4',2017)
print(new_Car.get_description_name())
new_Car.reading_odometer()
new_Car.update_odometer(23)
new_Car.reading_odometer()
new_Car.update_odometer(24)

#
class Battery():
    """battery simulation"""
    def __init__(self,battery_size=70):
        self.battery_size=battery_size

    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kWh battery.")
        
#
class Electric(Car):#need to insert parent object
    """ Electric extends Car object"""
    #    def __init__(self,make,model,year,battery_size=0):
    #       super().__init__(make,model,year)
    #       self.battery_size=battery_size
        
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()

    def fetch_battery(self):
        print("This car has a "+str(self.battery_size)+"-kWh battery.")

my_tesla=Electric('tesla','model s',2017)
print(my_tesla.get_description_name())
#my_tesla.fetch_battery()



my_tesla=Electric('tesla','model s',2017)
my_tesla.battery.describe_battery()
        
