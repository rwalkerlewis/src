[sflrosrtm2]
Cat:    RSF/user/jsun
Desc:   2-D Low-rank One-step Pre-stack Reverse-Time-Migration
DocCmd: sflrosrtm2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fsrc data)
Port:   stdout rsf w req 	RSF standard output (containing Fimg1 data)
Port:   img2 rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   left rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   leftb rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rec rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   refl rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   right rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rightb rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   tmpbwf rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   tmpwf rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  bot int  -  40 		
Param:  dbg enum-bool  -  n 		debug mode - doesn't propagate receiver wavefield 
Param:  gdep float  -  -1.0 		recorder depth on grid
Param:  gpl int  -   -  		recorder length on index
Param:  gpx int  -   -  		recorder starting location on index
Param:  gpz int  -  0 		recorder depth on index
Param:  lft int  -  40 		
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  rectx int  -  1 		
Param:  rectz int  -  1 		
Param:  repeat int  -  0 		
Param:  rht int  -  40 		Width of abc layer 
Param:  slx float  -  -1.0 		source location x 
Param:  slz float  -  -1.0 		source location z 
Param:  snapinter int  -  10 		snap interval 
Param:  spx int  -  -1 		source location x (index)
Param:  spz int  -  -1 		source location z (index)
Param:  srcill enum-bool  -  y 		true - source illumination; false - receiver illumination 
Param:  srctrunc float  -  0.4 		
Param:  top int  -  40 		
Param:  verb enum-bool  -  n 		verbosity
Param:  wantrecord enum-bool  -  y 		if n, using record data generated by this program 
Param:  wantwf enum-bool  -  n 		output forward and backward wavefield

