class Kilometres:
    def __init__(self, user_value):
        self.user_value = user_value

    def kmtokm(self, user_value):
        conversion = float(user_value)
        output = f"{conversion} km"
        return output

    def kmtomi(self, user_value):
        conversion = float(user_value) / 1.667
        output = f"{round(conversion, 3)} mi"
        return output

    def kmtom(self, user_value):
        conversion = float(user_value) * 1_000
        output = f"{round(conversion, 3)} m"
        return output

    def kmtoy(self, user_value):
        conversion = float(user_value) * 1093.61
        output = f"{round(conversion, 3)} yd"
        return output

    def kmtof(self, user_value):
        conversion = float(user_value) * 3280.84
        output = f"{round(conversion, 3)} ft"
        return output

    def kmtoi(self, user_value):
        conversion = float(user_value) * 39370.1
        output = f"{round(conversion, 3)} in"
        return output

    def kmtocm(self, user_value):
        conversion = float(user_value) * 100_000
        output = f"{round(conversion, 3)} cm"
        return output

    def kmtomm(self, user_value):
        conversion = float(user_value) * 1_000_000
        output = f"{round(conversion, 3)} mm"
        return output

    def kmtomicm(self, user_value):
        conversion = float(user_value) * 1_000_000_000
        output = f"{round(conversion, 3)} µm"
        return output

    def kmtonm(self, user_value):
        conversion = float(user_value) * 1_000_000_000_000
        output = f"{round(conversion, 3)} nm"


class Miles:
    def __init__(self, user_value):
        self.user_value = user_value

    def mitokm(self, user_value):
        conversion = float(user_value) * 1.60934
        output = f"{conversion} km"
        return output

    def mitomi(self, user_value):
        conversion = float(user_value)
        output = f"{round(conversion, 3)} mi"
        return output

    def mitom(self, user_value):
        conversion = float(user_value) * 1609.34
        output = f"{round(conversion, 3)} m"
        return output

    def mitoy(self, user_value):
        conversion = float(user_value) * 1760
        output = f"{round(conversion, 3)} yd"
        return output

    def mitof(self, user_value):
        conversion = float(user_value) * 5280
        output = f"{round(conversion, 3)} ft"
        return output

    def mitoi(self, user_value):
        conversion = float(user_value) * 63360
        output = f"{round(conversion, 3)} in"
        return output

    def mitocm(self, user_value):
        conversion = float(user_value) * 160934
        output = f"{round(conversion, 3)} cm"
        return output

    def mitomm(self, user_value):
        conversion = float(user_value) * 1.60934 * (10 ** 6)
        output = f"{round(conversion, 3)} mm"
        return output

    def mitomicm(self, user_value):
        conversion = float(user_value) * 1.60934 * (10 ** 9)
        output = f"{round(conversion, 3)} µm"
        return output

    def mitonm(self, user_value):
        conversion = float(user_value) * 1.60934 * (10 ** 12)
        output = f"{round(conversion, 3)} nm"


class Metres:
    def __init__(self, user_value):
        self.user_value = user_value

    def mtokm(self, user_value):
        conversion = float(user_value) / 1_000
        output = f"{conversion} km"
        return output

    def mtomi(self, user_value):
        conversion = float(user_value) / 1609.34
        output = f"{round(conversion, 3)} mi"
        return output

    def mtom(self, user_value):
        conversion = float(user_value)
        output = f"{round(conversion, 3)} m"
        return output

    def mtoy(self, user_value):
        conversion = float(user_value) * 1.09361
        output = f"{round(conversion, 3)} yd"
        return output

    def mtof(self, user_value):
        conversion = float(user_value) * 3.28084
        output = f"{round(conversion, 3)} ft"
        return output

    def mtoi(self, user_value):
        conversion = float(user_value) * 39.3701
        output = f"{round(conversion, 3)} in"
        return output

    def mtocm(self, user_value):
        conversion = float(user_value) * 1_00
        output = f"{round(conversion, 3)} cm"
        return output

    def mtomm(self, user_value):
        conversion = float(user_value) * 10 ** 3
        output = f"{round(conversion, 3)} mm"
        return output

    def mtomicm(self, user_value):
        conversion = float(user_value) * 10 ** 6
        output = f"{round(conversion, 3)} µm"
        return output

    def mtonm(self, user_value):
        conversion = float(user_value) * 10 ** 9
        output = f"{round(conversion, 3)} nm"


class Yards:
    def __init__(self, user_value):
        self.user_value = user_value

    def ytokm(self, user_value):
        conversion = float(user_value) * 0.0009144
        output = f"{conversion} km"
        return output

    def ytomi(self, user_value):
        conversion = float(user_value) * 0.000568182
        output = f"{round(conversion, 3)} mi"
        return output

    def ytom(self, user_value):
        conversion = float(user_value) * 0.9144
        output = f"{round(conversion, 3)} m"
        return output

    def ytoy(self, user_value):
        conversion = float(user_value)
        output = f"{round(conversion, 3)} yd"
        return output

    def ytof(self, user_value):
        conversion = float(user_value) * 3
        output = f"{round(conversion, 3)} ft"
        return output

    def ytoi(self, user_value):
        conversion = float(user_value) * 36
        output = f"{round(conversion, 3)} in"
        return output

    def ytocm(self, user_value):
        conversion = float(user_value) * 91.44
        output = f"{round(conversion, 3)} cm"
        return output

    def ytomm(self, user_value):
        conversion = float(user_value) * 914.4
        output = f"{round(conversion, 3)} mm"
        return output

    def ytomicm(self, user_value):
        conversion = float(user_value) * 914400
        output = f"{round(conversion, 3)} µm"
        return output

    def ytonm(self, user_value):
        conversion = float(user_value) * 9.144 * (10 ** 8)
        output = f"{round(conversion, 3)} nm"
        return output


class Feet:
    def __init__(self, user_value):
        self.user_value = user_value

    def ftokm(self, user_value):
        conversion = float(user_value) * 0.0003048
        output = f"{conversion} km"
        return output

    def ftomi(self, user_value):
        conversion = float(user_value) * 0.000189394
        output = f"{round(conversion, 3)} mi"
        return output

    def ftom(self, user_value):
        conversion = float(user_value) * 0.3048
        output = f"{round(conversion, 3)} m"
        return output

    def ftoy(self, user_value):
        conversion = float(user_value) / 3
        output = f"{round(conversion, 3)} yd"
        return output

    def ftof(self, user_value):
        conversion = float(user_value)
        output = f"{round(conversion, 3)} ft"
        return output

    def ftoi(self, user_value):
        conversion = float(user_value) * 12
        output = f"{round(conversion, 3)} in"
        return output

    def ftocm(self, user_value):
        conversion = float(user_value) * 30.48
        output = f"{round(conversion, 3)} cm"
        return output

    def ftomm(self, user_value):
        conversion = float(user_value) * 304.8
        output = f"{round(conversion, 3)} mm"
        return output

    def ftomicm(self, user_value):
        conversion = float(user_value) * 304800
        output = f"{round(conversion, 3)} µm"
        return output

    def ftonm(self, user_value):
        conversion = float(user_value) * 3.048 * (10 ** 8)
        output = f"{round(conversion, 3)} nm"
        return output


class Inches:
    def __init__(self, user_value):
        self.user_value = user_value

    def itokm(self, user_value):
        conversion = float(user_value) * 2.54 * (10 ** -5)
        output = f"{conversion} km"
        return output

    def itomi(self, user_value):
        conversion = float(user_value) * 1.5783 * (10 ** -5)
        output = f"{round(conversion, 3)} mi"
        return output

    def itom(self, user_value):
        conversion = float(user_value) * 0.0254
        output = f"{round(conversion, 3)} m"
        return output

    def itoy(self, user_value):
        conversion = float(user_value) / 36
        output = f"{round(conversion, 3)} yd"
        return output

    def itof(self, user_value):
        conversion = float(user_value) / 12
        output = f"{round(conversion, 3)} ft"
        return output

    def itoi(self, user_value):
        conversion = float(user_value)
        output = f"{round(conversion, 3)} in"
        return output

    def itocm(self, user_value):
        conversion = float(user_value) * 2.54
        output = f"{round(conversion, 3)} cm"
        return output

    def itomm(self, user_value):
        conversion = float(user_value) * 25.4
        output = f"{round(conversion, 3)} mm"
        return output

    def itomicm(self, user_value):
        conversion = float(user_value) * 25400
        output = f"{round(conversion, 3)} µm"
        return output

    def itonm(self, user_value):
        conversion = float(user_value) * 2.54 * (10 ** 7)
        output = f"{round(conversion, 3)} nm"
        return output


class Centimetres:
    def __init__(self, user_value):
        self.user_value = user_value

    def cmtokm(self, user_value):
        conversion = float(user_value) * (10 ** -5)
        output = f"{conversion} km"
        return output

    def cmtomi(self, user_value):
        conversion = float(user_value) * 6.2137 * (10 ** -5)
        output = f"{round(conversion, 3)} mi"
        return output

    def cmtom(self, user_value):
        conversion = float(user_value) * 0.01
        output = f"{round(conversion, 3)} m"
        return output

    def cmtoy(self, user_value):
        conversion = float(user_value) / 91.44
        output = f"{round(conversion, 3)} yd"
        return output

    def cmtof(self, user_value):
        conversion = float(user_value) * 0.0328084
        output = f"{round(conversion, 3)} ft"
        return output

    def cmtoi(self, user_value):
        conversion = float(user_value) / 2.54
        output = f"{round(conversion, 3)} in"
        return output

    def cmtocm(self, user_value):
        conversion = float(user_value)
        output = f"{round(conversion, 3)} cm"
        return output

    def cmtomm(self, user_value):
        conversion = float(user_value) * 10
        output = f"{round(conversion, 3)} mm"
        return output

    def cmtomicm(self, user_value):
        conversion = float(user_value) * 10000
        output = f"{round(conversion, 3)} µm"
        return output

    def cmtonm(self, user_value):
        conversion = float(user_value) * 10 ** 7
        output = f"{round(conversion, 3)} nm"
        return output


class Millimetres:
    def __init__(self, user_value):
        self.user_value = user_value

    def mmtokm(self, user_value):
        conversion = float(user_value) * (10 ** -6)
        output = f"{conversion} km"
        return output

    def mmtomi(self, user_value):
        conversion = float(user_value) * 6.2137 * (10 ** -7)
        output = f"{round(conversion, 3)} mi"
        return output

    def mmtom(self, user_value):
        conversion = float(user_value) * 0.001
        output = f"{round(conversion, 3)} m"
        return output

    def mmtoy(self, user_value):
        conversion = float(user_value) * 0.00109361
        output = f"{round(conversion, 3)} yd"
        return output

    def mmtof(self, user_value):
        conversion = float(user_value) * 0.00328084
        output = f"{round(conversion, 3)} ft"
        return output

    def mmtoi(self, user_value):
        conversion = float(user_value) * 0.0393701
        output = f"{round(conversion, 3)} in"
        return output

    def mmtocm(self, user_value):
        conversion = float(user_value) * 0.1
        output = f"{round(conversion, 3)} cm"
        return output

    def mmtomm(self, user_value):
        conversion = float(user_value)
        output = f"{round(conversion, 3)} mm"
        return output

    def mmtomicm(self, user_value):
        conversion = float(user_value) * 1000
        output = f"{round(conversion, 3)} µm"
        return output

    def mmtonm(self, user_value):
        conversion = float(user_value) * (10 ** 6)
        output = f"{round(conversion, 3)} nm"
        return output


class Micrometres:
    def __init__(self, user_value):
        self.user_value = user_value

    def mictokm(self, user_value):
        conversion = float(user_value) * (10 ** -9)
        output = f"{conversion} km"
        return output

    def mictomi(self, user_value):
        conversion = float(user_value) * 6.2137 * (10 ** -10)
        output = f"{round(conversion, 3)} mi"
        return output

    def mictom(self, user_value):
        conversion = float(user_value) * (10 ** -6)
        output = f"{round(conversion, 3)} m"
        return output

    def mictoy(self, user_value):
        conversion = float(user_value) * 1.0936 * (10 ** -6)
        output = f"{round(conversion, 3)} yd"
        return output

    def mictof(self, user_value):
        conversion = float(user_value) * 3.2808 * (10 ** -6)
        output = f"{round(conversion, 3)} ft"
        return output

    def mictoi(self, user_value):
        conversion = float(user_value) * 3.937 * (10 ** -5)
        output = f"{round(conversion, 3)} in"
        return output

    def mictocm(self, user_value):
        conversion = float(user_value) * (10 ** -4)
        output = f"{round(conversion, 3)} cm"
        return output

    def mictomm(self, user_value):
        conversion = float(user_value) * 0.001
        output = f"{round(conversion, 3)} mm"
        return output

    def mtomicm(self, user_value):
        conversion = float(user_value)
        output = f"{round(conversion, 3)} µm"
        return output

    def mictonm(self, user_value):
        conversion = float(user_value) / 1000
        output = f"{round(conversion, 3)} nm"
        return output
