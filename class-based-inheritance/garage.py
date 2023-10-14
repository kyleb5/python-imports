class Rogue:
    def __init__(self, fuel_capcity, main_color, maxium_occupancy):
        self.fuel_capacity = fuel_capcity
        self.main_color = main_color
        self.maximum_occupancy = maxium_occupancy
        self.fuel_level = fuel_capcity

    def refuel_tank(self):
        self.fueL_level = self.fuel_capacity
        print(f"The {self.main_color} Rogue's fuel tank is now full.")

    def drive(self):
        if self.fuel_level > 0:
            print(f"The {self.main_color} Rogue is driving.")
            self.fuel_level -= 1
        else:
            print('The fuel tank is empty. Please refuel.')

    def turn(self, direction):
        print(f"The {self.main_color} Rogue turns {direction}")

    def stop(self):
        print(f"The {self.main_color} Rogue has gracefully stopped.")


class Tank:
    def __init__(self, fuel_capcity, main_color, maxium_occupancy):
        self.fuel_capacity = fuel_capcity
        self.main_color = main_color
        self.maximum_occupancy = maxium_occupancy
        self.fuel_level = fuel_capcity

    def refuel_tank(self):
        self.fueL_level = self.fuel_capacity
        print(f"The {self.main_color} Tank's fuel tank is now full.")

    def drive(self):
        if self.fuel_level > 0:
            print(f"The {self.main_color} Tank is driving.")
            self.fuel_level -= 1
        else:
            print('The fuel tank is empty. Please refuel.')

    def turn(self, direction):
        print(f"The {self.main_color} Tank turns {direction}")

    def stop(self):
        print(f"The {self.main_color} Tank has gracefully stopped.")


class M3:
    def __init__(self, fuel_capcity, main_color, maxium_occupancy):
        self.fuel_capacity = fuel_capcity
        self.main_color = main_color
        self.maximum_occupancy = maxium_occupancy
        self.fuel_level = fuel_capcity

    def refuel_tank(self):
        self.fueL_level = self.fuel_capacity
        print(f"The {self.main_color} M3's fuel tank is now full.")

    def drive(self):
        if self.fuel_level > 0:
            print(f"The {self.main_color} M3 is driving.")
            self.fuel_level -= 1
        else:
            print('The fuel tank is empty. Please refuel.')

    def turn(self, direction):
        print(f"The {self.main_color} M3 turns {direction}")

    def stop(self):
        print(f"The {self.main_color} M3 has gracefully stopped.")


my_rogue = Rogue(fuel_capcity=15, main_color="Black", maxium_occupancy=5)
my_tank = Tank(fuel_capcity=1, main_color="Pink", maxium_occupancy=125)
my_m3 = M3(fuel_capcity=15, main_color="Black", maxium_occupancy=4)


my_rogue.refuel_tank()
my_rogue.turn("Right")
my_rogue.drive()
my_rogue.refuel_tank()
my_rogue.drive()
my_rogue.stop()

my_tank.refuel_tank()
my_tank.turn("Right")
my_tank.drive()
my_tank.refuel_tank()
my_tank.drive()
my_tank.stop()

my_m3.refuel_tank()
my_m3.turn("Right")
my_m3.drive()
my_m3.refuel_tank()
my_m3.drive()
