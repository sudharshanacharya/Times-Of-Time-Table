def Spl(sub1, position):
    highest = max(sem5.pos_a, sem5.pos_b, sem5.pos_c)
    if highest in [0, 2, 4]:
        for loop in (highest - sem5.pos_a):
            if sem5.pos_a < highest:
                sub2 = get_one_sub(position)
                a.append(sub2)
                class_engaged[a_fac[sub2]] += 1
                a_hours[sub2] -= 1
                sem5.pos_a += 1

            if sem5.pos_b < highest:
                sub2 = get_one_sub(position)
                b.append(sub2)
                class_engaged[b_fac[sub2]] += 1
                b_hours[sub2] -= 1
                sem5.pos_b += 1

            if sem5.pos_c < highest:
                sub2 = get_one_sub(position)
                c.append(sub2)
                class_engaged[c_fac[sub2]] += 1
                c_hours[sub2] -= 1
                sem5.pos_c += 1

        for i in range(2):
            a.append(sub1)
            b.append(sub1)
            c.append(sub1)
            class_engaged[b_fac[sub1]] += 1
            sem5.pos_a += 1
            sem5.pos_b += 1
            sem5.pos_c += 1
            a_hours[sub1] -= 1
            b_hours[sub1] -= 1
            c_hours[sub1] -= 1
        return 0
    return 1
