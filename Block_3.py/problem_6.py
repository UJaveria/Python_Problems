"""
Write a function that takes a sentence and returns it with every word capitalized, without using 
.title() (use .split() , .capitalize() , and .join() )."""


def capitalized(sentence) :
    string =  sentence.split()
    for i in string :
        st = str(i)
        print(st.capitalize(), end= " ")
sentence = input("Enter sentence : ")
capitalized(sentence)