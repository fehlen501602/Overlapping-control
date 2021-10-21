#This module calculates the overlap solution space for each given pose. 

import trimesh
import pymeshlab
import pymesh
import numpy as np
import sys
sys.path.append(r'/home/xxyfehlen501602/workspace/')
import get_model
import os

def ssp_overlap(folder_name, input_mv, input_ssp):
    fileCounter = 0
    for root, dirs, files in os.walk('/mnt/c/Users/fehle/test/%s/' % folder_name):
        for file in files:
            if file.startswith('%s-configu' % input_mv):
                fileCounter += 1
    a = []
    filePath = '/mnt/c/Users/fehle/test/%s/' % folder_name
    fileList = os.listdir(filePath)
    for i in range (0,fileCounter):
        mesh = trimesh.load_mesh(filePath + fileList[i])
        center = mesh.center_mass
        a.append(center)
    
    # save_center
    points = np.array(a)
    ms1 = pymeshlab.MeshSet()
    ms1.load_new_mesh('/mnt/c/Users/fehle/test/%s/%s.stl' % (folder_name, input_mv))
    pca = ms1.compute_geometric_measures().get('pca')
    bias = [[0,0,-42]] # overlapping test 3
    #bias = [[0,0,42]] # overlapping test 7, 6, 5
    center_bias= np.dot(bias,pca)
    print(center_bias)
    for i in range (0,fileCounter):
      points[i] = np.add(points[i], center_bias)
    np.savetxt(filePath + 'configuration.xyz', points,fmt='%f',delimiter=' ')
    
    # ssp_overlap
    ms = pymeshlab.MeshSet()
    ms.load_new_mesh(filePath + 'configuration.xyz')
    ms.delaunay_triangulation()
    ms.convex_hull()
    ms.save_current_mesh(filePath + 'ssp_overlap.stl')
    mesh_1 = pymesh.load_mesh('/mnt/c/Users/fehle/test/overlappingtest3/vpc_y_0/%s.stl' % input_ssp)
    mesh_1 = pymesh.convex_hull(mesh_1, engine='auto', with_timing=False)
    mesh_2 = pymesh.load_mesh(filePath + 'ssp_overlap.stl')
    path = filePath + 'overlap.stl'
    get_model.get_intersection(mesh_1,mesh_2,path)
    overlap = pymeshlab.MeshSet()
    overlap.load_new_mesh(path)
    return overlap

if __name__ == '__main__':
    folder_name = 'overlappingtest3/intersection01_in_0'
    ##normal Meshes
    input_mv = 'mv_vpc_y_0'
    input_ssp ='ssp_vpc_y_0_tcp'
    
    ##gedrehte Meshes
    #input_mv = 'mv_vpc_y_1_gedreht'
    #input_ssp ='ssp_vpc_y_1_tcp_gedreht'
    

    ## normal Meshes
    ssp_overlap(folder_name,input_mv,input_ssp) 

    ## gedrehte Meshes
    #path ='/mnt/c/Users/fehle/test/overlappingtest9/intersection01_in_1/%s.stl' %  input_mv
    #angle_x=get_model.get_angle_x(path[:-12]+'.stl')
    #angle_y=get_model.get_angle_y(path[:-12]+'.stl')
    #angle_z=get_model.get_angle_z(path[:-12]+'.stl')
    #get_model.get_gedrehte_Lage(angle_x, angle_y, angle_z,ssp_overlap(folder_name,input_mv,input_ssp)).save_current_mesh('/mnt/c/Users/fehle/test/overlappingtest9/intersection01_in_1/overlap_gedreht.stl')
