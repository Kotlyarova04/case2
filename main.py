import ru_local as ru
prd = input(ru.PERIOD)
if prd.lower() == 'да' or prd.lower() == 'yes':
    print(ru.RESIDENT)
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
else:
    question2 = input(ru.PRD_EXIT)
    if question2.lower() == 'нет' or question2.lower() == 'no':
        print(ru.NON_RESIDENT)
        question2_1 = input(ru.NONRES_Q_1)
        question2_1 = question2_1.strip('.,!?-:;_ ')
        if question2_1.lower() == 'да' or question2_1.lower() == 'yes':
            print(ru.ANSWER, '15%')
        else:
            question2_2 = input(ru.NONRES_Q_2)
            question2_2 = question2_2.strip('.,!?-:;_ ')
            if question2_2.lower() == 'да' or question2_2.lower() == 'yes':
                print(ru.ANSWER, '15%')
            else:
                question2_3 = input(ru.NONRES_Q_3)
                question2_3 = question2_3.strip('.,!?-:;_ ')
                if question2_3.lower() == 'да' or question2_3.lower() == 'yes':
                    print(ru.ANSWER, '5%')
                else:
                    question2_4 = input(ru.NONRES_Q_4)
                    question2_4 = question2_4.strip('.,!?-:;_ ')
                    if question2_4.lower() == 'да' or question2_4.lower() == 'yes':
                        question2_5 = input(ru.NONRES_Q_5)
                        question2_5 = question2_5.strip('.,!?-:;_ ')
                        if question2_5.lower() == 'да' or question2_5.lower() == 'yes':
                            print(ru.ANSWER, '15% + 650 000', ru.CURRENCY)
                        else:
                            print(ru.ANSWER, '13%')
                    else:
                        question2_6 = input(ru.NONRES_Q_6)
                        question2_6 = question2_6.strip('.,!?-:;_ ')
                        if question2_6.lower() == 'да' or question2_6.lower() == 'yes':
                            question2_5 = input(ru.NONRES_Q_5)
                            question2_5 = question2_5.strip('.,!?-:;_ ')
                            if question2_5.lower() == 'да' or question2_5.lower() == 'yes':
                                print(ru.ANSWER, '15% + 650 000', ru.CURRENCY)
                            else:
                                print(ru.ANSWER, '13%')
                        else:
                            print(ru.ANSWER, '30%')
    else:
        print(ru.DATES)

