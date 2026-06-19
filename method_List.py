# append()  -->  add an element in the end of List

myFriends = ["Osama" , "Ahmed" , "Sayed"]

myFriends.append("Alaa")
myFriends.append(True)
print (myFriends)

MyOldFriends = ["Omar" , "Ali" , "Abdo"]
myFriends.append(MyOldFriends)
print (myFriends)

print(myFriends[2])
print(myFriends[4])
print(myFriends[5][1])

print("=" * 50)

# extend()  -->  The same of append but there is a difference , you should to run it and show the result

a = [1 , 2 , 3 , 4]
b = ["A" , "B" , "C"]

a.extend(b)
print(a)

print("=" * 50)

# remove()  -->  delete the element in the list

x = [1 , 2 , 3 , 4 , 5 , "Osama" , True , "Osama" , "Osama"]

x.remove("Osama")
print(x)

print("=" * 50)

# sort()  -->  arrangement the elements

y = [1 , 2 , 100 , 120 , -10 , 17 , 29]

y.sort()
print(y)

y.sort(reverse=True)
print(y)

print("=" * 50)

# reserve  -->  يعكس العناصر

z = [10 , 1 , 9 , 80 , 100 , "Osama" , 100]

z.reverse()
print(z)

print("=" * 50)

# clear()  -->  يشيل العناصر

m = [1 , 2 , 3 , 4]

m.clear()
print(m)


print("=" * 50)

# copy()  -->  copy the elements

n = [1 , 2 , 3 , 4]

o = n.copy()

print (n)
print (o)

n.append(5)

print (n)
print (o)

print("=" * 50)

# count()  -->  count the elements of the list

p = [1 , 2 , 4 , 3 , 9 , 10 , 1 , 2 , 1]
print(p.count(1))

print("=" * 50)

# index()  -->  توصل للعنصر اللي انا عايزه

p = [1 , 2 , 4 , 3 , 9 , 10 , 1 , 2 , 1]
print(p.index(2))

print("=" * 50)

# insert(index , object)  -->  add element in position that you are choosing it

f = [1, 2 , 3 , 4 , 5 , "A" , "B" , "C"]

f.insert(1,"Test")
print(f)

print("=" * 50)

# pop(index)  -->  يجيب العنصر اللي انت عايزه في الليست

f = [1, 2 , 3 , 4 , 5 , "A" , "B" , "C"]
print(f.pop(2))