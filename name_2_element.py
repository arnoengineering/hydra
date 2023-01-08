import pandas as pd
import numpy as np


def find_elm(sy):
    index_ls = np.where(df["Element Symbol"] == sy.title())
    if len(index_ls[0]) > 0:

        el = df.iloc[int(index_ls[0])]  # find corresponding freq
    else:
        el = []
    return el


def split_text(text):
    test = True
    newtext = text[:]
    let = text.pop(0)

    ret_el = find_elm(let)
    ret_n = name_ret[-1]
    name_cnt = len(name_ret)
    if len(ret_el) > 0:
        name_ret[-1].append(ret_el)
    else:
        test = False
    if len(text) > 0:
        split_text(text)
    else:
        print(f"\n\ntest 1end, text:{text}, let:{let}, namels:")
        print_elem(name_ret[-1])
        sum_el(name_ret[-1], test)
        print(f"\ntest 1end aft sum, text: {text}, let:{let},")

    # run with both
    if len(newtext) > 1:
        # print(f"test 2, text:{newtext}, let:{let}")
        let2 = "".join(newtext[:2])
        print(let2)
        newtext = newtext[2:]
        ret_elm2 = find_elm(let2)
        if len(ret_elm2) > 0:
            if len(name_ret) == 0:
                name_ret.append([])
            print_elem(name_ret[-1])
            print(test)
            if test:  # got one so new path
                name_ret.append(ret_n + [ret_elm2])
                print("dif ls")
                print_elem(name_ret[-1])
                print_elem(ret_n)
            else:
                name_ret[name_cnt-1].append(ret_elm2)
                print("same ls")
                print_elem(name_ret[-1])

            test = True
            if len(newtext) > 0:
                split_text(newtext)
            else:
                print(f"\n\ntest 2, text:{newtext}, let:{let2}, namels: ")
                print_elem(name_ret[-1])
                sum_el(name_ret[-1], test)
                print(f"\ntest 2 aft sum, text:{newtext}, let:{let2},")
        else:
            test = False
    if not test:
        print('pop')
        name_ret.pop()


def print_elem(ls, pr=True):
    ls_out = [(x['Element Name'], x['Element Atomic number']) for x in ls]
    if pr:
        print(ls_out)


def print_deb(cnt, split, num, cur, let):
    print(f'test: {cnt}, let:{let}, text:{cur}')
    print(f"\n\ntest 1end,  namels:")
    print_elem(name_ret[-1])


def sum_el(ls, in_x):
    # ret_x = in_x
    ls_out = [x['Element Symbol'] for x in ls]
    ls_out_n = "".join(ls_out).upper()
    if ls_out_n != name.upper():
        print('remove, ', ls_out)
        name_ret.pop()
    else:
        print('left', ls_out)
    #     ret_x = False
    # return ret_x


df = pd.read_excel("element_list.xlsx")


tab_ls = []
name_ret = [[]]
name = "Arno"
split_text(list(name.upper()))
print("\n\nfinal")
for i in name_ret:
    print_elem(i)
