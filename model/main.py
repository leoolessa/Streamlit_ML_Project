import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


def create_model(data):
    X = data.drop(['diagnosis'], axis=1)
    y = data['diagnosis']
    
    #scale the data
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
        
    #split the data
    X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.30, random_state=42)
        
    #train the model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    #test the model
    y_pred = model.predict(X_test)
    print('Accuracy of the model: ', accuracy_score(y_test, y_pred))
    print('Classification report: \n', classification_report(y_test,y_pred))
    
    return model, scaler



    
    
    
def main():
    data = pd.read_csv('data/data.csv')
    model, scaler = create_model(data)    

  




if __name__ == '__main__':
    main()