"""
Loop through a sentence's characters and use continue to skip vowels, 
building up a new string of only consonants"""

sentence = input("Enter a sentence : ")

for ch in sentence.lower() :
    if (ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u") :
        continue
    else :
        print(ch,end="")