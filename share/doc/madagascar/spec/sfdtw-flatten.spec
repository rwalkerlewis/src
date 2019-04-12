[sfdtw-flatten]
Cat:    RSF/user/luke
Desc:   flattens a gather or similar object to its stack using dtw, optionally writes out shifts, currently set up for (time,gather,space) for 2d imaging
DocCmd: sfdtw-flatten | cat
Port:   stdin  rsf r req 	RSF standard input (containing _in data)
Port:   stdout rsf w req 	RSF standard output (containing _out data)
Param:  exp float  -  2 		error exponent (g-f)^exp 
Param:  maxshift int  -   -  		
Param:  shifts string  -   -  		output gather flattening shifts (auxiliary output file name)
Param:  strain float  -  1.0 		maximum strain 

