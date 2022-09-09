Python 3.10.6 (v3.10.6:9c7b4bd164, Aug  1 2022, 17:13:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def subtract(x,y):
    """This is a docstring fo the subtract function."""
    return a - b
print(subtract._doc_)
SyntaxError: invalid syntax
print (subtract._doc_)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print (subtract._doc_)
NameError: name 'subtract' is not defined
def subtract(x,y):
    """This is a docstring of the subtract function."""
    return a - b

print (subtract._doc_)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print (subtract._doc_)
AttributeError: 'function' object has no attribute '_doc_'. Did you mean: '__doc__'?
print (subtract.__doc__)
This is a docstring of the subtract function.
