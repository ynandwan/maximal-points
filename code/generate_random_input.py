import sys
n = int(sys.argv[1])
import numpy as np
a = np.random.randint(99999999, size = 3*n)
a = np.unique(a)
a = a[(a.size % 3) : ]
np.random.shuffle(a)
b = a.reshape(-1,3)
fh = open('../input/input_{}.txt'.format(b.shape[0]),'w')
print(b.shape[0],file=fh)
print('\n'.join([' '.join(list(map(str,x))) for x in b]),file=fh)
fh.close()
