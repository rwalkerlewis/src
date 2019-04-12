[sfdtw]
Cat:    RSF/user/luke
Desc:   
DocCmd: sfdtw | cat
Port:   stdin  rsf r req 	RSF standard input (containing _in data)
Port:   stdout rsf w req 	RSF standard output (containing _out data)
Param:  accum string  -   -  		accumulation errors from forward and backtracking (auxiliary output file name)
Param:  error string  -   -  		misfit error (auxiliary output file name)
Param:  exp float  -  2 		error exponent (g-f)^exp 
Param:  maxshift int  -   -  		
Param:  ref string  -   -  		auxiliary input file name
Param:  shifts string  -   -  		output integer shifts as floats (auxiliary output file name)
Param:  strain float  -  1.0 		maximum strain 

