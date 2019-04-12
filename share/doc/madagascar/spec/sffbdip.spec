[sffbdip]
Cat:    RSF/user/chen
Desc:   omnidirectional dip estimation
DocCmd: sffbdip | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  eta float  -  0.75 		steps for iteration 
Param:  idip float  -  0.0 		initial dip 
Param:  liter int  -  20 		number of linear iterations 
Param:  niter int  -  5 		number of iterations 
Param:  radius float  -  1.0 		interpolating radius for opwd 
Param:  rect1 int  -  0 		dip smoothness on 1st axis 
Param:  rect2 int  -  0 		dip smoothness on 2nd axis 
Param:  verb enum-bool  -  n 		verbosity flag 

