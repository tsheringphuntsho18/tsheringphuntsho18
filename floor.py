input_string = '(((((((((())'
def findFloorAtEnd(input_string):
    floor_at_end=0
    for i in input_string:
        if i == '(':
            floor_at_end +=1 # goes up the floor
        else:
            floor_at_end -=1 #goes down the floor
    print('At the end,you will be at floor number:',floor_at_end)
    
findFloorAtEnd(input_string)
        