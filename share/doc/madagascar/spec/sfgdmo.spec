[sfgdmo]
Cat:    RSF/system/seismic
Desc:   Gardner's DMO for regularly sampled 2-D data (slow method)
DocCmd: sfgdmo | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  b0 float  -  -85 		first angle 
Param:  db float  -  1 		angle increment 
Param:  eps float  -  0.01 		stretch regularization 
Param:  nb int  -  171 		number of angles 

