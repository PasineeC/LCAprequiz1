import math #math.sqrt may be handy.

if __name__ == '__main__':
    N = int(input('Number of values:'))
    first_num = N
    list_number = []
    while N > 0:
        value = float(input('value:'))
        value_square = value ** 2
        N -= 1
        list_number.append(value_square)
    ss = sum(list_number)
    rms = math.sqrt(ss/first_num)
    print('RMS = {:,.2f}'.format(rms))