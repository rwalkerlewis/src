[sfmpilrrtm_ts]
Cat:    RSF/user/zhiguang
Desc:   One-step lowrank RTM with time-shift imaging condition
DocCmd: sfmpilrrtm_ts | cat
Port:   Fbwf rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Ffwf rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Fimg2 rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Fpadvel rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Fsrc rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dtau float  -   -  		interval of time-shift 
Param:  gpz int  -   -  		depth of geophone 
Param:  nb int  -   -  		padded boundary width 
Param:  ncut int  -  0 		number of cutting samples for generating non-negative source wavelet 
Param:  ndr int  -  1 		receiver interval 
Param:  nds int  -   -  		source interval in number of dx 
Param:  nr0 int  -  0 		receiver starting point in rnx 
Param:  ntau int  -   -  		number of time-shift 
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  path1 string  -   -  		path of left matrices './mat/left' 
Param:  path2 string  -   -  		path of right matrices './mat/left' 
Param:  rectx int  -  2 		source smoothing in x-direction 
Param:  rectz int  -  2 		source smoothing in z-direction 
Param:  repeat int  -  2 		repeat numbers of source smoothing 
Param:  rnx int  -   -  		coverage area of one shot 
Param:  scalet int  -  1 		wavefield storage interval 
Param:  snap int  -  100 		wavefield output interval when wantwf=y 
Param:  snapshot int  -  0 		print out the wavefield snapshots of this shot 
Param:  spx int  -   -  		horizontal location of source 
Param:  spz int  -   -  		depth of source 
Param:  srctrunc float  -  0.4 		source truncation 
Param:  taper int  -  0 		if not 0, tapering in the frequency domain 
Param:  tau0 float  -   -  		origin of time-shift 
Param:  thresh float  -  0.92 		tapering threshold 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  wantwf enum-bool  -  n 		if true, output wavefield of a certain (snapshot=) shot 

