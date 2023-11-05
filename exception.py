
try:
    f=open('new.txt')
    if f.name !="new.txt":
        raise  Exception
except TypeError as e:
    print(e)
except Exception as e:
    print('error will be occured',e)
else:
    print(f.read())
    f.close()
finally:
    print('excute successfully')
