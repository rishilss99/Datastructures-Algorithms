import array
import collections

arr = array.array('l')
list = [1,2,3,4,5,5]
list.pop(5)
print(list)

dict = {5:"He",6:"Fe",8:"The",2:"Re"}

a = array.array('d',[2,3,4])
b = array.array('d',[5,6,7])
arr2d = array.array('d',a)

n = int(input())
st = ""
for i in range(n):
    st = st + input()
print(st,'\n')

dict1 = {"day1" : "Mon" ,"day2" : "Tue"}
dict2 = {"day3" : "Wed" , "day4" : "Thurs"}

res = collections.ChainMap(dict1,dict2)
print(res)