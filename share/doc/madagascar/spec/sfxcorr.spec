[sfxcorr]
Cat:    RSF/user/chenyk
Desc:   Cross-correlation function
DocCmd: sfxcorr | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   match rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  l int  -   -  		maxlag of auto/cross correlation function
LDesc:  (defaults to: n1y-1)
Param:  lagfile string  -   -  		auxiliary output file name

