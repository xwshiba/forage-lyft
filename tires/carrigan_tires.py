from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, tires_wear_array):
        self.tires_wear_array = tires_wear_array

    def needs_service(self):
        for tire in self.tires_wear_array:
            if tire >= 0.9:
                return True
        return False
        