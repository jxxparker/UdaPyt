# #Functions

# # def fn_name(param1, param2):
# #     value = do_something()
# #     return value

# def no_return():
#     pass

# x = no_return
# print(x)

x = 2
def fun(y):
    z = 5
    print(locals())
    print(globals()['x'])
    print(x,y,z)
fun(3)