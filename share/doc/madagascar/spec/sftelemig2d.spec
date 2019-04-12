[sftelemig2d]
Cat:    RSF/user/jeff
Desc:   None
DocCmd: sftelemig2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing infile data)
Port:   stdout rsf w req 	RSF standard output (containing outfile data)
Port:   Svel rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   cig rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   rwf rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   swf rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps   -   -  		Taper on the side boundaries (npts)
LDesc:  (defaults to: 0.01)
Param:  forward   -   -  		Forward scattering (T/F)
LDesc:  (defaults to: n)
Param:  nh   -   -  		Number of subsurface offsets (between 1 and 128)
LDesc:  (defaults to: 0)
Param:  ntaper   -   -  		Taper on the side boundaries (npts)
LDesc:  (defaults to: 40)
Param:  source_norm   -   -  		Normalize the image by the power of the SWF (T/F)
LDesc:  (defaults to: n)
Param:  verbose   -   -  		Verbose (T/F)
LDesc:  (defaults to: n)

