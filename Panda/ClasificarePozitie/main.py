import json
import clasificare_generala
from ClasificareEndGame import clasificare_end_game
from ClasificareMiddleGame import clasificare_middle_game
from ClasificareOppening import clasificare_oppening

def __main__(input):
    try: 
       data = json.loads(input)

       pozitie = data.get("pozitie") # first except

       time_of_the_game = clasificare_generala(pozitie) # secound except
       type_of_pozitie = 'unclasified'
       if time_of_the_game == "oppening":
          type_of_pozitie = clasificare_oppening(pozitie)
       elif time_of_the_game == "midlegame":
          type_of_pozitie = clasificare_middle_game(pozitie)
       elif time_of_the_game == "endgame":
          type_of_pozitie = clasificare_end_game(pozitie)

        return type_of_pozitie
    except json.JSONDecoderError:
       return "Error: Inputul nu este un JSON valid."
    except Exception as e: 
       return e 
    

# o sa primeasca o pozitie si o sa trimita mai departe tipul pozitiei
if __name__ == "__main__":
    # primeste pozitia
    input_json = '{"pozitie": "RNBKQBNR/PPPPPPPP/////pppppppp/rnbkqbnr"}'
    pozition_type = __main__(input_json)
    
    
    