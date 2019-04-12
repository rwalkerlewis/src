[sfztrace]
Cat:    RSF/user/fomels
Desc:   Multiple arrivals by depth marching
DocCmd: sfztrace | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Param:  a0 float  -  -90. 		starting angle (in degrees) 
Param:  da float  -  0.5 		angle increment (in degrees) 
Param:  iorder int  -  4 		interpolation accuracy for grid 
Param:  na int  -  362 		number of angles 
Param:  nt int  -   -  		ray length bound 
LDesc:  (defaults to: nx*nz)
Param:  order int  -  3 		interpolation accuracy for velocity 
Param:  vel enum-bool  -  y 		y, input is velocity; n, slowness 

