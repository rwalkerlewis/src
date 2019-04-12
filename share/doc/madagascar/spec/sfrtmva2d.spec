[sfrtmva2d]
Cat:    RSF/user/pyang
Desc:   RTM with checkpointing in 2D acoustic media
DocCmd: sfrtmva2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fv data)
Port:   stdout rsf w req 	RSF standard output (containing Fw data)
Port:   p1 rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   p2 rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   rho rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   tau rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   tauo rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  csdgather enum-bool  -  y 		default, common shot-gather; if n, record at every point
Param:  dt float  -   -  		time sampling interval 
Param:  fm float  -  20.0 		dominant freq of Ricker wavelet 
Param:  gxbeg int  -   -  		x-begining index of receivers, starting from 0 
Param:  gzbeg int  -   -  		z-begining index of receivers, starting from 0 
Param:  jgx int  -  1 		receiver x-axis jump interval 
Param:  jgz int  -  0 		receiver z-axis jump interval 
Param:  jsx int  -   -  		source x-axis  jump interval  
Param:  jsz int  -  0 		source z-axis jump interval  
Param:  kt int  -   -  		output px and pz component at kt 
Param:  nb int  -  20 		thickness of PML ABC 
Param:  ng int  -   -  		number of geophones/receivers per shot 
Param:  nob int  -   -  		number of buffers, default=optimal value 
LDesc:  (defaults to: (int)log2f(nt))
Param:  ns int  -   -  		number of shots 
Param:  nt int  -   -  		number of time steps 
Param:  sxbeg int  -   -  		x-begining index of sources, starting from 0 
Param:  szbeg int  -   -  		z-begining index of sources, starting from 0 
Param:  tdmute int  -   -  		number of deleyed time samples to mute 
LDesc:  (defaults to: 2./(fm*dt))
Param:  verb enum-bool  -  n 		verbosity 
Param:  vmute float  -  1500 		muting velocity to remove the low-freq noise, unit=m/s

