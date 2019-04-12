[sfewefd2d_gpu_dev]
Cat:    RSF/user/rweiss
Desc:   2D elastic time-domain FD modeling with GPU (with experimental functionalities)
DocCmd: sfewefd2d_gpu_dev | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fwav data)
Port:   stdout rsf w req 	RSF standard output (containing Fdat data)
Port:   ccc rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   den rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rec rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sou rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   um rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   uo rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wfl rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dabc enum-bool  -  n 		absorbing BC 
Param:  free enum-bool  -  n 		free surface flag 
Param:  gpu int  -  0 		ID of the GPU to be used 
Param:  jdata int  -  1 		extract receiver data every jdata time steps 
Param:  jsnap int  -   -  		save wavefield every jsnap time steps 
LDesc:  (defaults to: nt)
Param:  nbell int  -  5 		bell size 
Param:  snap enum-bool  -  n 		wavefield snapshots flag 
Param:  ssou enum-bool  -  n 		stress source 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  wavSrc enum-bool  -  y 		if yes, look for a source wavelet.  if no, look for initial displacement fields (uo and um) 

