#from numpy.ma.extras import average


def greeting(name,):
    print("To the\t" + "LNCT")




def lettergenerator(name, date, ending):
    st = f"Hello mam,\n This is {name} and I will not come to college on {date}"
    print(st)
    print(ending)

def average(a, b):
    return (a+b)/2

print("Executing Function..")
greeting("Teacher",)
lettergenerator("Aniket", "26th oct","Thanks you")
#lettergenerator("Mehra", "20th oct", "Thanks")
print(average(34, 23))
print("done")