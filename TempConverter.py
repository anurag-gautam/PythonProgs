import sys

def Fahrenheit2Celcius(Tf):
    Tc=(5 * (Tf-32))/9
    return Tc

def Celcius2Fahrenheit(Tc):
    Tf=(9 * Tc)/5 + 32
    return Tf

if __name__ == "__main__":
    print "Temperature Converter"
    try:
        Temp = float(raw_input("Enter a temperature: "))
    except:
        print >> sys.stderr, "Invalid Value..Try Again!..."
        sys.exit()


    print "Convert to (F or f)ahrenheit or (C or c)elsius? "
    choice = raw_input()
    if choice == "F" or choice == "f":
        print "Entered Temperature is {} Celcius and its conversion in Fahrenheit is {:.2f}".format(Temp,Celcius2Fahrenheit(Temp))
    elif choice == "C" or choice == "c":
        print "Entered Temperature is {} Fahrenheit and its conversion in Celcius is {:.2f}".format(Temp,Fahrenheit2Celcius(Temp))
    else:
        print "Respond with F or C option..Try again! "