

def add_mat(f_matrix, s_matrix, result):
    with open(f_matrix,'r') as file:
        mat = file.readlines()
        row = len(mat)  
        column = len(mat[0].split())   
    return mat,row,column 

    
    
    with open(s_matrix,'r') as file:
        mat = file.readlines()
        row = len(mat)  
        column = len(mat[0].split())   
    return mat,row,column 

    row = []
    for i in range(len(f_matrix)):
        column = []
        for j in range(len(f_matrix[i].split())):
            val = int(f_matrix[i].split()[j]) + int(s_matrix[i].split()[j])
            column.append(val)
        row.append(column)
    print(row)



row = [] #สร้างลิสต์ไว้เก็บ ผลลัพธ์ที่บวกกัน ทุกแถว

#ให้ index ของ mat1 ออกมา คือ 0 และ 1
for i in range(len(mat1)):  

    #สร้างลิสต์ไว้เก็บ ผลลัพธ์ที่บวกกันแค่แถวเดียว
    column = []
    for j in range(len(mat1[i].split())):
        val = int(mat1[i].split()[j]) + int(mat2[i].split()[j])
        column.append(val)

    #นำแต่ละแถวเข้าไปอยู่ใน ลิสต์ row
    row.append(column)


with open("outmat.txt","w") as result:
    for i in row:
        for j in i:

            #เขียนแต่ละแถวลงไปในไฟล์ txt โดยให้มีช่องว่างและเว้นบรรทัดในแต่ละแถว
            result.write(str(j))
            result.write(' ')
        result.write('\n')


