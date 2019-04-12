[sfdagtaper]
Cat:    RSF/user/aklokov
Desc:   Edge tapering for dip-angle gathers
DocCmd: sfdagtaper | cat
Port:   stdin  rsf r req 	RSF standard input (containing dataFile data)
Port:   stdout rsf w req 	RSF standard output (containing outFile data)
Param:  len float  -   -  		length of the taper function (in degree) 
LDesc:  (defaults to: 5.f)

