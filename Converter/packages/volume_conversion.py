class Gallons:
    def __init__(self, user_value):
        self.user_value = user_value

    def gtog(self, user_value):
        conversion = float(user_value)
        output = f"{round(conversion, 3)} gal"
        return output

    def gtocm(self, user_value):
        conversion = float(user_value) / 264.172
        output = f"{round(conversion, 3)} m\N{SUPERSCRIPT THREE}"
        return output

    def gtol(self, user_value):
        conversion = float(user_value) * 3.785
        output = f"{round(conversion, 3)} l"
        return output

    def gtocf(self, user_value):
        conversion = float(user_value) / 7.481
        output = f"{round(conversion, 3)} ft\N{SUPERSCRIPT THREE}"
        return output

    def gtoci(self, user_value):
        conversion = float(user_value) * 231
        output = f"{round(conversion, 3)} in\N{SUPERSCRIPT THREE}"
        return output

    def gtoml(self, user_value):
        conversion = float(user_value) * 3785.41
        output = f"{round(conversion, 3)} mL"
        return output

    def gtof(self, user_value):
        conversion = float(user_value) * 128
        output = f"{round(conversion, 3)} fl oz"
        return output

    def gtoq(self, user_value):
        conversion = float(user_value) * 4
        output = f"{round(conversion, 3)} qt"
        return output

    def gtocup(self, user_value):
        conversion = float(user_value) * 15.773
        output = f"{round(conversion, 3)} cups"
        return output


class CubicMetre:
    def __init__(self, user_value):
        self.user_value = user_value

    def cmtog(self, user_value):
        conversion = float(user_value) * 264.172
        output = f"{round(conversion, 3)} gal"
        return output

    def cmtocm(self, user_value):
        conversion = float(user_value)
        output = f"{round(conversion, 3)} m\N{SUPERSCRIPT THREE}"
        return output

    def cmtol(self, user_value):
        conversion = float(user_value) * 1_000
        output = f"{round(conversion, 3)} l"
        return output

    def cmtocf(self, user_value):
        conversion = float(user_value) * 35.3147
        output = f"{round(conversion, 3)} ft\N{SUPERSCRIPT THREE}"
        return output

    def cmtoci(self, user_value):
        conversion = float(user_value) * 61023.7
        output = f"{round(conversion, 3)} in\N{SUPERSCRIPT THREE}"
        return output

    def cmtoml(self, user_value):
        conversion = float(user_value) * 1_000_000
        output = f"{round(conversion, 3)} mL"
        return output

    def cmtof(self, user_value):
        conversion = float(user_value) * 33813.96
        output = f"{round(conversion, 3)} fl oz"
        return output

    def cmtoq(self, user_value):
        conversion = float(user_value) * 1056.69
        output = f"{round(conversion, 3)} qt"
        return output

    def cmtocup(self, user_value):
        conversion = float(user_value) * 4166.67
        output = f"{round(conversion, 3)} cups"
        return output


class Litre:
    def __init__(self, user_value):
        self.user_value = user_value

    def ltog(self, user_value):
        conversion = float(user_value) * 0.264172
        output = f"{round(conversion, 3)} gal"
        return output

    def ltocm(self, user_value):
        conversion = float(user_value) / 1000
        output = f"{round(conversion, 3)} m\N{SUPERSCRIPT THREE}"
        return output

    def ltol(self, user_value):
        conversion = float(user_value)
        output = f"{round(conversion, 3)} l"
        return output

    def ltocf(self, user_value):
        conversion = float(user_value) * 0.0353147
        output = f"{round(conversion, 3)} ft\N{SUPERSCRIPT THREE}"
        return output

    def ltoci(self, user_value):
        conversion = float(user_value) * 61.0237
        output = f"{round(conversion, 3)} in\N{SUPERSCRIPT THREE}"
        return output

    def ltoml(self, user_value):
        conversion = float(user_value) * 1_000
        output = f"{round(conversion, 3)} mL"
        return output

    def ltof(self, user_value):
        conversion = float(user_value) * 33.814
        output = f"{round(conversion, 3)} fl oz"
        return output

    def ltoq(self, user_value):
        conversion = float(user_value) * 1.05669
        output = f"{round(conversion, 3)} qt"
        return output

    def ltocup(self, user_value):
        conversion = float(user_value) * 4.16667
        output = f"{round(conversion, 3)} cups"
        return output


class CubicFeet:
    def __init__(self, user_value):
        self.user_value = user_value

    def cftog(self, user_value):
        conversion = float(user_value) * 7.48052
        output = f"{round(conversion, 3)} gal"
        return output

    def cftocm(self, user_value):
        conversion = float(user_value) * 0.0283168
        output = f"{round(conversion, 3)} m\N{SUPERSCRIPT THREE}"
        return output

    def cftol(self, user_value):
        conversion = float(user_value) * 28.3168
        output = f"{round(conversion, 3)} l"
        return output

    def cftocf(self, user_value):
        conversion = float(user_value)
        output = f"{round(conversion, 3)} ft\N{SUPERSCRIPT THREE}"
        return output

    def cftoci(self, user_value):
        conversion = float(user_value) * 1728
        output = f"{round(conversion, 3)} in\N{SUPERSCRIPT THREE}"
        return output

    def cftoml(self, user_value):
        conversion = float(user_value) * 28316.8
        output = f"{round(conversion, 3)} mL"
        return output

    def cftof(self, user_value):
        conversion = float(user_value) * 957.96
        output = f"{round(conversion, 3)} fl oz"
        return output

    def cftoq(self, user_value):
        conversion = float(user_value) * 29.9221
        output = f"{round(conversion, 3)} qt"
        return output

    def cftocup(self, user_value):
        conversion = float(user_value) * 117.987
        output = f"{round(conversion, 3)} cups"
        return output


class CubicInch:
    def __init__(self, user_value):
        self.user_value = user_value

    def citog(self, user_value):
        conversion = float(user_value) * 0.004329
        output = f"{round(conversion, 3)} gal"
        return output

    def citocm(self, user_value):
        conversion = float(user_value) / 61023.7
        output = f"{conversion} m\N{SUPERSCRIPT THREE}"
        return output

    def citol(self, user_value):
        conversion = float(user_value) / 61.0237
        output = f"{round(conversion, 3)} l"
        return output

    def citocf(self, user_value):
        conversion = float(user_value) / 1.805
        output = f"{round(conversion, 5)} ft\N{SUPERSCRIPT THREE}"
        return output

    def citoci(self, user_value):
        conversion = float(user_value)
        output = f"{round(conversion, 3)} in\N{SUPERSCRIPT THREE}"
        return output

    def citoml(self, user_value):
        conversion = float(user_value) * 16.3871
        output = f"{round(conversion, 3)} mL"
        return output

    def citof(self, user_value):
        conversion = float(user_value) * 0.576744
        output = f"{round(conversion, 3)} fl oz"
        return output

    def citoq(self, user_value):
        conversion = float(user_value) * 0.0171316
        output = f"{round(conversion, 3)} qt"
        return output

    def citocup(self, user_value):
        conversion = float(user_value) * 0.0682794
        output = f"{round(conversion, 3)} cups"
        return output


class MilliLitre:
    def __init__(self, user_value):
        self.user_value = user_value

    def mltog(self, user_value):
        conversion = float(user_value) * 0.000264172
        output = f"{conversion} gal"
        return output

    def mltocm(self, user_value):
        conversion = float(user_value) / 1_000_000
        output = f"{conversion} m\N{SUPERSCRIPT THREE}"
        return output

    def mltol(self, user_value):
        conversion = float(user_value) / 1_000
        output = f"{round(conversion, 3)} l"
        return output

    def mltocf(self, user_value):
        conversion = float(user_value) / 28317
        output = f"{conversion} ft\N{SUPERSCRIPT THREE}"
        return output

    def mltoci(self, user_value):
        conversion = float(user_value) * 0.0610237
        output = f"{round(conversion, 3)} in\N{SUPERSCRIPT THREE}"
        return output

    def mltoml(self, user_value):
        conversion = float(user_value)
        output = f"{round(conversion, 3)} mL"
        return output

    def mltof(self, user_value):
        conversion = float(user_value) * 0.0351951
        output = f"{round(conversion, 3)} fl oz"
        return output

    def mltoq(self, user_value):
        conversion = float(user_value) * 0.00105669
        output = f"{round(conversion, 3)} qt"
        return output

    def mltocup(self, user_value):
        conversion = float(user_value) * 0.00416667
        output = f"{round(conversion, 3)} cups"
        return output


class FluidOunce:
    def __init__(self, user_value):
        self.user_value = user_value

    def fltog(self, user_value):
        conversion = float(user_value) * 0.00750594
        output = f"{round(conversion, 4)} gal"
        return output

    def fltocm(self, user_value):
        conversion = float(user_value) / 35195.1
        output = f"{conversion} m\N{SUPERSCRIPT THREE}"
        return output

    def fltol(self, user_value):
        conversion = float(user_value) / 35.1951
        output = f"{round(conversion, 3)} l"
        return output

    def fltocf(self, user_value):
        conversion = float(user_value) / 996.977
        output = f"{round(conversion, 3)} ft\N{SUPERSCRIPT THREE}"
        return output

    def fltoci(self, user_value):
        conversion = float(user_value) * 1.73387
        output = f"{round(conversion, 3)} in\N{SUPERSCRIPT THREE}"
        return output

    def fltoml(self, user_value):
        conversion = float(user_value) * 28.4131
        output = f"{round(conversion, 3)} mL"
        return output

    def fltof(self, user_value):
        conversion = float(user_value)
        output = f"{round(conversion, 3)} fl oz"
        return output

    def fltoq(self, user_value):
        conversion = float(user_value) * 0.0300237
        output = f"{round(conversion, 4)} qt"
        return output

    def fltocup(self, user_value):
        conversion = float(user_value) * 0.118388
        output = f"{round(conversion, 3)} cups"
        return output


class Quart:
    def __init__(self, user_value):
        self.user_value = user_value

    def qtog(self, user_value):
        conversion = float(user_value) * 0.25
        output = f"{round(conversion, 3)} gal"
        return output

    def qtocm(self, user_value):
        conversion = float(user_value) * 0.000946353
        output = f"{round(conversion, 3)} m\N{SUPERSCRIPT THREE}"
        return output

    def qtol(self, user_value):
        conversion = float(user_value) * 0.946353
        output = f"{round(conversion, 3)} l"
        return output

    def qtocf(self, user_value):
        conversion = float(user_value) * 0.0334201
        output = f"{round(conversion, 3)} ft\N{SUPERSCRIPT THREE}"
        return output

    def qtoci(self, user_value):
        conversion = float(user_value) * 57.75
        output = f"{round(conversion, 3)} in\N{SUPERSCRIPT THREE}"
        return output

    def qtoml(self, user_value):
        conversion = float(user_value) * 946.353
        output = f"{round(conversion, 3)} mL"
        return output

    def qtof(self, user_value):
        conversion = float(user_value) * 32
        output = f"{round(conversion, 3)} fl oz"
        return output

    def qtoq(self, user_value):
        conversion = float(user_value)
        output = f"{round(conversion, 3)} qt"
        return output

    def qtocup(self, user_value):
        conversion = float(user_value) * 3.94314
        output = f"{round(conversion, 3)} cups"
        return output


class Cup:
    def __init__(self, user_value):
        self.user_value = user_value

    def cuptog(self, user_value):
        conversion = float(user_value) * 0.0634013
        output = f"{round(conversion, 3)} gal"
        return output

    def cuptocm(self, user_value):
        conversion = float(user_value) * 0.00024
        output = f"{round(conversion, 3)} m\N{SUPERSCRIPT THREE}"
        return output

    def cuptol(self, user_value):
        conversion = float(user_value) * 0.24
        output = f"{round(conversion, 3)} l"
        return output

    def cuptocf(self, user_value):
        conversion = float(user_value) * 0.00847552
        output = f"{round(conversion, 3)} ft\N{SUPERSCRIPT THREE}"
        return output

    def cuptoci(self, user_value):
        conversion = float(user_value) * 14.6457
        output = f"{round(conversion, 3)} in\N{SUPERSCRIPT THREE}"
        return output

    def cuptoml(self, user_value):
        conversion = float(user_value) * 240
        output = f"{round(conversion, 3)} mL"
        return output

    def cuptof(self, user_value):
        conversion = float(user_value) * 8.44682
        output = f"{round(conversion, 3)} fl oz"
        return output

    def cuptoq(self, user_value):
        conversion = float(user_value) * 0.253605
        output = f"{round(conversion, 3)} qt"
        return output

    def cuptocup(self, user_value):
        conversion = float(user_value)
        output = f"{round(conversion, 3)} cups"
        return output
