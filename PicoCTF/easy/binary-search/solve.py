r = int(input("maximum: ")) 
l = 0

while l <= r:
    m = l + (r - l)//2
    print(m)
    
    res = input("higher, lower or equal: ")
    if res == "higher":
        l = m
    if res == "lower":
        r = m
    if res == "equal":
        print("index is ",m)
        break
