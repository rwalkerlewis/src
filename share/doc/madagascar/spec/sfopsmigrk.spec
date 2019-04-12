[sfopsmigrk]
Cat:    RSF/user/roman
Desc:   Shot-recorder Oriented prestack migration data is (shots x recs x time)
DocCmd: sfopsmigrk | cat
Port:   stdin  rsf r req 	RSF standard input (containing dist data)
Port:   stdout rsf w req 	RSF standard output (containing imag data)
Port:   data rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   dept rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   time rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  is_offset enum-bool  -  n 		
Param:  tolz float  -  2.0 		

