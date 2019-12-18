import h5py
import tables
print(tables.open_file('TRAAADZ128F9348C2E.h5', mode='r'))
print("="*50)
f = h5py.File('TRAAADZ128F9348C2E.h5', 'r')
print(list(f.keys()))
print(list(f['musicbrainz'].keys()))

