[sfpdrscan2d]
Cat:    RSF/user/aklokov
Desc:   Velocity Scan by 2D Parametric Development of Reflections
DocCmd: sfpdrscan2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing dataFile data)
Port:   stdout rsf w req 	RSF standard output (containing outFile data)
Param:  aux string  -   -  		output file containing semblance measure of CIGs stacking (auxiliary output file name)
Param:  pd float  -   -  		increment of positions in stack section 
LDesc:  (defaults to: recStep_)
Param:  pn int  -   -  		number of positions in stack section 
LDesc:  (defaults to: recNum_)
Param:  po float  -   -  		start position in stack section 
LDesc:  (defaults to: shotStart_)
Param:  vd float  -  50 		increment of velocities 
Param:  vn int  -  1 		number of scanned velocities  
Param:  vo float  -  1500 		start velocity 
Param:  wh int  -  11 		height of a vertical window for semblance calculation 

