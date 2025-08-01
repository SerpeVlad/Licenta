#random forest classifier for training a model to classify chess positions into opening, middlegame, and endgame categories
from sklearn.linear_model import LogisticRegression as logistic_regression
from sklearn.ensemble import RandomForestClassifier as random_forest_classifier
from sklearn.tree import DecisionTreeClassifier as decision_tree_classifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
#import fen_to_features
from fen_to_features import fen_to_features

def train_logistic_regression(data,output_path="C:\\Users\\serpe\\Desktop\\LICENTA\\Panda\\ClasificarePozitie\\Training\\Raports\\LR2.txt"):
    #X = data.drop(columns=['type', "fen", "how_moves", "game_id"]) # 10 games 0.74; 11 games 0.76
    X = data.drop(columns=['type', "fen", "game_id"]) # 10 games0.74; 11 games 0.76

    y = data["type"]
    

    lst_accuracies = []
    lst_clfs = []
    for i in range(5):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=i)

        clf = random_forest_classifier(random_state=i)

        clf.fit(X_train, y_train)

        y_pred = clf.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)
        lst_accuracies.append(accuracy)
        lst_clfs.append(clf)
    #save best model and make an raport in a .txt file
    best_accuracy_index = lst_accuracies.index(max(lst_accuracies))
    best_clf = lst_clfs[best_accuracy_index]
    with open(output_path, "w") as f:
        f.write(str(best_clf))
        f.write("\nAccuracy: " + str(max(lst_accuracies)))
        f.write("\nReport:\n" + classification_report(y_test, y_pred))
        f.write("Number of games: " + str(data['game_id'].nunique()))
    return lst_clfs, lst_accuracies

def train_random_forest(data, output_path="C:\\Users\\serpe\\Desktop\\LICENTA\\Panda\\ClasificarePozitie\\Training\\Raports\\RF2.txt"):
    X = data.drop(columns=['type', "fen", "game_id"])
    y = data["type"]

    lst_accuracies = []
    lst_clfs = []
    for i in range(5):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=i)
        #X = data.drop(columns=['type', "fen", "how_moves", "game_id"]) # 10 games 0.74; 11 games 0.76

        clf = random_forest_classifier(random_state=i)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        lst_accuracies.append(accuracy)
        lst_clfs.append(clf)
    # Save best model and make a report in a .txt file
    best_accuracy_index = lst_accuracies.index(max(lst_accuracies))
    best_clf = lst_clfs[best_accuracy_index]
    with open(output_path, "w") as f:
        f.write(str(best_clf))
        f.write("\nAccuracy: " + str(max(lst_accuracies)))
        f.write("\nReport:\n" + classification_report(y_test, y_pred))
        f.write("Number of games: " + str(data['game_id'].nunique()))
    return lst_clfs, lst_accuracies

def train_decision_tree(data, output_path="C:\\Users\\serpe\\Desktop\\LICENTA\\Panda\\ClasificarePozitie\\Training\\Raports\\DT.txt"):
    X = data.drop(columns=['type', "fen", "game_id"])
    y = data["type"]

    lst_accuracies = []
    lst_clfs = []
    for i in range(5):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=i)
        #X = data.drop(columns=['type', "fen", "how_moves", "game_id"]) # 10 games 0.74; 11 games 0.76

        clf = decision_tree_classifier(random_state=i)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        lst_accuracies.append(accuracy)
        lst_clfs.append(clf)
    # Save best model and make a report in a .txt file
    best_accuracy_index = lst_accuracies.index(max(lst_accuracies))
    best_clf = lst_clfs[best_accuracy_index]
    with open(output_path, "w") as f:
        f.write(str(best_clf))
        f.write("\nAccuracy: " + str(max(lst_accuracies)))
        f.write("\nReport:\n" + classification_report(y_test, y_pred))
        f.write("Number of games: " + str(data['game_id'].nunique()))
    return lst_clfs, lst_accuracies


def make_dataset(input_oppening,input_middlegame, input_endgame):
    df_oppening = pd.read_csv(input_oppening, low_memory=False)
    df_middlegame = pd.read_csv(input_middlegame, low_memory=False)
    df_endgame = pd.read_csv(input_endgame, low_memory=False)

    df_oppening['type'] = 'oppening'
    df_middlegame['type'] = 'middlegame'
    df_endgame['type'] = 'endgame'

    df_combined = pd.concat([df_oppening, df_middlegame, df_endgame], ignore_index=True)
    #suffle the dataset
    df_combined = df_combined.sample(frac=1, random_state=42).reset_index(drop=True)
    df_combined = fen_to_features(df_combined)
    return df_combined

input_oppenings = "C:\\Users\\serpe\\Desktop\\LICENTA\\Panda\\ClasificarePozitie\\Datasets\\oppenings.csv"
input_middlegame = "C:\\Users\\serpe\\Desktop\\LICENTA\\Panda\\ClasificarePozitie\\Datasets\\middlegames.csv"
input_endgame = "C:\\Users\\serpe\\Desktop\\LICENTA\\Panda\\ClasificarePozitie\\Datasets\\endgames.csv"

data = make_dataset(input_oppenings, input_middlegame, input_endgame)
print("Dataset created with sample:\n", data.sample(5))

#clfs, accuracies = train_logistic_regression(data)
#clfs, accuracies = train_random_forest(data)
clfs, accuracies = train_decision_tree(data)
print("Accuracies:", accuracies)
print("Best accuracy:", max(accuracies))