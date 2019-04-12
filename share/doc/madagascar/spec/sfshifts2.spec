[sfshifts2]
Cat:    RSF/user/zgeng
Desc:   Apply linear time shifts on multiple traces
DocCmd: sfshifts2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing shift data)
Param:  ds int  -   -  		shift sampling 
Param:  s0 int  -   -  		first shift (in number of samples along 1st axis) 

