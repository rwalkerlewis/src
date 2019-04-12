[sfrevent]
Cat:    RSF/user/aklokov
Desc:   Compute reflection event
DocCmd: sfrevent | cat
Port:   stdin  rsf r req 	RSF standard input (containing reflFile data)
Port:   stdout rsf w req 	RSF standard output (containing dataFile data)
Param:  deriv string  -   -  		first derivative estimated along the reflection boundary (auxiliary input file name)
Param:  eps float  -   -  		receiver position accuracy (in km) 
LDesc:  (defaults to: 0.5 * hStep)
Param:  hd float  -   -  		step in offset (in km) 
LDesc:  (defaults to: 0.05f)
Param:  hn int  -  51 		number of offsets 
Param:  ho float  -   -  		start offset (in s) 
LDesc:  (defaults to: 0.f)
Param:  sd float  -   -  		step in source position (in km) 
LDesc:  (defaults to: 0.025f)
Param:  sn int  -  1 		number of sources 
Param:  so float  -   -  		start source position (in s) 
LDesc:  (defaults to: 0.f)
Param:  td float  -   -  		step in time (in s) 
LDesc:  (defaults to: 0.004f)
Param:  tn int  -  1001 		number of time samples 
Param:  to float  -   -  		start time (in s) 
LDesc:  (defaults to: 0.f)
Param:  vel float  -   -  		constant velocity value (in km/s) 
LDesc:  (defaults to: 2.f)

