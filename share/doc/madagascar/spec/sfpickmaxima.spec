[sfpickmaxima]
Cat:    RSF/user/zhiguang
Desc:   Picking local maxima on the first axis with evenly spaced windows
DocCmd: sfpickmaxima | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   npicks rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   semblance rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  max float  -   -  		maximum value of time 
LDesc:  (defaults to: o1+(n1-1)*d1)
Param:  min float  -   -  		minimum value of time 
LDesc:  (defaults to: o1)
Param:  np int  -   -  		maximum number of picks 
LDesc:  (defaults to: n1)
Param:  nw int  -  1 		number of windows 
Param:  parab enum-bool  -  n 		if y, parabolic interpolation 
Param:  removal enum-bool  -  y 		if y, remove adjacent events based on semblance 
Param:  space float  -  100. 		minimum distance bewteen picked events 

