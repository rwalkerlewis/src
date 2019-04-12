[sfmaskval]
Cat:    RSF/user/bash
Desc:   Mask values inside or outside of a range
DocCmd: sfmaskval | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  lower float  -   -  		lower range limit 
LDesc:  (defaults to: -FLT_MAX)
Param:  lowerval float  -   -  		lower range value 
LDesc:  (defaults to: -FLT_MAX)
Param:  upper float  -   -  		upper range limit 
LDesc:  (defaults to: +FLT_MAX)
Param:  upperval float  -   -  		upper range value 
LDesc:  (defaults to: +FLT_MAX)

