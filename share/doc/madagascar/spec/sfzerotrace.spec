[sfzerotrace]
Cat:    RSF/user/chenyk
Desc:   Zero part of traces in order to make aliasing
DocCmd: sfzerotrace | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  beg float  -   -  		zero part beginning point 
LDesc:  (defaults to: o2)
Param:  j int  -  2 		jump step between two consecutive zero parts 
Param:  l int  -  1 		length of each zero part 

