from pip._vendor.msgpack.fallback import xrange

a = 'bcjkkkvbvsdvovscy'
target = 'boy'
target2 = '123456'


def is_in(x, ta):
    flag = []
    for i in xrange(len(ta)):
        flag.append(0)

    count = 0
    list_ta = list(ta)
    for tt in list_ta:
        # print('tt = ',tt)
        if tt in x:
            flag[count] = 1
        count += 1

    return flag


def charge_flag(flag):  # list flag 全是1 才满足要求
    flag_count = 0
    for f1 in flag:
        if f1 == 1:
            flag_count += 1

    if flag_count < len(flag):
        return False
    if flag_count == len(flag):
        return True


def print_my(x, ta):
    bool_my = charge_flag(is_in(x, ta))
    if bool_my:
        print("%s 在 %s 中" % (ta, x))
    else:
        print("%s 不在 %s 中" % (ta, x))


# print(is_in(a,target))
# print(is_in(a,target2))
print_my(a, target)
print_my(a, target2)
