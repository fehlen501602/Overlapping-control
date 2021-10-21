##  Caculation of the corresponding overlap solution space in overlap solution space_1 for one arbitrary point in the 
## overlap solution space_0. If the point is not given, it will be automated set as mass center of the overlap solution space 

import pymesh
import pymeshlab
import trimesh
import numpy as np
import sys
sys.path.append(r'/home/xxyfehlen501602/workspace/')
import mv_translation
import get_model


def OverlapSolutionSpaceOfOnePoint(point_in_a, measurement_volume_0_path, measurement_volume_1_path):
  overlapssp_0 = trimesh.load_mesh(measurement_volume_0_path[:-14] + 'reduced_overlap.stl')
  #overlapssp_0 = trimesh.load_mesh(measurement_volume_0_path[:-14] + 'overlap.stl')
  if point_in_a == True:
     center = point_in_a
  else:
     center = overlapssp_0.center_mass
  inputfile = measurement_volume_1_path
  mv=pymeshlab.MeshSet()
  mv.load_new_mesh(measurement_volume_0_path)
  mv1 = pymeshlab.MeshSet()
  mv1.load_new_mesh(inputfile)
  mass = mv.compute_geometric_measures().get('center_of_mass')
  pca = mv.compute_geometric_measures().get('pca')
  bias = [[0,0,42]] # overlapping test 5
  #bias = [[0,0,-42]] # overlapping test 3
  origin_bias= np.dot(bias,pca)
  origin = np.add(mass, origin_bias)
  mv.transform_translate_center_set_origin(traslmethod = 'XYZ translation', axisx = center[0]-origin[0][0], axisy = center[1]-origin[0][1], axisz = center[2]-origin[0][2])
  mv.save_current_mesh(measurement_volume_0_path[:-14] + 'centermv.stl')
  
  a = mv.current_mesh().vertex_matrix()
  b = mv1.current_mesh().vertex_matrix()
  
  points = []
  tx = a[7][0]-b[1][0]
  ty = a[7][1]-b[1][1]
  tz = a[7][2]-b[1][2]
  points.append(mv_translation.main(inputfile, tx, ty, tz).get_mass_properties()[1])

  tx = a[4][0]-b[1][0]
  ty = a[4][1]-b[1][1]
  tz = a[4][2]-b[1][2]
  points.append(mv_translation.main(inputfile, tx, ty, tz).get_mass_properties()[1])

  tx = a[4][0]-b[6][0]
  ty = a[4][1]-b[6][1]
  tz = a[4][2]-b[6][2]
  points.append(mv_translation.main(inputfile, tx, ty, tz).get_mass_properties()[1])

  tx = a[2][0]-b[0][0]
  ty = a[2][1]-b[0][1]
  tz = a[2][2]-b[0][2]
  points.append(mv_translation.main(inputfile, tx, ty, tz).get_mass_properties()[1])

  tx = a[2][0]-b[3][0]
  ty = a[2][1]-b[3][1]
  tz = a[2][2]-b[3][2]
  points.append(mv_translation.main(inputfile, tx, ty, tz).get_mass_properties()[1])

  tx = a[3][0]-b[1][0]
  ty = a[3][1]-b[1][1]
  tz = a[3][2]-b[1][2]
  points.append(mv_translation.main(inputfile, tx, ty, tz).get_mass_properties()[1])

  tx = a[3][0]-b[2][0]
  ty = a[3][1]-b[2][1]
  tz = a[3][2]-b[2][2]
  points.append(mv_translation.main(inputfile, tx, ty, tz).get_mass_properties()[1])

  tx = a[6][0]-b[4][0]
  ty = a[6][1]-b[4][1]
  tz = a[6][2]-b[4][2]
  points.append(mv_translation.main(inputfile, tx, ty, tz).get_mass_properties()[1])

  tx = a[5][0]-b[0][0]
  ty = a[5][1]-b[0][1]
  tz = a[5][2]-b[0][2]
  points.append(mv_translation.main(inputfile, tx, ty, tz).get_mass_properties()[1])

  tx = a[0][0]-b[2][0]
  ty = a[0][1]-b[2][1]
  tz = a[0][2]-b[2][2]
  points.append(mv_translation.main(inputfile, tx, ty, tz).get_mass_properties()[1])

  tx = a[0][0]-b[5][0]
  ty = a[0][1]-b[5][1]
  tz = a[0][2]-b[5][2]
  points.append(mv_translation.main(inputfile, tx, ty, tz).get_mass_properties()[1])

  tx = a[1][0]-b[7][0]
  ty = a[1][1]-b[7][1]
  tz = a[1][2]-b[7][2]
  points.append(mv_translation.main(inputfile, tx, ty, tz).get_mass_properties()[1])

  tx = a[1][0]-b[4][0]
  ty = a[1][1]-b[4][1]
  tz = a[1][2]-b[4][2]
  points.append(mv_translation.main(inputfile, tx, ty, tz).get_mass_properties()[1])

  #bias = [[0,0,42]] # overlapping test 5
  bias = [[0,0,-42]] # overlapping test 3
  pca_1 = mv1.compute_geometric_measures().get('pca')
  center_bias= np.dot(bias,pca_1)
  for i in range (0, len(points)):
    points[i] = np.add(points[i], center_bias[0])
  np.savetxt(inputfile[:-14] + 'mv.xyz', points ,fmt='%f',delimiter=' ')

  ms = pymeshlab.MeshSet()
  ms.load_new_mesh(inputfile[:-14] + 'mv.xyz')
  ms.delaunay_triangulation()
  ms.convex_hull()
  ms.save_current_mesh(inputfile[:-14] + 'overlap_center.stl')

  mesh_1 = pymesh.load_mesh(inputfile[:-14] + 'overlap_center.stl')
  mesh_2 = pymesh.load_mesh(inputfile[:-14] + 'reduced_overlap.stl')
  #mesh_2 = pymesh.load_mesh(inputfile[:-14] + 'overlap.stl')
  path = inputfile[:-14] + 'overlap_ssp_center.stl'
  get_model.get_intersection(mesh_1,mesh_2,path)



if __name__ == '__main__':
 mv_0_path =  '/mnt/c/Users/fehle/test/overlappingtest3/intersection01_in_0/mv_vpc_y_0.stl'
 mv_1_path =  '/mnt/c/Users/fehle/test/overlappingtest3/intersection01_in_1/mv_vpc_y_1.stl'
 point_in_a=[]
 OverlapSolutionSpaceOfOnePoint(point_in_a, mv_0_path, mv_1_path)
