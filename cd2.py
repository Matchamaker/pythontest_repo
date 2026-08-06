def count():

    Z=0

    f = open("data2.txt", "r")
    z = f.read()
    w = z.split()
    for ch in w:
        if ch == "a":
            Z += 1
    f.close()

    return Z
print(count())
 
 

