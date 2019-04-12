[sfspitzbl]
Cat:    RSF/user/lcasasan
Desc:   Missing data interpolation in 2-D using F-X Prediction Error Filters
DocCmd: sfspitzbl | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  f1 float  -  0.0 		lower  frequency in band limited signal >= 0.0  
Param:  f2 float  -  1.0 		higher frequency in band limited signal <= 1.0  (normalized nyquist)
Param:  norm enum-bool  -  y 		normalization flag 
Param:  ntraces int  -  1 		number of traces to be interpolated 
Param:  order int  -  3 		linear PEF order
Param:  verb enum-bool  -  n 		verbosity flag 

