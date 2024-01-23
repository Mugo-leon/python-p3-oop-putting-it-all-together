# shoe.py

class Shoe:
    def __init__(self, brand=None, size=None):
        self._brand = brand
        self._size = size
        self._condition = None  # Initialize _condition attribute

    @property
    def brand(self):
        return self._brand

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        try:
            int(value)  # Attempt to convert to an integer
        except ValueError:
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        print("Your shoe is as good as new!")  # Update the output message
        self._condition = "New"  # Set _condition to "New" after repair

    @property
    def condition(self):
        return self._condition

