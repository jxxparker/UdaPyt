def echo(arg):
    return arg

type(echo)     # <class 'function'>
hex(id(echo))  # 0x1003c2bf8
print(echo)    # <function echo at 0x1003c2bf8>

foo = echo
hex(id(foo))   # 0x1003c2bf8
print(foo)     # <function echo at 0x1003c2bf8>

'echo' in locals()

isinstance(echo, object)  # => True