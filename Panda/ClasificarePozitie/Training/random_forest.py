import pickle
from sklearn.linear_model import LogisticRegression as logistic_regression
from sklearn.ensemble import RandomForestClassifier as random_forest_classifier
from sklearn.tree import DecisionTreeClassifier as decision_tree_classifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
#import fen_to_features
from fen_to_features import fen_to_features
from learning_curve import plot_learning_curve
def train_random_forest(data, output_path="C:\\Users\\serpe\\Desktop\\LICENTA\\Panda\\ClasificarePozitie\\Training\\Raports\\RF3"):
    #salveaza o parte din data 30% pentru test dupa training
    data_test = data.sample(frac=0.3, random_state=42)
    y_test_real = data_test['type'].values  # Salvează etichetele reale

    data_test = data_test.drop(columns=['type', "fen", "game_id"])
    data = data.drop(data_test.index)
    X = data.drop(columns=['type', "fen", "game_id"])
    y = data["type"]

    lst_accuracies = []
    lst_clfs = []
    lst_raports = []
    for i in range(5):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=i)

        param_grid = {
            'n_estimators': [100, 200],
            'max_depth': [None, 10, 20],
            'min_samples_split': [2, 5]
        }
        clf = random_forest_classifier(random_state=i)
        grid_search = GridSearchCV(clf, param_grid, cv=5)
        grid_search.fit(X_train, y_train)
        clf = grid_search.best_estimator_
        y_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        lst_accuracies.append(accuracy)
        lst_clfs.append(clf)

        raport_str = ""
        corect_guess = 0
        for idx, row in enumerate(data_test.values):
            pred = clf.predict([row])[0]
            if y_test_real[idx] == pred:
                corect_guess += 1
        raport_str += f"    Number of test positions: {len(data_test)}\n"
        raport_str += f"    Number of correct guesses: {corect_guess}\n"
        raport_str += f"    Accuracy: {corect_guess / len(data_test) * 100:.2f}%\n"
        raport_str += f"    Precision: {corect_guess / (corect_guess + (len(data_test) - corect_guess)) * 100:.2f}%\n"
        raport_str += f"    Opening predicted as endgame: " + str(((y_test == 'endgame') & (y_pred == 'opening')).sum())
        raport_str += f"\n    Endgame predicted as opening: " + str(((y_test == 'opening') & (y_pred == 'endgame')).sum())+"\n"
        raport_str += f"\n    Opening predicted as middlegame: " + str(((y_test == 'middlegame') & (y_pred == 'opening')).sum())
        raport_str += f"\n    Middlegame predicted as opening: " + str(((y_test == 'opening') & (y_pred == 'middlegame')).sum())
        raport_str += f"\n    Middlegame predicted as endgame: " + str(((y_test == 'endgame') & (y_pred == 'middlegame')).sum())
        raport_str += f"\n    Endgame predicted as middlegame: " + str(((y_test == 'middlegame') & (y_pred == 'endgame')).sum())
        lst_raports.append(raport_str)

    # Save best model and make a report in a .txt file
    best_accuracy_index = lst_accuracies.index(max(lst_accuracies))
    best_clf = lst_clfs[best_accuracy_index]
    with open(output_path + ".txt", "w") as f:
        f.write(str(best_clf))
        f.write("\nTraining")
        f.write("\n     Accuracy: " + str(max(lst_accuracies)))
        f.write("\n     Report:\n" + classification_report(y_test, y_pred))
        f.write("     Number of games: " + str(data['game_id'].nunique()))
        f.write("\n     Best parameters: " + str(grid_search.best_params_))
        f.write("\n     Opening predicted as endgame: " + str(((y_test == 'endgame') & (y_pred == 'opening')).sum()))
        f.write("\n     Endgame predicted as opening: " + str(((y_test == 'opening') & (y_pred == 'endgame')).sum())+"\n")
        f.write("\n     Opening predicted as middlegame: " + str(((y_test == 'middlegame') & (y_pred == 'opening')).sum()))
        f.write("\n     Middlegame predicted as opening: " + str(((y_test == 'opening') & (y_pred == 'middlegame')).sum()))
        f.write("\n     Middlegame predicted as endgame: " + str(((y_test == 'endgame') & (y_pred == 'middlegame')).sum()))
        f.write("\n     Endgame predicted as middlegame: " + str(((y_test == 'middlegame') & (y_pred == 'endgame')).sum()))
        f.write("\nTest")
        f.write("\n"+lst_raports[best_accuracy_index])

    p = output_path.split("\\")
    plot_learning_curve(f"{output_path}.png", best_clf, X_train, y_train, title=p[-1])
    with open("C:\\Users\\serpe\\Desktop\\LICENTA\\Panda\\ClasificarePozitie\\Training\\Models\\" + p[-1] + ".model", "wb") as f:
        pickle.dump(best_clf, f)
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

#data = make_dataset(input_oppenings, input_middlegame, input_endgame)
data = pd.read_csv("C:\\Users\\serpe\\Desktop\\LICENTA\\Panda\\ClasificarePozitie\\Datasets\\positions_fen_features.csv", low_memory=False)

print("Dataset created with sample:\n", data.sample(5))

clfs, accuracies = train_random_forest(data)
print("Accuracies:", accuracies)
print("Best accuracy:", max(accuracies))