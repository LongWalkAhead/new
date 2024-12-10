


def convert_f_c(temperature_f):
    temperature_c = (temperature_f-32) * 5/9
    return temperature_c
try: 
    temperature_f = float(input(f"the temperature is "))
    temperature_c = convert_f_c(temperature_f)
except ValueError:
    print("please try again")
else:
    print(f" {temperature_f} degrees fahrenheit is {temperature_c} degrees celcius")
finally:
    print("thank you for using this application!")






#Fahrenheit - 32 * 5/9.