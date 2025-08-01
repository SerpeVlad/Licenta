import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve

def plot_learning_curve(save_path,estimator, X, y, title="Learning Curve", cv=5, scoring="accuracy", train_sizes=np.linspace(0.1, 1.0, 5)):
    """
    Plots a learning curve for a given estimator and dataset.
    """
    plt.figure(figsize=(8, 6))
    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=cv, scoring=scoring, train_sizes=train_sizes, n_jobs=-1, shuffle=True, random_state=42
    )
    train_scores_mean = np.mean(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)

    plt.plot(train_sizes, train_scores_mean, 'o-', color="r", label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g", label="Cross-validation score")
    plt.title(title)
    plt.xlabel("Training examples")
    plt.ylabel(scoring.capitalize())
    plt.legend(loc="best")
    plt.grid()
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()
