[sfmkcmp]
Cat:    RSF/user/yliu
Desc:   Make a synthtic two-layer CMP gather with known t0
DocCmd: sfmkcmp | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing spcmp data)
Param:  dt float  -  0.001 		sampling on 1-th axis(time)
Param:  dx float  -  50 		sampling on 2-th axis(offset)
Param:  n1 int  -  1000 		number of n1
Param:  n2 int  -  20 		number of n2
Param:  o1 float  -  0 		
Param:  o2 float  -  0 		
Param:  t01 float  -  0.4 		t01 start point 
Param:  t02 float  -  0.8 		t02 start point 
Param:  v01 float  -  1000 		first event rms vel 
Param:  v02 float  -  1000 		second event rms vel 
Param:  verb enum-bool  -  n 		dimensions 

