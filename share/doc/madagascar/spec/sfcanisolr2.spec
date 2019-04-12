[sfcanisolr2]
Cat:    RSF/user/jsun
Desc:   Lowrank decomposition for 2-D anisotropic wave propagation (Complex)
DocCmd: sfcanisolr2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing velz data)
Port:   stdout rsf w req 	RSF standard output (containing right data)
Port:   fft rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   left rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   vels rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  approx   -   -  		Type of approximation (0=exact 1=zone 2=acoustic)
LDesc:  (defaults to: 2)
Param:  dt   -   -  		time step
Param:  eps   -   -  		tolerance
LDesc:  (defaults to: 1.e-4)
Param:  mode   -   -  		wave mode (0=p wave, 1=Sv wave)
LDesc:  (defaults to: 0)
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 20)
Param:  os   -   -  		
LDesc:  (defaults to: true)
Param:  relation   -   -  		Type of q relationship (0=shale, 1=sand, 2=carbonate, default being smallest error)
LDesc:  (defaults to: 3)
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)
Param:  sub   -   -  		for twostep, default true
LDesc:  (defaults to: true)
Param:  taper   -   -  		wavenumber tapering flag
LDesc:  (defaults to: 1.0)

