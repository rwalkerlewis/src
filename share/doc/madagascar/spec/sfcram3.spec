[sfcram3]
Cat:    RSF/user/cram
Desc:   3-D angle-domain Kirchhoff migration based on escape tables
DocCmd: sfcram3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing esct data)
Port:   stdout rsf w req 	RSF standard output (containing imag data)
Param:  agath string  -   -  		Scattering angle gathers (angle, azimuth, z, x, y) (auxiliary output file name)
Param:  amp enum-bool  -  y 		n - do not apply amplitude correction weights 
Param:  armax float  -   -  		Maximum allowed area for an exit ray branch 
LDesc:  (defaults to: 100.0*dy*dx)
Param:  armin float  -   -  		Minimum allowed area for an exit ray branch 
LDesc:  (defaults to: 0.01*dy*dx)
Param:  data string  -   -  		Processed prestack data (auxiliary input file name)
Param:  dazmax float  -  180.0 		Maximum allowed dip angle at z max 
Param:  dazmin float  -  180.0 		Maximum allowed dip angle at z min 
Param:  dbx float  -   -  		Size of search bins in x 
LDesc:  (defaults to: 10.0*dx)
Param:  dby float  -   -  		Size of search bins in y 
LDesc:  (defaults to: 10.0*dy)
Param:  ddaemon string  -   -  		Daemon for distributed data storage (auxiliary input file name)
Param:  dipagath string  -   -  		Dip angle gathers (angle, azimuth, z, x, y) (auxiliary output file name)
Param:  dipimap string  -   -  		Dip gathers illumination (angle, azimuth, z, x, y) (auxiliary output file name)
Param:  dipsmap string  -   -  		Dip gathers energy (angle, azimuth, z, x, y) (auxiliary output file name)
Param:  dxm float  -   -  		Taper length in x 
LDesc:  (defaults to: 5.0*dx)
Param:  dym float  -   -  		Taper length in y 
LDesc:  (defaults to: 5.0*dy)
Param:  extrap enum-bool  -  n 		y - extrapolate migrated samples in gathers 
Param:  hits string  -   -  		Image illumination (z, x, y) (auxiliary output file name)
Param:  imap string  -   -  		SCattering gathers illumination (angle, azimuth, z, x, y) (auxiliary output file name)
Param:  inorm enum-bool  -  n 		y - normalize gathers for illumination 
Param:  mute enum-bool  -  n 		y - mute signal in constant z plane before stacking 
Param:  nc int  -  0 		Number of threads to use for ray tracing (OMP_NUM_THREADS by default) 
Param:  np int  -  1 		number of image points to buffer before accessing data 
Param:  oazmax float  -  180.0 		Maximum allowed scattering angle at z max 
Param:  oazmin float  -  180.0 		Maximum allowed scattering angle at z min 
Param:  outaz enum-bool  -  y 		n - stack azimuth direction before output 
Param:  smap string  -   -  		Scattering gathers energy (angle, azimuth, z, x, y) (auxiliary output file name)
Param:  survey string  -   -  		Survey info for input data (auxiliary input file name)
Param:  vconst float  -  1.5 		Constant velocity, if vz= is not used 
Param:  vz string  -   -  		Velocity model for amplitude weights (auxiliary input file name)

