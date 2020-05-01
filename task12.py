Convert = input("To convert the temperature in Celcius to Fahrenheit, press 'f'. To convert the temperature in Fahrenheit to Celcius, press 'c'. In order ro quit - any other key: ")

if Convert == 'f':   
    def Convert_C_to_F (C):
        Fahrenheit=(C*9/5)+32
        print(Fahrenheit)
    C=float(input("Enter a temperature in Celcius: "))
    Convert_C_to_F (C)
    
elif Convert == 'c':
    def Convert_F_to_C (F):
        Celcius=(F-32)*5/9
        print(Celcius)
    F=float(input("Enter a temperature in Fahrenheit: "))
    Convert_F_to_C (F)
