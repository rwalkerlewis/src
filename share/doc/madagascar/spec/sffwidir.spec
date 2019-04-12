[sffwidir]
Cat:    RSF/user/zhiguang
Desc:   Update the conjugate direction in full waveform inversion
DocCmd: sffwidir | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   grad0 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   grad1 rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  beta string  -   -  		auxiliary output file name
Param:  option string  -   -  		CG update parameter (Polak, Fletcher-Reeves, Fletcher, Dai-Yuan) 

