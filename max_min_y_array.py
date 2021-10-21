import pymeshlab
import numpy as np

def find_max_y_array(inputfile):
    ms = pymeshlab.MeshSet()
    ms.load_new_mesh(inputfile)
    a = ms.current_mesh().vertex_matrix()
    max_y_array = np.random.random((4,3))
    
    max_y_array[0] = a[5] #overlappingtest 3,5,6,7
    max_y_array[1] = a[7]
    max_y_array[2] = a[6]
    max_y_array[3] = a[3]
    #max_y_array[0] = a[6] #overlappingtest 8 backside
    #max_y_array[1] = a[3]
    #max_y_array[2] = a[5]
    #max_y_array[3] = a[7]
    return max_y_array

def find_min_y_array(inputfile):
    ms = pymeshlab.MeshSet()
    ms.load_new_mesh(inputfile)
    a = ms.current_mesh().vertex_matrix()
    min_y_array = np.random.random((4,3))

    
    min_y_array[0] = a[0] #overlappingtest 3,5,6,7
    min_y_array[1] = a[1]
    min_y_array[2] = a[4]
    min_y_array[3] = a[2]    
    #min_y_array[0] = a[2] #overlappingtest 8 backside
    #min_y_array[1] = a[4]
    #min_y_array[2] = a[1]
    #min_y_array[3] = a[0]     
    return min_y_array


#if __name__ == '__main__':
#    inputfile = '/mnt/c/Users/fehle/test/intersection02_in_0/mv_sp_y_0.stl'
#    print(find_max_y_array(inputfile))
#    print(find_min_y_array(inputfile))

