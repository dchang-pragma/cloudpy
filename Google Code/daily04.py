def repeat(s, exclaim):
    """
    Returns the string 's' repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    result = s + s + s # can also use "s * 3" which is faster (Why?)
    if exclaim:
        result = result + '!!!'
    return result



# s = 'Hello '
s = 2
s = repeat(s, True)
print(repeat(s, True))


def multiply_by_2(x):
    return 2*x

x = 1
x = multiply_by_2(x)
print(multiply_by_2(x))