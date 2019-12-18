import os
# returns list
main=['A','B']
a=ord('A')
sub_dirA=[chr(i) for i in range(a,a+26)]
sub_dirB=[chr(i) for i in range(a,a+9)]
sub_dirA1=[chr(i) for i in range(a,a+26)]
sub_dirB1=[chr(i) for i in range(a,a+26)]
sub_dirB2=[chr(i) for i in range(a,a+10)]
for i in main:
    if i=='A':
        for j in sub_dirA:
            for k in sub_dirA1:
                path=os.path.join('data',i,j,k)
                print(os.listdir(path))
    if i=='B':
        for j in sub_dirB:
            if j!='I':
                for k in sub_dirB1:
                    path=os.path.join('data',i,j,k)
                    print(os.listdir(path))
            else:
                for k in sub_dirB2:
                    path=os.path.join('data',i,j,k)
                    print(os.listdir(path))
                    