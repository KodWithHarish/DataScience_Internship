import sys 
arg=sys.argv
if len(arg)>2:
    x=int(arg[1])
    y=int(arg[2])
    sum=x+y
    print(sum)
else:
    print("Argument Error")

# python sum.py 3 4