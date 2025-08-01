import pandas as pd

def describe_raw_dataset(nume):
    """
    Describe the columns of a DataFrame.
    """
    input_path = "Datasets\\raw_dataset.csv"
    data = pd.read_csv(input_path,low_memory=False)
    str_raport = ''

    str_col = ''
    for col in data.columns:
        str_col += col + ': ' + '\n'    
        str_col += '  -' + 'Type: ' + str(data[col].dtype) + '\n'
        str_col += '  -' + 'Unique values: ' + str(data[col].nunique()) + '\n'
        str_col += '  -' + 'Missing values: ' + str(data[col].isnull().sum()) + '\n'
        if data[col].dtype == 'float64' or data[col].dtype == 'int64':
            str_col += '  -' + 'Mean: ' + str(data[col].mean()) + '\n'
        elif data[col].dtype == 'object':
            str_col += '  -' + 'Mean: ' + ' Notapplicable' + '\n'


    str_game = ''
    for col in data.groupby('game_id').size().index:
        pass
    #numarul de jocuri unice
    nr_unique_games = data['game_id'].nunique()
    #media mutarilor pentru fiecare joc
    
    termination_of_games = str(data['termination'].unique().tolist())

    nr_moves_median = data.groupby('game_id').size().median().astype(int).astype(str)
    min_nr_moves = data.groupby('game_id').size().min().astype(int).astype(str)
    max_nr_moves = data.groupby('game_id').size().max().astype(int).astype(str)

    str_raport = 'About columns: \n'

    str_raport += str_col + '\n\n'

    str_raport += 'Number of games: ' + str(nr_unique_games) + '\n'
    str_raport += 'Median number of moves for each game: ' + nr_moves_median + '\n'
    str_raport += 'Min number of moves for a game: ' + min_nr_moves + '\n'
    str_raport += 'Max number of moves for a game: ' + max_nr_moves + '\n\n'

    str_raport += 'Termination of games: ' + termination_of_games + '\n'


    print(str_raport)
    with open('Datasets\\Raports\\' + nume + '.txt', 'w') as f:
        f.write(str_raport)

def describe_oppenings(nume):
    """
    Describe the columns of a DataFrame.
    """

    input_path = "C:\\Users\\serpe\\Desktop\\LICENTA\\Panda\\ClasificarePozitie\\Datasets\\"+nume+".csv"
    data = pd.read_csv(input_path,low_memory=False)
    str_raport = ''

    str_col = ''
    for col in data.columns:
        str_col += col + ': ' + '\n'    
        str_col += '  -' + 'Type: ' + str(data[col].dtype) + '\n'
        str_col += '  -' + 'Unique values: ' + str(data[col].nunique()) + '\n'
        str_col += '  -' + 'Missing values: ' + str(data[col].isnull().sum()) + '\n'
        if data[col].dtype == 'float64' or data[col].dtype == 'int64':
            str_col += '  -' + 'Mean: ' + str(data[col].mean()) + '\n'
        elif data[col].dtype == 'object':
            str_col += '  -' + 'Mean: ' + ' Notapplicable' + '\n'


    str_game = ''
    for col in data.groupby('game_id').size().index:
        pass
    #numarul de jocuri unice
    nr_unique_games = data['game_id'].nunique()
    #media mutarilor pentru fiecare joc
    

    nr_moves_median = data.groupby('game_id').size().median().astype(int).astype(str)
    min = data.groupby('game_id').size().min().astype(float)/2
    min_nr_moves = min.astype(str)
    max = data.groupby('game_id').size().max().astype(float)/2
    max_nr_moves = max.astype(str)

    str_raport = 'About columns: \n'

    str_raport += str_col + '\n\n'

    str_raport += 'Number of games: ' + str(nr_unique_games) + '\n'
    str_raport += 'Median number of moves for each game: ' + nr_moves_median + '\n'
    str_raport += 'Min number of moves for a game: ' + min_nr_moves + '\n'
    str_raport += 'Max number of moves for a game: ' + max_nr_moves + '\n\n'
    #make media materialului pentru fiecare culoare, calculeazo din fen
    piece_dict = {
        'P': 1, 'N': 2, 'B': 3, 'R': 4, 'Q': 5, 'K': 6,
        'p': 7, 'n': 8, 'b': 9, 'r': 10, 'q': 11, 'k': 12
    }
    lst_material_alb = []
    lst_material_negru = []
    lst_nr_pioni_alb = []
    lst_nr_pioni_negru = []
    lst_pioni_la_loc_alb = []
    lst_pioni_la_loc_negru = []
    for index, row in data.iterrows():
        ma = 0
        mn = 0
        nrpa = 0
        nrpn = 0
        pla = 0 # pioni la loc alb
        pln = 0 # pioni la loc negru
        fen = row['fen']
        parts = fen.split(' ')
    
        # Convertim tabla de șah într-o matrice 8x8
        rows = parts[0].split('/')
        for i in range(8):
            row = rows[i]
            if i == 1 or i == 6:
                for c in row:
                    if c == 'p':
                        pln += 1
                    if c == 'P':
                        pla += 1
            for char in row:
                if char.isupper():
                    if char == 'P':
                        nrpa += 1
                        ma += 1
                    elif char == 'N':
                        ma += 3
                    elif char == 'B':
                        ma += 3
                    elif char == 'R':
                        ma += 5
                    elif char == 'Q':
                        ma += 9
                elif char.islower():
                    if char == 'p':
                        nrpn += 1
                        mn += 1
                    elif char == 'n':
                        mn += 3
                    elif char == 'b':
                        mn += 3
                    elif char == 'r':
                        mn += 5
                    elif char == 'q':
                        mn += 9

        lst_material_alb.append(ma)
        lst_material_negru.append(mn)
        lst_nr_pioni_alb.append(nrpa)
        lst_nr_pioni_negru.append(nrpn)
        lst_pioni_la_loc_alb.append(pla)
        lst_pioni_la_loc_negru.append(pln)
    mma = sum(lst_material_alb) / len(lst_material_alb)
    mmn = sum(lst_material_negru) / len(lst_material_negru)
    mnrpa = sum(lst_nr_pioni_alb) / len(lst_nr_pioni_alb)
    mnrpn = sum(lst_nr_pioni_negru) / len(lst_nr_pioni_negru)
    str_raport += "Material mediu Alb: " + str(mma) + '\n'
    str_raport += "Material mediu Negru: " + str(mmn) + '\n'
    str_raport += "Material mediu: " + str((mma + mmn) / 2) + '\n'
    str_raport += "Numar mediu de pioni Alb: " + str(mnrpa) + '\n'
    str_raport += "Numar mediu de pioni Negru: " + str(mnrpn) + '\n'
    str_raport += "Numar mediu de pioni: " + str((mnrpa + mnrpn) / 2) + '\n'
    str_raport += "Pioni la loc mediu Alb: " + str(sum(lst_pioni_la_loc_alb) / len(lst_pioni_la_loc_alb)) + '\n'
    str_raport += "Pioni la loc mediu Negru: " + str(sum(lst_pioni_la_loc_negru) / len(lst_pioni_la_loc_negru)) + '\n'
    str_raport += "Pioni la loc mediu: " + str((sum(lst_pioni_la_loc_alb) + sum(lst_pioni_la_loc_negru)) / (len(lst_pioni_la_loc_alb) + len(lst_pioni_la_loc_negru))) + '\n'

    print(str_raport)
    with open('C:\\Users\\serpe\\Desktop\\LICENTA\\Panda\\ClasificarePozitie\\Datasets\\Raports\\' + nume + '.txt', 'w') as f:
        f.write(str_raport)


def  describe_fen_features(nume):
    """
    Describe the columns of a DataFrame.
    """

    input_path = "C:\\Users\\serpe\\Desktop\\LICENTA\\Panda\\ClasificarePozitie\\Datasets\\"+nume+".csv"
    data = pd.read_csv(input_path,low_memory=False)
    str_raport = ''

    str_col = ''

    str_game = ''
    for col in data.groupby('game_id').size().index:
        pass
    #numarul de jocuri unice
    nr_unique_games = data['game_id'].nunique()
    #media mutarilor pentru fiecare joc
    

    nr_moves_median = data.groupby('game_id').size().median().astype(int).astype(str)
    min = data.groupby('game_id').size().min().astype(float)/2
    min_nr_moves = min.astype(str)
    max = data.groupby('game_id').size().max().astype(float)/2
    max_nr_moves = max.astype(str)

    str_raport = 'About columns: \n'

    str_raport += str_col + '\n\n'

    str_raport += 'Number of games: ' + str(nr_unique_games) + '\n'
    str_raport += 'Median number of moves for each game: ' + nr_moves_median + '\n'
    str_raport += 'Min number of moves for a game: ' + min_nr_moves + '\n'
    str_raport += 'Max number of moves for a game: ' + max_nr_moves + '\n\n'

    piece_dict = {
        'P': 1, 'N': 2, 'B': 3, 'R': 4, 'Q': 5, 'K': 6,
        'p': 7, 'n': 8, 'b': 9, 'r': 10, 'q': 11, 'k': 12
    }
    lst_material_alb = []
    lst_material_negru = []
    lst_nr_pioni_alb = []
    lst_nr_pioni_negru = []
    for index, row in data.iterrows():
        ma = 0
        mn = 0
        nrpa = 0
        nrpn = 0
        for i in range(1,16):
            if row[f"P{i}"] != 0:
                if row[f"P{i}"] == 1:
                    nrpa += 1
                    ma += 1
                elif row[f"P{i}"] == 2:
                    ma += 3
                elif row[f"P{i}"] == 3:
                    ma += 3
                elif row[f"P{i}"] == 4:
                    ma += 5
                elif row[f"P{i}"] == 5:
                    ma += 9
            if row[f"p{i}"] != 0:
                if row[f"p{i}"] == 7:
                    nrpn += 1
                    mn += 1
                elif row[f"p{i}"] == 8:
                    mn += 3
                elif row[f"p{i}"] == 9:
                    mn += 3
                elif row[f"p{i}"] == 10:
                    mn += 5
                elif row[f"p{i}"] == 11:
                    mn += 9
            lst_material_alb.append(ma)
            lst_material_negru.append(mn)
            lst_nr_pioni_alb.append(nrpa)
            lst_nr_pioni_negru.append(nrpn)
    #make media materialului pentru fiecare culoare
    mma = sum(lst_material_alb) / len(lst_material_alb)
    mmn = sum(lst_material_negru) / len(lst_material_negru)
    mnrpa = sum(lst_nr_pioni_alb) / len(lst_nr_pioni_alb)
    mnrpn = sum(lst_nr_pioni_negru) / len(lst_nr_pioni_negru)
    str_raport += "Openings: " + str(len(data[data['type'].isin(['oppening'])])) + '\n'
    str_raport += "Middlegames: " + str(len(data[data['type'].isin(['middlegame'])])) + '\n'
    str_raport += "Endgames: " + str(len(data[data['type'].isin(['endgame'])])) + '\n'
    str_raport += "Material mediu: " + str((mma + mmn) / 2) + '\n'
    str_raport += "Material mediu Alb: " + str(mma) + '\n'
    str_raport += "Material mediu Negru: " + str(mmn) + '\n'
    str_raport += "Numar mediu de pioni Alb: " + str(mnrpa) + '\n'
    str_raport += "Numar mediu de pioni Negru: " + str(mnrpn) + '\n'
    str_raport += "Numar mediu de pioni: " + str((mnrpa + mnrpn) / 2) + '\n'
    str
    print(str_raport)
    with open('C:\\Users\\serpe\\Desktop\\LICENTA\\Panda\\ClasificarePozitie\\Datasets\\Raports\\' + nume + '.txt', 'w') as f:
        f.write(str_raport)


#describe_raw_dataset("raw_dataset")
#describe_oppenings("oppenings")
#describe_oppenings("middlegames")
#describe_oppenings("endgames")
describe_fen_features("positions_fen_features")