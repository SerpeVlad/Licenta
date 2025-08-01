import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def fen_to_features(data):
    """
    Convertește un string FEN într-un set de caracteristici numerice.
    """
    # Valoarea materială pentru fiecare tip de piesă
    piece_values = {'p': 1, 'n': 3, 'b': 3, 'r': 5, 'q': 9, 'k': 0}
    
    data['how_moves'] = 0  # 1 alb, 0 negru
    data["Q"] = 0  # White Castling Rights Queen Side
    data["q"] = 0  # Black Castling Rights Queen Side
    data["K"] = 0  # White Castling Rights King Side
    data["k"] = 0  # Black Castling Rights King Side
    for i in range(16):
        data[f"P{i+1}"] = 0  # Piesa1 Alb
        data[f"P{i+1}x"] = 0  # Piesa1 Alb X
        data[f"P{i+1}y"] = 0  # Piesa1 Alb Y

        data[f"p{i+1}"] = 0  # Piesa1 Negru
        data[f"p{i+1}x"] = 0  # Piesa1 Negru X
        data[f"p{i+1}y"] = 0  # Piesa1 Negru Y

    piece_dict = {
        'P': 1, 'N': 2, 'B': 3, 'R': 4, 'Q': 5, 'K': 6,
        'p': 7, 'n': 8, 'b': 9, 'r': 10, 'q': 11, 'k': 12
    }


    for index, row in data.iterrows():
        piece_count_white = 0
        piece_count_black = 0
        fen = row['fen']
        parts = fen.split(' ')
        if parts[1] == 'w':
            data.at[index, 'how_moves'] = 1
        else:   
            data.at[index, 'how_moves'] = 0
        if "K" in parts[2]:
            data.at[index, 'K'] = 1
        if "k" in parts[2]:
            data.at[index, 'k'] = 1
        if "Q" in parts[2]:
            data.at[index, 'Q'] = 1     
        if "q" in parts[2]:
            data.at[index, 'q'] = 1
        # Convertim tabla de șah într-o matrice 8x8
        rows = parts[0].split('/')
        for i in range(8):
            row = rows[i]
            for char in row:
                column_count = 0
                if char.isdigit() == True:
                    column_count += int(char)
                elif char.isupper():
                    piece_count_white += 1
                    data[f"P{piece_count_white}"] = piece_dict[char]
                    data[f"P{piece_count_white}x"] = column_count
                    data[f"P{piece_count_white}y"] = 8 - i
                elif char.islower():
                    piece_count_black += 1
                    data[f"p{piece_count_black}"] = piece_dict[char]
                    data[f"p{piece_count_black}x"] = column_count
                    data[f"p{piece_count_black}y"] = 8 - i
                


    data.to_csv("C:\\Users\\serpe\\Desktop\\LICENTA\\Panda\\ClasificarePozitie\\Datasets\\positions_fen_features.csv", index=False)
    return data
