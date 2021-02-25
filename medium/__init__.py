def a(b):
    # print(b)
    if(b==0):
        return 0
    return str(b)+(str(a(b-1)))

print(10%10)