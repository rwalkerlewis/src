[sfspitz]
Cat:    RSF/user/lcasasan
Desc:   Missing data interpolation in 2-D using F-X Prediction Error Filters
DocCmd: sfspitz | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  norm enum-bool  -  y 		normalization flag 
Param:  ntraces int  -  1 		number of traces to be interpolated 
Param:  order int  -  3 		linear PEF order
Param:  verb enum-bool  -  n 		verbosity flag 

