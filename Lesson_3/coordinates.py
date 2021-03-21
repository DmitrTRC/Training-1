def get_quadrant(coord_x, coord_y):
    answer = 0
    if coord_x > 0 and coord_y > 0:
        answer = 1
    elif coord_x < 0 and coord_y > 0:
        answer = 2
    elif coord_x < 0 and coord_y < 0:
        answer = 3
    elif coord_x > 0 and coord_y < 0:
        answer = 4
    elif coord_x == 0 and coord_y == 0:
        answer = 0
    elif coord_x == 0:
        answer = -1
    else:
        answer = -2
    return answer


def print_quadrant(quadrant):
    if quadrant > 0:
        print(f'Point in {quadrant} quadrant')
    elif quadrant < 0:
        if quadrant == -1:
            print('Point on O-Y beam ')
        else:
            print('Point on O-X beam ')
    else:
        print('Zero point')


while True:
    x = float(input('X -> '))
    y = float(input('Y -> '))
   
    print_quadrant(get_quadrant(x, y))
    if input('Do you want to continue ? ') != 'y':
        break
