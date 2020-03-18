def f():
    print "f()"

# function name overwritten? -> yes
f()
f = 1
f()