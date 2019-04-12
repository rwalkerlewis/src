[sfslopescan]
Cat:    RSF/user/chen
Desc:   slope estimation by stack scan
DocCmd: sfslopescan | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  nw int  -  5 		window size is 2*nw+1 
Param:  rect1 int  -  2 		window size on the 1st dimension 
Param:  rect2 int  -  2 		window size on the 2nd dimension 

