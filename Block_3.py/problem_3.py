"""
Count how many times the letter "a" appears in a sentence 
(try .count() first, then try it without .count() using ideas you already have)."""
# using .count()
sentence = input("Enter sentence : ")
count_a = sentence.lower().count("a")
print(count_a)

# without .count()
sentence = input("Enter sentence : ")
count = 0
for ch in sentence.lower() :
    if ch == "a" :
        count += 1
print(count)