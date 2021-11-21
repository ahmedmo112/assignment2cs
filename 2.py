h1 = int(input("h1="))
m1 = int(input("m1="))
s1 = int(input("s1="))

h2 = int(input("h2="))
m2 = int(input("m2="))
s2 = int(input("s2="))

print(f"First time is {h1}:{m1}:{s1} ")
print(f"Second time is {h2}:{m2}:{s2} ")

if s1 > s2:
    s3 = s1 - s2
    print(s3)
else:
    s1 = s1 + 60
    m1 = m1 - 1
    s3 = s1 - s2
    print(s3)

if m1 > m2:
    m3 = m1 - m2
    print(m3)
else:
    m1 = m1 + 60
    h1 = h1 - 1
    m3 = m1 - m2
    print(m3)

if h1 >= h2:
    h3 = h1 - h2
    print(h3)
else:
    print("wrong input")

print(f"The difference between two times is {h3}:{m3}:{s3} ")
