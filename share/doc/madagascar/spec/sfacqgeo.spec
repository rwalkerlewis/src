[sfacqgeo]
Cat:    RSF/user/jsun
Desc:   generating acquisition geometry file for sfmpicfftrtm
DocCmd: sfacqgeo | cat
Port:   stdout rsf w req 	RSF standard output (containing Fgeo data)
Param:  noff int  -   -  		near offset 
Param:  npad int  -   -  		computational domain padding 
Param:  nx int  -   -  		dimension in x 
Param:  ny int  -   -  		dimension in y 
Param:  nz int  -   -  		dimension in z 
Param:  rec_nx int  -   -  		number of receivers in x   
Param:  rec_ny int  -   -  		number of receivers in y   
Param:  rec_z int  -   -  		receiver position in depth 
Param:  roll int  -   -  		acquisition pattern: 0-> fixed-spread, 1-> towed-streamer to the negative 
Param:  sou_jx int  -   -  		source interval in x 
LDesc:  (defaults to: (sou_nx>1)? (nx-sou_ox)/(sou_nx-1):0)
Param:  sou_jy int  -   -  		source interval in y 
LDesc:  (defaults to: (sou_ny>1)? (ny-sou_oy)/(sou_ny-1):0)
Param:  sou_nx int  -   -  		number of sources in x        
Param:  sou_ny int  -   -  		number of sources in y        
Param:  sou_ox int  -   -  		source starting location in x 
Param:  sou_oy int  -   -  		source starting location in y 
Param:  sou_z int  -   -  		source position in depth      

