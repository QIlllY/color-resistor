class Resistor:
    def __init__(self, color_code):
        self.color_code = color_code
        self.color_bands = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
                            "green": 5, "blue": 6, "violet": 7, "gray": 8, "white": 9}
        self.multiplier_bands = {"pink": 0.001, "silver": 0.01, "gold": 0.1, "black": 1, "brown": 10,
                                 "red": 100, "orange": 1000, "yellow": 10000, "green": 100000,
                                 "blue": 1000000, "violet": 10000000, "gray": 100000000, "white": 1000000000}
        self.tolerance_bands = {"silver": 10, "gold": 5, "brown": 1, "red": 2, "green": 0.5,
                                "blue": 0.25, "violet": 0.1, "gray": 0.05}

        self.parse_color_code()
        self.calculate_resistance()
        self.calculate_tolerance()

    def parse_color_code(self):
        self.band1 = self.color_bands[self.color_code.split()[0]]
        self.band2 = self.color_bands[self.color_code.split()[1]]
        self.band3 = self.multiplier_bands[self.color_code.split()[2]]
        self.band4 = self.tolerance_bands.get(self.color_code.split()[3], None)

    def calculate_resistance(self):
        resistance = (self.band1 * 10 + self.band2) * self.band3
        if resistance >= 1000000:
            self.resistance = str(resistance / 1000000) + "M"
        elif resistance >= 1000:
            self.resistance = str(resistance / 1000) + "k"
        else:
            self.resistance = str(resistance)

    def calculate_tolerance(self):
        if self.band4 is not None:
            self.tolerance = str(self.band4) + "%"
        else:
            self.tolerance = "unknown"

    def get_resistance(self):
        return self.resistance

    def get_tolerance(self):
        return self.tolerance


if __name__ == '__main__':
    resistor = Resistor("brown gray orange gold")
    print("Resistance: ", resistor.get_resistance())
    print("Tolerance: ", resistor.get_tolerance())
