[sfinternalmult]
Cat:    RSF/user/yliu
Desc:   Generate internal multiples by using virtual seismic data
DocCmd: sfinternalmult | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  both enum-bool  -  n 		receiver flag, if y, receiver with both sides 
Param:  dif string  -   -  		auxiliary input file name
Param:  jumpo int  -  1 		jump in offset dimension, only for stack=n 
Param:  jumps int  -  1 		jump in shot dimension, only for stack=n  
Param:  stack enum-bool  -  n 		stack flag, if y, no common multiple gather 
Param:  verb enum-bool  -  n 		verbosity flag 

