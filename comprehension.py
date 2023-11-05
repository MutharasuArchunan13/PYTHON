#list comprehension
nums=[1,2,3,4,5,6,7,8,9]
my_list=[]
for num in nums:
    my_list.append(num)
print(my_list)

#in comprehension in list
my_list=[num for num in nums]
print(my_list)


#dictionary conprehension
diction={'blue','block','muth'}
nary={'star','rock','arasu'}
my_dict={}
for dic,nan in zip(diction,nary):
    my_dict[dic]=nan
print(my_dict)
#or
my_dict={dic:nan for dic,nan in zip(diction,nary)}
print(my_dict)


#set comprehension
sets=[1,1,2,4,3,2,5,3,6,4,6,3,2]
set_list=set()
for set in sets:
    set_list.add(set)
print(set_list)
#or
set_list={set for set in sets}
print(set_list)

#generator expression
num = [1,2,3,4,5,6,7,8]
def gen_exp(nums):
    for n in nums:
        yield n*n
gen_res=gen_exp(num)
print(gen_res)