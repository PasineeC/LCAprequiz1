if __name__ == '__main__':
    operating = 12
    capacity_mAh = float(input('Battery capacity (mAh):'))
    capacity_Ah = capacity_mAh / 1000
    Wh = capacity_Ah * operating

    print('At its 12 V rating, it stores %.2f Wh.'%Wh)