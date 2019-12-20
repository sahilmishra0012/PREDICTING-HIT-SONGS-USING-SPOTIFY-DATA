import h5py
import tables
f1 = h5py.File('TRAAKVD12903CE8474.h5', 'r')
a=list(f1['metadata']['songs'])[0][9].decode('UTF-8')
b=list(f1['metadata']['songs'])[0][14].decode('UTF-8')
c=list(f1['metadata']['songs'])[0][18].decode('UTF-8')
d=list(f1['musicbrainz']['songs'])[0][1]
print([[a],[b],[c],[d]])
