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
    the function push_zero_for_total_length padding the blocks with n-1 zeros, 
    where n is the length of h[n] (filter coefficients)
    And finally return the array
'''
def push_zero_for_total_length(lst,time):
    out = []
    for x in lst:
        out.append(push_zero(x,time))
    return out

m,xn,n,hn,l = get()
xn_s = []
xn_s = splt(xn,l)
xn_sz = push_zero_for_total_length(xn_s,n-1)
hn_sz = push_zero(hn,len(xn_sz[0])-len(hn))
par_out = []

for j in xn_sz:
    par_out.append(convolution(j,hn_sz))
print(par_out,"Par")
full_out = []
length = len(par_out)
dummy = 0
z=0
front = 0
back = 0
one_lenght = len(par_out[0])
for i in range(length):
    if i == 0:
        if len(par_out) > 2:
            full_out.extend(par_out[i][:one_lenght-n+1])
        else:
            full_out.extend(par_out[i])
    if i == length-1:
        if len(par_out) > 2:
            full_out.extend(par_out[i])
        else:
            full_out = push_zero(full_out,l+n-1)
            block = []
            block = push_zero(block,l)
            block.extend(par_out[1])
            print(block,"blo")
            j = 0
            out = []
            for i in block:
                out.append(full_out[j] + i)
                j+=1
            full_out = out
    if i != 0 and i != length-1:
        z = 0
        front = 0
        back = 0
        for k in par_out[i]:
            if z > one_lenght - n:
                full_out.append(k + par_out[i+1][back])
                back+=1
                z+=1
            elif z < n-1:
                full_out.append(k + par_out[i-1][(one_lenght-n+1)+front])
                front += 1
                z+=1
            else:
                full_out.append(k)
                z+=1
print(xn_s,"\n",hn_sz,"\n",par_out)

print("Filtering long data sequence by overlap add method. \noutput: ")    
print(full_out)
