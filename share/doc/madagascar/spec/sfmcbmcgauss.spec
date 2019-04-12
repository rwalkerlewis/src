[sfmcbmcgauss]
Cat:    RSF/user/browaeys
Desc:   Monte Carlo integration of cos(2t).P(x1,x2).P(y1,y2)
DocCmd: sfmcbmcgauss | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  iseed int  -  -33 		random generator seed 
Param:  m1 float  -  0.0 		mean for deviates 
Param:  n int  -  100 		number of random deviates pairs 
Param:  s1 float  -  1.0 		standard deviation for deviates 

