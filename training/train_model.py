import os
import joblib

import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import cross_val_score
import pandas as pd


MODEL_FILE = "model.pkl"
PIPELINE_FILE = "pipeline.pkl"

def build_pipeline(num_attribs, cat_attribs):
    num_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])
    cat_pipeline = Pipeline([
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ])
    full_pipeline = ColumnTransformer([
        ("num", num_pipeline, num_attribs),
        ("cat", cat_pipeline, cat_attribs)
    ])
    return full_pipeline


if not os.path.exists(MODEL_FILE):
    #TRAINING PHASE
    housing = pd.read_excel("housing_data.xlsx")
    housing["income_cat"] = pd.cut(housing["median_income"],
                                   bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf],
                                   labels=[1,2,3,4,5])
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(housing, housing['income_cat']):
        housing = housing.loc[train_index].drop("income_cat", axis=1)

    housing_label = housing["median_house_value"].copy()
    housing_feature = housing.drop("median_house_value", axis=1)
    num_attribs = housing_feature.drop("ocean_proximity", axis=1).columns.tolist()
    cat_attribs = ["ocean_proximity"]


    pipeline = build_pipeline(num_attribs, cat_attribs)

    housing_prepared = pipeline.fit_transform(housing_feature)

    model = RandomForestRegressor(random_state=42)
    model.fit(housing_prepared, housing_label)


    #save model and pipeline
    joblib.dump(model, MODEL_FILE)
    joblib.dump(pipeline, PIPELINE_FILE)

    print("model trained and saved.")
