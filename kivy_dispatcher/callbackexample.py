# callback = a function that is an argument in another function
# Call back example
def square_val(val):
    return val ** 2

def caller(func, i):
    return(func(i))

a_list = range(0, 10)
print(a_list)

# list comprehension
newlist = [caller(square_val, i) for i in a_list]
print(newlist)
