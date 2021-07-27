#Sequences
#The first category of collections we examine are sequences – sized, iterable ordered containers of data. We'll see the similarities and differences between three sequence types - list, tuple, and string

s = 'Udacity'

# print(s[0])
# print(s[1])
# print(s[4])
# print(s[7]) #wont work

# print(s[-1]) # y
# print(s[-2])

#--------
# print(s[0:2]) #Ud from 0 - 2
# print(s[0:3]) #Uda
# print(s[4:7]) #ity

print(s[1:5:2]) #dc first number is where we start
                #   second is where we end
                #   last number is the jumping number

print(s[4::-2]) #iaU   first number is where we start
                #       :: means go back
