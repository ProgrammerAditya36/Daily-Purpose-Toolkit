class Celsius:
    def __init__(self, user_value):
        self.user_value = user_value

    def ctoc(self, user_value):
        conversion = float(user_value)
        output = f"{conversion} °C"
        return output

    def ctof(self, user_value):
        conversion = float(user_value) * 9 / 5 + 32
        output = f"{round(conversion, 3)} °F"
        return output

    def ctok(self, user_value):
        conversion = float(user_value) + 273.15
        output = f"{conversion} °K"
        return output

    def ctor(self, user_value):
        conversion = float(user_value) * 9 / 5 + 491.67
        output = f"{round(conversion, 3)} °Ra"
        return output


class Fahrenheit:
    def __init__(self, user_value):
        self.user_value = user_value

    def ftoc(self, user_value):
        conversion = (float(user_value) - 32) * 5 / 9
        output = f"{round(conversion, 3)} °C"
        return output

    def ftof(self, user_value):
        conversion = float(user_value)
        output = f"{conversion} °F"
        return output

    def ftok(self, user_value):
        conversion = (float(user_value) - 32) * 5 / 9 + 273.15
        output = f"{round(conversion, 3)} °K"
        return output

    def ftor(self, user_value):
        conversion = float(user_value) + 459.67
        output = f"{round(conversion, 3)} °R"
        return output


class Kelvin:
    def __init__(self, user_value):
        self.user_value = user_value

    def ktoc(self, user_value):
        conversion = float(user_value) - 273.15
        output = f"{conversion} °C"
        return output

    def ktof(self, user_value):
        conversion = (float(user_value) - 273.15) * 9 / 5 - 32
        output = f"{round(conversion, 3)} °F"
        return output

    def ktok(self, user_value):
        conversion = float(user_value)
        output = f"{conversion} °K"
        return output

    def ktor(self, user_value):
        conversion = float(user_value) * 1.8
        output = f"{round(conversion, 3)} °R"
        return output


class Rankine:
    def __init__(self, user_value):
        self.user_value = user_value

    def rtoc(self, user_value):
        conversion = (float(user_value) - 491.67) * 5 / 9
        output = f"{round(conversion, 3)} °C"
        return output

    def rtof(self, user_value):
        conversion = float(user_value) - 459.67
        output = f"{round(conversion, 3)} °F"
        return output

    def rtok(self, user_value):
        conversion = float(user_value) / 1.8
        output = f"{round(conversion, 3)} °K"
        return output

    def rtor(self, user_value):
        conversion = float(user_value)
        output = f"{conversion} °R"
        return output
