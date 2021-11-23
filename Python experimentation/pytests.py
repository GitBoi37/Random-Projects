import copy
import timeit

def deepCopyArray(arr):
    a = arr
    b = copy.deepcopy(a)

def listDeepCopyArray(arr):
    a = arr
    b = [i[:] for i in a]

#test if file is ran as a script
if __name__ == "__main__":
    a = [[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4]]
    n = 10000
    f1 = "deepCopyArray"
    f2 = "listDeepCopyArray"
    r = 15
    t1 = timeit.repeat(f"{f1}({a})", number=n, globals=globals())
    t2 = timeit.repeat(f"({a})", number=n,globals=globals())
    a1 = sum(t1)/len(t1)
    a2 = sum(t2)/len(t2)
    print(f"repeated {n} times averaged over {r} trials\n{f1}: {a1}")
    print(f"{f2}: {a2}")
    print(f"{f2} is {a1/a2} times faster than {f1}")
