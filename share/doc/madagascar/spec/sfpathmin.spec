[sfpathmin]
Cat:    RSF/user/luke
Desc:   One dimensional path minimization for optimization input file has first coordinate parameter, second coordinate time
DocCmd: sfpathmin | cat
Port:   stdin  rsf r req 	RSF standard input (containing _in data)
Port:   stdout rsf w req 	RSF standard output (containing _out data)
Param:  aniso1 float  -   -  		aniso of 2nd axis relative to first   
LDesc:  (defaults to: D[1]/D[0])
Param:  damp float  -  .5 		if the path goes out of bounds, we reflect and dampen the rate of change by this much 
Param:  dorder int  -  6 		derivative order 
Param:  eps float  -  0. 		if the change and gradient are simultaneously lower than this, terminate  early 
Param:  g float  -  .1 		scaling the gradient by how much 
Param:  k float  -  1 		stiffness relative to attraction
Param:  kink float  -  1 		resistance to kinks  
Param:  knots int  -  11 		number of knots 
Param:  lr float  -  .3 		learning rate 
Param:  niter int  -  10 		
Param:  nsmooth int  -  1 		number of gradient smoothings  
Param:  shove float  -  1000 		size of initial random lateral shove 
Param:  srad int  -  2 		smoothing radius for gradient 

