import pandas as pd
import numpy as np

chat_id = 506238275  # Ваш chat ID, не меняйте название переменной


def solution(x: np.array, y: np.array) -> bool:
    x_bins, bins = np.histogram(x, bins=20)
    y_bins, _ = np.histogram(y, bins)
    phi = np.sum((y_bins - x_bins) ** 2 / x_bins)
    df = len(x_bins) - 1
    # chi2_th = chi2.ppf(1 - 0.1, df)
    chi2_th = 27.203571029356826
    return phi > chi2_th


def test_solution():
    historical_data = pd.read_csv('pb2_data/historical_data.csv')
    modified_data_1 = pd.read_csv('pb2_data/modified_data_of_type_1.csv')
    modified_data_2 = pd.read_csv('pb2_data/modified_data_of_type_2.csv')
    modified_data_3 = pd.read_csv('pb2_data/modified_data_of_type_3.csv')

    results = []

    for i in range(len(historical_data)):
        x = historical_data.iloc[i].values
        y1 = modified_data_1.iloc[i].values
        y2 = modified_data_2.iloc[i].values
        y3 = modified_data_3.iloc[i].values

        result_1 = solution(x, y1)
        result_2 = solution(x, y2)
        result_3 = solution(x, y3)

        results.append((result_1, result_2, result_3))

    for i, (res1, res2, res3) in enumerate(results):
        print(f"Row {i + 1}:")
        print(f"  Result for modified_data_of_type_1: {res1}")
        print(f"  Result for modified_data_of_type_2: {res2}")
        print(f"  Result for modified_data_of_type_3: {res3}")


test_solution()
