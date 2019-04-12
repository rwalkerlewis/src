[sfwinscan]
Cat:    RSF/user/yliu
Desc:   Picking scanned data window trace by trace with fixed t0
DocCmd: sfwinscan | cat
Port:   stdin  rsf r req 	RSF standard input (containing cmp data)
Port:   stdout rsf w req 	RSF standard output (containing outf data)
Param:  deltav float  -  20 		step lenth for velocity scan 
Param:  n int  -  100 		numbers of velscan
Param:  t0 float  -  0.5 		t0 fixed 
Param:  v0 float  -  1000 		init Vel for velocity scan 
Param:  winsz int  -  200 		for each trace,the width of window. unit:sample point 

