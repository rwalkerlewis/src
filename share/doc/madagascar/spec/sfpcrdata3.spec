[sfpcrdata3]
Cat:    RSF/user/cram
Desc:   Prepare data for 3-D angle-domain migration
DocCmd: sfpcrdata3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing data data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  KMAH enum-bool  -  y 		y - account for phase shifts due to KMAH index 
Param:  diff enum-bool  -  y 		y - apply differentiation 
Param:  erefl enum-bool  -  n 		y - assume data modeled with exploding reflector 
Param:  filter enum-bool  -  y 		y - antialiasing filter for data 
Param:  verb enum-bool  -  n 		verbosity flag 

