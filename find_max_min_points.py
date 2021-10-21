#This module calculates the extreme points for each input mesh model.

import numpy as np
from numpy import *

def find_max(model):
  maxarray = []
  a = model.vertices
  for i in range (0, 4):
    try:
     n = np.where(a==np.max(a,axis=0))[0]
     maxarray.append(a[n])
     maxarray[0] = np.unique(maxarray[0],axis=0)
     a = np.delete(a,n,0)
    except ValueError:
      pass
    continue
  try:
   return concatenate((maxarray[0], maxarray[1], maxarray[2], maxarray[3]),axis = 0)
  except IndexError:
    pass
  return concatenate((maxarray[0], maxarray[1], maxarray[2]),axis = 0)

def find_min(model):
  minarray = []
  a = model.vertices
  for i in range (0, 4):
    try:
     n = np.where(a==np.min(a,axis=0))[0]
     minarray.append(a[n])
     minarray[0] = np.unique(minarray[0],axis=0)
     a = np.delete(a,n,0)
    except ValueError:
      pass
    continue
  try:
   return concatenate((minarray[0], minarray[1],minarray[2],minarray[3]),axis = 0)
  except IndexError:
    pass
  return concatenate((minarray[0], minarray[1],minarray[2]),axis = 0)

#if __name__ == '__main__':
#  model=pymesh.load_mesh('/mnt/c/Users/fehle/test/overlappingtest/vpc_y_0/ssp_vpc_y_0_tcp.stl')
#  mv_1=pymesh.load_mesh('/mnt/c/Users/fehle/test/andere/mv_sp_y_1.stl')
#  mv_0=pymesh.load_mesh('/mnt/c/Users/fehle/test/andere/mv_sp_y_0.stl')
#print(find_max(model))
#print(find_min(model))
#print(find_max(mv_1))
#print(find_min(mv_1))
#print(find_max(mv_0))
#print(find_min(mv_0))
