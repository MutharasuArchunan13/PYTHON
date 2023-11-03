# normally function is a set of codes  in python 'def'  keyword used to create a function
def hello():
    print('hello world')
    return 9
print(hello())


def students(name,age=20):
    return '{}, {} welcome dear'.format(name,age)

print(students('arun',30))


#arbitary argument now we don't know about the arguments are receives to use arbitary argument   *arg  return tupes 
def child(*args):
    return args
print(child('kumar','jaas','laks'))

#keyword argument 
def childs(child1,child2):
    print(child1,child2)

print(childs(child1='sahi',child2='babi'))


#arbitary keyword argument  **swargs  return dictionary
def bikes(**sargs):
    print(sargs)

print(bikes(fname='anubu',name='muthu'))

#Too check a year leaf or not

months=[0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leaf(year):
    return year % 4 ==0 and (year % 100 !=0 or year % 400 ==0)

def month_day(year,month):
    if not 1<=month <=12:
        print('invalid month')
    if month == 2 and  is_leaf(year) == True: return 29
    if 1<=month <=12:
        return months[month]

print(is_leaf(2000))
print(month_day(2004,2))