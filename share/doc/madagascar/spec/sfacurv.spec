[sfacurv]
Cat:    RSF/user/chen
Desc:   Azimuth CURVature
DocCmd: sfacurv | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  interp string  -   -  		interpolation method: maxflat lagrange bspline 
Param:  nazmuth int  -  10 		azimuth number 
Param:  order int  -  2 		approximating order of finite difference 
Param:  rect1 int  -  1 		smoothness on 1st axis 
Param:  rect2 int  -  1 		smoothness on 2nd axis 
Param:  rect3 int  -  1 		smoothness on 3rd axis 

