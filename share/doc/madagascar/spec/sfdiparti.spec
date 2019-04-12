[sfdiparti]
Cat:    RSF/user/aklokov
Desc:   diparti
DocCmd: sfdiparti | cat
Port:   stdin  rsf r req 	RSF standard input (containing piFile data)
Port:   stdout rsf w req 	RSF standard output (containing resFile data)
Param:  apert float  -  1000 		diffraction summation aperture 
Param:  gamma float  -   -  		velocity-model-accuracy parameter 
LDesc:  (defaults to: 1.f)
Param:  itd float  -   -  		step in time (in ms) 
LDesc:  (defaults to: tStep_)
Param:  itn int  -   -  		number of imaged depth samples 
LDesc:  (defaults to: tNum_)
Param:  ito float  -   -  		first imaged time (in ms) 
LDesc:  (defaults to: tStart_)
Param:  ixd float  -   -  		step in positions (in m) 
LDesc:  (defaults to: xStep_)
Param:  ixn int  -   -  		number of imaged positions 
LDesc:  (defaults to: xNum_)
Param:  ixo float  -   -  		first imaged position (in m) 
LDesc:  (defaults to: xStart_)
Param:  ppd float  -   -  		step in processed partial images 
LDesc:  (defaults to: dipStep_)
Param:  ppn int  -   -  		number of processed partial images 
LDesc:  (defaults to: dipNum_)
Param:  ppo float  -   -  		first processed partial image 
LDesc:  (defaults to: dipStart_)
Param:  semb string  -   -  		output file containing semblance (auxiliary output file name)
Param:  sembWindow int  -  11 		vertical window for semblance calculation (in samples) 
Param:  vel string  -   -  		velocity model file (velocity in km/s) (auxiliary input file name)

