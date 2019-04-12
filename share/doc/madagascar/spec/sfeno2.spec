[sfeno2]
Cat:    RSF/user/fomels
Desc:   Convert velocity to slowness and compute gradient using ENO interpolation
DocCmd: sfeno2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing vel data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  is_inverse enum-bool  -   -  		make vel to slowness 
LDesc:  (defaults to: 1)
Param:  order int  -  3 		interpolation order 

