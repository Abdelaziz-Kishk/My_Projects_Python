# len()  -->   يشوف الكلمه عباره عن كام حرف

a = "I love python"
print(len(a))

print("=" * 50)

# strip()   rstrip()   lstrip()   -->   يشيل المسافات اللي في الاول او الاخر او الاتنين

b = "     I love python   "
print(b.strip())
print(b.rstrip())
print(b.lstrip())

print("=" * 50)

# title() -->  يخلي اول حرف في كل كلمه كابيتال

c = "I love 2d graphics And 3g Technology and python"
print(c.title())

print("=" * 50)

# capitalize()  -->  يخلي اول حرف في اول كلمه هي اللي كابيتال

d = "i love 2d graphics And 3g Technology and python"
print(d.capitalize())

print("=" * 50)

# zfill()  -->  شوف ال رن

e , f , g = "1" , "11" , "111"

print(e)
print(f)
print(g)

print(e.zfill(3))
print(f.zfill(3))
print(g.zfill(3))

print("=" * 50)

# upper()  -->  يخلي كل الحروف كابيتال
# lower()  -->  يخلي كل الحروف اسمول

h = "ZizO"

print(h.upper())
print(h.lower())

print("=" * 50)

# split() rsplit()  -->  يحط كل كلمه في الليست

i = "I Love python and PHP"

print(i.split())
print(i.rsplit())

print("=" * 50)

# center()

j = "Zizo"

print(j.center(8))   # spaces
print(j.center(8,"#"))   # hashes
print(j.center(8,"@"))   # @

print("=" * 50)

# count() == rjust() ljust()  -->  يشوف الكلمه دي موجوده كام مره

k = "I love python and PHP Becouse PHP is Easy"

print(k.count("PHP"))
print(k.count("PHP" , 0 , 25))  # يبحث من الحرف رقم 0 ل 25 كام مره موجوده PHP

print("=" * 50)

# swapcase()  -->  هيقلب الحروف كابيتال ل اسمول والعكس

l = "I Love Python"
m = "i love pYTHON"

print(l.swapcase())
print(m.swapcase())

print("=" * 50)

# startswith()  -->  True || False
# endswith()  -->    True || False

l = "I Love Python"

print(l.startswith("I"))
print(l.startswith("S"))
print(l.startswith("P" , 7 , 12))

print(l.endswith("I"))
print(l.endswith("n"))
print(l.endswith("e" , 2 , 6))

print("=" * 50)

# index(SubString , Start , End)
# find(SubString , Start , End)

n = "I love python"

print(n.index("p"))           # 7
print(n.index("p" , 0 , 10))  # 7
#print(n.index("p" , 0 , 5))  # error

print(n.find("p"))           # 7
print(n.find("p" , 0 , 10))  # 7
print(n.find("p" , 0 , 5))   # -1

print("=" * 50)

# replace(old value , new value , count)

o = "Hello One Two Three One One"

print(o.replace("One" , "1"))
print(o.replace("One" , "1" , 1))
print(o.replace("One" , "1" , 2))


print("=" * 50)

# join(Iterable)

p = ["Osama" , "Mohamed" , "Elsayed"]

print("-".join(p))
print(" ".join(p))
print(",".join(p))
