import math 

def rec_to_pol(x,y):
    polar = math.sqrt(x**2 + y**2)
    degree = math.degrees(math.atan2(y, x))
    return polar, degree

if __name__ == '__main__':
    r, c = input('Enter (x y):').split()
    m, a = rec_to_pol(float(r), float(c))
    print("polar: {:.2f} with {:.2f} degree".format(m,a))

