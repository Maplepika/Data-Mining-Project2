# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 20:08:12 2018

@author: neilp
"""

import pandas as pd
import graphviz as gz
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier
        
data = pd.read_csv("data.csv")
data_X = data[data.columns[:2]]
data_Y = data[data.columns[2]]

X_train, X_test, Y_train, Y_test = train_test_split(data_X, data_Y, test_size = 0.2)
tree = DecisionTreeClassifier(criterion = "entropy", max_depth = 3, random_state = 0)
tree.fit(X_train, Y_train)

export_graphviz(tree, out_file = "tree_ent.dot", feature_names = ["X", "Y"])

forest =RandomForestClassifier(criterion = "entropy", n_estimators = 10, random_state = 0)
forest.fit(X_train, Y_train)