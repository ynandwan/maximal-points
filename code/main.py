import os
import utils 
import argparse 
import point, sort
import staircase 
from IPython.core.debugger import Pdb

def main(input_file,output_file):
    l = utils.read_input(input_file)
    sort.quicksort(l,key=lambda p: p.x)
    maximal_points = []
    sc = staircase.Staircase2D()
    
    #Pdb().set_trace()
    for i in range(len(l)-1,-1,-1):
        p = l[i]
        #print(p)
        #debug
        #if p.ind in [0,29,47,48,64]:
        is_maximal = sc.update(point.Point2D(p.ind,p.y,p.z))
        #print(sc.maximal_points.inorder_traverse())
        #if sc.size > 0:
        #    sc.maximal_points.display()
        #
        #print('-----------------')
        if is_maximal:
            maximal_points.append(p)
    #
    sort.quicksort(maximal_points,key=lambda p: p.ind)
    fh = open(output_file,'w')
    print(len(maximal_points),file=fh)
    for mp in maximal_points:
        print(mp.ind,file=fh)
    #
    fh.close()



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file',help='input_file_name',type=str,default='../input/input1.txt')
    parser.add_argument('--output_file',help='output written in output file',default='../output/my_output.txt')

    args = parser.parse_args()
    main(args.input_file, args.output_file)


