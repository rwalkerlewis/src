[sfduffing1]
Cat:    RSF/user/yliu
Desc:   1D signal analysis by using Duffing differential equation solved by 4th order Runge-Kutta method
DocCmd: sfduffing1 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  cosine enum-bool  -  y 		if n need extenal input for periodic restoring force 
Param:  gamma float  -  0.75 		strength of external force
Param:  kxi float  -  1 		adjustment for input signal
Param:  omega float  -  1 		angular frequence of external force
Param:  phi float  -  0. 		phase of cosine signal unit=pi
Param:  pow1 int  -  1 		power of first non-linear restitution term
Param:  pow2 int  -  3 		power of second non-linear restitution term
Param:  restor string  -   -  		auxiliary input file name
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  x0 float  -  0 		initial value of x0
Param:  y0 float  -  0 		initial value of y0

