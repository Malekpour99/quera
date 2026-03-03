# https://quera.org/problemset/129729?tab=description
# ---------------------------------------------------


class Chain:
    def __init__(self, initial_value):
        if isinstance(initial_value, (int, float)):
            self._acceptable_types = (int, float)
        elif isinstance(initial_value, str):
            self._acceptable_types = (str,)
        else:
            raise Exception("invalid operation")

        self._value = initial_value

    def __call__(self, call_value):
        if not isinstance(call_value, self._acceptable_types):
            raise Exception("invalid operation")

        if self._acceptable_types == (int, float):
            self._value += call_value
        elif self._acceptable_types == (str,):
            self._value += " " + str(call_value)
        return self

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        if self._acceptable_types == (int, float):
            # For numbers, return without quotes and clean up .0 for integers
            if isinstance(self._value, float) and self._value.is_integer():
                return str(int(self._value))
            return str(self._value)
        else:
            # For strings, return with quotes
            return repr(str(self._value))

    def __eq__(self, other):
        if not isinstance(other, self._acceptable_types):
            raise Exception("invalid operation")

        if self._acceptable_types == (int, float):
            return float(self._value) == float(other)
        elif self._acceptable_types == (str,):
            return str(self) == str(other)
        else:
            raise Exception("invalid operation")
