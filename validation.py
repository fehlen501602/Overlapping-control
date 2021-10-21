## For one point a in overlap solution space_0 and its corresponding overlap solution space in overlap solution space_1, 
##calculate the furthest measurement volume from point a, check the overlap between the measurement volume on point a and this 
##furthest measurement volume
## They should have at least one point or line overlap
## When point a is not given, it is set as mass center of the overlap solution space_0 as default

import pymesh
import trimesh
import numpy as np
import pymeshlab


def FurthestPoints(point_of_a, path_a, path_b):
    osp_a = trimesh.load_mesh(path_a + 'reduced_overlap.stl')
    osp_b = pymesh.load_mesh(path_b + 'overlap_ssp_center.stl')
    if point_of_a == True:
        center = point_of_a
    else:
        center = osp_a.center_mass
    vertices = osp_b.vertices
    PointsDistance = []
    distance = []
    for i in range (0, len(vertices)):
        point = vertices[i]
        squared_dist = np.sum((center-point)**2, axis=0)
        dist = np.sqrt(squared_dist)           
        a = np.array([center, point, dist], dtype=object)
        PointsDistance.append(a)
        distance.append([dist])
    max_distance = np.max(distance)
    index = np.where(distance == max_distance)[0] 
    point_b = PointsDistance[index[0]][1]
    return point_b

def CollisionValidation(path,measurement_volume,coordinates):    
    mv = pymeshlab.MeshSet()
    mv.load_new_mesh(path + measurement_volume)
    mass = mv.compute_geometric_measures().get('center_of_mass')
    pca = mv.compute_geometric_measures().get('pca')
    bias = [[0,0,42]]#overlapping test5
    #bias = [[0,0,-42]]#overlapping test3
    origin_bias= np.dot(bias,pca)
    origin = np.add(mass, origin_bias)
    mv.transform_translate_center_set_origin(traslmethod = 'XYZ translation', axisx = -origin[0][0]+coordinates[0], axisy = -origin[0][1]+coordinates[1], axisz = -origin[0][2]+coordinates[2])
    mv.save_current_mesh(path + 'furthestmv.stl')

if __name__ == '__main__':
    path_a =  '/mnt/c/Users/fehle/test/overlappingtest5/intersection01_in_1/'
    path_b =  '/mnt/c/Users/fehle/test/overlappingtest5/intersection01_in_0/'
    mv_b = 'mv_vpc_y_0.stl'
    point_of_a = []
    c_b = FurthestPoints(point_of_a, path_a, path_b)
    CollisionValidation(path_b, mv_b, c_b)
