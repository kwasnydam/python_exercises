def u_n(n):
    #u(n) = u(n - u(n-1)) + u(n - u(n-2))
    #if n <= 2:
    #    return 1
    #return u_n(n - u_n(n-1)) + u_n(n - u_n(n-2))
    #it turns out that recursive algorithm is not the greatest idea, even though it works
    pass

def build_u_list(num):
    u_list = list()
    u_list.append(1)
    u_list.append(1)
    for val in range(2,num):
        el = u_list[val - u_list[val - 1]] + u_list[val - u_list[val - 2]]
        u_list.append(el)
    return u_list

def length_sup_u_k(n, k):
    count = 0
    u_list = build_u_list(n)
    for i in range(1, n):
        if u_list[i] >= k:
            count += 1
        else:
            pass
    return count

def comp(n):
    count = 0
    u_list = build_u_list(n)
    for i in range(1, n):
        if u_list[i] < u_list[i-1]:
            count += 1
        else:
            pass
    return count
def main():
    #test_u_n -> its working
    #for n in range(1, 23):
    #    print('{}: {}'.format(n,u_n(n)))
    #print([build_u_list(150)])
    '''
    print('{} {} is {} should be {}'.format(50, 25, length_sup_u_k(50, 25), 2))
    print('{} {} is {} should be {}'.format(3332, 973, length_sup_u_k(3332, 973), 1391))
    print('{} {} is {} should be {}'.format(2941, 862, length_sup_u_k(2941, 862), 1246))
    '''
    print('{} is {} should be {}'.format(74626, comp(74626), 37128))
    print('{} is {} should be {}'.format(60441, comp(60441), 30054))

main()
