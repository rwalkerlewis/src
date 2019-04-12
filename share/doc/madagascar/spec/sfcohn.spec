[sfcohn]
Cat:    RSF/user/pyang
Desc:   Coherence calculations in the presence of structural dip
DocCmd: sfcohn | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dp1 float  -  0.5 		
Param:  dp2 float  -  0.5 		
Param:  idip string  -   -  		inline dip (auxiliary output file name)
Param:  mode string  -   -  		coherence mode: c1, c2, c3 
Param:  np1 int  -  9 		inline slope 
Param:  np2 int  -  9 		xline slope 
Param:  ntw int  -  5 		half window size for coherence 
Param:  nxw int  -  5 		half window size for coherence 
Param:  nyw int  -  5 		half window size for coherence 
Param:  op1 float  -  -2.0 		
Param:  op2 float  -  -2.0 		
Param:  twod enum-bool  -  y 		y: only twod coherence 
Param:  verb enum-bool  -  y 		verbosity 
Param:  xdip string  -   -  		crossline dip (auxiliary output file name)

