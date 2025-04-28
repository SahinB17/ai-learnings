import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import sklearn.metrics as sm

data=pd.read_csv("./data/Salary.csv")
#plt.scatter(data.Years,data.Salary,color ="red",marker="+")
plt.xlabel('Experience in years')
plt.ylabel('Salary')

x_train,x_test,y_train,y_test = train_test_split(data.Years,data.Salary,test_size=0.2,random_state=42)

#plt.scatter(x_train,y_train,color="blue",label='Training data')
#lt.scatter(x_test,y_test,color="red",label="Test data")
#plt.legend()


reg=linear_model.LinearRegression()
reg.fit(x_train.values.reshape(-1,1),y_train.values)

prediction=reg.predict(x_test.values.reshape(-1,1))
plt.plot(x_test,prediction,label="Linear Regression",color='b')
plt.scatter(x_test.values.reshape(-1,1),y_test.values,label="Actual Test Data",color="g")
plt.legend()


#print(reg.coef_,reg.intercept_)

print(f"score :{reg.score(x_test.values.reshape(-1,1),y_test.values)}")
mse = sm.mean_squared_error(y_test,prediction)
print(f"MSE :{mse}")
plt.show()
#reg=linear_model.LinearRegression()
#reg.fit(data[['Years']],data.Salary)

#plt.plot(data.Years,reg.predict(data[['Years']]))
#plt.show()
