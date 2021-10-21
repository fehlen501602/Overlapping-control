#It is tasked with compiling configuration rules and apply them on the models

import trimesh
import pymesh
import numpy as np
import sys
sys.path.append(r'/home/xxyfehlen501602/workspace/')
import mv_translation
import find_max_min_points
import max_min_y_array
import get_model


#GM_zmax
def configu_z_max(inputfile_1, inputfile_2, inputfile_3): #inputfile_1: global overlapping measurement volume; inputfile_2: solution space; inputfile_3: measurement volume
    global_omv = trimesh.load_mesh(inputfile_1)
    ssp = trimesh.load_mesh(inputfile_2)
    a = find_max_min_points.find_max(pymesh.load_mesh(inputfile_1))# find max in all directions
    e = find_max_min_points.find_min(pymesh.load_mesh(inputfile_1))
    gom_max_z = np.where(a[:, 2:]==np.max(a[:, 2:],axis=0))[0] # gom_max_z
    gom_min_z = np.where(e[:, 2:]==np.min(e[:, 2:],axis=0))[0] # gom_min_z
    index = np.where(a[:, 2:]==np.max(a[:, 2:],axis=0))[0]# index of z_max
    for i in range (0, 3):
     b = np.delete(a,index,0)
     index = np.union1d(index, np.where(a[:, 2:]==np.max(b[:, 2:],axis=0))[0])
    min_y_array = max_min_y_array.find_min_y_array(inputfile_3)
    max_y_array = max_min_y_array.find_max_y_array(inputfile_3)
    c = find_max_min_points.find_max(pymesh.load_mesh(inputfile_2))
    d = find_max_min_points.find_min(pymesh.load_mesh(inputfile_2))
    ssp_max_y = np.where(c[:, 1:2]==np.max(c[:, 1:2],axis=0))[0]
    ssp_max_z = np.where(c[:, 2:]==np.max(c[:, 2:],axis=0))[0]
    ssp_min_z = np.where(d[:, 2:]==np.min(d[:, 2:],axis=0))[0]   
    for i in range (0,index.size):
      if a[gom_max_z][0][2] > c[ssp_max_z][0][2] and e[gom_min_z][0][2] < d[ssp_min_z][0][2]:
            if a[index][i][1] < ssp.center_mass[1]:
              if a[index][i][0] > ssp.center_mass[0]:
                tx = a[index][i][0]-min_y_array[2][0] #GM z_max
                ty = a[index][i][1]-min_y_array[2][1]
                tz = a[index][i][2]-min_y_array[2][2]
                outputfile = inputfile_3[:-4] + '-configu_z_max%i.stl' % i
                mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
              else:
                tx = a[index][i][0]-min_y_array[0][0] #GM z_max
                ty = a[index][i][1]-min_y_array[0][1]
                tz = a[index][i][2]-min_y_array[0][2]
                outputfile = inputfile_3[:-4] + '-configu_z_max%i.stl' % i
                mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
            else:
              if a[index][i][0] > ssp.center_mass[0]:
                if a[index][i][1] > c[ssp_max_y][0][1]:
                 tx = a[index][i][0]-max_y_array[1][0] #GM z_max
                 ty = a[index][i][1]-max_y_array[1][1]
                 tz = a[index][i][2]-max_y_array[1][2]
                 outputfile = inputfile_3[:-4] + '-configu_z_max%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                else:
                 tx = a[index][i][0]-min_y_array[2][0] #GM z_max
                 ty = a[index][i][1]-min_y_array[2][1]
                 tz = a[index][i][2]-min_y_array[2][2]
                 outputfile = inputfile_3[:-4] + '-configu_z_max%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)                  
              else:
                if a[index][i][1] > c[ssp_max_y][0][1]:
                 tx = a[index][i][0]-max_y_array[3][0] #GM z_max
                 ty = a[index][i][1]-max_y_array[3][1]
                 tz = a[index][i][2]-max_y_array[3][2]
                 outputfile = inputfile_3[:-4] + '-configu_z_max%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                else:
                 tx = a[index][i][0]-min_y_array[0][0] #GM z_max
                 ty = a[index][i][1]-min_y_array[0][1]
                 tz = a[index][i][2]-min_y_array[0][2]
                 outputfile = inputfile_3[:-4] + '-configu_z_max%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
      elif a[gom_max_z][0][2] < c[ssp_max_z][0][2] and e[gom_min_z][0][2] < d[ssp_min_z][0][2]:
          if a[index][i][1] < ssp.center_mass[1]:
             if a[index][i][0] > ssp.center_mass[0]:
                 tx = a[index][i][0]-min_y_array[3][0] #GM z_max
                 ty = a[index][i][1]-min_y_array[3][1]
                 tz = a[index][i][2]-min_y_array[3][2]
                 outputfile = inputfile_3[:-4] + '-configu_z_max%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
             else:
                 tx = a[index][i][0]-min_y_array[1][0] #GM z_max
                 ty = a[index][i][1]-min_y_array[1][1]
                 tz = a[index][i][2]-min_y_array[1][2]
                 outputfile = inputfile_3[:-4] + '-configu_z_max%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
          else:
            if a[index][i][1] > c[ssp_max_y][0][1]:
              if a[index][i][0] > ssp.center_mass[0]:
                 tx = a[index][i][0]-max_y_array[0][0] #GM z_max
                 ty = a[index][i][1]-max_y_array[0][1]
                 tz = a[index][i][2]-max_y_array[0][2]
                 outputfile = inputfile_3[:-4] + '-configu_z_max%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
              else:
                 tx = a[index][i][0]-max_y_array[2][0] #GM z_max
                 ty = a[index][i][1]-max_y_array[2][1]
                 tz = a[index][i][2]-max_y_array[2][2]
                 outputfile = inputfile_3[:-4] + '-configu_z_max%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
            else:
              if a[index][i][0] > ssp.center_mass[0]:
                 tx = a[index][i][0]-min_y_array[3][0] #GM z_max
                 ty = a[index][i][1]-min_y_array[3][1]
                 tz = a[index][i][2]-min_y_array[3][2]
                 outputfile = inputfile_3[:-4] + '-configu_z_max%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
              else:
                 tx = a[index][i][0]-min_y_array[1][0] #GM z_max
                 ty = a[index][i][1]-min_y_array[1][1]
                 tz = a[index][i][2]-min_y_array[1][2]
                 outputfile = inputfile_3[:-4] + '-configu_z_max%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)        
      elif a[gom_max_z][0][2] > c[ssp_max_z][0][2] and e[gom_min_z][0][2] > d[ssp_min_z][0][2]:                      
          if a[index][i][1] < ssp.center_mass[1]:
             if a[index][i][0] > ssp.center_mass[0]:
                 tx = a[index][i][0]-min_y_array[2][0] #GM z_max
                 ty = a[index][i][1]-min_y_array[2][1]
                 tz = a[index][i][2]-min_y_array[2][2]
                 outputfile = inputfile_3[:-4] + '-configu_z_max%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
             else:
                 tx = a[index][i][0]-min_y_array[0][0] #GM z_max
                 ty = a[index][i][1]-min_y_array[0][1]
                 tz = a[index][i][2]-min_y_array[0][2]
                 outputfile = inputfile_3[:-4] + '-configu_z_max%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
          else:
            if a[index][i][1] > c[ssp_max_y][0][1]:
              if a[index][i][0] > ssp.center_mass[0]:
                 tx = a[index][i][0]-max_y_array[1][0] #GM z_max
                 ty = a[index][i][1]-max_y_array[1][1]
                 tz = a[index][i][2]-max_y_array[1][2]
                 outputfile = inputfile_3[:-4] + '-configu_z_max%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
              else:
                 tx = a[index][i][0]-max_y_array[3][0] #GM z_max
                 ty = a[index][i][1]-max_y_array[3][1]
                 tz = a[index][i][2]-max_y_array[3][2]
                 outputfile = inputfile_3[:-4] + '-configu_z_max%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)    
            else:
              if a[index][i][0] > ssp.center_mass[0]:
                 tx = a[index][i][0]-min_y_array[2][0] #GM z_max
                 ty = a[index][i][1]-min_y_array[2][1]
                 tz = a[index][i][2]-min_y_array[2][2]
                 outputfile = inputfile_3[:-4] + '-configu_z_max%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
              else:
                 tx = a[index][i][0]-min_y_array[0][0] #GM z_max
                 ty = a[index][i][1]-min_y_array[0][1]
                 tz = a[index][i][2]-min_y_array[0][2]
                 outputfile = inputfile_3[:-4] + '-configu_z_max%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)                 



#GM_zmin
def configu_z_min(inputfile_1, inputfile_2, inputfile_3): #inputfile_1: global overlapping measurement volume; inputfile_2: solution space; inputfile_3: measurement volume
    global_omv = trimesh.load_mesh(inputfile_1)
    ssp = trimesh.load_mesh(inputfile_2)
    a = find_max_min_points.find_min(pymesh.load_mesh(inputfile_1))# find min in all directions
    e = find_max_min_points.find_max(pymesh.load_mesh(inputfile_1))
    gom_max_z = np.where(e[:, 2:]==np.max(e[:, 2:],axis=0))[0] # gom_max_z
    gom_min_z = np.where(a[:, 2:]==np.min(a[:, 2:],axis=0))[0] # gom_min_z
    index = np.where(a[:, 2:]==np.min(a[:, 2:],axis=0))[0]# index of z_min
    for i in range (0, 3):
     b = np.delete(a,index,0)
     index = np.union1d(index, np.where(a[:, 2:]==np.min(b[:, 2:],axis=0))[0])
    min_y_array = max_min_y_array.find_min_y_array(inputfile_3)
    max_y_array = max_min_y_array.find_max_y_array(inputfile_3)
    c = find_max_min_points.find_max(pymesh.load_mesh(inputfile_2))
    d = find_max_min_points.find_min(pymesh.load_mesh(inputfile_2))
    ssp_max_y = np.where(c[:, 1:2]==np.max(c[:, 1:2],axis=0))[0]
    ssp_max_z = np.where(c[:, 2:]==np.max(c[:, 2:],axis=0))[0]
    ssp_min_z = np.where(d[:, 2:]==np.min(d[:, 2:],axis=0))[0]        
    for i in range (0,index.size):
      if e[gom_max_z][0][2] > c[ssp_max_z][0][2] and a[gom_min_z][0][2] < d[ssp_min_z][0][2]:
            if a[index][i][1] < ssp.center_mass[1]:
              if a[index][i][0] > ssp.center_mass[0]:
                tx = a[index][i][0]-min_y_array[3][0] #GM z_min
                ty = a[index][i][1]-min_y_array[3][1]
                tz = a[index][i][2]-min_y_array[3][2]
                outputfile = inputfile_3[:-4] + '-configu_z_min%i.stl' % i
                mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
              else:
                tx = a[index][i][0]-min_y_array[1][0] #GM z_min
                ty = a[index][i][1]-min_y_array[1][1]
                tz = a[index][i][2]-min_y_array[1][2]
                outputfile = inputfile_3[:-4] + '-configu_z_min%i.stl' % i
                mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
            else:
              if a[index][i][0] > ssp.center_mass[0]:
                if a[index][i][1] > c[ssp_max_y][0][1]:
                 tx = a[index][i][0]-max_y_array[0][0] #GM z_min
                 ty = a[index][i][1]-max_y_array[0][1]
                 tz = a[index][i][2]-max_y_array[0][2]
                 outputfile = inputfile_3[:-4] + '-configu_z_min%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                else:
                 tx = a[index][i][0]-min_y_array[3][0] #GM z_min
                 ty = a[index][i][1]-min_y_array[3][1]
                 tz = a[index][i][2]-min_y_array[3][2]
                 outputfile = inputfile_3[:-4] + '-configu_z_min%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)    
              else:
                if a[index][i][1] > c[ssp_max_y][0][1]:
                 tx = a[index][i][0]-max_y_array[2][0] #GM z_min
                 ty = a[index][i][1]-max_y_array[2][1]
                 tz = a[index][i][2]-max_y_array[2][2]
                 outputfile = inputfile_3[:-4] + '-configu_z_min%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                else:
                 tx = a[index][i][0]-min_y_array[1][0] #GM z_min
                 ty = a[index][i][1]-min_y_array[1][1]
                 tz = a[index][i][2]-min_y_array[1][2]
                 outputfile = inputfile_3[:-4] + '-configu_z_min%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)                  
      elif e[gom_max_z][0][2] < c[ssp_max_z][0][2] and a[gom_min_z][0][2] < d[ssp_min_z][0][2]:
          if a[index][i][1] < c[ssp_max_y][0][1]:  
             if a[index][i][0] > ssp.center_mass[0]:
                 tx = a[index][i][0]-min_y_array[3][0] #GM z_min
                 ty = a[index][i][1]-min_y_array[3][1]
                 tz = a[index][i][2]-min_y_array[3][2]
                 outputfile = inputfile_3[:-4] + '-configu_z_min%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
             else:
                 tx = a[index][i][0]-min_y_array[1][0] #GM z_min
                 ty = a[index][i][1]-min_y_array[1][1]
                 tz = a[index][i][2]-min_y_array[1][2]
                 outputfile = inputfile_3[:-4] + '-configu_z_min%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
          else:
             if a[index][i][0] > ssp.center_mass[0]:
                 tx = a[index][i][0]-max_y_array[0][0] #GM z_min
                 ty = a[index][i][1]-max_y_array[0][1]
                 tz = a[index][i][2]-max_y_array[0][2]
                 outputfile = inputfile_3[:-4] + '-configu_z_min%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
             else:
                 tx = a[index][i][0]-max_y_array[2][0] #GM z_min
                 ty = a[index][i][1]-max_y_array[2][1]
                 tz = a[index][i][2]-max_y_array[2][2]
                 outputfile = inputfile_3[:-4] + '-configu_z_min%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)        
      elif e[gom_max_z][0][2] > c[ssp_max_z][0][2] and a[gom_min_z][0][2] > d[ssp_min_z][0][2]:
        if a[index][i][1] < c[ssp_max_y][0][1]:
            if a[index][i][0] > ssp.center_mass[0]:
                tx = a[index][i][0]-min_y_array[2][0] #GM z_min
                ty = a[index][i][1]-min_y_array[2][1]
                tz = a[index][i][2]-min_y_array[2][2]
                outputfile = inputfile_3[:-4] + '-configu_z_min%i.stl' % i
                mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
            else:
                tx = a[index][i][0]-min_y_array[0][0] #GM z_min
                ty = a[index][i][1]-min_y_array[0][1]
                tz = a[index][i][2]-min_y_array[0][2]
                outputfile = inputfile_3[:-4] + '-configu_z_min%i.stl' % i
                mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
        else:
            if a[index][i][0] > ssp.center_mass[0]:
                tx = a[index][i][0]-max_y_array[1][0] #GM z_min
                ty = a[index][i][1]-max_y_array[1][1]
                tz = a[index][i][2]-max_y_array[1][2]
                outputfile = inputfile_3[:-4] + '-configu_z_min%i.stl' % i
                mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
            else:
                tx = a[index][i][0]-max_y_array[3][0] #GM z_min
                ty = a[index][i][1]-max_y_array[3][1]
                tz = a[index][i][2]-max_y_array[3][2]
                outputfile = inputfile_3[:-4] + '-configu_z_min%i.stl' % i
                mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)


#GM_xmax
def configu_x_max(inputfile_1, inputfile_2, inputfile_3):
    global_omv = trimesh.load_mesh(inputfile_1)
    ssp = trimesh.load_mesh(inputfile_2)
    a = find_max_min_points.find_max(pymesh.load_mesh(inputfile_1))# find max in all directions
    e = find_max_min_points.find_min(pymesh.load_mesh(inputfile_1))
    gom_max_z = np.where(a[:, 2:]==np.max(a[:, 2:],axis=0))[0] # gom_max_z
    gom_min_z = np.where(e[:, 2:]==np.min(e[:, 2:],axis=0))[0] # gom_min_z
    index = np.where(a[:, :1]==np.max(a[:, :1],axis=0))[0]# index of x_max
    for i in range (0, 3):
     b = np.delete(a,index,0)
     index = np.union1d(index, np.where(a[:, :1]==np.max(b[:, :1],axis=0))[0])
    c = find_max_min_points.find_max(pymesh.load_mesh(inputfile_2))
    d = find_max_min_points.find_min(pymesh.load_mesh(inputfile_2))
    ssp_max_y = np.where(c[:, 1:2]==np.max(c[:, 1:2],axis=0))[0]
    ssp_max_z = np.where(c[:, 2:]==np.max(c[:, 2:],axis=0))[0]
    ssp_min_z = np.where(d[:, 2:]==np.min(d[:, 2:],axis=0))[0]        
    min_y_array = max_min_y_array.find_min_y_array(inputfile_3)
    max_y_array = max_min_y_array.find_max_y_array(inputfile_3)
    for i in range (0, index.size):
      if a[gom_max_z][0][2] > c[ssp_max_z][0][2] and e[gom_min_z][0][2] < d[ssp_min_z][0][2]:
            if a[index][i][0] > ssp.center_mass[0]:
                if a[index][i][1] < ssp.center_mass[1]:
                    if a[index][i][2] > ssp.center_mass[2]:
                      tx = a[index][i][0]-min_y_array[2][0] #GM x_max
                      ty = a[index][i][1]-min_y_array[2][1]
                      tz = a[index][i][2]-min_y_array[2][2]
                      outputfile = inputfile_3[:-4] + '-configu_x_max%i.stl' % i
                      mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                    else:
                      tx = a[index][i][0]-min_y_array[3][0] #GM x_max
                      ty = a[index][i][1]-min_y_array[3][1]
                      tz = a[index][i][2]-min_y_array[3][2]
                      outputfile = inputfile_3[:-4] + '-configu_x_max%i.stl' % i
                      mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                else:
                  if a[index][i][1] > c[ssp_max_y][0][1]:
                    if a[index][i][2] > ssp.center_mass[2]:
                      tx = a[index][i][0]-max_y_array[1][0] #GM x_max
                      ty = a[index][i][1]-max_y_array[1][1]
                      tz = a[index][i][2]-max_y_array[1][2]
                      outputfile = inputfile_3[:-4] + '-configu_x_max%i.stl' % i
                      mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                    else:
                      tx = a[index][i][0]-max_y_array[0][0] #GM x_max
                      ty = a[index][i][1]-max_y_array[0][1]
                      tz = a[index][i][2]-max_y_array[0][2]
                      outputfile = inputfile_3[:-4] + '-configu_x_max%i.stl' % i
                      mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                  else:
                    if a[index][i][2] > ssp.center_mass[2]:
                      tx = a[index][i][0]-min_y_array[2][0] #GM x_max
                      ty = a[index][i][1]-min_y_array[2][1]
                      tz = a[index][i][2]-min_y_array[2][2]
                      outputfile = inputfile_3[:-4] + '-configu_x_max%i.stl' % i
                      mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                    else:
                      tx = a[index][i][0]-min_y_array[3][0] #GM x_max
                      ty = a[index][i][1]-min_y_array[3][1]
                      tz = a[index][i][2]-min_y_array[3][2]
                      outputfile = inputfile_3[:-4] + '-configu_x_max%i.stl' % i
                      mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)                    
            else:
                if a[index][i][1] < ssp.center_mass[1]:
                    if a[index][i][2] > ssp.center_mass[2]:
                      tx = a[index][i][0]-min_y_array[0][0] #GM x_max
                      ty = a[index][i][1]-min_y_array[0][1]
                      tz = a[index][i][2]-min_y_array[0][2]
                      outputfile = inputfile_3[:-4] + '-configu_x_max%i.stl' % i
                      mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                    else:
                      tx = a[index][i][0]-min_y_array[1][0] #GM x_max
                      ty = a[index][i][1]-min_y_array[1][1]
                      tz = a[index][i][2]-min_y_array[1][2]
                      outputfile = inputfile_3[:-4] + '-configu_x_max%i.stl' % i
                      mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                else:
                    if a[index][i][2] > ssp.center_mass[2]:
                      tx = a[index][i][0]-max_y_array[3][0] #GM x_max
                      ty = a[index][i][1]-max_y_array[3][1]
                      tz = a[index][i][2]-max_y_array[3][2]
                      outputfile = inputfile_3[:-4] + '-configu_x_max%i.stl' % i
                      mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                    else:
                      tx = a[index][i][0]-max_y_array[2][0] #GM x_max
                      ty = a[index][i][1]-max_y_array[2][1]
                      tz = a[index][i][2]-max_y_array[2][2]
                      outputfile = inputfile_3[:-4] + '-configu_x_max%i.stl' % i
                      mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)                    
      elif a[gom_max_z][0][2] < c[ssp_max_z][0][2] and e[gom_min_z][0][2] < d[ssp_min_z][0][2]:
            if a[index][i][1] < ssp.center_mass[1]:
              if a[index][i][0] > ssp.center_mass[0]:
                 tx = a[index][i][0]-min_y_array[3][0] #GM x_max
                 ty = a[index][i][1]-min_y_array[3][1]
                 tz = a[index][i][2]-min_y_array[3][2]
                 outputfile = inputfile_3[:-4] + '-configu_x_max%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
              else:
                 tx = a[index][i][0]-min_y_array[1][0] #GM x_max
                 ty = a[index][i][1]-min_y_array[1][1]
                 tz = a[index][i][2]-min_y_array[1][2]
                 outputfile = inputfile_3[:-4] + '-configu_x_max%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
            else:
               if a[index][i][1] > c[ssp_max_y][0][1]:
                  if a[index][i][0] > ssp.center_mass[0]:
                     tx = a[index][i][0]-max_y_array[0][0] #GM x_max
                     ty = a[index][i][1]-max_y_array[0][1]
                     tz = a[index][i][2]-max_y_array[0][2]
                     outputfile = inputfile_3[:-4] + '-configu_x_max%i.stl' % i
                     mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                  else:
                     tx = a[index][i][0]-max_y_array[2][0] #GM x_max
                     ty = a[index][i][1]-max_y_array[2][1]
                     tz = a[index][i][2]-max_y_array[2][2]
                     outputfile = inputfile_3[:-4] + '-configu_x_max%i.stl' % i
                     mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
               else:
                  if a[index][i][0] > ssp.center_mass[0]:
                     tx = a[index][i][0]-min_y_array[3][0] #GM x_max
                     ty = a[index][i][1]-min_y_array[3][1]
                     tz = a[index][i][2]-min_y_array[3][2]
                     outputfile = inputfile_3[:-4] + '-configu_x_max%i.stl' % i
                     mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                  else:
                     tx = a[index][i][0]-max_y_array[2][0] #GM x_max
                     ty = a[index][i][1]-max_y_array[2][1]
                     tz = a[index][i][2]-max_y_array[2][2]
                     outputfile = inputfile_3[:-4] + '-configu_x_max%i.stl' % i
                     mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)                      
      elif a[gom_max_z][0][2] > c[ssp_max_z][0][2] and e[gom_min_z][0][2] > d[ssp_min_z][0][2]:
          if a[index][i][1] < ssp.center_mass[1]:
             if a[index][i][0] > ssp.center_mass[0]:
                 tx = a[index][i][0]-min_y_array[2][0] #GM x_max
                 ty = a[index][i][1]-min_y_array[2][1]
                 tz = a[index][i][2]-min_y_array[2][2]
                 outputfile = inputfile_3[:-4] + '-configu_x_max%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
             else:
                 tx = a[index][i][0]-min_y_array[0][0] #GM x_max
                 ty = a[index][i][1]-min_y_array[0][1]
                 tz = a[index][i][2]-min_y_array[0][2]
                 outputfile = inputfile_3[:-4] + '-configu_x_max%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
          else:
             if a[index][i][1] > c[ssp_max_y][0][1]:
                 if a[index][i][0] > ssp.center_mass[0]:
                     tx = a[index][i][0]-max_y_array[1][0] #GM x_max
                     ty = a[index][i][1]-max_y_array[1][1]
                     tz = a[index][i][2]-max_y_array[1][2]
                     outputfile = inputfile_3[:-4] + '-configu_x_max%i.stl' % i
                     mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                 else:
                     tx = a[index][i][0]-max_y_array[3][0] #GM x_max
                     ty = a[index][i][1]-max_y_array[3][1]
                     tz = a[index][i][2]-max_y_array[3][2]
                     outputfile = inputfile_3[:-4] + '-configu_x_max%i.stl' % i
                     mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
             else:
                 if a[index][i][0] > ssp.center_mass[0]:
                     tx = a[index][i][0]-min_y_array[2][0] #GM x_max
                     ty = a[index][i][1]-min_y_array[2][1]
                     tz = a[index][i][2]-min_y_array[2][2]
                     outputfile = inputfile_3[:-4] + '-configu_x_max%i.stl' % i
                     mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                 else:
                     tx = a[index][i][0]-max_y_array[3][0] #GM x_max
                     ty = a[index][i][1]-max_y_array[3][1]
                     tz = a[index][i][2]-max_y_array[3][2]
                     outputfile = inputfile_3[:-4] + '-configu_x_max%i.stl' % i
                     mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)        


#GM_xmin:
def configu_x_min(inputfile_1, inputfile_2, inputfile_3):
    global_omv = trimesh.load_mesh(inputfile_1)
    ssp = trimesh.load_mesh(inputfile_2)
    a = find_max_min_points.find_min(pymesh.load_mesh(inputfile_1))# find min in all directions
    e = find_max_min_points.find_max(pymesh.load_mesh(inputfile_1))
    gom_max_z = np.where(e[:, 2:]==np.max(e[:, 2:],axis=0))[0] # gom_max_z
    gom_min_z = np.where(a[:, 2:]==np.min(a[:, 2:],axis=0))[0] # gom_min_z    
    index = np.where(a[:, :1]==np.min(a[:, :1],axis=0))[0]# index of x_min
    for i in range (0, 3):
     b = np.delete(a,index,0)
     index = np.union1d(index, np.where(a[:, :1]==np.min(b[:, :1],axis=0))[0])
    min_y_array = max_min_y_array.find_min_y_array(inputfile_3)
    max_y_array = max_min_y_array.find_max_y_array(inputfile_3)
    c = find_max_min_points.find_max(pymesh.load_mesh(inputfile_2))
    d = find_max_min_points.find_min(pymesh.load_mesh(inputfile_2))
    ssp_max_y = np.where(c[:, 1:2]==np.max(c[:, 1:2],axis=0))[0]
    ssp_max_z = np.where(c[:, 2:]==np.max(c[:, 2:],axis=0))[0]
    ssp_min_z = np.where(d[:, 2:]==np.min(d[:, 2:],axis=0))[0]    
    for i in range (0, index.size):
      if e[gom_max_z][0][2] > c[ssp_max_z][0][2] and a[gom_min_z][0][2] < d[ssp_min_z][0][2]:
            if a[index][i][0] > ssp.center_mass[0]:
                if a[index][i][1] < ssp.center_mass[1]:
                    if a[index][i][2] > ssp.center_mass[2]:
                      tx = a[index][i][0]-min_y_array[2][0] #GM x_min
                      ty = a[index][i][1]-min_y_array[2][1]
                      tz = a[index][i][2]-min_y_array[2][2]
                      outputfile = inputfile_3[:-4] + '-configu_x_min%i.stl' % i
                      mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                    else:
                      tx = a[index][i][0]-min_y_array[3][0] #GM x_min
                      ty = a[index][i][1]-min_y_array[3][1]
                      tz = a[index][i][2]-min_y_array[3][2]
                      outputfile = inputfile_3[:-4] + '-configu_x_min%i.stl' % i
                      mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                else:
                    if a[index][i][2] > ssp.center_mass[2]:
                      tx = a[index][i][0]-max_y_array[1][0] #GM x_min
                      ty = a[index][i][1]-max_y_array[1][1]
                      tz = a[index][i][2]-max_y_array[1][2]
                      outputfile = inputfile_3[:-4] + '-configu_x_min%i.stl' % i
                      mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                    else:
                      tx = a[index][i][0]-max_y_array[0][0] #GM x_min
                      ty = a[index][i][1]-max_y_array[0][1]
                      tz = a[index][i][2]-max_y_array[0][2]
                      outputfile = inputfile_3[:-4] + '-configu_x_min%i.stl' % i
                      mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)                    
            else:
                if a[index][i][1] < ssp.center_mass[1]:
                    if a[index][i][2] > ssp.center_mass[2]:
                      tx = a[index][i][0]-min_y_array[0][0] #GM x_min
                      ty = a[index][i][1]-min_y_array[0][1]
                      tz = a[index][i][2]-min_y_array[0][2]
                      outputfile = inputfile_3[:-4] + '-configu_x_min%i.stl' % i
                      mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                    else:
                      tx = a[index][i][0]-min_y_array[1][0] #GM x_min
                      ty = a[index][i][1]-min_y_array[1][1]
                      tz = a[index][i][2]-min_y_array[1][2]
                      outputfile = inputfile_3[:-4] + '-configu_x_min%i.stl' % i
                      mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                else:
                    if a[index][i][1] > c[ssp_max_y][0][1]:
                      if a[index][i][2] > ssp.center_mass[2]:
                       tx = a[index][i][0]-max_y_array[3][0] #GM x_min
                       ty = a[index][i][1]-max_y_array[3][1]
                       tz = a[index][i][2]-max_y_array[3][2]
                       outputfile = inputfile_3[:-4] + '-configu_x_min%i.stl' % i
                       mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                      else:
                       tx = a[index][i][0]-max_y_array[2][0]
                       ty = a[index][i][1]-max_y_array[2][1]
                       tz = a[index][i][2]-max_y_array[2][2]
                       outputfile = inputfile_3[:-4] + '-configu_x_min%i.stl' % i
                       mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)                        
                    else:
                      if a[index][i][2] > ssp.center_mass[2]:
                       tx = a[index][i][0]-min_y_array[0][0] #GM x_min
                       ty = a[index][i][1]-min_y_array[0][1]
                       tz = a[index][i][2]-min_y_array[0][2]
                       outputfile = inputfile_3[:-4] + '-configu_x_min%i.stl' % i
                       mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                      else:
                       tx = a[index][i][0]-min_y_array[1][0]
                       ty = a[index][i][1]-min_y_array[1][1]
                       tz = a[index][i][2]-min_y_array[1][2]
                       outputfile = inputfile_3[:-4] + '-configu_x_min%i.stl' % i
                       mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)                
      elif e[gom_max_z][0][2] < c[ssp_max_z][0][2] and a[gom_min_z][0][2] < d[ssp_min_z][0][2]:
          if a[index][i][1] < ssp.center_mass[1]:
            if a[index][i][0] > ssp.center_mass[0]:
                tx = a[index][i][0]-min_y_array[3][0] #GM x_min
                ty = a[index][i][1]-min_y_array[3][1]
                tz = a[index][i][2]-min_y_array[3][2]
                outputfile = inputfile_3[:-4] + '-configu_x_min%i.stl' % i
                mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
            else:
                tx = a[index][i][0]-min_y_array[1][0] #GM x_min
                ty = a[index][i][1]-min_y_array[1][1]
                tz = a[index][i][2]-min_y_array[1][2]
                outputfile = inputfile_3[:-4] + '-configu_x_min%i.stl' % i
                mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
          else:
            if a[index][i][1] > c[ssp_max_y][0][1]:
                if a[index][i][0] > ssp.center_mass[0]:
                 tx = a[index][i][0]-max_y_array[0][0] #GM x_max
                 ty = a[index][i][1]-max_y_array[0][1]
                 tz = a[index][i][2]-max_y_array[0][2]
                 outputfile = inputfile_3[:-4] + '-configu_x_min%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                else:
                 tx = a[index][i][0]-max_y_array[2][0] #GM x_max
                 ty = a[index][i][1]-max_y_array[2][1]
                 tz = a[index][i][2]-max_y_array[2][2]
                 outputfile = inputfile_3[:-4] + '-configu_x_min%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
            else:
                if a[index][i][0] > ssp.center_mass[0]:
                 tx = a[index][i][0]-max_y_array[0][0] #GM x_min
                 ty = a[index][i][1]-max_y_array[0][1]
                 tz = a[index][i][2]-max_y_array[0][2]
                 outputfile = inputfile_3[:-4] + '-configu_x_min%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                else:
                 tx = a[index][i][0]-min_y_array[1][0] #GM x_min
                 ty = a[index][i][1]-min_y_array[1][1]
                 tz = a[index][i][2]-min_y_array[1][2]
                 outputfile = inputfile_3[:-4] + '-configu_x_min%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
      elif e[gom_max_z][0][2] > c[ssp_max_z][0][2] and a[gom_min_z][0][2] > d[ssp_min_z][0][2]:
        if a[index][i][1] < ssp.center_mass[1]:
            if a[index][i][0] > ssp.center_mass[0]:
                tx = a[index][i][0]-min_y_array[2][0] #GM x_min
                ty = a[index][i][1]-min_y_array[2][1]
                tz = a[index][i][2]-min_y_array[2][2]
                outputfile = inputfile_3[:-4] + '-configu_x_min%i.stl' % i
                mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
            else:
                tx = a[index][i][0]-min_y_array[0][0] #GM x_min
                ty = a[index][i][1]-min_y_array[0][1]
                tz = a[index][i][2]-min_y_array[0][2]
                outputfile = inputfile_3[:-4] + '-configu_x_min%i.stl' % i
                mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
        else:
            if a[index][i][1] > c[ssp_max_y][0][1]:
                if a[index][i][0] > ssp.center_mass[0]:
                 tx = a[index][i][0]-max_y_array[1][0] #GM x_min
                 ty = a[index][i][1]-max_y_array[1][1]
                 tz = a[index][i][2]-max_y_array[1][2]
                 outputfile = inputfile_3[:-4] + '-configu_x_min%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                else:
                 tx = a[index][i][0]-max_y_array[3][0] #GM x_min
                 ty = a[index][i][1]-max_y_array[3][1]
                 tz = a[index][i][2]-max_y_array[3][2]
                 outputfile = inputfile_3[:-4] + '-configu_x_min%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
            else:
                if a[index][i][0] > ssp.center_mass[0]:
                 tx = a[index][i][0]-max_y_array[1][0] #GM x_min
                 ty = a[index][i][1]-max_y_array[1][1]
                 tz = a[index][i][2]-max_y_array[1][2]
                 outputfile = inputfile_3[:-4] + '-configu_x_min%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                else:
                 tx = a[index][i][0]-min_y_array[0][0] #GM x_min
                 ty = a[index][i][1]-min_y_array[0][1]
                 tz = a[index][i][2]-min_y_array[0][2]
                 outputfile = inputfile_3[:-4] + '-configu_x_min%i.stl' % i
                 mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)

#GM_ymax
def configu_y_max(inputfile_1, inputfile_2, inputfile_3):
    global_omv = trimesh.load_mesh(inputfile_1)
    ssp = trimesh.load_mesh(inputfile_2)
    a = find_max_min_points.find_max(pymesh.load_mesh(inputfile_1))# find max in all directions
    e = find_max_min_points.find_min(pymesh.load_mesh(inputfile_1))
    gom_max_z = np.where(a[:, 2:]==np.max(a[:, 2:],axis=0))[0] # gom_max_z
    gom_min_z = np.where(e[:, 2:]==np.min(e[:, 2:],axis=0))[0] # gom_min_z    
    index = np.where(a[:, 1:2]==np.max(a[:, 1:2],axis=0))[0]# index of y_max    
    for i in range (0, 3):
     b = np.delete(a,index,0)
     index = np.union1d(index, np.where(a[:, 1:2]==np.max(b[:, 1:2],axis=0))[0])
    min_y_array = max_min_y_array.find_min_y_array(inputfile_3)
    max_y_array = max_min_y_array.find_max_y_array(inputfile_3)
    c = find_max_min_points.find_max(pymesh.load_mesh(inputfile_2))
    d = find_max_min_points.find_min(pymesh.load_mesh(inputfile_2))
    ssp_max_y = np.where(c[:, 1:2]==np.max(c[:, 1:2],axis=0))[0]
    ssp_max_z = np.where(c[:, 2:]==np.max(c[:, 2:],axis=0))[0]
    ssp_min_z = np.where(d[:, 2:]==np.min(d[:, 2:],axis=0))[0]        
    for i in range (0, index.size):
      if a[gom_max_z][0][2] > c[ssp_max_z][0][2] and e[gom_min_z][0][2] < d[ssp_min_z][0][2]:
            if a[index][i][0] > ssp.center_mass[0]:
              if a[index][i][1] > c[ssp_max_y][0][1]:
                if a[index][i][2] > ssp.center_mass[2]:
                  tx = a[index][i][0]-max_y_array[1][0] #GM y_max
                  ty = a[index][i][1]-max_y_array[1][1]
                  tz = a[index][i][2]-max_y_array[1][2]
                  outputfile = inputfile_3[:-4] + '-configu_y_max%i.stl' % i
                  mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                else:
                  tx = a[index][i][0]-max_y_array[0][0] #GM y_max
                  ty = a[index][i][1]-max_y_array[0][1]
                  tz = a[index][i][2]-max_y_array[0][2]
                  outputfile = inputfile_3[:-4] + '-configu_y_max%i.stl' % i
                  mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
              else:
                if a[index][i][2] > ssp.center_mass[2]:
                  tx = a[index][i][0]-min_y_array[2][0] #GM y_max
                  ty = a[index][i][1]-min_y_array[2][1]
                  tz = a[index][i][2]-min_y_array[2][2]
                  outputfile = inputfile_3[:-4] + '-configu_y_max%i.stl' % i
                  mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                else:
                  tx = a[index][i][0]-min_y_array[3][0] #GM y_max
                  ty = a[index][i][1]-min_y_array[3][1]
                  tz = a[index][i][2]-min_y_array[3][2]
                  outputfile = inputfile_3[:-4] + '-configu_y_max%i.stl' % i
                  mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)                
            else:
              if a[index][i][1] > c[ssp_max_y][0][1]:
                if a[index][i][2] > ssp.center_mass[2]:
                  tx = a[index][i][0]-max_y_array[3][0] #GM y_max
                  ty = a[index][i][1]-max_y_array[3][1]
                  tz = a[index][i][2]-max_y_array[3][2]
                  outputfile = inputfile_3[:-4] + '-configu_y_max%i.stl' % i
                  mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                else:
                  tx = a[index][i][0]-max_y_array[2][0] #GM y_max
                  ty = a[index][i][1]-max_y_array[2][1]
                  tz = a[index][i][2]-max_y_array[2][2]
                  outputfile = inputfile_3[:-4] + '-configu_y_max%i.stl' % i
                  mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
              else:
                if a[index][i][2] > ssp.center_mass[2]:
                  tx = a[index][i][0]-min_y_array[0][0] #GM y_max
                  ty = a[index][i][1]-min_y_array[0][1]
                  tz = a[index][i][2]-min_y_array[0][2]
                  outputfile = inputfile_3[:-4] + '-configu_y_max%i.stl' % i
                  mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                else:
                  tx = a[index][i][0]-min_y_array[1][0] #GM y_max
                  ty = a[index][i][1]-min_y_array[1][1]
                  tz = a[index][i][2]-min_y_array[1][2]
                  outputfile = inputfile_3[:-4] + '-configu_y_max%i.stl' % i
                  mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)                
      elif a[gom_max_z][0][2] < c[ssp_max_z][0][2] and e[gom_min_z][0][2] < d[ssp_min_z][0][2]:
            if a[index][i][0] > ssp.center_mass[0]:
                tx = a[index][i][0]-max_y_array[0][0] #GM y_max
                ty = a[index][i][1]-max_y_array[0][1]
                tz = a[index][i][2]-max_y_array[0][2]
                outputfile = inputfile_3[:-4] + '-configu_y_max%i.stl' % i
                mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
            else:
                tx = a[index][i][0]-max_y_array[2][0] #GM y_max
                ty = a[index][i][1]-max_y_array[2][1]
                tz = a[index][i][2]-max_y_array[2][2]
                outputfile = inputfile_3[:-4] + '-configu_y_max%i.stl' % i
                mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)        
      elif a[gom_max_z][0][2] > c[ssp_max_z][0][2] and e[gom_min_z][0][2] > d[ssp_min_z][0][2]:
            if a[index][i][0] > ssp.center_mass[0]:
                tx = a[index][i][0]-max_y_array[1][0] #GM y_max
                ty = a[index][i][1]-max_y_array[1][1]
                tz = a[index][i][2]-max_y_array[1][2]
                outputfile = inputfile_3[:-4] + '-configu_y_max%i.stl' % i
                mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
            else:
                tx = a[index][i][0]-max_y_array[3][0] #GM y_max
                ty = a[index][i][1]-max_y_array[3][1]
                tz = a[index][i][2]-max_y_array[3][2]
                outputfile = inputfile_3[:-4] + '-configu_y_max%i.stl' % i
                mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)        


#GM_ymin
def configu_y_min(inputfile_1, inputfile_2, inputfile_3):
    global_omv = trimesh.load_mesh(inputfile_1)
    ssp = trimesh.load_mesh(inputfile_2)
    a = find_max_min_points.find_min(pymesh.load_mesh(inputfile_1))# find min in all directions
    e = find_max_min_points.find_max(pymesh.load_mesh(inputfile_1))
    gom_max_z = np.where(e[:, 2:]==np.max(e[:, 2:],axis=0))[0] # gom_max_z
    gom_min_z = np.where(a[:, 2:]==np.min(a[:, 2:],axis=0))[0] # gom_min_z    
    index = np.where(a[:, 1:2]==np.min(a[:, 1:2],axis=0))[0]# index of y_min
    for i in range (0, 3):
     b = np.delete(a,index,0)
     index = np.union1d(index, np.where(a[:, 1:2]==np.min(b[:, 1:2],axis=0))[0])
    min_y_array = max_min_y_array.find_min_y_array(inputfile_3)
    max_y_array = max_min_y_array.find_max_y_array(inputfile_3)
    c = find_max_min_points.find_max(pymesh.load_mesh(inputfile_2))
    d = find_max_min_points.find_min(pymesh.load_mesh(inputfile_2))
    ssp_max_y = np.where(c[:, 1:2]==np.max(c[:, 1:2],axis=0))[0]
    ssp_max_z = np.where(c[:, 2:]==np.max(c[:, 2:],axis=0))[0]
    ssp_min_z = np.where(d[:, 2:]==np.min(d[:, 2:],axis=0))[0]
    for i in range (0, index.size):
      if e[gom_max_z][0][2] > c[ssp_max_z][0][2] and a[gom_min_z][0][2] < d[ssp_min_z][0][2]:
            if a[index][i][0] > ssp.center_mass[0]:
                if a[index][i][2] > ssp.center_mass[2]:
                  tx = a[index][i][0]-min_y_array[2][0] #GM y_min
                  ty = a[index][i][1]-min_y_array[2][1]
                  tz = a[index][i][2]-min_y_array[2][2]
                  outputfile = inputfile_3[:-4] + '-configu_y_min%i.stl' % i
                  mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                else:
                  tx = a[index][i][0]-min_y_array[3][0] #GM y_min
                  ty = a[index][i][1]-min_y_array[3][1]
                  tz = a[index][i][2]-min_y_array[3][2]
                  outputfile = inputfile_3[:-4] + '-configu_y_min%i.stl' % i
                  mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
            else:
                if a[index][i][2] > ssp.center_mass[2]:
                  tx = a[index][i][0]-min_y_array[0][0] #GM y_min
                  ty = a[index][i][1]-min_y_array[0][1]
                  tz = a[index][i][2]-min_y_array[0][2]
                  outputfile = inputfile_3[:-4] + '-configu_y_min%i.stl' % i
                  mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
                else:
                  tx = a[index][i][0]-min_y_array[1][0] #GM y_min
                  ty = a[index][i][1]-min_y_array[1][1]
                  tz = a[index][i][2]-min_y_array[1][2]
                  outputfile = inputfile_3[:-4] + '-configu_y_min%i.stl' % i
                  mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
      elif e[gom_max_z][0][2] < c[ssp_max_z][0][2] and a[gom_min_z][0][2] < d[ssp_min_z][0][2]:
            if a[index][i][0] > ssp.center_mass[0]:
                tx = a[index][i][0]-min_y_array[3][0] #GM y_min
                ty = a[index][i][1]-min_y_array[3][1]
                tz = a[index][i][2]-min_y_array[3][2]
                outputfile = inputfile_3[:-4] + '-configu_y_min%i.stl' % i
                mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
            else:
                tx = a[index][i][0]-min_y_array[1][0] #GM y_min
                ty = a[index][i][1]-min_y_array[1][1]
                tz = a[index][i][2]-min_y_array[1][2]
                outputfile = inputfile_3[:-4] + '-configu_y_min%i.stl' % i
                mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)        
      elif e[gom_max_z][0][2] > c[ssp_max_z][0][2] and a[gom_min_z][0][2] > d[ssp_min_z][0][2]:
            if a[index][i][0] > ssp.center_mass[0]:
                tx = a[index][i][0]-min_y_array[2][0] #GM y_min
                ty = a[index][i][1]-min_y_array[2][1]
                tz = a[index][i][2]-min_y_array[2][2]
                outputfile = inputfile_3[:-4] + '-configu_y_min%i.stl' % i
                mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)
            else:
                tx = a[index][i][0]-min_y_array[0][0] #GM y_min
                ty = a[index][i][1]-min_y_array[0][1]
                tz = a[index][i][2]-min_y_array[0][2]
                outputfile = inputfile_3[:-4] + '-configu_y_min%i.stl' % i
                mv_translation.main(inputfile_3, tx, ty, tz).save(outputfile)        



if __name__ == '__main__':
  ##gedrehte Meshes
  #gm_path = '/mnt/c/Users/fehle/test/overlappingtest9/overlap_meshes/global_mv_vpc_y_1.stl'
  #gom_path = '/mnt/c/Users/fehle/test/overlappingtest9/overlap_meshes/simplified_intersection_0_1.stl'
  #get_model.get_normal_Lage(get_model.get_angle_x(gm_path),get_model.get_angle_y(gm_path),get_model.get_angle_z(gm_path), get_model.get_model(gom_path)).save_current_mesh('/mnt/c/Users/fehle/test/overlappingtest9/overlap_meshes/simplified_intersection_0_1_gedreht.stl')
  #ssp_path = '/mnt/c/Users/fehle/test/overlappingtest9/vpc_y_1/ssp_vpc_y_1_tcp.stl'
  #get_model.get_normal_Lage(get_model.get_angle_x(ssp_path),get_model.get_angle_y(ssp_path),get_model.get_angle_z(ssp_path), get_model.get_model(ssp_path)).save_current_mesh('/mnt/c/Users/fehle/test/overlappingtest9/vpc_y_1/ssp_vpc_y_1_tcp_gedreht.stl')
  #mv_path = '/mnt/c/Users/fehle/test/overlappingtest9/intersection01_in_1/mv_vpc_y_1.stl'
  #get_model.get_normal_Lage(get_model.get_angle_x(mv_path),get_model.get_angle_y(mv_path),get_model.get_angle_z(mv_path), get_model.get_model(mv_path)).save_current_mesh('/mnt/c/Users/fehle/test/overlappingtest9/intersection01_in_1/mv_vpc_y_1_gedreht.stl')
  
  #inputfile_1 = '/mnt/c/Users/fehle/test/overlappingtest9/overlap_meshes/simplified_intersection_0_1_gedreht.stl'
  #inputfile_2 = '/mnt/c/Users/fehle/test/overlappingtest9/vpc_y_1/ssp_vpc_y_1_tcp_gedreht.stl'
  #inputfile_3 = '/mnt/c/Users/fehle/test/overlappingtest9/intersection01_in_1/mv_vpc_y_1_gedreht.stl'
  
  ##normal Meshes
  inputfile_1 = '/mnt/c/Users/fehle/test/overlappingtest3/overlap_meshes/simplified_intersection_0_1.stl'
  inputfile_2 = '/mnt/c/Users/fehle/test/overlappingtest3/vpc_y_0/ssp_vpc_y_0_tcp.stl'
  inputfile_3 = '/mnt/c/Users/fehle/test/overlappingtest3/intersection01_in_0/mv_vpc_y_0.stl'
  
  configu_z_max(inputfile_1, inputfile_2, inputfile_3)
  configu_z_min(inputfile_1, inputfile_2, inputfile_3)
  configu_x_max(inputfile_1, inputfile_2, inputfile_3)
  configu_x_min(inputfile_1, inputfile_2, inputfile_3)
  configu_y_max(inputfile_1, inputfile_2, inputfile_3)
  configu_y_min(inputfile_1, inputfile_2, inputfile_3)
  