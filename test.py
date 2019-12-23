import h5py
import tables
f1 = h5py.File('TRAESJK128E0792227.h5', 'r')
a=list(f1['analysis'])
print(a)
