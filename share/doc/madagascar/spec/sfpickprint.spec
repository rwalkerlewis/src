[sfpickprint]
Cat:    RSF/user/zhiguang
Desc:   Write predictive painting result into a txt file
DocCmd: sfpickprint | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   npick rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   pick rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   semblance rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  cut float  -  0. 		muting value in boundary 
Param:  verb enum-bool  -  y 		if y, print icdp/ncdp during operation 

