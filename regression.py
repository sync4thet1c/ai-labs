#Import libraries
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression



#Read the Dataset 
dataset = pd.read_csv('Weather0.csv')
#dataset = pd.read_xlsx('WeatherM.xlsx')# if you have Exel file 

#print(dataset.describe())
X=["Year"]
y=["MeanTemp"]

# our data points on a 2-D graph 
dataset.plot(x='Year', y='MeanTemp', style='o')  
plt.title('Year vs Mean Temperature')  
plt.xlabel('Year')  
plt.ylabel('Mean Temperature')  
plt.show()

#Here we use 90% from our data set to train our model 
X_train, X_test, y_train, y_test = train_test_split( dataset[X].values , dataset[y].values, test_size=0.9, random_state=0)

#to train our algorithm. For that, we need to import LinearRegression class,
regressor = LinearRegression()
regressor.fit(X_train,y_train)

y_pred = regressor.predict(X_test)
#Checking our predicted data vs real data
df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
print (df.head(10))
#Ploting predicted data vs real data
df1 = df.head(10)
df1.plot(kind='bar',figsize=(12,8))
plt.grid(which='major', linestyle='-', linewidth='0.8', color='red')
plt.grid(which='minor', linestyle=':', linewidth='0.8', color='blue')
plt.show()

#For retrieving the slope:
print ("the slope")
print(regressor.coef_)


#ploting our test data
plt.scatter(X_test, y_test,  color='gray')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.show()

#adding a specific year to predict weather by user
print ("Input the year you want to predict weather in it : ")
inp_ur_dataf=list()
inp_ur_dataf.append(int(input()))
print(regressor.predict([inp_ur_dataf]),"\n")
