[sfofpwd]
Cat:    RSF/user/pwd
Desc:   Objective function of dip estimation with PWD filters
DocCmd: sfofpwd | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing of data)
Param:  dp float  -   -  		dip sampling 
LDesc:  (defaults to: 2*p0/(1.-np))
Param:  nj int  -  1 		antialiasing 
Param:  np int  -  100 		number of dips 
Param:  order int  -  1 		accuracy order 
Param:  p0 float  -   -  		dip origin 

