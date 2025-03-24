import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def train_model(data):
    X = data.drop('voter_turnout', axis=1)
    y = data['voter_turnout']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return model, accuracy

if __name__ == "__main__":
    data_file = "path/to/voting_data.csv"
    data = load_data(data_file)
    model, accuracy = train_model(data)
    print("Model Accuracy:", accuracy)