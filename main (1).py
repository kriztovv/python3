'''#1
import random
velikost = int(input("velikost:"))
matrix = [[column for column in range(velikost)] for row in range(velikost)]
maxcislo = int(input("max cislo: "))

def randmatice(velikostm, maxcislom):
    for j in range (velikostm):
        for i in range (velikostm):
                matrix[i][j] = random.randint(0, maxcislom)
    return(matrix)
    
print(randmatice(velikost, maxcislo))'''

#2
velikost = int(input("velikost:"))
matrix = [[column for column in range(velikost)] for row in range(velikost)]

def sachovnice(velikostm):
        for j in range (velikostm):
            for i in range (velikostm):
                if(j % 2 == 0):
                    matrix[i][j] = 1
                else: 
                    matrix[i][j] = 0

def print_matrix(matrixm):
    # Loop over each row
    for i in range(len(matrixm)):
        # Loop over each column in the current row
        for j in range(len(matrixm[i])):
            # Print element at row i, column j
            print(matrixm[i][j], end=' ')
        # Print a new line after each row
        print()

sachovnice(velikost)
print_matrix(matrix)




ERROR UKOL 2!!!!












