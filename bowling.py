def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):  # amíg a game lista tart

        if game[i] == '/':      # ha a listaelem '/', akkor a result = 10 - last értéke
            result += 10 - get_value(game[i-1])  
 
        else:
            result += get_value(game[i])       #  ha a listaelem egyéb, akkor a result értéke a get_value visszatérési értéke
        
        
        if frame < 10  and get_value(game[i]) == 10:    # ha nem az utolsó frame-nél járunk  és a get_value visszatérési értéke 10
            if game[i] == '/':                          # és ha a lista elem '/'
                result += get_value(game[i+1])          # akkor a result egyenlő a get_value visszatérési értékével a következő listaelemnél
            elif game[i] == 'X' or 'x':                 # vagy ha a listaelem  'X' vagy 'x' 
                result += get_value(game[i+1])          # akkor a result egyenlő a get_value visszatérési értékével a következő listaelemnél
                if game[i+2] == '/':                    # ha a game lista következő utáni eleme '/'
                    result += 10 - get_value(game[i+1]) # akkor a result értéke 10 mínusz get_value visszatérési értéke a következő listaelemnél
                else:                                   # egyéb esetben
                    result += get_value(game[i+2])      # a result értéke a get_value visszatérési értéke a következő utáni listaelemnél
        
        if not in_first_half:                           # ha nem az első próbálkozás
            frame += 1                                  # akkor ugorjunk a következő frame-re
        if in_first_half:                               # ha az első gurításnál tartunk
            in_first_half = False                       # akkor jöjjön a következő gurítás
        else:                                           # ha a második gurításnál tartunk, akkor...
            in_first_half = True                        # állítsuk vissza az elsőre
        
        if is_x(game, i):            # ha a listaelem 'X' vagy 'x', akkor... 
            in_first_half = True                        # ... állítsuk a következő elsőgurítás következik...
            frame += 1                                  # ... a  következő frame-ben
    
    # The game score is the total of all frame scores.
    return result

def is_x(game, i):
    return game[i] == 'X' or game[i] == 'x'

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
