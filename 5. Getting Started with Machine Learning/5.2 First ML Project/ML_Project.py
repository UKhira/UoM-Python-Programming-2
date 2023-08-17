# Importing Libraries
import numpy as np          
import pandas as pd                      # data handling
import seaborn as sns                    # visualization
sns.set_palette('husl')
import matplotlib.pyplot as plt          # visualization
# % matplotlib inline

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
col_name = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names = col_name)

print(dataset.shape)
# will display (150,5) if data successfully loaded

print(dataset.head())
# will display data as a table

print(dataset.describe())
# will give count, min, max,... in each column

print(dataset.info())
# will provide information of dataset (variable type, memory usage,...)

print(dataset['class'].value_counts())
# will display each value counts in "class" field according to ("setosa","versicolor","virginica") seperation


# Extracting data in plot (violin-plot)
print("\n"*4)

sns.violinplot(y = 'class', x = 'sepal-length', data = dataset, inner = 'quartile')
plt.show()
sns.violinplot(y = 'class', x = 'sepal-width', data = dataset, inner = 'quartile')
plt.show()
sns.violinplot(y = 'class', x = 'petal-length', data = dataset, inner = 'quartile')
plt.show()
sns.violinplot(y = 'class', x = 'petal-width', data = dataset, inner = 'quartile')
plt.show()

# Pair Plot
sns.pairplot(dataset, hue='class', markers='+')
plt.show()

# Correlation heat map
# plt.figure(figsize = (7,5))
# sns.heatmap(dataset.corr(), annot = True, cmap = 'cubehelix_r')
# plt.show()


# Correlation Heatmap
# plt.figure(figsize=(7,5))
# sns.heatmap(dataset.corr(), annot=True, cmap='jet')
# plt.show()


# Drop the column that contain 'class' label
X = dataset.drop(['class'], axis = 1)
Y = dataset['class']
print(f'X shape: {X.shape} | Y shape: {Y.shape} ')

# Split: 80% for training, 20% for testing
from sklearn.model_selection import train_test_split 
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.20, random_state = 1)


# Support vector machine algorithm
from sklearn.svm import SVC
svn = SVC()
svn.fit(X_train, Y_train)


# Model evaluation
# Predict from the test dataset
predictions = svn.predict(X_test)

# Calculate the accuracy
from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test, predictions))

# A detailed clarification report
from sklearn.metrics import classification_report
print(classification_report(Y_test, predictions))

# Confusion matrix
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
ConfusionMatrixDisplay.from_predictions(
    Y_test, predictions
)
plt.show()

# Save the model
import pickle
with open('SVM.pickle','wb') as f:
    pickle.dump(svn, f)
    
    
# Load the model
with open('SVM.pickle', 'rb') as f:
    model = pickle.load(f)
print(model.predict(X_test))