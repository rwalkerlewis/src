[sfshot2grid]
Cat:    RSF/user/psava
Desc:   Synthesize shot/receiver wavefields for 3-D SR migration
DocCmd: sfshot2grid | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fr data)
Port:   stdout rsf w req 	RSF standard output (containing Frec data)
Port:   swf rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   wav rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dx float  -   -  		x sampling 
Param:  dy float  -  1 		y sampling 
Param:  nx int  -   -  		x samples 
Param:  ny int  -  1 		y samples 
Param:  ox float  -   -  		x origin 
Param:  oy float  -  0 		y origin 

