from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from qiskit.utils import algorithm_globals
from sklearn.svm import SVC
from qiskit.circuit.library import ZZFeatureMap
from qiskit.circuit.library import RealAmplitudes
from qiskit.algorithms.optimizers import COBYLA
from qiskit.primitives import Sampler
from matplotlib import pyplot as plt
from IPython.display import clear_output
from qiskit_machine_learning.algorithms.classifiers import VQC
import time
from sklearn.decomposition import (PCA)
from qiskit.circuit.library import EfficientSU2

iris_data = load_iris()
    #print(iris_data.DESCR)


features = iris_data.data
labels = iris_data.target

df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
df["class"] = pd.Series(iris_data.target)

def createSeaborn(df):
     hackaton_palete = sns.color_palette("magma", 3)
     sns.pairplot(df, hue="class", palette=hackaton_palete)
     SeabornCharts = plt
     plt.savefig('seeborn.png')
     SeabornCharts.show()





#algorithm_globals.random_seed = 123

def createClassicalML(df):
     train_features, test_features, train_labels, test_labels = train_test_split(
     features, labels, train_size=0.8, random_state=algorithm_globals.random_seed)
     svc = SVC()
     _ = svc.fit(train_features, train_labels)
     train_score_c4 = svc.score(train_features, train_labels)
     test_score_c4 = svc.score(test_features, test_labels)
     print(f"Classical SVC on the training dataset: {train_score_c4:.2f}")
     print(f"Classical SVC on the test dataset:     {test_score_c4:.2f}")



def createFirstCircuit(df):
    train_features, test_features, train_labels, test_labels = train_test_split(
        features, labels, train_size=0.8, random_state=algorithm_globals.random_seed)

    num_features = features.shape[1]

    feature_map = ZZFeatureMap(feature_dimension=num_features, reps=1)
    feature_map.decompose().draw(output="mpl", fold=29)
    plt.savefig('cirucit28.png')
    plt.show()
    ansatz = RealAmplitudes(num_qubits=num_features, reps=1)
    ansatz.decompose().draw(output="mpl", fold=20)
    plt.savefig('cirucit20.png')
    plt.show()
    optimizer = COBYLA(maxiter=100)
    sampler = Sampler()
    vqc = VQC(
         sampler=sampler,
         feature_map=feature_map,
         ansatz=ansatz,
         optimizer=optimizer,
         callback=callback_graph,
     )

    # clear objective value history
    objective_func_vals = []

    start = time.time()
    vqc.fit(train_features, train_labels)
    elapsed = time.time() - start
    print(f"Training time: {round(elapsed)} seconds")
    train_score_q4 = vqc.score(train_features, train_labels)
    test_score_q4 = vqc.score(test_features, test_labels)
    print(f"Quantum VQC on the training dataset: {train_score_q4:.2f}")
    print(f"Quantum VQC on the test dataset:     {test_score_q4:.2f}")


objective_func_vals = []
plt.rcParams["figure.figsize"] = (12, 6)
def callback_graph(weights, obj_func_eval):
    clear_output(wait=True)
    objective_func_vals.append(obj_func_eval)
    plt.rcParams["figure.figsize"] = (12, 6)
    plt.rcParams['axes.facecolor'] = "peru"
    plt.title("Objective function value against iteration")
    plt.xlabel("Iteration")
    plt.ylabel("Objective function value")
    plt.plot(range(len(objective_func_vals)), objective_func_vals,color='pink')
    plt.show()







def reduceQuantumML(df):
    train_features, test_features, train_labels, test_labels = train_test_split(
        features, labels, train_size=0.8, random_state=algorithm_globals.random_seed)


    features = PCA(n_components=2).fit_transform(features)

    plt.rcParams["figure.figsize"] = (6, 6)
    sns.scatterplot(x=features[:, 0], y=features[:, 1], hue=labels, palette="tab10")
    plt.show()

reduceQuantumML()
# train_features, test_features, train_labels, test_labels = train_test_split(
#     features, labels, train_size=0.8, random_state=algorithm_globals.random_seed
# )
#
# svc.fit(train_features, train_labels)
#
# train_score_c2 = svc.score(train_features, train_labels)
# test_score_c2 = svc.score(test_features, test_labels)
#
# print(f"Classical SVC on the training dataset: {train_score_c2:.2f}")
# print(f"Classical SVC on the test dataset:     {test_score_c2:.2f}")
#
#
# num_features = features.shape[1]
#
# feature_map = ZZFeatureMap(feature_dimension=num_features, reps=1)
# ansatz = RealAmplitudes(num_qubits=num_features, reps=3)
#
#
# optimizer = COBYLA(maxiter=40)
#
# vqc = VQC(
#     sampler=sampler,
#     feature_map=feature_map,
#     ansatz=ansatz,
#     optimizer=optimizer,
#     callback=callback_graph,
# )
#
# # clear objective value history
# objective_func_vals = []
#
# # make the objective function plot look nicer.
# plt.rcParams["figure.figsize"] = (12, 6)
#
#
# start = time.time()
# vqc.fit(train_features, train_labels)
# elapsed = time.time() - start
#
# print(f"Training time: {round(elapsed)} seconds")
#
#
# train_score_q2_ra = vqc.score(train_features, train_labels)
# test_score_q2_ra = vqc.score(test_features, test_labels)
#
# print(f"Quantum VQC on the training dataset using RealAmplitudes: {train_score_q2_ra:.2f}")
# print(f"Quantum VQC on the test dataset using RealAmplitudes:     {test_score_q2_ra:.2f}")
#
#
# ansatz = EfficientSU2(num_qubits=num_features, reps=3)
# optimizer = COBYLA(maxiter=40)
#
# vqc = VQC(
#     sampler=sampler,
#     feature_map=feature_map,
#     ansatz=ansatz,
#     optimizer=optimizer,
#     callback=callback_graph,
# )
#
# # clear objective value history
# objective_func_vals = []
#
# start = time.time()
# vqc.fit(train_features, train_labels)
# elapsed = time.time() - start
#
# print(f"Training time: {round(elapsed)} seconds")
#
# train_score_q2_eff = vqc.score(train_features, train_labels)
# test_score_q2_eff = vqc.score(test_features, test_labels)
#
# print(f"Quantum VQC on the training dataset using EfficientSU2: {train_score_q2_eff:.2f}")
# print(f"Quantum VQC on the test dataset using EfficientSU2:     {test_score_q2_eff:.2f}")
#
#
# print(f"Model                           | Test Score | Train Score")
# print(f"SVC, 4 features                 | {train_score_c4:10.2f} | {test_score_c4:10.2f}")
# print(f"VQC, 4 features, RealAmplitudes | {train_score_q4:10.2f} | {test_score_q4:10.2f}")
# print(f"----------------------------------------------------------")
# print(f"SVC, 2 features                 | {train_score_c2:10.2f} | {test_score_c2:10.2f}")
# print(f"VQC, 2 features, RealAmplitudes | {train_score_q2_ra:10.2f} | {test_score_q2_ra:10.2f}")
# print(f"VQC, 2 features, EfficientSU2   | {train_score_q2_eff:10.2f} | {test_score_q2_eff:10.2f}")