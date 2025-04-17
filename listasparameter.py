def addition(a,b,c,d,e):
    return a+b+c+d+e

l = [1,2,3,4,5]
print(addition(*l)) #output: 15


#the presence of * in front of the list makes the list to become a tuple of values
# the absence of * will bring an error like "TypeError: addition() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'"
#it presence in printing a list produces space separated values

print(*l) #output: 1 2 3 4 5