[sfweiajs]
Cat:    RSF/user/psava
Desc:   Adjoint source construction for image-domain waveform tomography
DocCmd: sfweiajs | cat
Port:   stdin  rsf r req 	RSF standard input (containing Feic data)
Port:   stdout rsf w req 	RSF standard output (containing Faso data)
Port:   bwf rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   coo rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  conj enum-bool  -   -  		flag 
Param:  irun string  -   -  		
Param:  verb enum-bool  -  n 		verbosity flag 

