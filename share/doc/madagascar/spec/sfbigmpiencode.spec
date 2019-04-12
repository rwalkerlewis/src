[sfbigmpiencode]
Cat:    RSF/user/cwp
Desc:   shot encoding with arbitrary phase and amplitude weights using MPI on a distributed cluster
DocCmd: sfbigmpiencode | cat
Port:   encode rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dprefix string  -   -  		printf like statement that can be evaluated to find the data files corresponding to shot records 
Param:  dx float  -   -  		dx of output grid points 
Param:  dy float  -   -  		dy of output grid points 
Param:  eprefix string  -   -  		printf like statement that can be evaluated for the output encodings 
Param:  nx int  -   -  		# of output grid x points 
Param:  ny int  -   -  		# of output grid y points 
Param:  ox float  -   -  		ox of output grid points 
Param:  oy float  -   -  		ox of output grid points 
Param:  shots string  -   -  		shot-file name, dimensions are 1xNS 
Param:  verb enum-bool  -  n 		

