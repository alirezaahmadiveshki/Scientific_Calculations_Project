# solving least square problem using cholesky decomposition

# min||AX - b|| if A shape is (m, n) and m >= n

# the caclulations error is in python defult 
# the result in the termainal is rounded to 5 digit

import numpy as np
# using numpy for operating on matrices[the operatoins used: Adding, multiplying and transposing]
import math



def main():
    A_array = np.array([
                    [1, 1, 0],
                    [1, 0, 1],
                    [0, 1, 1]
                    ])

    b_array = np.array([
                    [3],
                    [7],
                    [6],
                    ])
    

    def norm(arr):
        res = 0
        for i in arr:
            res += i**2
        res = math.sqrt(res)
        return res
    

    row = A_array.shape[0]
    col = A_array.shape[1]

    R = np.zeros((row, col))


    A_columns = []
    for i in range(col):
        a = A_array[: ,i]
        A_columns.append(a)


    Q_list = []
    Q_hat_list = []

    # ---------------

    q1_hat = A_columns[0] 
    Q_hat_list.append(q1_hat)
    R[0][0] = norm(q1_hat)
    q1 = q1_hat/R[0][0]
    Q_list.append(q1)

    # ---------------
    for n in range(1, col):
        temp_sum = 0
        for i in range(n):
            q = Q_list[i]
            matrix_q = np.matrix(q)
            matrix_q = matrix_q.getT()
            transposed_matrix_q = matrix_q.getT()
            matrix_col = np.matrix(A_columns[n])
            matrix_col = matrix_col.getT()
            R[i][n] = (transposed_matrix_q * matrix_col).item(0, 0)
            temp_sum += R[i][n] * matrix_q

        A_Matrix = np.matrix(A_columns[n])
        q2_hat = A_Matrix.getT() - temp_sum
        q2_hat = np.squeeze(np.asarray(q2_hat))
        Q_hat_list.append(q2_hat)
        R[n][n] = norm(q2_hat)
        q2 = q2_hat/R[n][n]
        Q_list.append(q2)


    Q_matrix = np.matrix(Q_list)
    Q_matrix = Q_matrix.getT()
    Q_hat_matrix = np.matrix(Q_hat_list)
    Q_hat_matrix = Q_hat_matrix.getT()

    b = np.matrix(b_array)

    Qtb = Q_matrix.getT() * b

    arr_y = np.squeeze(np.asarray(Qtb))
    arr_R = np.squeeze(np.asarray(R))
    X = np.zeros((col, 1))
    for i in range(col-1, -1, -1):
        if i == 2:
            X[i][0] = (1/arr_R[i][i]) * (arr_y[i])
        else:
            X[i][0] = (1/arr_R[i][i]) * (arr_y[i] - sum(X[j][0]*arr_R[i][j] for j in range(col-1, 0, -1)))


    X = np.matrix(X)

    print()
    print("--------- (QR decomposition ----------)")
    print()
    print("------------- A matrix ----------------")
    print(A_array)
    print("------------- Q hat matrix -----------")
    print(Q_hat_matrix)
    print("------------- Q matrix ---------------")
    print(Q_matrix)
    print("------------- R matrix ----------------")
    print(R)
    print("------------- Q * R -------------------")
    print(Q_matrix * R)
    print("------ QR's error of calculation --------")
    print()
    print("---> error matrix for decomposition")
    print()
    error_matrix_for_decomposition = A_array - (Q_matrix * R)
    print(error_matrix_for_decomposition)
    print()
    print("infinite norm of error for QR decomposition: ", abs(error_matrix_for_decomposition).max())
    print()
    print("----------- (AX = b -> X = ?) --------------")
    print()
    print("-------------------- b ---------------------")
    print(b)
    print("-------------------- Qt --------------------")
    print(Q_matrix.getT())
    print("----------------- Qt * b -------------------")
    print(Qtb)
    print("---------- (R * X = Qtb -> X = ?) -----------")
    print()
    print("---------------- X ---------------")
    print(X)
    print("------------ error_matrix = A*X - b --------")
    error_matrix = (np.matrix(A_array) * X) - b
    print(error_matrix)
    print()
    print("infinite norm of error: ", abs(error_matrix).max())
    print()
    print()


main()  


def pending():
    # example arrays
    A_array = np.array([
                    [1, 0, 4],
                    [2, 2, 10],
                    [1, -2, 1],
                    [1, -2, -2]
                    ])

    b_array = np.array([
                    [3],
                    [7],
                    [6],
                    [1]
                    ])

    print()
    print("%"*40)
    print("welcome")
    print("%"*40)
    print()

    while True:
        print("-"*40)
        print("choose one of the below options: ")
        print("-"*40)
        print()
        print("1 for writing A and b matrices manually")
        print("2 for an example")
        print("3 for quiting")
        print()
        inp = int(input("your option: ").strip())
        print()
        print()
        if inp == 1:
            print("fill the below matrices(comma seperated numbers)")
            try:
                dim = input("the dimentions of the A\n(comma seperated integers and the first number greater equal to second one): ").strip().split(" ")
                row = int(dim[0])
                column = int(dim[1])
                if column > row or not isinstance(row, int) or not isinstance(column, int):
                    raise ValueError
            except:
                print("invalid input please try again")
                continue
            try:
                A = input(f"enter {row*column} numbers for A matrix\n(camma seperated numbers): ").strip().split()
                A = list(map(lambda x: float(x), A))
                len(A)
                if len(A) != row*column:
                    raise ValueError("invalid input please try again")
                A = np.array(A)
                new_A_array = A.reshape(row, column)
            except:
                print("invalid input please try again")
                continue
            try:
                b = input(f"enter {row} numbers for A matrix\n(camma seperated numbers): ").strip().split()
                b = list(map(lambda x: float(x), b))
                if len(A) != row*column:
                    raise ValueError("invalid input please try again")
                b = np.array(b)
                new_b_array = b.reshape(row, 1)
            except:
                print("invalid input please try again")
                continue

        elif inp == 2:
            ...
        elif inp == 3:
            break


# pending()