[sfmodrefl3]
Cat:    RSF/system/seismic
Desc:   Normal reflectivity modeling
DocCmd: sfmodrefl3 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dp float  -   -  		slope sampling 
Param:  dt float  -   -  		time sampling 
Param:  eps float  -  0.01 		stretch regularization 
Param:  moveout enum-bool  -  y 		if apply moveout 
Param:  np int  -   -  		slope samples 
Param:  nt int  -   -  		time samples 
Param:  p0 float  -   -  		slope origin 
Param:  sparse int  -  10 		sparseness of reflectivity 

