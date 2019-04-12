[sfanalytical]
Cat:    RSF/user/fomels
Desc:   First-arrival traveltime table using analytical traveltimes
DocCmd: sfanalytical | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  order int  -  3 		interpolation accuracy for velocity 
Param:  vel enum-bool  -  y 		y, input is velocity; n, slowness 
Param:  yshot float  -   -  		
LDesc:  (defaults to: x0 + 0.5*(nx-1)*dx)
Param:  zshot float  -   -  		read velocity or slowness 
LDesc:  (defaults to: z0)

