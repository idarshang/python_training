input_string=input('Enter a string')
input_string=input_string.casefold()
print(input_string)
vowels='aeiou'
def numofvowels(input):
    num_vowels=[vowel for vowel in input if vowel in vowels]
    return  num_vowels

print(numofvowels(input_string))