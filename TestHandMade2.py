import random
import unittest
def  MatrixTurn(Matrix, M, N, T):
    A = []
    for i in range(len(Matrix)):
        A.append(list(Matrix[i]))
    perimetr = []
    temp = []
    while len(A) > 2 and len (A[0]) > 2:               # Разбираем матрицу на "периметры"
        for i in range(len(A[0])):
            temp.append(A[0][i])
        del A[0]
        for i in range(len(A)-1):
            temp.append(A[i][len(A[i])-1])
            del A[i][len(A[i])-1]
        for i in range(-1, -len(A[len(A)-1])-1, -1):
            temp.append(A[len(A)-1][i])
        del A[len(A)-1]
        for i in range(-1, -len(A)-1, -1):
            temp.append(A[i][0])
            del A[i][0]
        perimetr.append(temp)
        temp = []
    if N >= M:                                    # Последний периметр, состоящий из 2-х строк (горизонтальная или квадратная матрица)
        for i in range(len(A[0])):
            temp.append(A[0][i])
        del A[0]
        for i in range(-1, -len(A[0])-1, -1):
            temp.append(A[0][i])
        del A[0]
    else:                                         # ... или из 2х столбцов - Вертикальная матрица
        temp.append(A[0][0])
        for i in range(len(A)):
            temp.append(A[i][1])
            del A[i][1]
        for i in range(-1, -len(A), -1):
            temp.append(A[i][0])
        del A
    perimetr.append(temp)
    perimetr.reverse()
    for i in range(len(perimetr)):            # Проворачиваем каждую линию "периметра"
        for j in range(T):
            perimetr[i].insert(0, perimetr[i].pop())
    A = []                  # Сборка повернутой матрицы производится в обратном порядке - от внутрених слоев к внешним
    if N >= M:                                                  # Для горизонтальной или квадратной матрицы
        R = N - M
        A.append([]) 
        A.append([])
        for j in range(len(perimetr)):
            if j == 0:                                          # заполняем внутренний периметр (только 2 строки)
                z = len(perimetr[0])
                for i in range(len(perimetr[0])):
                    if i < z//2:
                        A[0].append(perimetr[0][i])
                    else:
                        A[1].insert(0, perimetr[0][i])
            else:                                              # Заполняем следующие периметры
                A.insert(0, [])
                A.append([])
                for i in range(len(perimetr[j])):              # Верхняя строка
                    if i < R + 2 * j + 2:
                        A[0].append(perimetr[j][i])
                    elif i < R + 4 * j + 2:                    # Правый столбец
                        A[i - (R + 2 * j + 2 - 1)].append(perimetr[j][i])
                    elif i < (2 * R + 6 * j + 3):
                        A[len(A)-1].insert(0, perimetr[j][i])  # нижняя строка без первого члена
                    else:
                        A[-1 -(i - 2*R - 6*j - 3)].insert(0, perimetr[j][i])   # Левый столбец включая нижнюю строку  
    else:                                                       # Для матрицы, вытянутой ветикально
        R = M - N
        for i in range (R + 2):                            # Создаем внутренний периметр - матрица в 2 столбца, высотой R+2 строки
            A.append([])      
        for j in range(len(perimetr)):
            if j == 0:                                          # заполняем внутренний периметр 
                for i in range(len(perimetr[j])):
                    if i < 2:                                  # Верхняя строка
                        A[0].append(perimetr[j][i])
                    elif i < (R + 3):                           # Правый столбец
                        A[i-1].append(perimetr[j][i])
                    else:                                        # Левый столбец
                        A[-(i - R - 2)].insert(0, perimetr[j][i]) 
            else:
                A.insert(0, [])
                A.append([])
                for i in range(len(perimetr[j])):                             # Верхняя строка
                    if i < 2 * j + 2:
                        A[0].append(perimetr[j][i])
                    elif i < R + 4 * j + 2:                                   # Правый столбец
                        A[i - ( 2 * j + 2 - 1)].append(perimetr[j][i])
                    elif i < (R + 6 * j + 4):
                        A[len(A)-1].insert(0, perimetr[j][i])                 # нижняя строка
                    else:
                        A[-(i - R - 6 * j - 2)].insert(0, perimetr[j][i])   # Левый столбец                  
    for i in range(len(A)):
        A[i] = ''.join(A[i])
    return A
class MyTestCase(unittest.TestCase):    
    
    def test_1(self):
        B = ['123456', '234567', '345678', '456789']
        C = ['212345', '343456', '456767', '567898']
        for i in range(len(B)):
            print(B[i])
        N = len(B[0])
        M = len(B)
        T = 1
        ring = MatrixTurn(B, M, N, T)
        print()
