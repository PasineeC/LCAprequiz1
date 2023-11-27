# with open('mat1.txt','r') as file:
#     mat1 = file.readlines() #['1 2 3 4\n', '8 9 7 2']
#     row1 = len(mat1) #2 แถว
#     column_wrong = len(mat1[0]) #8 ตัว รวมช่องว่าง
#     column1 = len(mat1[0].split())  #4 เอาช่องว่างออก

# with open('mat2.txt','r') as file:
#     mat2 = file.readlines() #['-2 5 0 1\n', '9 8 6 -4']
#     row2 = len(mat2)
#     column2 = len(mat2[0].split())

# first_num = int(mat1[0].split()[2]) #3
# sec_num = int(mat2[0].split()[2]) #0

# for i in range(len(mat1)): # 0 1
#     for j in range(len(mat1[0].split())): # 0 1 2 3 
#         val1 = int(mat1[i].split()[j])      # int(mat1[0].split()[0]) int(mat1[0].split()[1]) int(mat1[0].split()[2]) int(mat1[0].split()[3])
#         val2 = int(mat2[i].split()[j])      # int(mat1[1].split()[0]) int(mat1[1].split()[1]) int(mat1[1].split()[2]) int(mat1[1].split()[3])
#         result = val1 + val2
           
# row = [] # [[-1, 7, 3, 5], [17, 17, 13, -2]]
# for i in range(len(mat1)): # 0 1
#     column = [] #[-1, 7, 3, 5]
#                 #[17, 17, 13, -2]
#     for j in range(len(mat1[0].split())): # 0 1 2 3 
#         val1 = int(mat1[i].split()[j])      
#         val2 = int(mat2[i].split()[j])      
#         result = val1 + val2
#         column.append(result)
#     row.append(column)

# for i in row : #[-1, 7, 3, 5]
#                #[17, 17, 13, -2]
#     for j in i :# -1 7 3 5

# with open('outmat.txt','w') as final:
#     for i in row :
#         for j in i :
#             final.write(str(j)) #-1735171713-2
#             final.write(' ') #-1 7 3 5 17 17 13 -2
#         final.write('\n') # '-1 7 3 5\n','17 17 13 -2'

# open('outmat1.txt','w') #ไฟล์ ว่าง

def add_mat(f_file,s_file,o_file):
    def read_file(file_name):
        with open(file_name,'r') as f:
            mat = f.readlines()
            row = len(mat)
            column = len(mat[0].split())
        return mat, row, column
    
    mat1, row1, column1 = read_file(f_file)
    mat2, row2, column2 = read_file(s_file)

    if row1 == row2 and column1 == column2:
        row = []
        for i in range(len(mat1)): 
            column = [] 
            for j in range(len(mat1[0].split())):
                val1 = int(mat1[i].split()[j])      
                val2 = int(mat2[i].split()[j])      
                result = val1 + val2
                column.append(result)
            row.append(column)
        for i in row : 
            for j in i :
                with open(o_file,'w') as final:
                    for i in row :
                        for j in i :
                            final.write(str(j)) 
                            final.write(' ') 
                        final.write('\n') 
    else :
        open(o_file,"w")

add_mat('mat1.txt','mat2.txt','outmat.txt')
add_mat('mat1.txt','mat3.txt','outmat1.txt')










    
