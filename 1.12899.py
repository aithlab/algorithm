# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 20:14:00 2022

@author: aithlab
"""

N = int(input())
S = []

for _ in range(N):
  T, X = map(int, input().split())
  
  if T == 1:
    S += [X]
    S = sorted(S)
  elif T == 2:
    val_removed = S.pop(X-1)
    print(val_removed)
  else:
    raise ValueError("The input type %d is not avaiable."%(T))   
