[sfsemblancew]
Cat:    RSF/user/fomels
Desc:   Semblance over the specified axis
DocCmd: sfsemblancew | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  axis int  -  2 		which axis to stack 
Param:  nb int  -  2 		smoothing along the first axis 
Param:  weighted enum-bool  -  n 		if use weighted semblance 

