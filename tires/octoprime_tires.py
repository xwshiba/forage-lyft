from tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, tires_wear_array):
        self.tires_wear_array = tires_wear_array

    def needs_service(self):
        if sum(self.tires_wear_array) >= 3.0:
            return True
        return False
    