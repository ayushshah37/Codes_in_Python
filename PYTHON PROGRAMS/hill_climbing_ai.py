graph = [
    [5, 12, 8, 3, 19, 25, 10, 7],
    [15, 22, 18, 13, 29, 35, 20, 17],
    [25, 32, 34, 23, 39, 45, 30, 27],
    [35, 42, 38, 33, 49, 55, 40, 37],
    [45, 52, 48, 43, 59, 65, 50, 47],
    [55, 62, 58, 53, 69, 75, 60, 57],
    [65, 72, 68, 63, 79, 85, 70, 67],
    [75, 82, 78, 73, 89, 95, 80, 77]
]

state=[0,0]
max_value=-100
while True :
    old_value=max_value
    x=state[0]
    y=state[1]
    possible_moves=[[x-1,y],[x-1,y-1],[x,y-1],[x-1,y+1],[x,y+1],[x+1,y+1],[x+1,y],[x,y+1]]
    for x1,y1 in possible_moves:
        if 0<=x1<8  and 0<=y1<8:
            value=graph[x1,y1]
            if value>max_value:
                print(value)
                max_value=value
                state=[x1,y1]
        if old_max==max_value:
            print(state)
            break
print(f"max value is {max_value} at state :{state}")

