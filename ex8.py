'''Write a Python class to convert an integer to a roman numeral'''

class Convert:
    def to_roman(self, n):
        integar = [
            1000,900,500,400,
            100,90,50,40,
            10,9,5,4,
            1
            ]
        roman = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        num_roman = ''
        x = 0
        while n > 0:
            for i in range(n // integar[x]):
                num_roman += roman[x]
                n -= integar[x]
            x+=1
        return num_roman

print(Convert().to_roman(1))
