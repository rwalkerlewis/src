[sfseisxwell]
Cat:    RSF/user/yliu
Desc:   Select seismic data cross well position
DocCmd: sfseisxwell | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  nw int  -  0 		number of well points 
Param:  path string  -   -  		auxiliary output file name
Param:  well string  -   -  		auxiliary input file name
Param:  wx float-list  -   -  		well x coordinates  [nw]
Param:  wy float-list  -   -  		well y coordinates  [nw]

