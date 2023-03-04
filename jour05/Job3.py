charactere = (input("Chaine de charactère:"))

def reverse(word):
    if len (word) in [0, 1]:
        return word
    else:
        return word[-1] + reverse(word[-1])
    
#print(reverse(charactere))
word = charactere
print(word[::-1])