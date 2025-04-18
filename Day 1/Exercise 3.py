# This exercise requires us to swap the contents of glass1 and glass2 without re using the string "milk" or "juice"
glass1 = "milk"
glass2 = "juice"
print(glass1 + " " + glass2)

temp = glass1
glass1 = glass2
glass2 = temp
print(glass1 + " " + glass2)
