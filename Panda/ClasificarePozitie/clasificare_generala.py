#momentan da true falls ca am doar un mod de a defini pozitia

def test_pozitie_format(pozitie):
    # pozitie type string 
    # ex: pozitia de start rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
    # unde R N B K Q P p q k b n r
    # maybe in viitor o sa am si alte tipuri de a defini o pozitie
    if '/' not in pozitie:
        return False
    
    con = 0
    for c in pozitie:
        if c == '/':
            con += 1
        elif c not in "rnbqkpRNBQKP12345678 w -": 
            return False
    if con != 7:
        return False
    
    return True


def clasificare_generala(pozitie):
    # pozitie type string 
    if not test_pozitie_format(pozitie):
        raise "Pozitie not well defined"

    

