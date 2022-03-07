#!/usr/bin/env python
# coding: utf-8

# This file contains python code, which generates and verifies a counterexample to Brualdi and Csima's Conjecture.

import numpy as np

# -------------
# INPUT
# linearform2: a 3 by n matrix, with entries -1, 0, 1.
# nonnegsupport: a subset of [n]^3
# i: an integer between 0 and 2, inclusive.
# j: an integer between 0 and n-1, inclusive.
# n: a positive integer.
# -------------
# OUTPUT
# true or false
# -------------
# DESCRIPTION
# The matrix linearform2 represents a function on [n]^3. Let e_ij denote the basis matrix with 1 in the entry of the i+1-th
# row and j+1-th column, and 0 everywhere else. Then, e_ij(nonnegsupport) is the number of elements of nonnegsupport whose 
# i-th coordinate is equal to j (here the indexing is 0-based, as in the code). We extend this definition by linearity to 
# arbitrary 3 by n matrices. checkformhelper outputs true if for any 3 by n matrix M whose entries are in {1,0,-1}, sum to
# zero, and satisfies for any a<i+1 or (a=i+1 and b<=j+1) M[a,b]=linearform2[a,b], the function represented by M is strictly 
# negative when evaluated on nonnegsupport and is not identically zero on [n]^3.

def checkformhelper(linearform2,nonnegsupport,i,j,n):
    # Case where i+1=3 and j+1=n, so that there is only one matrix M satisfying the description. We perform the check on M.
    if(i==2 and j==n-1):
        # Check entries sum to zero
        total=0
        for k1 in range(0,3):
            for k2 in range(0,n):
                total += linearform2[k1][k2]
        if total != 0:
            return true
        # Check if the function represented by linearform2 is identically zero on [n]^3
        identicallyzero=true
        for k1 in range(n):
            if(identicallyzero==false):
                break;
            for k2 in range(n):
                if(identicallyzero==false):
                    break;
                for k3 in range(n):
                    if(linearform2[0][k1]+linearform2[1][k2]+linearform2[2][k3] != 0):
                        identicallyzero=false
        if(identicallyzero):
            return true
        # Check if the function represented by linearform2 is strictly negative when evaluated on nonnegsupport
        for (k1,k2,k3) in nonnegsupport:
            if(linearform2[0][k1]+linearform2[1][k2]+linearform2[2][k3] < 0):
                return true
        return false
    # In the case where not only one matrix M satisfying the description, we specify the "next" entry of linearform2 (again,
    # is in lexicographical order).
    if(j==n-1):
    
        result = true
        linearform2[i+1][0]=-1
        if(checkformhelper(linearform2,nonnegsupport,i+1,0,n)==false):
            result = false
            return result
        linearform2[i+1][0]=0
        if(checkformhelper(linearform2,nonnegsupport,i+1,0,n)==false):
            result = false
            return result
        linearform2[i+1][0]=1
        if(checkformhelper(linearform2,nonnegsupport,i+1,0,n)==false):
            result = false
            return result
        return result
    if(j!=n-1):
        result = true
        linearform2[i][j+1]=-1
        if(checkformhelper(linearform2,nonnegsupport,i,j+1,n)==false):
            result = false
            return result
        linearform2[i][j+1]=0
        if(checkformhelper(linearform2,nonnegsupport,i,j+1,n)==false):
            result = false
            return result
        linearform2[i][j+1]=1
        if(checkformhelper(linearform2,nonnegsupport,i,j+1,n)==false):
            result = false
            return result
        return result
    return true

# -------------
# INPUT
# n: a positive integer
# nonnegsupport: a subset of [n]^3
# -------------
# OUTPUT
# true or false
# -------------
# DESCRIPTION
# The matrix linearform2 represents a function on [n]^3. Let e_ij denote the basis matrix with 1 in the entry of the i+1-th
# row and j+1-th column, and 0 everywhere else. Then, e_ij(nonnegsupport) is the number of elements of nonnegsupport whose 
# i-th coordinate is equal to j (here the indexing is 0-based, as in the code). We extend this definition by linearity to 
# arbitrary 3 by n matrices. checkform outputs true if for any 3 by n matrix M whose entries are in {1,0,-1} and sum to zero,
# the function represented by M is strictly negative when evaluated on nonnegsupport and is not identically zero on [n]^3. 
def checkform(n, nonnegsupport):
    linearform2 = np.zeros((3,n))
    # Use the recursive helper function to check every possible case.
    return checkformhelper(linearform2,nonnegsupport,-1,n-1,n)

# -------------
# Main block
import numpy as np
linearform = [[-2,-1,0,1,2],[-2,-1,0,1,2],[-2,-1,0,1,2]]
# We create a subset of [n]^3, nonnegsupport. By design, linearform is nonnegative when evaluated on nonnegsupport.
n = len(linearform[0])
nonnegsupport = []
for i in range(n):
    for j in range(n):
        for k in range(n):
            if(linearform[0][i]+linearform[1][j]+linearform[2][k] >= 0):
                nonnegsupport.append((i,j,k))
# This will be a counterexample if this prints true
print(checkform(n, nonnegsupport))

