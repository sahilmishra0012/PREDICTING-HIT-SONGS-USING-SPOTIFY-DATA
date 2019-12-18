import h5py
import tables
# print(tables.open_file('TRAAADZ128F9348C2E.h5', mode='r'))
# print("="*50)
f1 = h5py.File('TRAAAAW128F429D538.h5', 'r')
#f2 = h5py.File('TRAABDL12903CAABBA.h5', 'r')
print(list(f1['metadata']['songs']))

