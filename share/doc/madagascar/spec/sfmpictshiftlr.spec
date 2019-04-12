[sfmpictshiftlr]
Cat:    RSF/user/zhiguang
Desc:   Correct time-shift gathers with two-step lowrank propagator
DocCmd: sfmpictshiftlr | cat
Port:   left rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   right rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  abc enum-bool  -  y 		absorbing boundary condition 
Param:  cmplx enum-bool  -  n 		use complex FFT 
Param:  dt float  -  0.001 		time interval 
Param:  nb int  -  60 		boundary width 
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  par float  -  0.01 		absorbing boundary coefficient 
Param:  taper enum-bool  -  y 		tapering 
Param:  thresh float  -  0.92 		thresholding 

