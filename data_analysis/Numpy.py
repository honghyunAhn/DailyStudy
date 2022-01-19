import numpy as np

arr1 = np.arange(15).reshape(3, 5)  # 15개의 값을 3행 5열로 만듦.
print(arr1)

np.arange(10)

arr1.shape  # arr1의 차원을 출력합니다.

arr3 = np.zeros((3, 4))  # 0을 출력
print(arr3)
print("---------------")
arr4 = np.ones((3, 4))  # 1을 출력
print(arr4)

arr5 = np.array([
    [1, 2, 3],
    [4, 5, 6]
], dtype=np.float64)

arr6 = np.array([
    [7, 8, 9],
    [10, 11, 12]
], dtype=np.float64)

# 사칙연산을 출력합니다.
print("arr5 + arr6 = ")
print(arr5 + arr6, "\n")
print("arr5 - arr6 = ")
print(arr5 - arr6, "\n")
print("arr5 * arr6 = ")
print(arr5 * arr6, "\n")
print("arr5 / arr6 = ")
print(arr5 / arr6, "\n")
