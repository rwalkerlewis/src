[sftslread]
Cat:    RSF/user/yliu
Desc:   Convert a TSL (MT, V5-2000 of Phoenix Geophysics) dataset to RSF
DocCmd: sftslread | cat
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  data string  -   -  		input data 
Param:  format enum-bool  -  n 		data format: [false] (TSL,TSH: 16) or [true] (TSn: 32) 
Param:  tfile string  -   -  		auxiliary output file name

