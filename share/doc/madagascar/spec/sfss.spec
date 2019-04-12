[sfss]
Cat:    RSF/user/chen
Desc:   generate simultaneous sources grid from delay file
DocCmd: sfss | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  d1 float  -  0.004 		original  
Param:  l1 string  -   -  		label 'Time' 
Param:  n1 int  -  1000 		samples 
Param:  o1 float  -  0.0 		sampling interval 
Param:  u1 string  -   -  		unit 's' 

