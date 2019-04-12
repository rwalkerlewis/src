[sfofsemb]
Cat:    RSF/user/fomels
Desc:   Objective function of dip estimation with semblance
DocCmd: sfofsemb | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing of data)
Param:  dp float  -   -  		dip sampling 
LDesc:  (defaults to: 2*p0/(1.-np))
Param:  np int  -  100 		number of dips 
Param:  p0 float  -   -  		dip origin 

