[sfps2d]
Cat:    RSF/user/pyang
Desc:   2-D attenuating wavefield simulation using Fourier Pseudo Spectral method
DocCmd: sfps2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fv data)
Port:   stdout rsf w req 	RSF standard output (containing Fw data)
Port:   Qp rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt float  -   -  		time sampling interval 
Param:  fm float  -  20.0 		dominant freq of Ricker wavelet 
Param:  kt int  -   -  		
LDesc:  (defaults to: nt)
Param:  nb int  -  20 		thickness of sponge ABC 
Param:  nt int  -   -  		number of time steps 

