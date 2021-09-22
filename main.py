import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from program import predictPrice

# reading the data
df = pd.read_csv("CAR DETAILS FROM CAR DEKHO.csv")

# spliting the input factors and the output into separate variables
X = df[["wheelbase", "carlength", "carwidth", "carheight",
        "curbweight", "enginesize", "stroke", "horsepower", "peakrpm"]]

Y = df["price"]

# splitting the data into train and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

# scaling the input factors(X)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

# inintializing the classifier
# we are using LinearRegression Because:-
# Linear regression analysis is used to predict the value of a variable based on the value of another variable.
# Logistic Regression is used to predict the values which is based on Yes or no / 1 or 0 (Classification based problems)

classifier = LinearRegression()
classifier.fit(X_train, Y_train)

# testing my model using X_test
prediction = classifier.predict(X_test)

# This will print a list of predictions
print(f"Predictions :- {prediction}")

# to calculate the accuracy of the regression problems we have to use r2_score(Linear Regression) and to calculate the accuracy of the classification based (Logistic Regression) problem we have to use accuracy_score()
Accuracy = r2_score(Y_test, prediction)
print(f"Accuracy :- {str(Accuracy)[2:4]}%")


# !Now we will give inputs and our model should predict the price of the car accordingly
Prediction = classifier.predict([predictPrice()])
print(f"{int(prediction[0])}$")  # Price is in dollars($)
