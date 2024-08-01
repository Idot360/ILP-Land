

def train(file, features):
    import pandas as pd
    from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
    from sklearn import ensemble

    training_data = pd.read_csv(file, index_col='ID')
    training_data = training_data.dropna(axis=0)

    X = training_data[features].to_numpy()
    y = training_data.Happiness.to_numpy()

    #clf = QuadraticDiscriminantAnalysis()
    #clf.fit(X, y)

    model = ensemble.RandomForestRegressor(random_state=2024, n_estimators=200)
    model.fit(X, y)

    return model
    


def main():
    
    file = 'processed_data.csv'
    features = ["Population","Land size","Working hours","Environment","Income","Cost of living","N recreational buildings","N office buildings","N essential buildings","N residential buildings"]

    model = train(file, features)

    return model



if __name__ == "__main__":
    main()



