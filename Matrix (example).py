#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

rows = int(input("Введите количество строк: "))

cols = int(input("Введите количество столбцов: "))

matrix_a = np.random.randint(0, 10, size=(rows, cols))

matrix_b = np.random.randint(0, 10, size=(rows, cols))

matrix_sum = matrix_a + matrix_b

print("\nМатрица A:")

print(matrix_a)

print("\nМатрица B:")

print(matrix_b)

print("\nСумма матриц:")

print(matrix_sum)

print("\nТранспонирование матрицы A:")

print(matrix_a.T)


