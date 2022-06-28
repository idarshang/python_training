input_string=input('Enter a string')
input_string=input_string.casefold()
print(input_string)
vowels='aeiou'
# vlist=[]
# for char in input_string:
#     if char in vowels:
#         vlist.append(char)
#
# print(vlist)
# num_vowels=[vowel for vowel in input_string if vowel in vowels]
#
# print(len(num_vowels),num_vowels)

# count number of times each vowel occures

vowel_count = {}.fromkeys(vowels, 0)
print(vowel_count)
for char in input_string:
    if char in vowels:
        vowel_count[char]+=1

print(vowel_count)



# def numofvowels(input):
#     num_vowels=[vowel for vowel in input if vowel in vowels]
#     return  num_vowels
#
# print(numofvowels(input_string))