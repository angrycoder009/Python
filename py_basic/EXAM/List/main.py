import copy
#creation of list
item = [1,2,3,5]

#properties-->
#mutable 
# ->> modify
item[0] = 3
item[1] = 4
item[2] = 6
item[3] = 8
print(item)  #output : [3, 4, 6, 8]

#differnt type of list

#empty list
l1=[]
print(l1) #ouput : []

#integer list
l2=[1,2,3,4]
print(l2) #ouptut : [1, 2, 3, 4]
#acceing value by indexing
print(l2[0] ,l2[1],l2[2],l2[3])

#string list
l3=["fruit",'banana',"pineapple"]
print(l3)  #output : ["fruit",'banana',"pineapple"]
#acceing value by indexing
print(l3[0] ,l3[1],l3[2])


 


 # list methods


 #append()-->used to add element to the end of list
i1=[1,2,3]
i1.append(4)
i1.append(5)
print(i1) #output :[1,2,3,4,5]


#max() ->> used to find maximum element in list
i2=[15,17,20]
print(max(i2)) #ouput : 20


#min() --> used to find minimum element in list
i3=[-12,-13,100,-300]
print(min(i3)) #output : -300

#reverse() -> used to reverse the object in list
i4=[1,2,3,4]
i4.reverse()
print(i4) #output :[4,2,3,1]

#remove() -> used to remove given object in list
i5=[1,2,3]
i5.remove(3)
print(i5) #output: [1, 2]

#sort()--> used to sort element by ascending or descending
i6=[10,40,100,50,70,60]
i6.sort()
print(i6) #output :[10, 40, 50, 60, 70, 100]

#pop() ->used to delete element by giving element
i7=[1,2,3]
i7.pop(1)
print(i7) #output :[1, 3]

#clear() ->used to clear or fully remove each element
i8=[0,1,2,3]
i8.clear()
print(i8)  #output :[]

#index() -> use to searching  index of element by giving object
i9=[1,2,3,4]
print(i9.index(3)) #output :2

#insert() ->used to insert element with the help of index
i10=[1,2,3,5,6]
i10.insert(3,10) 
print(i10) #output :[1,2,3,10,5,6]



#count() -> used to count the occurace of element
i11=[1,1,1,1,3,3,3,3,5,5,5,5]
print(i11.count(1)) #output :4
print(i11.count(3)) #output : 4
print(i11.count(5))  #output : 4


#copy() ->used to copy element without effection original element
i12=[1,2,3]
print(copy.copy(i12)) #output : copied element
i12[1]=4
print(i12) #output : [1,4,3]


#extend() ->used to merge one list to another
i13=[1,2,3]
i14=[4,5,6]
i13.extend(i14)
print(i13) #output : [1,2,3,,4,5,6]






#List slicing 

#1. Basic Slicing 
s1=[10,20,30,40,50]
print(s1[1:3]) #output : [20,30]

#2. Slicing with default values

#(i)From the begining of 4th element
s2=[1,2,3,4,5]
print(s2[:4]) #output : [1,2,3,4]

#(ii)from the fourth element to end
print(s2[1:]) #output : [2,3,4,5]

#(iii) the entire element
print(s2[:]) #output : [1,2,3,4,5]


#3.Slicing  with step
s3=[1,2,3,4,5]
print(s3[::2]) #output : [1,3,5]

#4. Negative indices
s4=[1,2,3,4,5]

#(i)from the beginnig to second lasat
print(s4[:-1]) #output : [1, 2, 3, 4]

#(ii) fromt the second last to beginning
print(s4[-5:]) #output : [1, 2, 3, 4, 5]

#(iii)reverse the list
print(s4[::-1]) #output : [5, 4, 3, 2, 1]



#4.Modifying list with slicing
s5=[1,2,3,4]
s5[1:3] =[5,6]
print(s5)  #output : [1, 5, 6, 4]


s6=[1,2,3,4,5,6,7,8,9]
print(s6[3:9:2])
print(s6[::2])



l=[1,2,3,4,5,6,7,8,9]
#return a list of numbers starting from last to second item of list
print(l[::-1][0:-1])
print(l[-1:-9:-1])
print(l[-1:0:-1])



#2.function to make pairs of two lsit
def make_pairs(l1,l2):
    len1=len(l1)
    len2=len(l2)
    if len1==len2:
      return [(l1[i],l2[i]) for i in range(0,len1) ]
      

print(make_pairs([1,2,3],[4,5,6]))



#3.function alternating(lst) 
#return true if alternatively odd  && even starting with even number
#otherwise return false
def alternating(lst):
   len1=len(lst)
   return [True for i in range(len1 - 1) if lst[0] % 2 == 0 and lst[i + 1] % 2 != 0] 

     

print(alternating([1,3,6,5]))