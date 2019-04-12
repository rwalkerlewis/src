[sfcompensate]
Cat:    RSF/user/jsun
Desc:   Complex-valued compensation (between two wavefields)
DocCmd: sfcompensate | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fnum data)
Port:   stdout rsf w req 	RSF standard output (containing Fres data)
Port:   den rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  cmplx enum-bool  -  y 		use complex i/o 
Param:  perc float  -  0.1 		precentage (of max) for protection when dividing 
Param:  verb enum-bool  -  n 		verbosity 

