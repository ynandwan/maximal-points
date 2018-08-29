from __future__ import print_function
import os
import utils 
import argparse 
import point, sort
import staircase 
#from IPython.core.debugger import Pdb

def main(input_file,output_file):
    l = utils.read_input(input_file)
    sort.quicksort(l,key=lambda p: p.x)
    maximal_points = []
    sc = staircase.Staircase2D()
    
    #Pdb().set_trace()
    for i in range(len(l)-1,-1,-1):
        p = l[i]
        #if p.ind == 951:
        #    #Pdb().set_trace()
        #    pass

        is_maximal = sc.update(point.Point2D(p.ind,p.y,p.z))
        #print(p)
        #print(sc.maximal_points.inorder_traverse())
        #if sc.size > 0:
        #    sc.maximal_points.display()
        
        #print('-----------------')
        if is_maximal:
            maximal_points.append(p)
    #
    sort.quicksort(maximal_points,key=lambda p: p.ind)
    if output_file == '':
        fh = None
    else:
        fh = open(output_file,'w')
    #
    print(len(maximal_points),file=fh)
    for mp in maximal_points:
        print(mp.ind,file=fh)
    #
    if fh:
        fh.close()



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file',help='input_file_name',type=str,default='input.txt')
    parser.add_argument('--output_file',help='output written in output file',default='')

    args = parser.parse_args()
    main(args.input_file, args.output_file)


