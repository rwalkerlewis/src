[sfafac]
Cat:    RSF/user/gee
Desc:   Wilson-Burg factorization
DocCmd: sfafac | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fa data)
Port:   stdout rsf w req 	RSF standard output (containing Ff data)
Param:  lag string  -   -  		auxiliary output file name
Param:  nf int  -  32 		factor coefficients 
Param:  niter int  -  20 		Wilson iterations 
Param:  nn int  -  1000 		Helix diameter 
Param:  ompchunk int  -  1 		OMP chunk size 
Param:  stable enum-bool  -  n 		stability flag 
Param:  verb enum-bool  -  n 		verbosity flag 

