[sftracealign]
Cat:    RSF/user/jeff
Desc:   None
DocCmd: sftracealign | cat
Port:   stdin  rsf r req 	RSF standard input (containing infile data)
Port:   stdout rsf w req 	RSF standard output (containing outfile data)
Port:   monitor rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   times rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  maxshift   -   -  		Maximum allowed time shift
Param:  nlen   -   -  		Window length of shift vector (in samples)
Param:  vel   -   -  		Rupture speed for linear shift
LDesc:  (defaults to: 1500.)

