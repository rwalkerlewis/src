[sffft3d]
Cat:    RSF/user/psava
Desc:   3D FFT with centering and Hermitian scaling
DocCmd: sffft3d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fi data)
Port:   stdout rsf w req 	RSF standard output (containing Fo data)
Param:  axis int  -  0 		FFT axis or axes 
Param:  cnt enum-bool  -  n 		centering 
Param:  inv enum-bool  -  n 		forward/inverse 
Param:  ompchunk int  -  1 		OpenMP data chunk size 
Param:  verb enum-bool  -  n 		verbosity flag 

