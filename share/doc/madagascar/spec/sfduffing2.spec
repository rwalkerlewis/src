[sfduffing2]
Cat:    RSF/user/yliu
Desc:   2D/3D Velocity analysis by using Duffing differential equation solved by 4th order Runge-Kutta method
DocCmd: sfduffing2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing cmp data)
Port:   stdout rsf w req 	RSF standard output (containing outf data)
Param:  cosine enum-bool  -  y 		if n need extenal input for periodic restoring force 
Param:  delta float  -  0.01 		The density of judgement grid
Param:  deltat0 float  -   -  		step lenth for t0 scan 
LDesc:  (defaults to: dt)
Param:  dv float  -  20 		step lenth for velocity scan 
Param:  gamma float  -  0.75 		strength of external force
Param:  gx float  -  2.0 		Size of grid
Param:  kxi float  -  1 		adjustment for input signal
Param:  omega float  -  1 		angular frequence of external force
Param:  phi float  -  0. 		phase of cosine signal unit=pi
Param:  pow1 int  -  1 		power of first non-linear restitution term
Param:  pow2 int  -  3 		power of second non-linear restitution term
Param:  restor string  -   -  		auxiliary input file name
Param:  t0 float  -   -  		t0 scan start point 
LDesc:  (defaults to: o1)
Param:  t0n int  -   -  		numbers of t0scan
LDesc:  (defaults to: n1)
Param:  v0 float  -  1000 		init Vel for velocity scan 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  vn int  -  100 		numbers of velscan
Param:  winsz int  -  200 		for each trace,the width of window. Unit:samples
Param:  x0 float  -  0 		initial value of x0
Param:  y0 float  -  0 		initial value of y0

