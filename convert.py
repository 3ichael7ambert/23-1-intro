def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """

    # YOUR CODE HERE
    if unit_in=="f" and unit_out=="c":
        temp=(temp-32)*5/9
    elif unit_in=="c" and unit_out=="f":
        temp=(temp*9/5)+32
    #Celcius to Kelvin
    elif unit_in=="c" and unit_out=="k":
        temp=temp+ 273.15

    #Fahreheit to Kelvin
    elif unit_in=="f" and unit_out=="k":
        temp=(temp-32)*5/9+273.15


    #Kelvin to Celcius
    elif unit_in=="k" and unit_out=="c":
        temp=temp-273.15


    #Kelvin to  Fehrenheit
    elif unit_in=="k" and unit_out=="f":
        temp=(temp-273.15)*9/5+32

    return temp

    
print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

print("c", "k", 32, convert_temp("c", "k", 32), "should be 305.15")
print("f", "k", 32, convert_temp("f", "k", 32), "should be 273.15")
print("k", "c", 32, convert_temp("k", "c", 32), "should be -241.15")
print("k", "f", 32, convert_temp("k", "f", 32), "should be -402.07")




# Ask for user input
unit_in = input("Enter input unit (f or c or k): ")
unit_out = input("Enter output unit (f or c or k): ")
temp = float(input("Enter temperature: "))

# Call the convert_temp function to convert the temperature
result = convert_temp(unit_in, unit_out, temp)

# Print the result
print(f"{temp:.2f} {unit_in} is equal to {result:.2f} {unit_out}")
