#to replace any word/letter/string in a string
givenString = '''Well, this is a string intended to be searched into, there might be grammatical blunders in it, however, I can assure you that it will serve it's true purpose.
In life, thing's might not go the way we want, however, we must remain positive.'''

#first method
method1 = givenString.replace("is","you've been replaced") #first parameter is the string to be removed while the second parameter is the replacement
print(method1) 
#second method
method2 = givenString.translate(givenString.maketrans("to","ci",""))#first and second argument must be of same length as they are same as replace arguments. The third argument is for deleting any string.
print(method2)#the replacement is one-to-one mapping; t becomes c and o becomes i

#to delete "is"
delete = givenString.translate(givenString.maketrans("","","is"))
print(delete)