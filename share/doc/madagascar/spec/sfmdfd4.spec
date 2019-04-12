[sfmdfd4]
Cat:    RSF/user/chen
Desc:   2D finite difference modeling	
DocCmd: sfmdfd4 | cat
Port:   stdin  rsf r req 	RSF standard input (containing modl data)
Port:   stdout rsf w req 	RSF standard output (containing data data)
Port:   div rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dr int  -  1 		receiver interval of unit 'dx' 
Param:  dt float  -  0.004 		time interval 
Param:  jt int  -  40 		wave movie time interval 
Param:  nr int  -  1 		receiver numbers 
Param:  nt int  -  1000 		time samples 
Param:  rx0 int  -  0 		x position index of first receiver 
Param:  rz int  -  0 		z position index of receivers 
Param:  sx int  -  0 		x position index of the source 
Param:  sz int  -  0 		z position index of the source 
Param:  w0 float  -  35.0 		central frequency for ricker/harmonic wavelet 
Param:  wave string  -   -  		wavefield movie file (auxiliary output file name)
Param:  wvlt int  -  0 		wavelet type 'ricker/harmonic/other' 

