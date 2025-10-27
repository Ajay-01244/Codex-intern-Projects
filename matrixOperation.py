import numpy as np
def create_matrix(mName):
    row = int(input(f"Enter no. of rows in {mName}"))
    col = int(input(f"Enter no. of col in {mName}"))
    try:
        if(row>0 and col>0):
            list =  []
            for i in range(row):
                list1 =[]
                for j in range(col):
                    element = int(input(f"Enter elemeent of matrix at ({i+1},{j+1}):"))
                    list1.append(element)
                list.append(list1)
            matrix = np.array(list)
            return matrix
        else:
            print("Zero Matrix")
            return 0
    except ValueError:
        print("please enter int number")
def display_matrix(result,title='Result'):
    "Display a matrix with a given title"
    print(f"\n--- {title} ----")
    print(result)
    print("---------------\n")

def operation():
    while True:
        print("/n Matrix Operation tool")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4. Transpose")
        print("5. Determinant")
        print("6.Inverse of matrix")
        print("7. Exit ")

        choice = int(input("Enter your choice (1-7)"))

        if(choice == 1):
            matrix1 = create_matrix("Matrix1")
            matrix2 = create_matrix("Matrix2")
            if(matrix1.shape[0] == matrix2.shape[0] & matrix1.shape[1] == matrix2.shape[1]):
                try:
                    sum = matrix1+matrix2
                    display_matrix(sum,"Matrix Addition Result")
                except ValueError as value:
                    print(f"Error:{value}. Matrices must have the same dimension")
            else:
                print("Dimension must be same")
        
        elif(choice == 2):
            matrix1 = create_matrix("Matrix1")
            matrix2 = create_matrix("Matrix2")
            if(matrix1.shape[0] == matrix2.shape[0] & matrix1.shape[1] == matrix2.shape[1]):
                try:
                    sub = matrix1-matrix2
                    display_matrix(sub,"Matrix Subtraction Result")
                except ValueError as value:
                    print(f"Error:{value}. Matrices must have the same dimension")
            else:
                print("Dimension must be same")

        elif(choice == 3):
            matrix1 = create_matrix("Matrix1")
            matrix2 = create_matrix("Matrix2")
            try:
                mul = np.dot(matrix1,matrix2)
                display_matrix(mul,"Matix multiplication Result")
            except ValueError as value:
                print(f"Error:{value}. number of column in matrix1 must be equal to no. of column in matrix2")   
        
        elif(choice == 4):
            matrix = create_matrix("Matrix1")
            Transpose = matrix.T
            display_matrix(Transpose,"Matrix Transpose Result")
        
        elif(choice == 5):
            matrix = create_matrix("Matrix1")
            if(matrix.shape[0]==matrix.shape[1]):
                det = np.linalg.det(matrix)
                display_matrix(det,"determinant value of matrix Result")
            else:
                print("you can ony calculate determinant of square matrix")

        elif(choice ==6):
            matrix = create_matrix("Matrix")
            if(matrix.shape[0]==matrix.shape[1]):
                det = np.linalg.det(matrix)
                if(det!=0):
                    ansInv = np.linalg.inv(matrix)
                    display_matrix(ansInv,"Inverse Result")
                else:
                    print("Sorry you can't calculate this ---Matrix must be Non Singular---")
            else:
                print("Matrix must be Square Matrix")
                
        
        elif(choice == 7):
            break
        
        else:
            print("Invalid Option")

        ch = input("Wants More? y/n")
        if ch in 'Nn':
            break
            
operation()