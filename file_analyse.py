import h5py
import tables
# print(tables.open_file('TRAAADZ128F9348C2E.h5', mode='r'))
# print("="*50)
f1 = h5py.File('TRBGQAO128EF35A1AD.h5', 'r')
print("Artist=>",list(f1['metadata']['songs'])[0][9])
print("Album=>",list(f1['metadata']['songs'])[0][14])
print("Song=>",list(f1['metadata']['songs'])[0][18])