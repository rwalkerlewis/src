[sfrotvol]
Cat:    RSF/user/aklokov
Desc:   3D volume rotation about a vertical axis
DocCmd: sfrotvol | cat
Port:   stdin  rsf r req 	RSF standard input (containing inFile data)
Port:   stdout rsf w req 	RSF standard output (containing outFile data)
Param:  theta float  -   -  		rotation angle 
LDesc:  (defaults to: 0.f)
Param:  xf float  -   -  		x-coord of the vertical axis 
LDesc:  (defaults to: 0.f)
Param:  yf float  -   -  		y-coord of the vertical axis 
LDesc:  (defaults to: 0.f)

