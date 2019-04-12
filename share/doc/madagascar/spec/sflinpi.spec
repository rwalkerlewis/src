[sflinpi]
Cat:    RSF/user/dmerzlikin
Desc:   3D Path-Summation Integral Operator as a Linear Filter
DocCmd: sflinpi | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  eps float  -  0.001 		
Param:  epst2 float  -  0.001 		
Param:  pad int  -   -  		output time samples 
LDesc:  (defaults to: nt)
Param:  passthr float  -  0.001 		
Param:  v_1 float  -   -  		path-integral range 
Param:  v_2 float  -   -  		
Param:  v_3 float  -   -  		
Param:  v_4 float  -   -  		

