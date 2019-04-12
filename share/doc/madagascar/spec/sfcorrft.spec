[sfcorrft]
Cat:    RSF/user/saragiotis
Desc:   Trace-by-trace or data-by-trace correlation using Fourier transform
DocCmd: sfcorrft | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing corr data)
Param:  axis int  -  1 		across which axis to correlate.
Param:  other string  -   -  		auxiliary input file name

