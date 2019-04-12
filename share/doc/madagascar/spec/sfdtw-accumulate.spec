[sfdtw-accumulate]
Cat:    RSF/user/luke
Desc:   
DocCmd: sfdtw-accumulate | cat
Port:   stdin  rsf r req 	RSF standard input (containing _in data)
Port:   stdout rsf w req 	RSF standard output (containing _out data)
Param:  dir int  -  0 		accumulation direction: 1 is forward, -1 is backward, 0 is both 
Param:  strain float  -  1 		maximum strain 

