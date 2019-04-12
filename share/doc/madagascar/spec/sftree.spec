[sftree]
Cat:    RSF/user/fomels
Desc:   Multiple arrivals with a fast algorithm
DocCmd: sftree | cat
Port:   stdin  rsf r req 	RSF standard input (containing vel data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  a0 float  -  -180. 		first angle (in degrees) 
Param:  da float  -  1. 		angle increment (in degrees) 
Param:  debug enum-bool  -  n 		debugging flag 
Param:  na int  -  361 		number of angles 
Param:  order int  -  3 		accuracy order 
Param:  vel enum-bool  -  y 		y: theinput is velocity; n: slowness 

