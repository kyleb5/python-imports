from appliances.kitchen.utility.dishwasher import DishWasher
from appliances.laundry.dryer import Dryer
from appliances.laundry.washer import Washer
from appliances.kitchen.utility.refrigerator import Refrigerator
from appliances.kitchen.coffeemaker import CoffeeMaker
from appliances.kitchen.can_opener import CanOpener

whirlpool_dishwasher = DishWasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red")
samsung_dryer = Dryer("red", "gas")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

can_opener = CanOpener("opened")
can_opener.open_can()
