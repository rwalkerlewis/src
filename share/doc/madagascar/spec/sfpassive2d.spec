[sfpassive2d]
Cat:    RSF/user/jsun
Desc:   2-D passive seismic RTM and its adjoint
DocCmd: sfpassive2d | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wave rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  abc enum-bool  -  n 		absorbing boundary condition 
Param:  adj enum-bool  -  n 		adjoint flag, 0: modeling, 1: migration 
Param:  cb float  -   -  		
LDesc:  (defaults to: 0.0f)
Param:  depth int  -  0 		surface 
Param:  dt float  -   -  		
Param:  nt int  -   -  		
Param:  pas enum-bool  -  n 		passive flag, 0: exploding reflector rtm, 1: passive seismic imaging 
Param:  snap int  -  0 		wavefield snapshot flag 
Param:  verb enum-bool  -  n 		verbosity flag 

