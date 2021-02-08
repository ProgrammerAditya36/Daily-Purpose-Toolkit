class KiloGrams:

    def __init__(self, user_value):
        self.user_value = user_value

    def kgTokg(self, user_value):
        conversion = float(user_value)
        output = f"{conversion}kg"
        return output

    def kgTolb(self, user_value):
        conversion = float(user_value) * 2.2046
        output = f"{round(conversion, 3)} lbs"
        return output

    def kgTotons(self, user_value):
        conversion = float(user_value) / 1_000
        output = f"{conversion} tons"
        return output

    def kgToounces(self, user_value):
        conversion = float(user_value) * 35.274
        output = f"{round(conversion, 3)} oz"
        return output

    def kgTograms(self, user_value):
        conversion = float(user_value) * 1_000
        output = f"{conversion} g"
        return output

    def kgTomilgrams(self, user_value):
        conversion = float(user_value) * 1_000_000
        output = f"{conversion} mg"
        return output

    def kgTomicrograms(self, user_value):
        conversion = float(user_value) * 1_000_000_000
        output = f"{conversion} µg"
        return output


class Pounds:

    def __init__(self, user_value):
        self.user_value = user_value

    def lbsTokg(self, user_value):
        conversion = float(user_value) / 2.2046
        output = f"{round(conversion, 2)}kg"
        return output

    def lbTolb(self, user_value):
        conversion = float(user_value)
        output = f"{conversion} lbs"
        return output

    def lbTotons(self, user_value):
        conversion = float(user_value) / 2.2046 / 1_000
        output = f"{conversion} tons"
        return output

    def lbToounces(self, user_value):
        conversion = float(user_value) / 2.2046 * 35.274
        output = f"{round(conversion, 3)} oz"
        return output

    def lbTograms(self, user_value):
        conversion = float(user_value) / 2.2046 * 1_000
        output = f"{round(conversion, 3)} g"
        return output

    def lbTomilgrams(self, user_value):
        conversion = float(user_value) / 2.2046 * 1_000_000
        output = f"{round(conversion, 3)} mg"
        return output

    def lbTomicrograms(self, user_value):
        conversion = float(user_value) / 2.2046 * 1_000_000_000
        output = f"{round(conversion, 3)} µg"
        return output


class Tons:

    def __init__(self, user_value):
        self.user_value = user_value

    def tonsTokg(self, user_value):
        conversion = float(user_value) * 1_000
        output = f"{conversion}kg"
        return output

    def tonsTolb(self, user_value):
        conversion = float(user_value) * 2.20462 * 1_000
        output = f"{round(conversion, 3)} lbs"
        return output

    def tonsTotons(self, user_value):
        conversion = float(user_value)
        output = f"{conversion} tons"
        return output

    def tonsToounces(self, user_value):
        conversion = float(user_value) * 35.274 * 1_000
        output = f"{round(conversion, 3)} oz"
        return output

    def tonsTograms(self, user_value):
        conversion = float(user_value) * 1_000_000
        output = f"{conversion} g"
        return output

    def tonsTomilgrams(self, user_value):
        conversion = float(user_value) * 1_000_000_000
        output = f"{conversion} mg"
        return output

    def tonsTomicrograms(self, user_value):
        conversion = float(user_value) * 1_000_000_000_000
        output = f"{conversion} µg"
        return output


class Ounces:

    def __init__(self, user_value):
        self.user_value = user_value

    def ouncesTokg(self, user_value):
        conversion = float(user_value) / 35.274
        output = f"{round(conversion, 3)}kg"
        return output

    def ouncesTolb(self, user_value):
        conversion = float(user_value) / 35.274 * 2.2046
        output = f"{round(conversion, 3)} lbs"
        return output

    def ouncesTotons(self, user_value):
        conversion = float(user_value) / 35.274 / 1_000
        output = f"{conversion} tons"
        return output

    def ouncesToounces(self, user_value):
        conversion = float(user_value)
        output = f"{conversion} oz"
        return output

    def ouncesTograms(self, user_value):
        conversion = float(user_value) / 32.274 * 1_000
        output = f"{round(conversion, 3)} g"
        return output

    def ouncesTomilgrams(self, user_value):
        conversion = float(user_value) / 32.274 * 1_000_000
        output = f"{round(conversion, 3)} mg"
        return output

    def ouncesTomicrograms(self, user_value):
        conversion = float(user_value) / 32.274 * 1_000_000_000
        output = f"{round(conversion, 2)} µg"
        return output


class Grams:

    def __init__(self, user_value):
        self.user_value = user_value

    def gramsTokg(self, user_value):
        conversion = float(user_value) / 1_000
        output = f"{conversion}kg"
        return output

    def gramsTolb(self, user_value):
        conversion = float(user_value) / 1_000 * 2.2046
        output = f"{round(conversion, 3)} lbs"
        return output

    def gramsTotons(self, user_value):
        conversion = float(user_value) / 1_000_000
        output = f"{conversion} tons"
        return output

    def gramsToounces(self, user_value):
        conversion = float(user_value) / 1_000 * 35.274
        output = f"{round(conversion, 3)} oz"
        return output

    def gramsTograms(self, user_value):
        conversion = float(user_value)
        output = f"{conversion} g"
        return output

    def gramsTomilgrams(self, user_value):
        conversion = float(user_value) * 1_000
        output = f"{conversion} mg"
        return output

    def gramsTomicrograms(self, user_value):
        conversion = float(user_value) * 1_000_000
        output = f"{conversion} µg"
        return output


class MilGrams:

    def __init__(self, user_value):
        self.user_value = user_value

    def milgramsTokg(self, user_value):
        conversion = float(user_value) / 1_000_000
        output = f"{conversion}kg"
        return output

    def milgramsTolb(self, user_value):
        conversion = float(user_value) / 1_000_000 * 2.2046
        output = f"{conversion} lbs"
        return output

    def milgramsTotons(self, user_value):
        conversion = float(user_value) / 1_000_000_000
        output = f"{conversion} tons"
        return output

    def milgramsToounces(self, user_value):
        conversion = float(user_value) / 1_000_000 * 35.274
        output = f"{round(conversion, 3)} oz"
        return output

    def milgramsTograms(self, user_value):
        conversion = float(user_value) / 1_000
        output = f"{round(conversion, 3)} g"
        return output

    def milgramsTomilgrams(self, user_value):
        conversion = float(user_value)
        output = f"{conversion} mg"
        return output

    def milgramsTomicrograms(self, user_value):
        conversion = float(user_value) * 1_000
        output = f"{conversion} µg"
        return output


class MicroGrams:

    def __init__(self, user_value):
        self.user_value = user_value

    def microTokg(self, user_value):
        conversion = float(user_value) / 1_000_000_000
        output = f"{conversion}kg"
        return output

    def microTolb(self, user_value):
        conversion = float(user_value) / 1_000_000_000 * 2.2046
        output = f"{conversion} lbs"
        return output

    def microTotons(self, user_value):
        conversion = float(user_value) / 1_000_000_000_000
        output = f"{conversion} tons"
        return output

    def microToounces(self, user_value):
        conversion = float(user_value) / 1_000_000_000 * 35.274
        output = f"{conversion} oz"
        return output

    def microTograms(self, user_value):
        conversion = float(user_value) / 1_000_000
        output = f"{conversion} g"
        return output

    def microTomilgrams(self, user_value):
        conversion = float(user_value) / 1_000
        output = f"{conversion} mg"
        return output

    def microTomicrograms(self, user_value):
        conversion = float(user_value)
        output = f"{conversion} µg"
        return output
