class Kmph:
    def __init__(self, user_value):
        self.user_value = user_value

    def kmtokm(self, user_value):
        conversion = float(user_value)
        output = f"{round(conversion, 3)} kmph"
        return output

    def kmtomi(self, user_value):
        conversion = float(user_value) / 1.60934
        output = f"{round(conversion, 3)} mph"
        return output

    def kmtom(self, user_value):
        conversion = float(user_value) / 3.6
        output = f"{round(conversion, 3)} m s"
        return output

    def kmtof(self, user_value):
        conversion = float(user_value) * 0.911344
        output = f"{round(conversion, 3)} ft s"
        return output

    def kmtokn(self, user_value):
        conversion = float(user_value) / 1.852
        output = f"{round(conversion, 3)} kn"
        return output


class Mph:
    def __init__(self, user_value):
        self.user_value = user_value

    def mItokm(self, user_value):
        conversion = float(user_value) * 1.60934
        output = f"{round(conversion, 3)} kmph"
        return output

    def mItomi(self, user_value):
        conversion = float(user_value)
        output = f"{round(conversion, 3)} mph"
        return output

    def mItom(self, user_value):
        conversion = float(user_value) / 2.237
        output = f"{round(conversion, 3)} m s"
        return output

    def mItof(self, user_value):
        conversion = float(user_value) * 1.46667
        output = f"{round(conversion, 3)} ft s"
        return output

    def mItokn(self, user_value):
        conversion = float(user_value) * 0.868976
        output = f"{round(conversion, 3)} kn"
        return output


class Mps:
    def __init__(self, user_value):
        self.user_value = user_value

    def mtokm(self, user_value):
        conversion = float(user_value) * 3.6
        output = f"{round(conversion, 3)} kmph"
        return output

    def mtomi(self, user_value):
        conversion = float(user_value) * 2.23694
        output = f"{round(conversion, 3)} mph"
        return output

    def mtom(self, user_value):
        conversion = float(user_value)
        output = f"{round(conversion, 3)} m s"
        return output

    def mtof(self, user_value):
        conversion = float(user_value) * 3.28084
        output = f"{round(conversion, 3)} ft s"
        return output

    def mtokn(self, user_value):
        conversion = float(user_value) * 1.94384
        output = f"{round(conversion, 3)} kn"
        return output


class Fps:
    def __init__(self, user_value):
        self.user_value = user_value

    def ftokm(self, user_value):
        conversion = float(user_value) * 1.09728
        output = f"{round(conversion, 3)} kmph"
        return output

    def ftomi(self, user_value):
        conversion = float(user_value) * 0.681818
        output = f"{round(conversion, 3)} mph"
        return output

    def ftom(self, user_value):
        conversion = float(user_value) * 0.3048
        output = f"{round(conversion, 3)} m s"
        return output

    def ftof(self, user_value):
        conversion = float(user_value)
        output = f"{round(conversion, 3)} ft s"
        return output

    def ftokn(self, user_value):
        conversion = float(user_value) * 0.592484
        output = f"{round(conversion, 3)} kn"
        return output


class Kn:
    def __init__(self, user_value):
        self.user_value = user_value

    def ktokm(self, user_value):
        conversion = float(user_value) * 1.852
        output = f"{round(conversion, 3)} kmph"
        return output

    def ktomi(self, user_value):
        conversion = float(user_value) * 1.15078
        output = f"{round(conversion, 3)} mph"
        return output

    def ktom(self, user_value):
        conversion = float(user_value) * 0.514444
        output = f"{round(conversion, 3)} m s"
        return output

    def ktof(self, user_value):
        conversion = float(user_value) * 1.68781
        output = f"{round(conversion, 3)} ft s"
        return output

    def ktokn(self, user_value):
        conversion = float(user_value) / 1.852
        output = f"{round(conversion, 3)} kn"
        return output
