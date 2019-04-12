[sfofpwd2]
Cat:    RSF/user/pwd
Desc:   Objective function of two dips estimation with PWD filters
DocCmd: sfofpwd2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing of data)
Param:  dp float  -   -  		first dip sampling 
LDesc:  (defaults to: 2*p0/(1.-np))
Param:  dq float  -   -  		second dip sampling 
LDesc:  (defaults to: 2*q0/(1.-nq))
Param:  nj int  -  1 		antialiasing 
Param:  np int  -  100 		number of dips 
Param:  nq int  -  100 		number of dips 
Param:  order int  -  1 		accuracy order 
Param:  p0 float  -   -  		first dip origin 
Param:  q0 float  -   -  		second dip origin 

