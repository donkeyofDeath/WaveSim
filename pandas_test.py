import pandas as pd

import numpy as np

import datetime as dt

# df = pd.read_csv("test_data2.csv")
# new_row = pd.DataFrame({"First": "Test 1", "Second": "Test 2", "Third": [np.array([[1., 2.], [3., 4.], [5., 6.]]).tolist()]})
# with open("test_data2.csv", "a") as file:
#    new_row.to_csv(file, index=False, sep=";")

print(isinstance(dt.datetime.utcnow(), dt.datetime))

num = 5.
my_array = np.array([1., 2., 3.])
my_matrix = np.array([[1., 2., 3.], [4., 5., 6.]])

"""
df = pd.DataFrame({"First": num,
                   "Second": [pd.array(my_array)],
                   "Third": [pd.DataFrame(my_matrix)]})

with open("new_test_data.csv", "a") as file:
    df.to_csv(file, header=True, index=False, sep=";")
"""

df2 = pd.read_csv("new_test_data.csv", delimiter=";")
print(pd.array(df2["Second"]))

"""
# Try to load data from a file
print("Start loading data.")
df = pd.read_csv("test_data/wave_sim1D_2021-03-01 15:05:26.csv", delimiter=";", dtype={
    "UTC date time": str,
    "number of grid points": int,
    "number of time steps": int,
    "grid spacing Δx": float,
    "time spacing Δt": float,
    "initial amplitudes": str,
    "initial velocities": str,
    "result": list})
print("Finished loading data")
with np.printoptions(threshold=np.inf):
    new_array = df["result"].to_numpy()
    print(type(new_array))
    # print(new_array)
"""
