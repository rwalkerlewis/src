[sfspectra]
Cat:    RSF/system/generic
Desc:   Frequency spectra
DocCmd: sfspectra | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  all enum-bool  -  n 		if y, compute average spectrum for all traces 
Param:  opt enum-bool  -  y 		if y, determine optimal size for efficiency 

