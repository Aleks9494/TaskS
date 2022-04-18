
def bread (func):
    def wrapper(m):
        print ('<=======>')
        func(m)
        print ('<_______>')
    return wrapper

def sous(func):
    def wrapper(m):
        print ('cheese sous')
        func(m)
        print ('tomato sous')
    return wrapper

def salat(input_arg, input_arg2):
    def my_decorator(func):
        def wrapper(m):
            print (input_arg)
            func(m)
            print (input_arg2)
        return wrapper
    return my_decorator

@bread
@sous
@salat ('cheese','salad')
def sandwitch(m):
    print (m)

sandwitch ('RiBay Meat')