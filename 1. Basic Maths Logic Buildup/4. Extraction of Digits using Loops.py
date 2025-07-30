# Extraction of Digits using Loops

"""
Concepts use in it:
    Let X = 1234

    - Modulo(%)(Remainder) - X%10 => 1234%10 => 4
    - Floor Division(//)(Remove Decimal Point) - X//10 => 1234//10 => 123 (Here floor division removes .4 from 123.4)
"""

"""
Example Code is Given Below
"""

X = int(input("Enter the Number :"))
Y = X
print()

while Y!=0:
    print(f"{Y}%10 :",Y%10)
    print(f'{Y}//10 :',Y//10)
    print()
    Y//=10

