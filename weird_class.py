# https://quera.org/problemset/16396
# ----------------------------------


class Foo:
    def __init__(self) -> None:
        self.x: int = 0

    @property
    def x(self):
        """Getter for x"""
        return self._x

    @x.setter
    def x(self, value):
        """Setter for x with custom logic"""
        if value >= 0:
            # If non-negative, store the last two digits as an int
            self._x = int(value) % 100
        else:
            # If negative, store -1
            self._x = -1
