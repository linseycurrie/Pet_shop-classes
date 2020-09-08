class PetShop:
    def __init__(self, name, pets, total_cash):
        self.name = name
        self.pets = pets
        self.total_cash = total_cash
        self.pets_sold = 0

    def stock_count(self):
        return len(self.pets)

    def increase_pets_sold(self):
        self.pets_sold += 1

    def increase_total_cash(self, amount):
        self.total_cash += amount

    def add_pet(self, pet):
        self.pets.append(pet)

    def remove_pet(self, pet):
        self.pets.remove(pet)

    def find_pet_by_name(self, pet_name):
        for pet in self.pets:
            if pet.name == pet_name:
                return pet    
    
    def sell_pet_to_customer(self, pet, customer):
        sell_pet = self.find_pet_by_name(pet)
        customer.pets.append(sell_pet)
        self.remove_pet(sell_pet)
        self.increase_pets_sold()
        self.increase_total_cash(sell_pet.price)
