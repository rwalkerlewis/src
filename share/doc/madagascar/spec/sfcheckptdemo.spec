[sfcheckptdemo]
Cat:    RSF/user/pyang
Desc:   RTM with checkpointing in 2D acoustic media
DocCmd: sfcheckptdemo | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fv data)
Port:   stdout rsf w req 	RSF standard output (containing Fw data)
Port:   p1 rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   p2 rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dt float  -   -  		time sampling interval 
Param:  fm float  -  20.0 		dominant freq of Ricker wavelet 
Param:  ft int  -  0 		first recorded time 
Param:  jt int  -  1 		time interval 
Param:  kt int  -   -  		output px and pz component at kt 
Param:  nb int  -  20 		thickness of PML ABC 
Param:  nob int  -   -  		number of buffers, default=optimal value 
LDesc:  (defaults to: (int)log2f(nt))
Param:  nt int  -   -  		number of time steps 
Param:  verb enum-bool  -  n 		verbosity, if y, output px and pz 

