import pandas as pd
import numpy as np 
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
from converter.csv_to_scikit import csv_to_scikit
import sys
from scrappers.iss.iss_sensors import main as scrape_iss
from scrappers.nasa.nasa_api import main as scrape_nasa

def process(input_file,output_folder):
    iris_data=csv_to_scikit(input_file)

    # iris_data = load_iris()
    # print(iris_data)

    features = iris_data["data"]
    labels = iris_data["target"]
    feature_names = iris_data["feature_names"]
    columns = iris_data["columns"]
    # print(features)
    # print(feature_names)
    # print(labels)
    # print(columns)
    print(features)
    print(feature_names)
    print(labels)
    print(columns)
    

    df = pd.DataFrame(features, columns=columns)
    df["class"] = pd.Series(feature_names)

    def createSeaborn(df):
     hackaton_palete = sns.color_palette("magma", 3)
     sns.pairplot(df, hue="class", palette=hackaton_palete)
    #  SeabornCharts = plt
     plt.savefig(output_folder+'/seeborn.png')
    #  SeabornCharts.show()
    plt.show()
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
        plt.savefig(output_folder+'/circuit28.png')
        # plt.show()
        ansatz = RealAmplitudes(num_qubits=num_features, reps=1)
        ansatz.decompose().draw(output="mpl", fold=20)
        plt.savefig(output_folder+'/circuit20.png')
        # plt.show()
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
        plt.savefig(output_folder+"/secondCircuit.png")
        print(f"Quantum VQC on the training dataset: {train_score_q4:.2f}")
        print(f"Quantum VQC on the test dataset:     {test_score_q4:.2f}")


    objective_func_vals = []
    plt.rcParams["figure.figsize"] = (12, 6)
    def callback_graph(weights, obj_func_eval):
        clear_output(wait=True)
        objective_func_vals.append(obj_func_eval)
        plt.rcParams["figure.figsize"] = (12, 6)
        plt.rcParams['axes.facecolor'] = "#160E3B"
        plt.title("Objective function value against iteration")
        plt.xlabel("Iteration")
        plt.ylabel("Objective function value")
        plt.plot(range(len(objective_func_vals)), objective_func_vals,color='#BD3977')
        # plt.show()




    def reduceSeeborn(features):
        hackaton_palete = sns.color_palette("magma", 3)
        df = pd.DataFrame(features, columns=feature_names)


        df["class"] = pd.Series(labels)
        df = df.iloc[::2]


        plt.rcParams["figure.figsize"] = (6, 6)
        sns.pairplot(df, hue="class", palette=hackaton_palete)
        plt.savefig(output_folder+'/reduceSeeborn.png')
        # plt.show()


    def reduceQuantumML():
        train_features, test_features, train_labels, test_labels = train_test_split(
    features, labels, train_size=0.8, random_state=algorithm_globals.random_seed)
        svc = SVC()
        _ = svc.fit(train_features, train_labels)
        svc.fit(train_features, train_labels)

        train_score_c2 = svc.score(train_features, train_labels)
        test_score_c2 = svc.score(test_features, test_labels)
        plt.savefig(output_folder+"/reduceML.png")
        print(f"Classical SVC on the training dataset: {train_score_c2:.2f}")
        print(f"Classical SVC on the test dataset:     {test_score_c2:.2f}")


    def createSecondCircuit(df):
        num_features = features.shape[1]
        train_features, test_features, train_labels, test_labels = train_test_split(
            features, labels, train_size=0.8, random_state=algorithm_globals.random_seed)

        feature_map = ZZFeatureMap(feature_dimension=num_features, reps=1)
        ansatz = RealAmplitudes(num_qubits=num_features, reps=3)

        optimizer = COBYLA(maxiter=40)
        sampler = Sampler()
        vqc = VQC(
        sampler=sampler,
        feature_map=feature_map,
        ansatz=ansatz,
        optimizer=optimizer,
        callback=callback_graph,
    )

        objective_func_vals = []
        plt.rcParams["figure.figsize"] = (12, 6)


        start = time.time()
        vqc.fit(train_features, train_labels)
        elapsed = time.time() - start

        print(f"Training time: {round(elapsed)} seconds")
        train_score_q2_ra = vqc.score(train_features, train_labels)
        test_score_q2_ra = vqc.score(test_features, test_labels)
        plt.savefig(output_folder+"/secondCircuit.png")
        print(f"Quantum VQC on the training dataset using RealAmplitudes: {train_score_q2_ra:.2f}")
        print(f"Quantum VQC on the test dataset using RealAmplitudes:     {test_score_q2_ra:.2f}")

    def createEffcientSU2():
        num_features = features.shape[1]
        train_features, test_features, train_labels, test_labels = train_test_split(
            features, labels, train_size=0.8, random_state=algorithm_globals.random_seed)

        feature_map = ZZFeatureMap(feature_dimension=num_features, reps=1)
        ansatz = RealAmplitudes(num_qubits=num_features, reps=3)


        optimizer = COBYLA(maxiter=40)
        sampler = Sampler()

        vqc = VQC(
        sampler=sampler,
        feature_map=feature_map,
        ansatz=ansatz,
        optimizer=optimizer,
        callback=callback_graph,
    )


        objective_func_vals = []

        start = time.time()
        vqc.fit(train_features, train_labels)
        elapsed = time.time() - start
        plt.savefig(output_folder+"/EfficientSU2.png")
        print(f"Training time: {round(elapsed)} seconds")
    
    createEffcientSU2()
    createSeaborn(df)
    createFirstCircuit(df)
    # reduceSeeborn(np.array(features))
    reduceQuantumML()
    createSecondCircuit(df)
    
args = len(sys.argv)-1
if args: 
    print("Processing")
    if sys.argv[1] == "iris":
        process("./csv/iris.csv","./public/charts/iris")
    elif sys.argv[1] == "iss": 
        scrape_iss()
        process("./csv/iss.csv","./public/charts/iss")
    elif sys.argv[1] == "nasa": 
        scrape_nasa()
        process("./csv/nasa.csv","./public/charts/nasa")
    print("FINISHED PROCESSING!")
else:
    print('Put in args one of this three options: "nasa", "iris" or "iss"')