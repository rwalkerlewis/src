[sfzero]
Cat:    RSF/user/fomels
Desc:   Zero crossings with sub-pixel resolution
DocCmd: sfzero | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   nzero rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  down enum-bool  -  n 		only zeros on the way down 
Param:  nw int  -  4 		Interpolation accuracy 

