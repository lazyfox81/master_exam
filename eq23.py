from math import sqrt

Q=60 #л/мин
Pn=20 #mPa
Q=Q*.001/60
print("Q=",Q, "m3/s")

Pi=3.14
Vd=5 #м/с

dy=sqrt(4*Q/(Pi*Vd))
# dy=20/1000 #m
print("dy=",dy*1000 , "mm")

ksi=.6
dz=1.13*sqrt(Q/((1-ksi*ksi)*Vd))
# dz=20/1000 #m
print("dz=",dz*1000 , "mm")