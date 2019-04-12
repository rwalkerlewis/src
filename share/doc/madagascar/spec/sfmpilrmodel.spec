[sfmpilrmodel]
Cat:    RSF/user/zhiguang
Desc:   One-step lowrank modeling
DocCmd: sfmpilrmodel | cat
Port:   Fpadvel rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Fwfld rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  ds float  -   -  		shot interval 
Param:  gpz int  -   -  		depth of geophone 
Param:  nb int  -   -  		boundary width 
Param:  ndr int  -  1 		receiver interval 
Param:  nr int  -   -  		receiver number 
LDesc:  (defaults to: rnx)
Param:  nr0 int  -  0 		receiver origin 
Param:  ns int  -   -  		shot number 
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  path1 string  -   -  		path of left matrices './mat/left' 
Param:  path2 string  -   -  		path of right matrices './mat/left' 
Param:  rectx int  -  2 		source smoothing in x-direction 
Param:  rectz int  -  2 		source smoothing in z-direction 
Param:  repeat int  -  2 		repeat numbers of source smoothing 
Param:  rnx int  -   -  		coverage area of one shot 
Param:  s0 float  -   -  		shot origin 
Param:  scalet int  -  1 		wavefield storage interval 
Param:  snap int  -  100 		wavefield output interval when wantwf=y 
Param:  snapshot int  -  0 		print out the wavefield snapshots of this shot 
Param:  spx int  -   -  		horizontal location of source 
Param:  spz int  -   -  		depth of source 
Param:  srctrunc float  -  0.4 		source truncation 
Param:  wantwf enum-bool  -  n 		want wavefield or not 

