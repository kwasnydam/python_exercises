'''
Bob is preparing to pass IQ test.
The most frequent task in this test is to find out which one of the given
numbers differs from the others.
Bob observed that one number usually differs from the others in evenness.
Help Bob — to check his answers, he needs a program that among the given numbers
finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)
'''

def iq_test(numbers):
    #print(numbers)
    index = 1
    even = {'count': 0,'index' :1}
    odd = {'count': 0,'index' :1}
    #print([num in numbers.split])
    for number in numbers.split():
        #print(number)
        if int(number)%2:
            even['count'] += 1
            even['index'] = index
        else:
            odd['count'] += 1
            odd['index'] = index
        index += 1
    if odd['count'] == 1:
        return odd['index']
    else:
        return even['index']



#Test.assert_equals(iq_test("2 4 7 8 10"),3)
#Test.assert_equals(iq_test("1 2 2"), 1)
def main():
    print('Is {} should be {}'.format(iq_test("2 4 7 8 10"), 3))
    print('Is {} should be {}'.format(iq_test("1 2 2"), 1))
    print('Is {} should be {}'.format(iq_test("1 3 4 9 113 111"), 3))

main()
