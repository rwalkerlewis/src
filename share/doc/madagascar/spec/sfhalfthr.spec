[sfhalfthr]
Cat:    RSF/user/chenyk
Desc:   Half thresholding using exact-value or percentile thresholding
DocCmd: sfhalfthr | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  ifperc int  -  1 		0, exact-value thresholding; 1, percentile thresholding. 
Param:  ifverb int  -  0 		0, not print threshold value; 1, print threshold value. 
Param:  other string  -   -  		auxiliary output file name
Param:  thr float  -   -  		thresholding level 

