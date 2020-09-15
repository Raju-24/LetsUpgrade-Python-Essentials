'''
Taking input
'''
N = 5
checkprime(N)
def checkprime(num):
    '''
    prime or not function
    '''
    if num > 1:
        count_sum = 0
        for i in range(2, num):
            if num % i == 0:
                count_sum = count_sum + 1
        if count_sum == 1:
            print(num, "is prime")
