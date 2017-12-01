def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):

        if game[i] == '/':
            result += 10 - get_value(game[i-1])   
        else:
            result += get_value(game[i])
        
        if frame < 10 and get_value(game[i]) == 10:
            result = strike_or_spare(game, i, result)
        
        if not in_first_half:
            frame += 1
        in_first_half = not in_first_half
        
        if is_x(game, i):
            in_first_half = True
            frame += 1

    return result

def strike_or_spare(game, i, result):
    if game[i] == '/':
        result += get_value(game[i+1])
    elif game[i] == 'X' or 'x':
        result += get_value(game[i+1])
        if game[i+2] == '/':
            result += 10 - get_value(game[i+1])
        else:
            result += get_value(game[i+2])
    return result


def is_x(game, i):
    return game[i] == 'X' or game[i] == 'x'


def get_value(char):
    open_points = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    roll_max = ['X', 'x', '/']
    for point in open_points:
        if char == point:            
            return int(point)

    for roll in roll_max:    
        if char == roll:
            return 10

    if char == '-':
        return 0

    raise ValueError()
