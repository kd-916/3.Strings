#count vowel
z=input("Enter the word to find number of vowel")

def vowel():
    a=z.count('a')+z.count('e')+z.count('i')+z.count('o')+z.count('u')+z.count('A')+z.count('E')+z.count('I')+z.count('O')+z.count('U')
    print(a)

vowel()
