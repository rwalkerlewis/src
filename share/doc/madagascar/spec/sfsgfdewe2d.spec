[sfsgfdewe2d]
Cat:    RSF/user/zhiguang
Desc:   2-D staggered-grid elastic time-domain FD modeling
DocCmd: sfsgfdewe2d | cat
Port:   datax rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   dataz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   rho rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vp rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vs rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dshot int  -  1 		shot interval, multiple of receiver intervals 
Param:  dt float  -   -  		time interval 
Param:  hsz int  -  5 		vertical position of recerivers 
Param:  nabs int  -  50 		width of padded boundary 
Param:  nshot int  -  1 		number of shots 
Param:  nx int  -   -  		coverage area for each shot 
LDesc:  (defaults to: nvx)
Param:  peak float  -  20 		peak frequency for Ricker wavelet (in Hz) 
Param:  sx_ini int  -   -  		horizontal position of shot point 
Param:  sz_ini int  -  5 		vertical position of shot point 
Param:  tmax float  -   -  		record length 

