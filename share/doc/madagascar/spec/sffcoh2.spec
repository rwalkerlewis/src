[sffcoh2]
Cat:    RSF/user/chen
Desc:   Fast C2 Coherence
DocCmd: sffcoh2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  idip string  -   -  		inline dip (auxiliary output file name)
Param:  max1 int  -  2 		inline slope 
Param:  max2 int  -  2 		xline slope 
Param:  min1 int  -  -2 		
Param:  min2 int  -  -2 		
Param:  ntw int  -  5 		half window size for time direction 
Param:  nxw int  -  5 		half window size for x2 
Param:  twod enum-bool  -  y 		y: only twod coherence 
Param:  verb enum-bool  -  y 		verbosity 
Param:  xdip string  -   -  		crossline dip (auxiliary output file name)

