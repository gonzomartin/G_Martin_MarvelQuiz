from Components import vars

def total(value):

    if value <= 10:
        vars.character = vars.characters[0]


    if value <= 20 and value > 10:
        vars.character = vars.characters[1]


    if value <= 30 and value > 20:
        vars.character = vars.characters[2]


    if value <= 40 and value > 30:
        vars.character = vars.characters[3]


    if value <= 50 and value > 40:
        vars.character = vars.characters[4]

    
    if value > 60:
        vars.character = "imposible to say who it is"

    print("It's " + vars.character)