input_string ='((())))(('
def findFloorAtEnd(input):
    floor_at_end = 0
    highest_floor = 0
    lowest_floor = 0
    for i in input:
        if i == '(':
            floor_at_end +=1
        else:
            floor_at_end -=1
        if floor_at_end > highest_floor:
            highest_floor=floor_at_end
        if floor_at_end < lowest_floor:
            lowest_floor=floor_at_end
    print(f'The highest floor you will be at is {highest_floor} and the lowest floor you would be is at {lowest_floor} and the final place is at {floor_at_end}')
findFloorAtEnd(input_string)