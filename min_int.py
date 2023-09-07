input=[10,-4,-1,25,-15,7,0]
def findMin(input):
    result_min=0
    for i in input:
        if i < result_min:
            result_min = i # new value is assign to the variable

    print('The minimum value is:',result_min)
findMin(input)
        