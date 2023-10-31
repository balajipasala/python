def myFun(arg1, arg2, arg3):
	print("arg1:", arg1)
	print("arg2:", arg2)
	print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Thunder", "for", "Thunder")
myFun(*args)

kwargs = {"arg1": "Thunder", "arg2": "for", "arg3": "Thunder"}
myFun(**kwargs)
