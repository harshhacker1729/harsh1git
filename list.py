l=[1,2,6,22,44,12,55,66]
c=["harsh","om","anand","krishna"]
#l[3:-3])
print(l[::-3])#its answer is [66,44,2] gap 3 from the last
print(l[::-1])#remember that reverse the all list in to oppsite
#print(l[1:])
#print(l[0:-1])"""
'''mutable we can change replace and change is called mutable list mutable '''
l[2]="harsh"
l.append("anand")#In last of list it will make on add more items in list
#append is used for add items to the list.
l.extend(c)
print(l)
