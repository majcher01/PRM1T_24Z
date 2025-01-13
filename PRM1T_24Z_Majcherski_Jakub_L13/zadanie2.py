import numpy as np

def funkcja(macierz,wektor):
    if(np.linalg.det(macierz)==0):
        raise Exception("Macierz osobliwa")
    q,r=np.linalg.qr(macierz)
    y=np.transpose(q)@wektor
    x=np.linalg.inv(r)@y

    return x

    
if __name__=="__main__":
    m1=[[1,2],[1,-1]]
    w1=[3,-3]

    m2=[[1,2],[2,4]]
    w2=[9,18]

    m3=[[1,0,-1,0,1],[0,2,-1,1,0],[-1,1,-1,1,0],[1,2,0,2,1],[2,0,2,0,-1]]
    w3=[1,2,0,6,3]

    for i in range(4):
        exp=f"print(funkcja(m{i},w{i}))"
        try:
            eval(exp)
        except Exception as e:
            print(e)
    
