lst_unique_games_revised = ["j1dkb5dw","a9tcp02g","szom2tog","rklpc7mk","1xb3os63",
                            "6x5nq6qd","fl7asfa0","7b44wxzu","7rzcutsf","9opx3qh7",
                            "vb3w3rmn","z2ncoii6","iinnkv77","n5crd00d","1hi3aveq"]
import pandas as pd

def get_games():
    input_path = "Datasets\\raw_dataset.csv"
    input_path = "C:\\Users\\serpe\\Desktop\\LICENTA\\Panda\\ClasificarePozitie\\Datasets\\raw_dataset.csv"
    data = pd.read_csv(input_path, low_memory=False)

    unique_games = data['game_id'].unique()
    unique_games = [g for g in unique_games if g not in lst_unique_games_revised]
    count = 0
    str = ""
    for g in unique_games:
        str += g + ": \n"
        game_data = data[data['game_id'] == g]
        for m in game_data['fen']:
            str +="" + m + ",," + g + '\n'
    
        count += 1
        if count > 4:
            break

    open("C:\\Users\\serpe\\Desktop\\LICENTA\\Panda\\ClasificarePozitie\\Datasets\\games.txt", "w").write(str)
    print(str)

get_games()