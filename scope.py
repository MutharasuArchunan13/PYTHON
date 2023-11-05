# in python have scope -->LEGB(local,enclose,global,built-in)
value = 'global_val'
def find_value():
    value='local_val'
    print(value)

find_value()
print(value)
#build-in
""" the build-in scope is global so we can override that function or methods """
def min(*a):
    pass

values=min(1,3,5,3,6,8,9)#expected output is 1 but
print(values)

x='global_x'
def outer():

    x='outer_x'
    def inner():
       global x
       x='inner_x'
       print(x)
    inner()
    print(x)
outer()
print(x)

