[sfsumamp]
Cat:    RSF/user/aklokov
Desc:   Stack energy between two input horizons
DocCmd: sfsumamp | cat
Port:   stdin  rsf r req 	RSF standard input (containing dataFile data)
Port:   stdout rsf w req 	RSF standard output (containing stackFile data)
Param:  badSample float  -   -  		non-interpreted sample in the horizons 
LDesc:  (defaults to: 99999.f)
Param:  bot string  -   -  		bottom horizon (auxiliary input file name)
Param:  top string  -   -  		top horizon (auxiliary input file name)

