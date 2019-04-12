[sfpresr]
Cat:    RSF/user/chenyk
Desc:   2-D simplest-form post-stack Kirchhoff time modeling and migration
DocCmd: sfpresr | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  aa enum-bool  -  n 		yes: apply reciprocal antialiaising operator 
Param:  adj enum-bool  -  y 		yes: migration, no: modeling 
Param:  sw int  -  0 		if > 0, select a branch of the antialiasing operation 
Param:  v0 float  -   -  		constant velocity (if no velocity=) 
Param:  vel string  -   -  		velocity file (auxiliary input file name)

