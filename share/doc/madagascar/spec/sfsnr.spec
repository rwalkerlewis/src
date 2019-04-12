[sfsnr]
Cat:    RSF/user/yliu
Desc:   Display dataset signal-noise-ratio
DocCmd: sfsnr | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Param:  nsw1 int  -  1 		sample-window beginning position (default=1)
Param:  nsw2 int  -   -  		sample-window end position (default=n1)
LDesc:  (defaults to: n1)
Param:  ntw1 int  -  1 		trace-window beginning position (default=1)
Param:  ntw2 int  -   -  		trace-window end position (default=n2)
LDesc:  (defaults to: n2)
Param:  type string  -   -  		[stack] method type, the default is stack 

