[sfmpilsLU]
Cat:    RSF/user/zhiguang
Desc:   Local similarity filter (solving with band matrix LU decomposition and parallelization)
DocCmd: sfmpilsLU | cat
Port:   adj1 rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   adj2 rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   input rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   obs rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   output rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  adjsrc enum-bool  -  n 		use shift instead of stretch 
Param:  dw float  -   -  		omega sampling 
Param:  nw int  -   -  		number of omega values 
Param:  rect1 int  -  50 		smoothing along first axis 
Param:  shift enum-bool  -  n 		use shift instead of stretch 
Param:  verb enum-bool  -  y 		verbosity flag 
Param:  w0 float  -   -  		omega origin 

