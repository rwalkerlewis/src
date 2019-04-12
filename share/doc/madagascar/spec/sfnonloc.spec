[sfnonloc]
Cat:    RSF/user/yliu
Desc:   Non-local (Bilateral) smoothing
DocCmd: sfnonloc | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  ax float  -   -  		Gaussian weight for the range distance 
Param:  bx float  -   -  		exponential weight for the domain distance (different if gaussian)
Param:  gauss enum-bool  -  n 		if y, Gaussian weight, whereas Triangle weight 
Param:  ns int  -   -  		spray radius 
Param:  repeat int  -  1 		repeat filtering several times 

