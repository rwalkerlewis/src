[sfjudgechaos]
Cat:    RSF/user/yliu
Desc:   Judgement of chaos
DocCmd: sfjudgechaos | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  delta float  -  0.01 		The cell size of grid
Param:  fixgrid enum-bool  -  n 		if y ,the total size of grid determined by gx 
Param:  gx float  -  2.0 		Total Size of fixed grid
Param:  ma enum-bool  -  n 		if y ,output auxilily file = mask
Param:  mask string  -   -  		auxiliary output file name
Param:  verb enum-bool  -  n 		verbosity flag 

