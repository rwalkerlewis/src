[sfdtw2]
Cat:    RSF/user/luke
Desc:   
DocCmd: sfdtw2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing _in data)
Port:   stdout rsf w req 	RSF standard output (containing _out data)
Param:  accum string  -   -  		optional output for accumulation errors (auxiliary output file name)
Param:  exp float  -  2 		error exponent (g-f)^exp 
Param:  maxshift int  -   -  		maximum shift to be tested 
Param:  nalter int  -  2 		number of horizontal and vertical smoothings 
Param:  ref string  -   -  		auxiliary input file name
Param:  shifts string  -   -  		optional output for shifts (auxiliary output file name)
Param:  strain1 float  -  1.0 		maximum strain in first axis 
Param:  strain2 float  -  1.0 		maximum strain in second axis, if > 1 no strain limit 

