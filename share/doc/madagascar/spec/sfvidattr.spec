[sfvidattr]
Cat:    RSF/user/fomels
Desc:   Slope-based velocity-independent data attributes
DocCmd: sfvidattr | cat
Port:   stdin  rsf r req 	RSF standard input (containing xdip data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   hdip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  half enum-bool  -  y 		if y, the second axis is half-offset instead of full offset 
Param:  what string  -   -  		what attribute to compute 

