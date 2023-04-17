import ru_local as ru
rsd = input(ru.RESIDENT)
if rsd in ['да', 'ДА', 'Да', 'дА']:
    a = input("res_q_1")
    if a.lower()=="да":
        print("answer", "9%")
    else:
        b = input("res_q_2")
        if b.lower()=="да":
            print("answer", "35%")
        else:
            c = input("res_q_3")
            if c.lower()=="да":
                print("answer", "35%")
            else:
                d = input("res_q_4")
                if d.lower()=="да":
                    print("answer", "35%")
                else:
                    e = input("res_q_5")
                    if e.lower()=="да":
                        print("answer", "13%")
                    else:
                        f = input("res_q_6")
                        if f.lower()=="да":
                            print("answer", "15% + 650 000", "currency")
                        else:
                            print("answer", "13%")
