'''
find weight of String
'''
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
str1 = input("Enter String for weight ").lower()
total = 0

for ch in str1:
    if ch in alphabet:
        total = total + (alphabet.index(ch)+1)

print(total)

# another way to find weight of string
alpha="abcdefghijklmnopqrstuvwxyz"
strings="abc"
counter=0
# Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
for i,v in enumerate(alpha,1):
    for j in strings:
        if v==j:
            counter+=i
print(counter)
