def predictPrice():
    wheelbase = float(input("Please Enter your car's wheel base \n"))
    carlength = float(input("Please Enter your car's total length \n"))
    carwidth = float(input("Please Enter your car's total width \n"))
    carheight = float(input("Please Enter your car's total height \n"))
    curbweight = float(input("Please Enter your car's curb height \n"))
    enginesize = float(input("Please Enter your car's Engine Size \n"))
    stroke = float(input("Please Enter your car's Stroke \n"))
    horsepower = float(input("Please Enter your car's horse Power \n"))
    peakrpm = float(
        input("Please Enter your car's RPM(revolutions per minute) \n"))

    return(wheelbase, carlength, carwidth, carheight, curbweight, enginesize, stroke, horsepower, peakrpm)
