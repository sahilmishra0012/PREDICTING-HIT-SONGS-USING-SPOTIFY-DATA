import os
import h5py
import csv
import pandas as pd

main=['A','B']
a=ord('A')
sub_dirA=[chr(i) for i in range(a,a+26)]
sub_dirB=[chr(i) for i in range(a,a+9)]
sub_dirA1=[chr(i) for i in range(a,a+26)]
sub_dirB1=[chr(i) for i in range(a,a+26)]
sub_dirB2=[chr(i) for i in range(a,a+10)]
count=0
ll1=[]
for i in main:
    if i=='A':
        for j in sub_dirA:
            for k in sub_dirA1:
                path=os.path.join('data',i,j,k)
                ll=os.listdir(path)
                for m in ll:
                    file_path=str(path+"/"+m)
                    count=count+1
                    f1 = h5py.File(file_path, 'r')
                    a=list(f1['metadata']['songs'])[0][9].decode('UTF-8')
                    b=list(f1['metadata']['songs'])[0][14].decode('UTF-8')
                    c=list(f1['metadata']['songs'])[0][18].decode('UTF-8')
                    d=list(f1['musicbrainz']['songs'])[0][1]
                    ll1.append([a,b,c,d])
    if i=='B':
        for j in sub_dirB:
            if j!='I':
                for k in sub_dirB1:
                    path=os.path.join('data',i,j,k)
                    ll=os.listdir(path)
                    for m in ll:
                        file_path=str(path+"/"+m)
                        count=count+1
                        f1 = h5py.File(file_path, 'r')
                        a=list(f1['metadata']['songs'])[0][9].decode('UTF-8')
                        b=list(f1['metadata']['songs'])[0][14].decode('UTF-8')
                        c=list(f1['metadata']['songs'])[0][18].decode('UTF-8')
                        d=list(f1['musicbrainz']['songs'])[0][1]
                        ll1.append([a,b,c,d])
            else:
                for k in sub_dirB2:
                    path=os.path.join('data',i,j,k)
                    ll=os.listdir(path)
                    for m in ll:
                        file_path=str(path+"/"+m)
                        count=count+1
                        f1 = h5py.File(file_path, 'r')
                        a=list(f1['metadata']['songs'])[0][9].decode('UTF-8')
                        b=list(f1['metadata']['songs'])[0][14].decode('UTF-8')
                        c=list(f1['metadata']['songs'])[0][18].decode('UTF-8')
                        d=list(f1['musicbrainz']['songs'])[0][1]
                        ll1.append([a,b,c,d])

df = pd.DataFrame.from_records(ll1)
print("File Saved")
df.to_excel('file.xls',index=False,header=False)
