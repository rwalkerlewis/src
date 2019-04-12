[sfmatch1d]
Cat:    RSF/user/lcasasan
Desc:   1D Least-Sqaure Adaptive Matched-Filter for Multiple Suppression
DocCmd: sfmatch1d | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  eps float  -  0.01 		dumping parameter  
Param:  method string  -   -  		method to use (old,new) 
Param:  multiple string  -   -  		auxiliary input file name
Param:  order int  -   -  		matchied-filter order 
LDesc:  (defaults to: w1-2)
Param:  transient enum-bool  -  n 		transient convolution [y/n] 
Param:  verb enum-bool  -  n 		
Param:  w1 int  -  9 		data window length along 1st dimentions (time/depth) 
Param:  w2 int  -  3 		data window length along 1st dimentions (time/depth) 

