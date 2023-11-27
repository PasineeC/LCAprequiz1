if __name__ == '__main__':

    capacity = float(input('Battery capacity (Wh):'))
    idle_mW = float(input('average power (idle, mW):'))
    norm_mW = float(input('average power (normal, mW):'))

    idle_W = idle_mW / 1000
    norm_W = norm_mW / 1000

    d_idle = capacity/idle_W
    d_norm = capacity/norm_W

    print('The battery will last %.0f hrs in idle mode.'%d_idle)
    print('The battery will last %.1f hrs in normal mode.'%d_norm)