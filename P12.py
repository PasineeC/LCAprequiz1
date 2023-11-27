def add_mat(f_file,s_file,o_file):
    def read_file(file_name):
        with open(file_name,'r') as file:
            mat = file.readlines()
            row = len(mat)
            column = len(mat[0].split())
            return mat, row, column

    mat1, row1, column1 = read_file(f_file)
    mat2, row2, column2 = read_file(s_file)

    if row1 == row2 and column1 == column2:
        row = []
        for i in range(len(mat1)):
            column = []
            for j in range(len(mat1[i].split())):
                val = int(mat1[i].split()[j]) + int(mat2[i].split()[j])
                column.append(val)
            row.append(column)

        with open(o_file,"w") as result:
            for i in row:
                for j in i:
                    result.write(str(j))
                    result.write(' ')
                result.write('\n')
    else:
        open(o_file,"w")

add_mat('mat1.txt', 'mat2.txt', 'outmat.txt')
add_mat('mat1.txt', 'mat3.txt', 'outmat1.txt')