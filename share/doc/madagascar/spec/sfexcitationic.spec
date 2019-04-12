[sfexcitationic]
Cat:    RSF/user/pyang
Desc:   Demo for excitation imaging condition
DocCmd: sfexcitationic | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fv data)
Port:   stdout rsf w req 	RSF standard output (containing Fout data)
Param:  csdgather enum-bool  -  y 		
Param:  dt float  -   -  		time sampling interval 
Param:  fm float  -  20.0 		dominant freq of Ricker wavelet 
Param:  gxbeg int  -   -  		x-begining index of receivers, starting from 0 
Param:  gzbeg int  -   -  		z-begining index of receivers, starting from 0 
Param:  jgx int  -  1 		receiver x-axis jump interval 
Param:  jgz int  -  0 		receiver z-axis jump interval 
Param:  jsx int  -   -  		source x-axis  jump interval  
Param:  jsz int  -  0 		source z-axis jump interval  
Param:  kt int  -  300 		output wavefield at time kt 
Param:  nb int  -  20 		thickness of sponge ABC 
Param:  ng int  -   -  		number of receivers 
LDesc:  (defaults to: nx)
Param:  ns int  -  1 		number of shots 
Param:  nt int  -   -  		number of time steps 
Param:  sxbeg int  -   -  		x-begining index of sources, starting from 0 
Param:  szbeg int  -   -  		z-begining index of sources, starting from 0 

