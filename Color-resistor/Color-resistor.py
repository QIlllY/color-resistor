class Resistor:
    """
    A class representing a resistor with a given color code.

    Attributes:
    -----------
    color_code : str
        A string representing the color code of the resistor in the format "band1 band2 band3 band4",
        where band1 and band2 are the color bands indicating the significant digits, band3 is the color
        band indicating the multiplier, and band4 is the color band indicating the tolerance (optional).

    color_bands : dict
        A dictionary containing the numerical values for each color band indicating the significant
        digits of a resistor.

    multiplier_bands : dict
        A dictionary containing the multiplier values for each color band indicating the multiplier
        of a resistor.

    tolerance_bands : dict
        A dictionary containing the tolerance values for each color band indicating the tolerance of
        a resistor.

    band1 : int
        An integer representing the value of the first significant digit of the resistor.

    band2 : int
        An integer representing the value of the second significant digit of the resistor.

    band3 : float
        A floating-point number representing the multiplier value of the resistor.

    band4 : float or None
        A floating-point number representing the tolerance value of the resistor, or None if there
        is no fourth band indicating the tolerance.

    resistance : str
        A string representing the resistance value of the resistor in ohms, kilohms or megohms.

    tolerance : str
        A string representing the tolerance value of the resistor as a percentage, or "unknown" if
        there is no fourth band indicating the tolerance.
    """

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
        """
        Parse the color code string and assign the appropriate numerical values to the instance variables
        band1, band2, band3 and band4.
        """
        self.band1 = self.color_bands[self.color_code.split()[0]]
        self.band2 = self.color_bands[self.color_code.split()[1]]
        self.band3 = self.multiplier_bands[self.color_code.split()[2]]
        self.band4 = self.tolerance_bands.get(self.color_code.split()[3], None)

    def calculate_resistance(self):
        """
        Calculates the resistance value of the resistor based on its color code.
        """
        resistance = (self.band1 * 10 + self.band2) * self.band3
        if resistance >= 1000000:
            self.resistance = str(resistance / 1000000) + "M"
        elif resistance >= 1000:
            self.resistance = str(resistance / 1000) + "k"
        else:
            self.resistance = str(resistance)

    def calculate_tolerance(self):
        """
        Calculates the tolerance value of the resistor based on its color code.
        """
        if self.band4 is not None:
            self.tolerance = str(self.band4) + "%"
        else:
            self.tolerance = "unknown"

    def get_resistance(self):
        """
        Returns the resistance value of the resistor.
        """
        return self.resistance

    def get_tolerance(self):
        """
        Returns the tolerance value of the resistor.
        """
        return self.tolerance


if __name__ == '__main__':
    resistor = Resistor("brown gray orange gold")
    print("Resistance: ", resistor.get_resistance())
    print("Tolerance: ", resistor.get_tolerance())
