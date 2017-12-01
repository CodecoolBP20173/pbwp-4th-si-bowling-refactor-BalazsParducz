def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        
        if game[i] == '/':
            result += 10 - last
        # If in two tries, he fails to knock them all down,
        # his score for that frame is the total number of pins knocked down in his two tries.
        else:
            result += get_value(game[i])
        
        
        if frame < 10  and get_value(game[i]) == 10:
            # If in two tries he knocks them all down,
            # this is called a “spare” and his score for the frame is ten
            # plus the number of pins knocked down on his next throw (in his next turn).
            
            if game[i] == '/':
                result += get_value(game[i+1])
            # If on his first try in the frame he knocks down all the pins,
            # this is called a “strike”. 
            # His turn is over, and his score for the frame is ten
            # plus the simple total of the pins knocked down in his next two rolls.
            elif game[i] == 'X' or 'x':
                result += get_value(game[i+1])
                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
        last = get_value(game[i])
        if not in_first_half:
            frame += 1
        if in_first_half == True:
            in_first_half = False
        else:
            in_first_half = True
        
        if game[i] == 'X' or game[i] == 'x':
            in_first_half = True
            frame += 1
    
    # The game score is the total of all frame scores.
    return result

def get_value(char):
    open_points = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    bonus = ['X', 'x', '/']
    for point in open_points:
        if char == point:            
            return int(point)
        
    for bs in bonus:    
        if char == bs:
            return 10
        
    if char == '-':
        return 0

    raise ValueError()
