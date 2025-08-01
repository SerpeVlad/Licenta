import pandas as pd

def add_position_type(csv_path, position_type):    
    try:
        data = pd.read_csv(csv_path, low_memory=False)
        data['type'] = position_type
        data.to_csv(csv_path, index=False)

        print(f"Procesat cu succes: '{csv_path}'. Adăugat tipul: '{position_type}'")

    except FileNotFoundError:
        print(f"EROARE: Fișierul nu a fost găsit la calea: {csv_path}")
    except Exception as e:
        print(f"EROARE la procesarea fișierului {csv_path}: {e}")


path_middlegame = "C:\\Users\\serpe\\Desktop\\LICENTA\\Panda\\ClasificarePozitie\\Datasets\\middlegames.csv"
path_endgame = "C:\\Users\\serpe\\Desktop\\LICENTA\\Panda\\ClasificarePozitie\\Datasets\\endgames.csv"
path_opening = "C:\\Users\\serpe\\Desktop\\LICENTA\\Panda\\ClasificarePozitie\\Datasets\\oppenings.csv" # Atenție, posibil typo: "opening"

add_position_type(path_middlegame, "middlegame")
add_position_type(path_endgame, "endgame")
add_position_type(path_opening, "opening")