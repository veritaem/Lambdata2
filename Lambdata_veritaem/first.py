import numpy
import pandas
from sklearn.model_selection import train_test_split
from collections import defaultdict

def check_nulls(df):
    # checks for instances of nulls in a pandas DataFrame
    # returns sum of nulls in df
    return df.isna().sum(), df.isna().sum().sum()


def three_way_split(
    X, y, train_size=0.8, val_size=0.1, test_size=0.1,
        random_state=None, shuffle=False):
    # Returns a 3 way split of train, test, and validate
        assert train_size + val_size + test_size == 1
        X_train_val, X_test, y_train_val, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state,
            shuffle=shuffle)

        X_train, X_val, y_train, y_val = train_test_split(
            X_train_val, y_train_val, test_size=val_size/(train_size+val_size),
            random_state=random_state, shuffle=shuffle)
        return X_train, X_val, X_test, y_train, y_val, y_test

class Customer:
    def __init__(self, name, age, bill, pay_method):
    self.name = name
    self.age = age
    self.bill = bill
    self.pay_method = pay_method

