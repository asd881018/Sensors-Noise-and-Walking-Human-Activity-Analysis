import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.utils import shuffle
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

def process_file(pathname):
    res = pd.read_csv(pathname, sep=',', header=0, index_col=None, names=[
                      'time', 'seconds', 'z', 'y', 'x'])
    return res

def main():

    dlp_5min = process_file('processed_data/dlp_5min.csv')
    drp_5min = process_file('processed_data/drp_5min.csv')
    mrp_5min = process_file('processed_data/mrp_5min.csv')
    slp_5min = process_file('processed_data/slp_5min.csv')
    srp_5min = process_file('processed_data/srp_5min.csv')
    
    # Splitting the 5-minute dataset into 10 equal parts.
    dlp_5min['name'] = 'diego'
    drp_5min['name'] = 'diego'
    mrp_5min['name'] = 'matt'
    slp_5min['name'] = 'sam'
    srp_5min['name'] = 'sam'

    dlsplit = np.array_split(dlp_5min, 30)
    drsplit = np.array_split(drp_5min, 30)
    mrsplit = np.array_split(mrp_5min, 30)
    slsplit = np.array_split(slp_5min, 30)
    srsplit = np.array_split(srp_5min, 30)

    tnames = []
    tdata = []

    for i in [dlsplit, drsplit, mrsplit, slsplit, srsplit]:
        for j in range(len(i) - 1):
            temp = i[j]

            if (temp['name'].all() == 'diego'):
                tnames.append('diego')
            if (temp['name'].all() == 'matt'):
                tnames.append('matt')
            if (temp['name'].all() == 'sam'):
                tnames.append('sam')

            temp['combined'] = temp['x'] + temp['y'] + temp['z']
            tdata.append(np.asarray(i[j]['combined']))

    training_data = pd.DataFrame(tnames)
    training_data['joined'] = pd.Series(tdata, index = training_data.index)
    training_data.rename(columns = {0 : 'name'}, inplace = True)
    training_data = pd.concat([training_data['name'], training_data.pop('joined').apply(pd.Series)], axis=1).dropna(axis = 1)

    ## ML portion starts here

    X = training_data.drop(columns = ['name'])
    y = training_data['name']

    X_train, X_valid, y_train, y_valid = train_test_split(X, y)

    bayes_model = make_pipeline(
        GaussianNB()
    )

    knn_model = make_pipeline(
        StandardScaler(),
        KNeighborsClassifier(n_neighbors = 8)
    )

    nn_model = make_pipeline(
        StandardScaler(),
        MLPClassifier(solver = 'lbfgs', hidden_layer_sizes = (16,8,4), activation = 'logistic', max_iter=100000)
    )

    dt_model = make_pipeline(
        StandardScaler(),
        DecisionTreeClassifier(max_depth = 125)
    )

    rf_model = make_pipeline(
        RandomForestClassifier(n_estimators = 1500 , max_depth = 3, min_samples_leaf = 5)
    )

    print('bayes')
    bayes_model.fit(X_train, y_train)
    print(bayes_model.score(X_train, y_train))
    print(bayes_model.score(X_valid, y_valid))
    print('')
    print('knn')
    knn_model.fit(X_train, y_train)
    print(knn_model.score(X_train, y_train))
    print(knn_model.score(X_valid, y_valid))
    print('')
    print('neural net')
    nn_model.fit(X_train, y_train)
    print(nn_model.score(X_train, y_train))
    print(nn_model.score(X_valid, y_valid))
    print('')
    print('decision tree')
    dt_model.fit(X_train, y_train)
    print(dt_model.score(X_train, y_train))
    print(dt_model.score(X_valid, y_valid))
    print('')
    print('random forest')
    rf_model.fit(X_train, y_train)
    print(rf_model.score(X_train, y_train))
    print(rf_model.score(X_valid, y_valid))