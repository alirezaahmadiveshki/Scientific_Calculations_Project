# solving least square problem using cholesky decomposition

# min||AX - b|| if A shape is (m, n) and m >= n

# the caclulations error is in python defult 
# the result in the termainal is rounded to 5 digit

import numpy as np
# using numpy for operating on matrices[the operatoins used: Adding, multiplying and transposing]
import math



def main(A_array, b_array):
    matrices = {} # we use this for showing the matrices


    # making A and b matrices
    A = np.matrix(A_array)
    matrices["A"] = A

    b = np.matrix(b_array)
    matrices["b"] = b

    # At * b = _b -> _b : b bar

    _b = A.getT() * b
    matrices["_b"] = _b

    # -----------------------

    At = A.getT() # At : transposed of A matrix
    R_Rt = At * A # R * Rt

    matrices["R * Rt(=At * A)"] = R_Rt


    # converting R_Rt to R * Rt

    def choleski(A):
        n = A.shape[0] # (n, n)[0] = n (dimention of the square matrix A)
        R = np.zeros((n, n)) # making an square matrix with zero elements for storing R
        Arr_R = np.squeeze(np.asarray(R))
        for i in range(n):
            for k in range(i+1):
                tmp_sum = sum(R[i][j]*R[k][j] for j in range(k))

                if i == k:
                    Arr_R[i][k] = math.sqrt(A.item(i, i) - tmp_sum)
                else:
                    Arr_R[i][k] = (1/R[k][k]*(A.item(i, k) - tmp_sum))
        R = np.matrix(R)   
        return R



    Rt = choleski(R_Rt)
    matrices["Rt"] = Rt
    R = np.asarray(Rt.getT())
    matrices["R"] = R

    # Rt*R*X = _b --> R*X = Y --> RtY = _b --> Y = ?

    arr_Rt = np.squeeze(np.asarray(Rt))
    arr_b = np.squeeze(np.asarray(_b))
    n = Rt.shape[0]
    Y = np.zeros((n, 1))
    for i in range(n):
        if i == 0:
            Y[i][0] = (1/arr_Rt[i][i]) * (arr_b[i])
        else:
            Y[i][0] = (1/arr_Rt[i][i]) * (arr_b[i] - sum(Y[j][0]*arr_Rt[i][j] for j in range(1)))
                

    Y = np.matrix(Y)
    matrices["Y"] = Y              


    # RX = Y --> X = ?

    arr_y = np.squeeze(np.asarray(Y))
    arr_R = np.squeeze(np.asarray(R))
    X = np.zeros((n, 1))
    for i in range(n-1, -1, -1):
        if i == 2:
            X[i][0] = (1/arr_R[i][i]) * (arr_y[i])
        else:
            X[i][0] = (1/arr_R[i][i]) * (arr_y[i] - sum(X[j][0]*arr_R[i][j] for j in range(n-1, 0, -1)))


    X = np.matrix(X)
    matrices["X"] = X

    # error margin finder
    # AX - b

    err = (A * X) - b
    matrices["error"] = err

    # computing infinote norm
    error_margin = err.max()

    # demonstraiting matrices 

    return matrices, error_margin



def showing(matrices, error_margin):
    s = ''
    for key, value in matrices.items():
        s += "*"*40 + '\n'
        value = value.round(5)
        s += f"{key} matrix:\n{value}" + '\n'
        s += "*"*40 + "\n\n"
    s += f"infinite norm of error matrix: {error_margin}\n\n"
    return s

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

            matrices, error_margin = main(new_A_array, new_b_array)
            print(showing(matrices, error_margin))    

        elif inp == 2:
            matrices, error_margin = main(A_array, b_array)
            print(showing(matrices, error_margin))
        elif inp == 3:
            break


pending()