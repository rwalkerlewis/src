[sfptaupmo3]
Cat:    RSF/system/seismic
Desc:   Slope-based tau-p 3D moveout
DocCmd: sfptaupmo3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (containing nmod data)
Param:  dip1 string  -   -  		slope field mesaure along dimension 2(auxiliary input file name)
Param:  dip2 string  -   -  		slope field mesaure along dimension 3(auxiliary input file name)
Param:  eps float  -  0.01 		stretch regularization 
Param:  tau0 string  -   -  		tau0(tau,p) (auxiliary output file name)

