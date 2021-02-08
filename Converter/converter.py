from tkinter import *
from packages.mass_conversion import *
from packages.temp_conversion import *
from packages.volume_conversion import *
from packages.length_conversion import *
from packages.speed_conversion import *


converter = Tk()
converter.title("Unit Converter")
converter.config(bg="#88a5db")

lbl_type = Label(converter,fg="#46484a",bg="#88a5db", font=("Tw Cen MT",20), text="Choose type of quantity:")
lbl_type.grid(row=1, column=0)
quantities = [
    "Mass",
    "Volume",
    "Temperature",
    "Length",
    "Speed"
]
quantity = StringVar()
quantity.set('Mass')
quantity_drop = OptionMenu(converter, quantity, *quantities)
quantity_drop.grid(row=1, column=1)
quantity_drop.config(fg="#46484a",bg="#88a5db", font=("Tw Cen MT",20))

mass_units = [
    "Kilograms",
    "Pounds",
    "Tons",
    "Ounces",
    "Grams",
    "Milligrams",
    "Micrograms"

]
vol_units = [
    "Gallons",
    "Cubic Metres",
    "Litres",
    "Cubic Feet",
    "Cubic Inches",
    "Millilitres",
    "Fluid Ounces",
    "Quarts",
    "Cups"
]
temp_units = [
    "Celsius",
    "Fahrenheit",
    "Kelvin",
    "Rankine"
]
length_units = [
    "Kilometres",
    "Miles",
    "Metres",
    "Yards",
    "Feet",
    "Inches",
    "Centimetres",
    "Millimetres",
    "Micrometres",
]
speed_units = [
    "Kilometres per hour",
    "Miles per hour",
    "Metre per second",
    "Foot per second",
    "Knots"
]


def selection_show():
    global ent_userinput
    global choice_quant
    global choice_quant2
    choice_quant = StringVar()
    choice_quant2 = StringVar()
    btn_convert.grid(row=6, column=1)
   
    lbl_userinput = Label(converter,fg="#46484a",bg="#88a5db", font=("Tw Cen MT",20), text="Enter quantity to convert:")
    lbl_userinput.grid(row=2, column=0)
    ent_userinput = Entry(converter,fg="#000",bg="#46484a", font=("Tw Cen MT",20), width=25,justify=RIGHT)
    ent_userinput.grid(row=2, column=1)

    frame = LabelFrame(converter,fg="#46484a",bg="#88a5db", font=("Tw Cen MT",20), height=100, width=500)
    frame.grid(row=4, column=1, columnspan=5)
    frame.grid_propagate(0)

    lbl_choose = Label(converter,fg="#46484a",bg="#88a5db", font=("Tw Cen MT",20), text="Select unit of entered quantity:")
    lbl_choose.grid(row=4, column=0)

    if quantity.get() == "Mass":
        mass_drop = OptionMenu(frame, choice_quant, *mass_units)
        mass_drop.grid(row=4, column=1)
    if quantity.get() == "Temperature":
        mass_drop = OptionMenu(frame, choice_quant, *temp_units)
        mass_drop.grid(row=4, column=1)
    if quantity.get() == "Volume":
        mass_drop = OptionMenu(frame, choice_quant, *vol_units)
        mass_drop.grid(row=4, column=1)
    if quantity.get() == "Length":
        mass_drop = OptionMenu(frame, choice_quant, *length_units)
        mass_drop.grid(row=4, column=1)
    if quantity.get() == "Speed":
        mass_drop = OptionMenu(frame, choice_quant, *speed_units)
        mass_drop.grid(row=4, column=1)
    mass_drop.config(fg="#46484a",bg="#88a5db", font=("Tw Cen MT",20))
    lbl_choose2 = Label(converter,fg="#46484a",bg="#88a5db", font=("Tw Cen MT",20), text="Convert to:")
    lbl_choose2.grid(row=5, column=0)
    if quantity.get() == "Mass":
        mass_drop2 = OptionMenu(frame, choice_quant2, *mass_units)
        mass_drop2.grid(row=5, column=1)
    if quantity.get() == "Temperature":
        mass_drop2 = OptionMenu(frame, choice_quant2, *temp_units)
        mass_drop2.grid(row=5, column=1)
    if quantity.get() == "Volume":
        mass_drop2 = OptionMenu(frame, choice_quant2, *vol_units)
        mass_drop2.grid(row=5, column=1)
    if quantity.get() == "Length":
        mass_drop2 = OptionMenu(frame, choice_quant2, *length_units)
        mass_drop2.grid(row=5, column=1)
    if quantity.get() == "Speed":
        mass_drop2 = OptionMenu(frame, choice_quant2, *speed_units)
        mass_drop2.grid(row=5, column=1)
    mass_drop2.config(fg="#46484a",bg="#88a5db", font=("Tw Cen MT",20))


btn_start = Button(converter,fg="#46484a",bg="#88a5db", font=("Tw Cen MT",20), text="Enter", command=selection_show)
btn_start.grid(row=1, column=2)

kilo_object = KiloGrams("")
pound_object = Pounds("")
ton_object = Tons("")
ounce_object = Ounces("")
gram_object = Grams("")
milligram_object = MilGrams("")
micro_object = MicroGrams("")

celsius_object = Celsius("")
fahrenheit_object = Fahrenheit("")
kelvin_object = Kelvin("")
rankine_object = Rankine("")


gallon_object = Gallons("")
cubicmetre_object = CubicMetre("")
litre_object = Litre("")
cubicfeet_object = CubicFeet("")
cubicinch_object = CubicInch("")
millilitre_object = MilliLitre("")
fluidoz_object = FluidOunce("")
quart_object = Quart("")
cup_object = Cup("")

km_object = Kilometres("")
mile_object = Miles("")
metre_object = Metres("")
yard_object = Yards("")
feet_object = Feet("")
inch_object = Inches("")
centimetre_object = Centimetres("")
millimetre_object = Millimetres("")
micrometre_object = Micrometres("")


kmph_object = Kmph("")
mph_object = Mph("")
mps_object = Mps("")
fps_object = Fps("")
kn_object = Kn("")


def conversion():
    lbl_error = Label(converter,fg="#46484a",bg="#88a5db", font=("Tw Cen MT",20), text="Oops! Invalid input. Please try again!")
    try:
        lol = float(ent_userinput.get())
        lbl_error.destroy()
    except ValueError:
        lbl_error.grid(row=7, column=1)

    ent_convert = Entry(converter,fg="#000",bg="#46484a", font=("Tw Cen MT",20), width=25)
    ent_convert.delete(0, END)

    value = ent_userinput.get()
    lbl_convert = Label(converter,bg="#88a5db",fg="#46484a", font=("Tw Cen MT",20), text="After Conversion:")
    lbl_convert.grid(row=7, column=0)

    if quantity.get() == "Mass":
        if choice_quant.get() == "Kilograms":
            if choice_quant2.get() == "Kilograms":
                output = kilo_object.kgTokg(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Pounds":
                output = kilo_object.kgTolb(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Tons":
                output = kilo_object.kgTotons(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Ounces":
                output = kilo_object.kgToounces(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Grams":
                output = kilo_object.kgTograms(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Milligrams":
                output = kilo_object.kgTomilgrams(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Micrograms":
                output = kilo_object.kgTomicrograms(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

        elif choice_quant.get() == "Pounds":
            if choice_quant2.get() == "Kilograms":
                output = pound_object.lbsTokg(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Pounds":
                output = pound_object.lbTolb(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Tons":
                output = pound_object.lbTotons(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Ounces":
                output = pound_object.lbToounces(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Grams":
                output = pound_object.lbTograms(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Milligrams":
                output = pound_object.lbTomilgrams(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Micrograms":
                output = pound_object.lbTomicrograms(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

        elif choice_quant.get() == "Tons":
            if choice_quant2.get() == "Kilograms":
                output = ton_object.tonsTokg(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Pounds":
                output = ton_object.tonsTolb(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Tons":
                output = ton_object.tonsTotons(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Ounces":
                output = ton_object.tonsToounces(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Grams":
                output = ton_object.tonsTograms(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Milligrams":
                output = ton_object.tonsTomilgrams(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Micrograms":
                output = ton_object.tonsTomicrograms(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

        elif choice_quant.get() == "Ounces":
            if choice_quant2.get() == "Kilograms":
                output = ounce_object.ouncesTokg(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Pounds":
                output = ounce_object.ouncesTolb(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Tons":
                output = ounce_object.ouncesTotons(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Ounces":
                output = ounce_object.ouncesToounces(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Grams":
                output = ounce_object.ouncesTograms(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Milligrams":
                output = ounce_object.ouncesTomilgrams(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Micrograms":
                output = ounce_object.ouncesTomicrograms(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

        elif choice_quant.get() == "Grams":
            if choice_quant2.get() == "Kilograms":
                output = gram_object.gramsTokg(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Pounds":
                output = gram_object.gramsTolb(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Tons":
                output = gram_object.gramsTotons(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Ounces":
                output = gram_object.gramsToounces(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Grams":
                output = gram_object.gramsTograms(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Milligrams":
                output = gram_object.gramsTomilgrams(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Micrograms":
                output = gram_object.gramsTomicrograms(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

        elif choice_quant.get() == "Milligrams":
            if choice_quant2.get() == "Kilograms":
                output = milligram_object.milgramsTokg(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Pounds":
                output = milligram_object.milgramsTolb(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Tons":
                output = milligram_object.milgramsTotons(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Ounces":
                output = milligram_object.milgramsToounces(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Grams":
                output = milligram_object.milgramsTograms(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Milligrams":
                output = milligram_object.milgramsTomilgrams(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Micrograms":
                output = milligram_object.milgramsTomicrograms(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

        elif choice_quant.get() == "Micrograms":
            if choice_quant2.get() == "Kilograms":
                output = micro_object.microTokg(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Pounds":
                output = micro_object.microTolb(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Tons":
                output = micro_object.microTotons(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Ounces":
                output = micro_object.microToounces(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Grams":
                output = micro_object.microTograms(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Milligrams":
                output = micro_object.microTomilgrams(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)

            elif choice_quant2.get() == "Micrograms":
                output = micro_object.microTomicrograms(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
    elif quantity.get() == "Temperature":
        if choice_quant.get() == "Celsius":
            if choice_quant2.get() == "Celsius":
                output = celsius_object.ctoc(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Fahrenheit":
                output = celsius_object.ctof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Kelvin":
                output = celsius_object.ctok(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Rankine":
                output = celsius_object.ctor(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
        elif choice_quant.get() == "Fahrenheit":
            if choice_quant2.get() == "Celsius":
                output = fahrenheit_object.ftoc(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Fahrenheit":
                output = fahrenheit_object.ftof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Kelvin":
                output = fahrenheit_object.ftok(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Rankine":
                output = fahrenheit_object.ftor(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
        elif choice_quant.get() == "Kelvin":
            if choice_quant2.get() == "Celsius":
                output = kelvin_object.ktoc(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Fahrenheit":
                output = kelvin_object.ktof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Kelvin":
                output = kelvin_object.ktok(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Rankine":
                output = kelvin_object.ktor(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
        elif choice_quant.get() == "Rankine":
            if choice_quant2.get() == "Celsius":
                output = rankine_object.rtoc(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Fahrenheit":
                output = rankine_object.rtof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Kelvin":
                output = rankine_object.rtok(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Rankine":
                output = rankine_object.rtor(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
    elif quantity.get() == "Volume":
        if choice_quant.get() == "Gallons":
            if choice_quant2.get() == "Gallons":
                output = gallon_object.gtog(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Metres":
                output = gallon_object.gtocm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Litres":
                output = gallon_object.gtol(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Feet":
                output = gallon_object.gtocf(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Inches":
                output = gallon_object.gtoci(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Millilitres":
                output = gallon_object.gtoml(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Fluid Ounces":
                output = gallon_object.gtof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Quarts":
                output = gallon_object.gtoq(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cups":
                output = gallon_object.gtocup(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
        elif choice_quant.get() == "Cubic Metres":
            if choice_quant2.get() == "Gallons":
                output = cubicmetre_object.cmtog(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Metres":
                output = cubicmetre_object.cmtocm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Litres":
                output = cubicmetre_object.cmtol(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Feet":
                output = cubicmetre_object.cmtocf(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Inches":
                output = cubicmetre_object.cmtoci(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Millilitres":
                output = cubicmetre_object.cmtoml(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Fluid Ounces":
                output = cubicmetre_object.cmtof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Quarts":
                output = cubicmetre_object.cmtoq(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cups":
                output = cubicmetre_object.cmtocup(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
        elif choice_quant.get() == "Litres":
            if choice_quant2.get() == "Gallons":
                output = litre_object.ltog(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Metres":
                output = litre_object.ltocm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Litres":
                output = litre_object.ltol(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Feet":
                output = litre_object.ltocf(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Inches":
                output = litre_object.ltoci(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Millilitres":
                output = litre_object.ltoml(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Fluid Ounces":
                output = litre_object.ltof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Quarts":
                output = litre_object.ltoq(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cups":
                output = litre_object.ltocup(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
        elif choice_quant.get() == "Cubic Feet":
            if choice_quant2.get() == "Gallons":
                output = cubicfeet_object.cftog(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Metres":
                output = cubicfeet_object.cftocm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Litres":
                output = cubicfeet_object.cftol(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Feet":
                output = cubicfeet_object.cftocf(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Inches":
                output = cubicfeet_object.cftoci(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Millilitres":
                output = cubicfeet_object.cftoml(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Fluid Ounces":
                output = cubicfeet_object.cftof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Quarts":
                output = cubicfeet_object.cftoq(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cups":
                output = cubicfeet_object.cftocup(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
        elif choice_quant.get() == "Cubic Inches":
            if choice_quant2.get() == "Gallons":
                output = cubicinch_object.citog(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Metres":
                output = cubicinch_object.citocm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Litres":
                output = cubicinch_object.citol(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Feet":
                output = cubicinch_object.citocf(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Inches":
                output = cubicinch_object.citoci(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Millilitres":
                output = cubicinch_object.citoml(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Fluid Ounces":
                output = cubicinch_object.citof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Quarts":
                output = cubicinch_object.citoq(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cups":
                output = cubicinch_object.citocup(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
        elif choice_quant.get() == "Millilitres":
            if choice_quant2.get() == "Gallons":
                output = millilitre_object.mltog(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Metres":
                output = millilitre_object.mltocm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Litres":
                output = millilitre_object.mltol(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Feet":
                output = millilitre_object.mltocf(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Inches":
                output = millilitre_object.mltoci(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Millilitres":
                output = millilitre_object.mltoml(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Fluid Ounces":
                output = millilitre_object.mltof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Quarts":
                output = millilitre_object.mltoq(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cups":
                output = millilitre_object.mltocup(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
        elif choice_quant.get() == "Fluid Ounces":
            if choice_quant2.get() == "Gallons":
                output = fluidoz_object.fltog(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Metres":
                output = fluidoz_object.fltocm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Litres":
                output = fluidoz_object.fltol(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Feet":
                output = fluidoz_object.fltocf(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Inches":
                output = fluidoz_object.fltoci(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Millilitres":
                output = fluidoz_object.fltoml(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Fluid Ounces":
                output = fluidoz_object.fltof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Quarts":
                output = fluidoz_object.fltoq(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cups":
                output = fluidoz_object.fltocup(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
        elif choice_quant.get() == "Quarts":
            if choice_quant2.get() == "Gallons":
                output = quart_object.qtog(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Metres":
                output = quart_object.qtocm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Litres":
                output = quart_object.qtol(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Feet":
                output = quart_object.qtocf(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Inches":
                output = quart_object.qtoci(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Millilitres":
                output = quart_object.qtoml(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Fluid Ounces":
                output = quart_object.qtof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Quarts":
                output = quart_object.qtoq(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cups":
                output = quart_object.qtocup(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
        elif choice_quant.get() == "Cups":
            if choice_quant2.get() == "Gallons":
                output = cup_object.cuptog(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Metres":
                output = cup_object.cuptocm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Litres":
                output = cup_object.cuptol(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Feet":
                output = cup_object.cuptocf(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cubic Inches":
                output = cup_object.cuptoci(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Millilitres":
                output = cup_object.cuptoml(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Fluid Ounces":
                output = cup_object.cuptof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Quarts":
                output = cup_object.cuptoq(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Cups":
                output = cup_object.cuptocup(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
    elif quantity.get() == "Length":
        if choice_quant.get() == "Kilometres":
            if choice_quant2.get() == "Kilometres":
                output = km_object.kmtokm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Miles":
                output = km_object.kmtomi(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Metres":
                output = km_object.kmtom(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Yards":
                output = km_object.kmtoy(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Feet":
                output = km_object.kmtof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Inches":
                output = km_object.kmtoi(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Centimetres":
                output = km_object.kmtocm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Millimetres":
                output = km_object.kmtomm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Micrometres":
                output = km_object.kmtomicm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Nanometres":
                output = km_object.kmtonm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
        elif choice_quant.get() == "Miles":
            if choice_quant2.get() == "Kilometres":
                output = mile_object.mitokm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Miles":
                output = mile_object.mitomi(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Metres":
                output = mile_object.mitom(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Yards":
                output = mile_object.mitoy(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Feet":
                output = mile_object.mitof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Inches":
                output = mile_object.mitoi(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Centimetres":
                output = mile_object.mitocm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Millimetres":
                output = mile_object.mitomm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Micrometres":
                output = mile_object.mitomicm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Nanometres":
                output = mile_object.mitonm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
        elif choice_quant.get() == "Metres":
            if choice_quant2.get() == "Kilometres":
                output = metre_object.mtokm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Miles":
                output = metre_object.mtomi(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Metres":
                output = metre_object.mtom(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Yards":
                output = metre_object.mtoy(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Feet":
                output = metre_object.mtof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Inches":
                output = metre_object.mtoi(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Centimetres":
                output = metre_object.mtocm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Millimetres":
                output = metre_object.mtomm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Micrometres":
                output = metre_object.mtomicm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Nanometres":
                output = metre_object.mtonm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
        elif choice_quant.get() == "Yards":
            if choice_quant2.get() == "Kilometres":
                output = yard_object.ytokm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Miles":
                output = yard_object.ytomi(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Metres":
                output = yard_object.ytom(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Yards":
                output = yard_object.ytoy(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Feet":
                output = yard_object.ytof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Inches":
                output = yard_object.ytoi(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Centimetres":
                output = yard_object.ytocm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Millimetres":
                output = yard_object.ytomm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Micrometres":
                output = yard_object.ytomicm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Nanometres":
                output = yard_object.ytonm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
        elif choice_quant.get() == "Feet":
            if choice_quant2.get() == "Kilometres":
                output = feet_object.ftokm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Miles":
                output = feet_object.ftomi(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Metres":
                output = feet_object.ftom(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Yards":
                output = feet_object.ftoy(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Feet":
                output = feet_object.ftof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Inches":
                output = feet_object.ftoi(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Centimetres":
                output = feet_object.ftocm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Millimetres":
                output = feet_object.ftomm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Micrometres":
                output = feet_object.ftomicm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Nanometres":
                output = feet_object.ftonm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
        elif choice_quant.get() == "Inches":
            if choice_quant2.get() == "Kilometres":
                output = inch_object.itokm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Miles":
                output = inch_object.itomi(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Metres":
                output = inch_object.itom(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Yards":
                output = inch_object.itoy(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Feet":
                output = inch_object.itof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Inches":
                output = inch_object.itoi(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Centimetres":
                output = inch_object.itocm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Millimetres":
                output = inch_object.itomm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Micrometres":
                output = inch_object.itomicm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Nanometres":
                output = inch_object.itonm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
        elif choice_quant.get() == "Centimetres":
            if choice_quant2.get() == "Kilometres":
                output = centimetre_object.cmtokm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Miles":
                output = centimetre_object.cmtomi(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Metres":
                output = centimetre_object.cmtom(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Yards":
                output = centimetre_object.cmtoy(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Feet":
                output = centimetre_object.cmtof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Inches":
                output = centimetre_object.cmtoi(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Centimetres":
                output = centimetre_object.cmtocm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Millimetres":
                output = centimetre_object.cmtomm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Micrometres":
                output = centimetre_object.cmtomicm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Nanometres":
                output = centimetre_object.cmtonm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
        elif choice_quant.get() == "Millimetres":
            if choice_quant2.get() == "Kilometres":
                output = millimetre_object.mmtokm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Miles":
                output = millimetre_object.mmtomi(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Metres":
                output = millimetre_object.mmtom(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Yards":
                output = millimetre_object.mmtoy(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Feet":
                output = millimetre_object.mmtof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Inches":
                output = millimetre_object.mmtoi(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Centimetres":
                output = millimetre_object.mmtocm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Millimetres":
                output = millimetre_object.mmtomm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Micrometres":
                output = millimetre_object.mmtomicm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Nanometres":
                output = millimetre_object.mmtonm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
        elif choice_quant.get() == "Micrometres":
            if choice_quant2.get() == "Kilometres":
                output = micrometre_object.mictokm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Miles":
                output = micrometre_object.mictomi(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Metres":
                output = micrometre_object.mictom(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Yards":
                output = micrometre_object.mictoy(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Feet":
                output = micrometre_object.mictof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Inches":
                output = micrometre_object.mictoi(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Centimetres":
                output = micrometre_object.mictocm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Millimetres":
                output = micrometre_object.mictomm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Micrometres":
                output = micrometre_object.mtomicm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Nanometres":
                output = micrometre_object.mictonm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
    elif quantity.get() == "Speed":
        if choice_quant.get() == "Kilometres per hour":
            if choice_quant2.get() == "Kilometres per hour":
                output = kmph_object.kmtokm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Miles per hour":
                output = kmph_object.kmtomi(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Metre per second":
                output = kmph_object.kmtom(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Foot per second":
                output = kmph_object.kmtof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Knots":
                output = kmph_object.kmtokn(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
        elif choice_quant.get() == "Miles per hour":
            if choice_quant2.get() == "Kilometres per hour":
                output = mph_object.mItokm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Miles per hour":
                output = mph_object.mItomi(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Metre per second":
                output = mph_object.mItom(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Foot per second":
                output = mph_object.mItof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Knots":
                output = mph_object.mItokn(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
        elif choice_quant.get() == "Metre per second":
            if choice_quant2.get() == "Kilometres per hour":
                output = mps_object.mtokm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Miles per hour":
                output = mps_object.mtomi(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Metre per second":
                output = mps_object.mtom(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Foot per second":
                output = mps_object.mtof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Knots":
                output = mps_object.mtokn(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
        elif choice_quant.get() == "Feet per second":
            if choice_quant2.get() == "Kilometres per hour":
                output = fps_object.ftokm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Miles per hour":
                output = fps_object.ftomi(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Metre per second":
                output = fps_object.ftom(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Foot per second":
                output = fps_object.ftof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Knots":
                output = fps_object.ftokn(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
        elif choice_quant.get == "Knots":
            if choice_quant2.get() == "Kilometres per hour":
                output = kn_object.ktokm(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Miles per hour":
                output = kn_object.ktomi(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Metre per second":
                output = kn_object.ktom(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Foot per second":
                output = kn_object.ktof(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)
            elif choice_quant2.get() == "Knots":
                output = kn_object.ktokn(value)
                ent_convert.insert(0, output)
                ent_convert.grid(row=7, column=1)


# button to convert unit

btn_convert = Button(converter,fg="#46484a",bg="#88a5db", font=("Tw Cen MT",20), text="Convert", command=conversion)
btnclose=Button(converter,text="Close",command=converter.destroy)
btnclose.grid(row=100,column=0,columnspan=converter.grid_size()[0],sticky="nsew")
btnclose.config(font=("Tw Cen MT",20),fg="#46484a",bg="#88a5db",relief=RAISED,bd=3,width=30)


# infinite loop
converter.mainloop()
