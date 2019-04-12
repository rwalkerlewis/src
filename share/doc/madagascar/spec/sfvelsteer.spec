[sfvelsteer]
Cat:    RSF/user/browaeys
Desc:   Velocity steering for 2D receivers array
DocCmd: sfvelsteer | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dvx float  -   -  		vx sampling 
Param:  dvy float  -   -  		vy sampling 
Param:  iypi int  -  0 		first depth position where velocity steering is computed 
Param:  iyps int  -   -  		last depth position where velocity steering is computed 
LDesc:  (defaults to: ny-1)
Param:  nvx int  -   -  		number of vx values 
Param:  nvy int  -   -  		number of vy values 
Param:  ovx float  -   -  		vx origin 
Param:  ovy float  -   -  		vy origin 
Param:  xp float  -   -  		lateral position where velocity steering is computed 

