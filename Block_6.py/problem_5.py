"""
Build a word-frequency counter: given a sentence, 
count how many times each word appears using a dictionary 
(loop through the words, use .get(word, 0) + 1 )."""

sentence = input("Enter a sentence : ")
my_dic = dict()
r = sentence.lower().split()
for i in r :
    my_dic.update({i : r.count(i)})
print(my_dic)