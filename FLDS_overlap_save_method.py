'''
    This code will do filtering of long data sequence using Overlap add method
      -> linear convolution is implemented using circular convolution
      -> This code uses martix method for circular convolution
    For easier understanding I divided the code into seperate functions
'''

'''
    time complexity = O(m*x*l)
    space compexity = O(mx+nx) 
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

import numpy as np

def get(): 
    mx = int(input("Enter the no of samples in input signals: "))
    xnx = [int(input()) for x in range(mx)]
    nx = int(input("Enter the no of filter coefficinets: "))
    hnx = [int(input()) for x in range(nx)]
    l = int(input("Enter block lenght of input: "))
    return mx,xnx,nx,hnx,l


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

'''
    The convolution function is used to convolve the block of input with h[n] and return the convolved output as array
'''
def convolution(xn,hn):
    xn_c = xn
    hn_c = hn
    ans = []
    total_len = len(xn)
    final = initial(hn_c)
    for x in range(total_len):
        temp = []
        for y in range(total_len):
            temp.append(final[y]*xn_c[y])
        ans.append(sum(temp))
        final = rotate(final)
        temp = []
    return ans

'''
    The function splt, splits the input into block, with each block length l
    And finally return the blocks of input in array of array format
        example: [[1,2],[3,4],.....,[89,7]]
     note:
        this function will automatically append zeros to the final block to match the block length
'''
def splt(xn,l):
    lngth = len(xn)
    rem = lngth%l
    if rem == 0:
        split_list = [xn[i:i + l] for i in range(0, lngth, l)]
    else:
        split_list = [xn[i:i + l] for i in range(0, len(xn), l)]
        last = split_list.pop()
        split_list.append(push_zero(last,l-len(last)))
    return split_list

'''
    the function push_to_first_of_x_block will creates the blocks of input, 
    where n is the length of h[n] (filter coefficients)
    And finally return the array
'''
def push_to_first_of_x_block(xn_s,n,l):
    block = []
    ans = []
    block = push_zero(block,n-1)
    block.extend(xn_s[:l])
    ans.append(block)
    f = 1
    i = 1
    count = 0
    block = []
    sat = 0
    for j in xn_s[l:]:
        if f == 1:
            block.extend(ans[i-1][-(n-1):])
            f=0
        block.append(j)
        count += 1
        if count == l and len(xn_sz) > l:
            ans.append(block)
            block = []
            count = 0
            f = 1
            sat = 1
    if sat == 0:
        if len(block) < l+n-1:
            block = push_zero(block, (l+n-1) - len(block))
        ans.append(block)
    return ans
'''
    this fuction will check wheter the last blocks last n-1 elements are non-zeros or zeros
    if zeros no problem
    if non-zeros, then it will create a new block with that last n-1 elements and return the final array
'''
def check(xn_sz,n,l):
    last = xn_sz[-1]
    con = 0
    for i in last[-(n-1):]:
        if i == 0:
            con+=1
    if con == n-1:
        pass
    elif con != n-1:
        block = []
        block.extend(last[-(n-1):])
        block = push_zero(block,l)
        xn_sz.append(block)
    return xn_sz


m,xn,n,hn,l = get()
xn_s = []
xn_s = splt(xn,l)
xn_sz = push_to_first_of_x_block(xn,n,l)
xn_sz = check(xn_sz,n,l)
hn_sz = push_zero(hn,len(xn_sz[0])-len(hn))
par_out = []
for j in xn_sz:
    par_out.append(convolution(j,hn_sz))
print("Convolved output for each blocks: ",par_out)
full_out = []
for i in par_out:
    for j in i[n-1:]:
        full_out.append(j)
print("Filtering long data sequence by overlap add method.")
print("Convolved output of x[n] i.e, input: ",full_out)
