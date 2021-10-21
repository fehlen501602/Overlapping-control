#This class encloses all the pre-calculation features, including simplification, orientation modification, 
# intersection calculation and models reduction etc.

import pymesh
import pymeshlab
import math

def get_model(path):
    ms = pymeshlab.MeshSet()
    ms.load_new_mesh(path)
    return ms


def get_intersection(model_A, model_B, save_path):
    intersection = pymesh.boolean(model_A, model_B, operation='intersection',
                   engine='igl')
    pymesh.save_mesh('%s' % save_path,intersection)
    return intersection

def get_simplified_intersection(model_A, model_B, save_path):
    intersection = pymesh.boolean(model_A, model_B, operation='intersection',
                   engine='igl')
    pymesh.save_mesh('%s' % save_path,intersection)
    ms = pymeshlab.MeshSet()
    ms.load_new_mesh('%s' % save_path)
    ms.simplification_quadric_edge_collapse_decimation(targetfacenum = 25, targetperc = 0, qualitythr = 0.3, preserveboundary = True, boundaryweight = 1)
    return ms

def get_simplified_model(model_A_path):
    ms = pymeshlab.MeshSet()
    ms.load_new_mesh('%s' % model_A_path)
    ms.simplification_quadric_edge_collapse_decimation(targetfacenum = 25, targetperc = 0, qualitythr = 0.3, preserveboundary = True, boundaryweight = 1, optimalplacement = True, autoclean  = True)
    return ms

def get_intersection_bboxmesh(intersection):
    bbox = pymesh.generate_box_mesh(intersection.bbox[0],intersection.bbox[1])    
    bbox_vertices = bbox.vertices
    return bbox_vertices


def get_angle_x(path):
    ms=pymeshlab.MeshSet()
    ms.load_new_mesh(path) 
    tan_x=ms.compute_geometric_measures().get('pca')[1][1]/ms.compute_geometric_measures().get('pca')[1][2]
    angle_x=  math.degrees(math.atan(tan_x))
    return angle_x


def get_angle_y(path):
    ms=pymeshlab.MeshSet()
    ms.load_new_mesh(path) 
    tan_y=ms.compute_geometric_measures().get('pca')[0][2]/ms.compute_geometric_measures().get('pca')[0][0]
    angle_y=  math.degrees(math.atan(tan_y))
    return angle_y


def get_angle_z(path):
    ms=pymeshlab.MeshSet()
    ms.load_new_mesh(path) 
    tan_z=ms.compute_geometric_measures().get('pca')[2][0]/ms.compute_geometric_measures().get('pca')[2][1]
    angle_z=  math.degrees(math.atan(tan_z))
    return angle_z

def get_normal_Lage(angle_x, angle_y, angle_z, ms, Backside = True):
    ms.transform_rotate(rotaxis  = 'Y axis', rotcenter = 'origin',angle = angle_y)
    ms.transform_rotate(rotaxis  = 'X axis', rotcenter = 'origin',angle = angle_x)
    ms.transform_rotate(rotaxis  = 'Z axis', rotcenter = 'origin',angle = angle_z)
    if Backside == True:
        ms.transform_rotate(rotaxis  = 'X axis', rotcenter = 'origin',angle = 180)
    return ms

def get_gedrehte_Lage(angle_x, angle_y, angle_z, ms, Backside = True):
   if Backside == True:
       ms.transform_rotate(rotaxis  = 'X axis', rotcenter = 'origin',angle = -180)
   ms.transform_rotate(rotaxis  = 'Z axis', rotcenter = 'origin',angle = -angle_z)
   ms.transform_rotate(rotaxis  = 'X axis', rotcenter = 'origin',angle = -angle_x)
   ms.transform_rotate(rotaxis  = 'Y axis', rotcenter = 'origin',angle = -angle_y)   
   return ms

def get_reduced_model(path):
    ms=pymeshlab.MeshSet()
    ms.load_new_mesh(path)
    ms.transform_scale_normalize(axisx = 0.9,uniformflag = True, scalecenter = 'barycenter')
    return ms

if __name__ == "__main__":
    mesh_1 = pymesh.load_mesh('/mnt/c/Users/fehle/test/overlappingtest3/overlap_meshes/global_mv_vpc_y_0.stl')
    mesh_2 = pymesh.load_mesh('/mnt/c/Users/fehle/test/overlappingtest3/overlap_meshes/global_mv_vpc_y_1.stl')
    path = '/mnt/c/Users/fehle/test/overlappingtest3/overlap_meshes/intersection_0_1.stl'
    get_intersection(mesh_1,mesh_2,path)
    get_simplified_intersection(mesh_1,mesh_2,path).save_current_mesh('/mnt/c/Users/fehle/test/overlappingtest3/overlap_meshes/simplified_intersection_0_1.stl')
    
    #path = '/mnt/c/Users/fehle/test/overlappingtest6/overlap_meshes/global_mv_vpc_y_0.stl'
    #ms = pymeshlab.MeshSet()
    #ms.load_new_mesh(path)
    #angle_y = get_angle_y(path)
    #angle_x = get_angle_x(path)
    #angle_z = get_angle_z(path)
    #normal = pymeshlab.MeshSet()
    #normal.load_new_mesh('/mnt/c/Users/fehle/test/overlappingtest6/overlap_meshes/normal_global_mv_vpc_y_0.stl')
    #get_gedrehte_Lage(angle_x, angle_y, angle_z, normal).save_current_mesh('/mnt/c/Users/fehle/test/overlappingtest6/overlap_meshes/gedrehte_global_mv_vpc_y_0.stl')