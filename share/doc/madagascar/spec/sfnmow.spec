[sfnmow]
Cat:    RSF/system/seismic
Desc:   Least-squares fitting of t^2-t_0^2 surfaces for elliptical slowness matrix, W
DocCmd: sfnmow | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  half enum-bool  -  y 		if y, the second axis is half-offset instead of full offset 
Param:  nw int  -  3 		
Param:  offset string  -   -  		If offset file is provided, it must be of the form:(auxiliary input file name)

