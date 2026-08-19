"""Predict then check the type of: 10 , 10.2, "10", True, 10==10.0, 10/2, 10//2 ."""
# Answers 
# 10 -> <class 'int'>
# 10.2 -> <class 'float'>
# "10" -> <class 'str'>
# True -> <class 'bool'>
# 10 == 10.0 .> <class 'bool'>
# 10/2 -> <class 'float'>
# 10//2 -> <class 'int'>
print(type(10))
print(type(10.2))
print(type("10"))
print(type(True))
print(type(10==10.0))
print(type(10/2))
print(type(10//2))