
def maximum(x,y):
	if(x>y):
		maximum=x
	else:
		maximum=y

	return maximum


def SumMulArray(array):
    totalsum = array[0]   # 0 defines the first number in array
    totalmul = array[0]
    for i in range(1,len(array)):
        totalsum+=array[i]    # i defines the corrosponding number in array
        totalmul*=array[i]
        
    return [totalsum,totalmul]

def printNumbers (a,b=4.0,c=6.0):
    print(a)
    print(b)
    print(c)

pi=3.1416