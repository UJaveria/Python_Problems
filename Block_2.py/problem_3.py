"""
Predict then check: bool(0), bool(1), bool(""), bool("False") -that last one
especially; make them explain why a non-empty string is always True regardless of what it says."""

# bool(0) False
# bool(1) True
# bool("") False
# bool("False") True
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("False"))

# Because it conatin values and these are of type boolean, predicting either here a value is or not. Its not for printing what it have in it
