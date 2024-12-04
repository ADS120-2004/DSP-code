'''
    This code will compute linear convolution for real values
      -> linear convolution is implemented using circular convolution
      -> This code uses martix method for circular convolution
    For easier understanding I divided the code into seperate functions
'''

'''
    time complexity = O(n^2) => O(m+n-1) => O(total_len^2)
    space compexity = O(n) => O(m+n-1) => O(total_len)
'''

'''
    This get() function is used to get input for user
    -> user should enter lenght of 
        1. length of input
        2. input array
        3. length of filter coefficients
        4. filter coefficients array
    And finally this function return all the input to the main function
'''
def get(): 
    mx = int(input("Enter the no of samples in input signals: "))
    xnx = [int(input()) for x in range(mx)]
    nx = int(input("Enter the no of samples in input signals: "))
    hnx = [int(input()) for x in range(nx)]
    return mx,xnx,nx,hnx


'''
    push_zero function is used to push zeros in the list, and return the final zeros appended list
'''
def push_zero(lst,times):
    for x in range(times):
        lst.append(0)
    return lst


'''
    correction(), this function is used to correct the length of input and filter cofficient array
    and it return the total length and corrected arrays
'''
def correction(m1,n1,l1,l2):
    total_len = m1 + n1 - 1
    if total_len > m1:
        l1 = push_zero(l1,total_len - m1)
    if total_len > n1:
        l2 = push_zero(l2,total_len - n1)
    return total_len,l1,l2


'''
    The initial() function is used to make the first array of filter coeffcient 
    example:
        consider length of filter cofficient array as n
        then the first array that need to be created is
            [h[0], h[n-1], h[n-2],......,h[n-n+1]]
    And finally this will return the array
'''
def initial(l1):
    l2 = []
    l2.append(l1[0])
    l3 = l1[1:]
    l2.extend(l3[::-1])   
    return l2


'''
     The rotate() function is used to rotate the array in anit-clockwise direction
'''
def rotate(l1):
    l2 = []
    l2.append(l1[-1])  
    l2.extend(l1[0:-1]) 
    return l2

m,xn,n,hn = get()
xn_c = []
hn_c = []
ans = []
total_len,xn_c,hn_c = correction(m,n,xn,hn)
final = initial(hn_c)
for x in range(total_len):
    temp = []
    for y in range(total_len):
        temp.append(final[y]*xn_c[y])
    ans.append(sum(temp))
    final = rotate(final)
    temp = []


'''
    The final Convolved answer will be stored in ans[] array
'''
print(ans)

