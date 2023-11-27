with open('mat1.txt','r') as file1:
    mat1 = file1.readlines()
    row1 = len(mat1)  
    column1 = len(mat1[0].split())

with open('mat2.txt','r') as file2:
    mat2 = file2.readlines()
    row2 = len(mat2)
    column2 = len(mat2[0].split())

with open('mat3.txt','r') as file3:
    mat3 = file3.readlines()
    row3 = len(mat3)
    column3 = len(mat3[0].split())

if row1 == row2 and column1 == column2 :
    row = []
    for i in range(len(mat1)):
        column = []
        for j in range(len(mat1[i])):
            val = int(mat1[i].split()[j]) + int(mat2[i].split()[j])
            column.append(val)
        row.append(column)
    with open("outmat.txt","w") as result:
        for i in row:
            for j in i:
                result.write(str(j))
                result.write(' ')
            result.write('\n')
else:
    open("outmat1.txt","w")
        


