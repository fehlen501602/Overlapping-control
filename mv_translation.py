#This module implements a translation method for the measurement volume

import sys
import numpy
from stl import mesh
sys.path.append(r'/home/xxyfehlen501602/workspace/')
import find_max_min_points

def main(inputfile, tx, ty, tz):
   this_mesh = mesh.Mesh.from_file(inputfile)  
   for i in range(0, len(this_mesh.vectors)):
      for j in range(0, len(this_mesh.vectors[i])):
         this_mesh.vectors[i][j] = this_mesh.vectors[i][j] + numpy.array([tx, ty, tz])
   return this_mesh
