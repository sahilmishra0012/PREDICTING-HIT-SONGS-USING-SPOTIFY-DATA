import h5py
import tables
# print(tables.open_file('TRAAADZ128F9348C2E.h5', mode='r'))
# print("="*50)
f1 = h5py.File('TRBGQAO128EF35A1AD.h5', 'r')
a=list(f1['metadata']['songs'])[0][9].decode('UTF-8')
b=list(f1['metadata']['songs'])[0][14].decode('UTF-8')
c=list(f1['metadata']['songs'])[0][18].decode('UTF-8')
d=list(f1['musicbrainz']['songs'])[0][1]
print("Artist=>",a)
print("Album=>",b)
print("Song=>",c)
print("Year of Release=>",d)
print((a,b,c,d))