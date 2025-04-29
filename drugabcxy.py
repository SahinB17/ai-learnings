import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.model_selection import train_test_split


data=pd.read_csv('./data/drug200.csv')

label=LabelEncoder()
data['Sex']=label.fit_transform(data['Sex'])
data['BP']=label.fit_transform(data['BP'])
data['Cholesterol']=label.fit_transform(data['Cholesterol'])
data['Drug']=label.fit_transform(data['Drug'])

#print(data.head())

x=data.drop(columns='Drug')
y=data.Drug

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,
                                           random_state=42)
best_model =None
best_score=0
d=[1,3,5,None]
best_depth=0

for i in d:
    model =DecisionTreeClassifier(criterion='entropy',max_depth=i)
    model.fit(xtrain,ytrain)
    train_acc=model.score(xtrain,ytrain)
    test_acc=model.score(xtest,ytest)
    print(f"Train score for depth {i}={train_acc}")
    print(f"Test acc for depth {i}={test_acc}")
    if test_acc>best_score:
        best_score=test_acc
        best_model=model
        best_depth=i

print(f"Best depth={best_depth}")
plt.figure(figsize=(12,8))
plot_tree(best_model,feature_names=x.columns,
    class_names=['DrugA','DrugB','DrugC','DrugX','DrugY'],filled=True,rounded=True)

plt.show()

y_pred=best_model.predict(xtest)
print(classification_report(ytest,y_pred))
print(confusion_matrix(ytest,y_pred))



sample = [[45, 1, 2, 0, 32.5]]
pred_enc = best_model.predict(sample)[0]
pred_label = label.inverse_transform([pred_enc])[0]
print(f"\nSample: {sample}")
print(f"Encoded prediction: {pred_enc}")
print(f"Predicted drug: {pred_label}")
