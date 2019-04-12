[sflint1]
Cat:    RSF/user/gee
Desc:   Linear interpolation
DocCmd: sflint1 | cat
Port:   stdin  rsf r req 	RSF standard input (containing dat data)
Port:   stdout rsf w req 	RSF standard output (containing mod data)
Port:   coord rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  d1 float  -   -  		regular axis sampling (for adj=y) 
Param:  n1 int  -   -  		regular axis size (for adj=y) 
Param:  o1 float  -   -  		regular axis origin (for adj=y) 

