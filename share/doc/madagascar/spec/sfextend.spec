[sfextend]
Cat:    RSF/user/sbader
Desc:   
DocCmd: sfextend | cat
Port:   stdin  rsf r req 	RSF standard input (containing loga data)
Port:   stdout rsf w req 	RSF standard output (containing log_eo data)
Param:  reflog string  -   -  		Reference log (switch=3)
Param:  switch int  -   -  		(0 = Two-sided axis extension by first and last non-zero sample in dataset); (2 = Two-sided axis reduction); (3 = Matches starting value and number of samples between input and reference well log); (else = pad data to dataset size by first and last nonzero sample); (4 = Testing)
Param:  val int  -   -  		Sample manipulation (switch=0/2)

