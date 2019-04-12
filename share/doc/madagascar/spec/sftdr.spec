[sftdr]
Cat:    RSF/user/sbader
Desc:   
DocCmd: sftdr | cat
Port:   stdin  rsf r req 	RSF standard input (containing sonica data)
Port:   stdout rsf w req 	RSF standard output (containing tdrFo data)
Port:   sonicFo rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dels float  -   -  		Depth step (units of m or ft)
Param:  ms int  -   -  		(0 = Units of sonic in s); (1 = Units of sonic in ms)
Param:  stretch float  -   -  		(0 = Output TDR from input sonic log); (1 = Output updated sonic and TDR)
Param:  tdrNew string  -   -  		

