import ru_local as ru
rsd = input(ru.RESIDENT)
if rsd.lower() == 'да' or rsd.lower() == 'yes':
    a = input(ru.RES_Q_1)
    if a.lower() == 'да' or a.lower() == 'yes':
        print(ru.ANSWER, "9%")
    else:
        b = input(ru.RES_Q_2)
        if b.lower() == 'да' or b.lower() == 'yes':
            print(ru.ANSWER, "35%")
        else:
            c = input(ru.RES_Q_3)
            if c.lower() == 'да' or c.lower() == 'yes':
                print(ru.ANSWER, "35%")
            else:
                d = input(ru.RES_Q_4)
                if d.lower() == 'да' or d.lower() == 'yes':
                    print(ru.ANSWER, "35%")
                else:
                    e = input(ru.RES_Q_5)
                    if e.lower() == 'да' or e.lower() == 'yes':
                        print(ru.ANSWER, "13%")
                    else:
                        f = input(ru.RES_Q_6)
                        if f.lower() == 'да' or f.lower() == 'yes':
                            print(ru.ANSWER, "15% + 650 000", ru.CURRENCY)
                        else:
                            print(ru.ANSWER, "13%")
