# taking an input list
list1=[1,2,2,4,5,6,8,9,8,4]
# taking an input empty list
list2=[]
count=0
for i in list1:
    if i not in list2:
        count=count+1
        list2.append(list1)
print(count)