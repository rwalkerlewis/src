[sfdvscan2d]
Cat:    RSF/user/aklokov
Desc:   Diffraction velocity analysis
DocCmd: sfdvscan2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing dataFile_ data)
Port:   stdout rsf w req 	RSF standard output (containing sembFile_ data)
Param:  cigNum int  -  1 		height of a vertical window for semblance calculation 
Param:  coher int  -  11 		height of a vertical window for semblance calculation 
Param:  dlim float  -   -  		defines dip-angle-window for the analysis 
LDesc:  (defaults to: fabs (dipStart_))
Param:  gd float  -  1 		increment of Vm/V parameter 
Param:  gn int  -  1 		number of scanned Vm/V values  
Param:  go float  -  1.0 		start of Vm/V parameter 
Param:  isSemb enum-bool  -  y 		y - output is semblance; n - stack power 
Param:  vel string  -   -  		velocity model file (velocity in km/s) (auxiliary input file name)

