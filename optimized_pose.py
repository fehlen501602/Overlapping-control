#With a pair of overlap solution space, calculate a pair of new poses, which maximize the overlap in the measurement space

import numpy as np
import pymesh
import sys
sys.path.append(r'/home/xxyfehlen501602/workspace/')
from numpy import loadtxt
import pymeshlab
import get_model


def AllLineSegmentsOfMeshModel(path):
    mesh = pymesh.load_mesh(path)
    LineSegments = []
    for i in range (0, int(mesh.faces.size/3)):
        l1 = np.append([mesh.vertices[mesh.faces[i][0]]],[mesh.vertices[mesh.faces[i][1]]], axis = 0)
        t1 = tuple(l1[0])
        t2 = tuple(l1[1])
        l2 = np.append([mesh.vertices[mesh.faces[i][1]]],[mesh.vertices[mesh.faces[i][2]]], axis = 0)
        t3 = tuple(l2[0])
        t4 = tuple(l2[1])        
        l3 = np.append([mesh.vertices[mesh.faces[i][0]]],[mesh.vertices[mesh.faces[i][2]]], axis = 0)
        t5 = tuple(l3[0])
        t6 = tuple(l3[1])        
        LineSegments.append([t1,t2])
        LineSegments.append([t3,t4])
        LineSegments.append([t5,t6])
    LineSegments_unique = []
    for i in LineSegments:
        if i not in LineSegments_unique:
            LineSegments_unique.append(i)
    LineSegments_unique = np.array(LineSegments_unique)
    for i in range (0, len(LineSegments_unique)):
        for j in range (0, len(LineSegments_unique)):
            try:
             A = LineSegments_unique[j][0] == LineSegments_unique[i][1]
             B = LineSegments_unique[j][1] == LineSegments_unique[i][0]
             if (A.all() == True) and (B.all() == True):
              LineSegments_unique = np.delete(LineSegments_unique, j, axis=0)
              break
            except IndexError:
              pass
            continue            
    return LineSegments_unique

def closestDistanceBetweenLines(a0,a1,b0,b1,clampAll=True,clampA0=False,clampA1=False,clampB0=False,clampB1=False):
    #Two lines defined by numpy.array pairs (a0,a1,b0,b1)
    #Return the closest points on each segment and their distance    
    # If clampAll=True, set all clamps to True, Limit the endpoint of the shortest line segment between two line segments on the line segment
    if clampAll:
        clampA0=True
        clampA1=True
        clampB0=True
        clampB1=True

    # Calculate denomitator
    A = a1 - a0
    B = b1 - b0
    magA = np.linalg.norm(A)#Norm
    magB = np.linalg.norm(B)

    _A = A / magA
    _B = B / magB

    cross = np.cross(_A, _B);
    denom = np.linalg.norm(cross)**2

    # If lines are parallel (denom=0) test if lines overlap.
    # If they don't overlap then there is a closest point solution.
    # If they do overlap, there are infinite closest positions, but there is a closest distance
    if not denom:
        d0 = np.dot(_A,(b0-a0))
        # Overlap only possible with clamping
        if clampA0 or clampA1 or clampB0 or clampB1:
            d1 = np.dot(_A,(b1-a0))
            # Is segment B before A?
            if d0 <= 0 >= d1:
                if clampA0 and clampB1:
                    if np.absolute(d0) < np.absolute(d1):
                        return a0,b0,np.linalg.norm(a0-b0)
                    return a0,b1,np.linalg.norm(a0-b1)
            # Is segment B after A?
            elif d0 >= magA <= d1:
                if clampA1 and clampB0:
                    if np.absolute(d0) < np.absolute(d1):
                        return a1,b0,np.linalg.norm(a1-b0)
                    return a1,b1,np.linalg.norm(a1-b1)
        # Segments overlap, return distance between parallel segments
        return None,None,np.linalg.norm(((d0*_A)+a0)-b0)
    # Lines criss-cross: Calculate the projected closest points
    t = (b0 - a0);
    detA = np.linalg.det([t, _B, cross])
    detB = np.linalg.det([t, _A, cross])
    t0 = detA/denom;
    t1 = detB/denom;
    pA = a0 + (_A * t0) # Projected closest point on segment A
    pB = b0 + (_B * t1) # Projected closest point on segment B
    # Clamp projections
    if clampA0 or clampA1 or clampB0 or clampB1:
        if clampA0 and t0 < 0:
            pA = a0
        elif clampA1 and t0 > magA:
            pA = a1
        if clampB0 and t1 < 0:
            pB = b0
        elif clampB1 and t1 > magB:
            pB = b1
        # Clamp projection A
        if (clampA0 and t0 < 0) or (clampA1 and t0 > magA):
            dot = np.dot(_B,(pA-b0))
            if clampB0 and dot < 0:
                dot = 0
            elif clampB1 and dot > magB:
                dot = magB
            pB = b0 + (_B * dot)
        # Clamp projection B
        if (clampB0 and t1 < 0) or (clampB1 and t1 > magB):
            dot = np.dot(_A,(pB-a0))
            if clampA0 and dot < 0:
                dot = 0
            elif clampA1 and dot > magA:
                dot = magA
            pA = a0 + (_A * dot)
    return pA,pB,np.linalg.norm(pA-pB)

def MinimumDistanceBeweenEdgesOf2Meshes(LineSegments_a, LineSegments_b, filePath_a, filePath_b):
   distances = []
   closestPoints = []
   for i in range (0, len(LineSegments_a)):
       for j in range (0, len(LineSegments_b)):
           a0 = LineSegments_a[i][0]
           a1 = LineSegments_a[i][1]
           b0 = LineSegments_b[j][0]
           b1 = LineSegments_b[j][1]
           closestPoints.append(closestDistanceBetweenLines(a0,a1,b0,b1,clampAll=True))           
           distances.append(closestDistanceBetweenLines(a0,a1,b0,b1,clampAll=True)[2])           
   distances = np.array(distances)          
   min_distance = distances[np.where(distances==np.min(distances,axis=0))]
   closestPointsPair = []
   for i in range(0, len(closestPoints)):   
        A = closestPoints[i][2] == np.array(min_distance)[0]
        if A == True:
           closestPointsPair.append(closestPoints[i])
   a = []
   b = []
   for i in range (0, len(closestPointsPair)):
        a.append(closestPointsPair[i][0])
        b.append(closestPointsPair[i][1])
   a_points = np.array(a)
   b_points = np.array(b)
   np.savetxt(filePath_a + 'new_closestpoints.xyz', a_points, fmt='%f',delimiter=' ')
   np.savetxt(filePath_b + 'new_closestpoints.xyz', b_points, fmt='%f',delimiter=' ')
   return closestPointsPair  

def MaximumOverlapBetween2MesurementVolume(path_a,path_b):
    mv1 = pymeshlab.MeshSet()
    mv1.load_new_mesh(path_a + 'mv_vpc_y_0.stl')
    mv2 = pymeshlab.MeshSet()
    mv2.load_new_mesh(path_b + 'mv_vpc_y_1.stl')

    mass_a = mv1.compute_geometric_measures().get('center_of_mass')
    pca_a = mv1.compute_geometric_measures().get('pca')
    bias_a = [[0,0,-42]] # overlapping test 6, 3
    #bias_a = [[0,0,42]] # overlapping test 5
    origin_bias= np.dot(bias_a,pca_a)
    origin_a = np.add(mass_a, origin_bias)    

    
    coordinates_a = []
    xyz = open(path_a + 'new_closestpoints.xyz')
    for line in xyz:
     x,y,z = line.split()
    coordinates_a.append([float(x), float(y), float(z)])
    
    mass_b = mv2.compute_geometric_measures().get('center_of_mass')
    pca_b = mv2.compute_geometric_measures().get('pca')
    #bias_b = [[0,0,42]] # overlapping test 6, 5
    bias_b = [[0,0,-42]] # overlapping test 3
    origin_bias= np.dot(bias_b,pca_b)
    origin_b = np.add(mass_b, origin_bias)   
    
    coordinates_b = []
    xyz = open(path_b + 'new_closestpoints.xyz')
    for line in xyz:
     x,y,z = line.split()
    coordinates_b.append([float(x), float(y), float(z)])

     
    mv1.transform_translate_center_set_origin(traslmethod = 'XYZ translation', axisx = -origin_a[0][0]+coordinates_a[0][0], axisy = -origin_a[0][1]+coordinates_a[0][1], axisz = -origin_a[0][2]+coordinates_a[0][2])
    mv1.save_current_mesh(path_a + 'new_closestmv.stl')
    mv2.transform_translate_center_set_origin(traslmethod = 'XYZ translation', axisx = -origin_b[0][0]+coordinates_b[0][0], axisy = -origin_b[0][1]+coordinates_b[0][1], axisz = -origin_b[0][2]+coordinates_b[0][2])    
    mv2.save_current_mesh(path_b + 'new_closestmv.stl')


if __name__ == "__main__":
 path_a = '/mnt/c/Users/fehle/test/overlappingtest3/intersection01_in_0/'
 path_b = '/mnt/c/Users/fehle/test/overlappingtest3/intersection01_in_1/'

 #without safe factor
 #LineSegments_a = AllLineSegmentsOfMeshModel(path_a + 'overlap.stl')
 #LineSegments_b = AllLineSegmentsOfMeshModel(path_b + 'overlap.stl')
 
 #safe factor
 get_model.get_reduced_model(path_a + 'overlap.stl').save_current_mesh(path_a + 'reduced_overlap.stl')
 get_model.get_reduced_model(path_b + 'overlap.stl').save_current_mesh(path_b + 'reduced_overlap.stl')

 LineSegments_a = AllLineSegmentsOfMeshModel(path_a + 'reduced_overlap.stl')
 LineSegments_b = AllLineSegmentsOfMeshModel(path_b + 'reduced_overlap.stl')

 mv1 = pymeshlab.MeshSet()
 mv1.load_new_mesh(path_a + 'mv_vpc_y_0.stl')
 mv2 = pymeshlab.MeshSet()
 mv2.load_new_mesh(path_b + 'mv_vpc_y_1.stl')
 MinimumDistanceBeweenEdgesOf2Meshes(LineSegments_a, LineSegments_b, path_a, path_b)
 MaximumOverlapBetween2MesurementVolume(path_a, path_b)









