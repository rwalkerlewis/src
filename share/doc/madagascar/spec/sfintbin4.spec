[sfintbin4]
Cat:    RSF/user/yliu
Desc:   5-D data binning
DocCmd: sfintbin4 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dr int  -  1 		
Param:  ds int  -  1 		
Param:  dx int  -  1 		
Param:  dy int  -  1 		
Param:  fold string  -   -  		output fold file 
Param:  head string  -   -  		header file 
Param:  rk string  -   -  		r key name 
Param:  rkey int  -   -  		r key number (if no rk), default is gwdep 
Param:  rmax int  -   -  		r maximum 
Param:  rmin int  -   -  		r minimum 
Param:  sk string  -   -  		s key name 
Param:  skey int  -   -  		s key number (if no sk), default is swdep 
Param:  smax int  -   -  		s maximum 
Param:  smin int  -   -  		s minimum 
Param:  xk string  -   -  		x key name 
Param:  xkey int  -   -  		x key number (if no xk), default is fldr 
Param:  xmax int  -   -  		x maximum 
Param:  xmin int  -   -  		x minimum 
Param:  yk string  -   -  		y key name 
Param:  ykey int  -   -  		y key number (if no yk), default is tracf 
Param:  ymax int  -   -  		y maximum 
Param:  ymin int  -   -  		y minimum 

