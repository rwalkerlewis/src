[sfshift]
Cat:    RSF/user/psava
Desc:   Fourier-domain shift in 1,2 and 3 dimensions
DocCmd: sfshift | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fi data)
Port:   stdout rsf w req 	RSF standard output (containing Fo data)
Param:  del1 float  -  0. 		delay on axis 1 
Param:  del2 float  -  0. 		delay on axis 2 
Param:  del3 float  -  0. 		delay on axis 3 
Param:  ompchunk int  -  1 		OpenMP data chunk size 
Param:  verb enum-bool  -  n 		verbosity flag 

