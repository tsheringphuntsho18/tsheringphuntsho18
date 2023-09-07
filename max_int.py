input = [1,10,44,12,0,-1]
def findMax(input):
    result_max=0
    for i in input:
        if i > result_max:
            result_max=i
    print('The maximum of the input is:',result_max)
findMax(input)