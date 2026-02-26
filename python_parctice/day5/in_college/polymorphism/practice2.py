class Vehicle:
    def __init__(self, vehicle_id, brand):
        self.vehicle_id = vehicle_id
        self.brand = brand

    def calculate_rent(self, time):
        return "select a proper vehicle"

# %%
class Car(Vehicle):
    def __init__(self, vehicle_id, brand, price_per_day):
        super().__init__(vehicle_id, brand)
        self.price_per_day = price_per_day
    def calculate_rent(self, day):
        return day*self.price_per_day

#%%
class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, price_per_hour):
        super().__init__(vehicle_id, brand)
        self.price_per_hour = price_per_hour
    def calculate_rent(self, hour_driven):
        return hour_driven*self.price_per_hour

# %%
class Truck(Vehicle):
    def __init__(self, vehicle_id, brand, price_per_km):
        super().__init__(vehicle_id, brand)
        self.price_per_km = price_per_km
    def calculate_rent(self, driven_km):
        return driven_km*self.price_per_km
# %%
t1 = Truck('WBO7J7651','mahindra', 100 )
print(t1.calculate_rent(100))

v1 = Vehicle('ojh687684','suzuki')
print(v1.calculate_rent(23))
