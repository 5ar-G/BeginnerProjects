class CAR:
    def __init__(self, model, year, miles, for_sale):

        self.model =model
        self.year = year
        self.miles = miles
        self.for_sale = for_sale

car1 = CAR("BMW",2020, 120000, True)
        
print(car1.model)