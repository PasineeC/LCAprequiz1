def power_equiv(watt):

    hp = watt / 745.7
    btum = watt / 0.293
    calm = watt * 14.33
    erg = watt * 1e7
    flbm = watt * 44.25

    return hp, btum, calm, erg, flbm

if __name__ == '__main__':

    pwatt = 100
    horsep, btuh, calmin, perg, footlbm = power_equiv(pwatt)

    print(pwatt, 'w = ', round(horsep,3), 'hp = ', round(btuh,3), 'btu/h =', round(calmin,3), 'cal/min =', round(perg,3), 'erg =', round(footlbm,3), 'f-lb/min')