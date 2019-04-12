[sffraclr2test]
Cat:    RSF/user/jsun
Desc:   Complex lowrank decomposition for 2-D constant-Q visco-acoustic wave equation. (Testing for exact disperison relation)
DocCmd: sffraclr2test | cat
Port:   stdin  rsf r req 	RSF standard input (containing vel data)
Port:   stdout rsf w req 	RSF standard output (containing right data)
Port:   fft rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   left rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  approx   -   -  		use Tieyuan's approximation
LDesc:  (defaults to: true)
Param:  c0   -   -  		reference velocity
Param:  dt   -   -  		time step
Param:  eps   -   -  		tolerance
LDesc:  (defaults to: 1.e-4)
Param:  mode   -   -  		mode of propagation: 0 is viscoacoustic (default); 1 is loss-dominated; 2 is dispersion dominated; 3 is acoustic
LDesc:  (defaults to: 0)
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 20)
Param:  rev   -   -  		reverse propagation
LDesc:  (defaults to: false)
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)
Param:  sign   -   -  		sign of solution: 0 is positive, 1 is negative
LDesc:  (defaults to: 0)
Param:  w0   -   -  		reference frequency

