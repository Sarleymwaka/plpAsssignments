class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

    def make_call(self, contact):
        print(f"{self.model} is calling {contact}... ")

    def charge(self, amount):
        self.battery += amount
        if self.battery > 100:
            self.battery = 100
        print(f"{self.model} charged to {self.battery}% 🔋")

    def show_details(self):
        print(f"{self.brand} {self.model} - Storage: {self.storage}GB, Battery: {self.battery}%")

class GamingPhone(Smartphone):
    def init(self, brand, model, storage, battery, refresh_rate):
        super().init(brand, model, storage, battery)
        self.refresh_rate = refresh_rate

    def play_game(self, game_name):
        if self.battery < 20:
            print(f"Battery too low to play {game_name}. Please charge!")
        else:
            print(f"Playing {game_name} at {self.refresh_rate}Hz refresh rate!")

    def show_details(self):
        print(f"Gaming Phone - {self.brand} {self.model} ({self.refresh_rate}Hz)")
        super().show_details()


phone1 = Smartphone("Samsung", "Galaxy A55", 128, 75)
phone2 = GamingPhone("ASUS", "ROG 7", 256, 50)

phone1.show_details()
phone1.make_call("Alice")
phone1.charge(15)

print() 
phone2.show_details()
phone2.play_game("Call of Duty")