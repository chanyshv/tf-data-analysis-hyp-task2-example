import numpy as np
from scipy.stats import anderson_ksamp

chat_id = 506238275  # Ваш chat ID, не меняйте название переменной


def solution(x: np.array, y: np.array) -> bool:
    result = anderson_ksamp([x, y])
    return result.significance_level < 0.08


# def test_solution():
#     historical_data = pd.read_csv('pb2_data/historical_data.csv')
#     modified_data_1 = pd.read_csv('pb2_data/modified_data_of_type_1.csv')
#     modified_data_2 = pd.read_csv('pb2_data/modified_data_of_type_2.csv')
#     modified_data_3 = pd.read_csv('pb2_data/modified_data_of_type_3.csv')
#
#     r1 = 0
#     r2 = 0
#     r3 = 0
#     for i in range(len(historical_data)):
#         x = historical_data.iloc[i].values
#         y1 = modified_data_1.iloc[i].values
#         y2 = modified_data_2.iloc[i].values
#         y3 = modified_data_3.iloc[i].values
#
#         result_1 = solution(x, y1)
#         result_2 = solution(x, y2)
#         result_3 = solution(x, y3)
#
#         if not result_1: r1 += 1
#         if not result_2: r2 += 1
#         if not result_3: r3 += 1
#
#     for i, r in enumerate([r1, r2, r3]):
#         print(f'{i + 1}: {r / 300}')
#
#
# def test_historical_data_pairs():
#     historical_data = pd.read_csv('pb2_data/historical_data.csv')
#
#     pair_results = []
#     pair_error_count = 0
#
#     for i in range(len(historical_data)):
#         for j in range(i + 1, len(historical_data)):
#             x = historical_data.iloc[i].values
#             y = historical_data.iloc[j].values
#
#             result = solution(x, y)
#             pair_results.append(result)
#
#             if result: pair_error_count += 1
#
#     print(f"Error frequency in historical data pairs: {pair_error_count / len(pair_results)}")
#
#
# test_solution()
# test_historical_data_pairs()