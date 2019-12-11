a=[1,2,3,4]
print('List given : ',a)
def rf(s):
    a[2]=7
    print(s)
    return
rf(a)
print("Updated List outside the method = ",a)