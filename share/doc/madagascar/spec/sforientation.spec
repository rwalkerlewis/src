[sforientation]
Cat:    RSF/user/chen
Desc:   orientation estimation by structural gradient tensor
DocCmd: sforientation | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  azimuth string  -   -  		auxiliary output file name
Param:  filt string  -   -  		filter type : ls, tls, tensor 
Param:  interp string  -   -  		interpolation method: maxflat lagrange bspline 
Param:  order int  -  2 		approximating order of finite difference 
Param:  rect1 int  -  0 		smoothness on 1st axis 
Param:  rect2 int  -  0 		smoothness on 2nd axis 
Param:  rect3 int  -  0 		smoothness on 3rd axis 
Param:  weight string  -   -  		auxiliary input file name

