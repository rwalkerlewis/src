[sffaultrbf1d]
Cat:    RSF/user/yunzhi
Desc:   Compute RBF across fault using fault attribute computed by Sobel filter
DocCmd: sffaultrbf1d | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  i0 int  -   -  		Reference trace position. 
Param:  r0 float  -  1.0 		Reference radial in RBF. 
Param:  scale float  -  1.0 		Fault attribute scaling factor (0.0 ~ factor). 
Param:  useinput enum-bool  -  y 		Flag: whether use the input fault attribute. 

