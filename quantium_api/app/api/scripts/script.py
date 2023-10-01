from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from qiskit.utils import algorithm_globals
from sklearn.svm import SVC

iris_data = load_iris()
    #print(iris_data.DESCR)


features = iris_data.data
labels = iris_data.target

df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
df["class"] = pd.Series(iris_data.target)


hackaton_palete=sns.color_palette("rocket", 3)
sns.pairplot(df, hue="class", palette=hackaton_palete)
SeabornCharts=plt
plt.savefig('./public/images/test/foo.png')
# plt.savefig('./public/images/test/foo.pdf')

# SeabornCharts.show()
SeabornCharts.savefig("test", dpi='figure', format=None)


algorithm_globals.random_seed = 123
train_features, test_features, train_labels, test_labels = train_test_split(
    features, labels, train_size=0.8, random_state=algorithm_globals.random_seed)




svc = SVC()
_ = svc.fit(train_features, train_labels)  # suppress printing the return value