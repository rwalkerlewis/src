[sfbackusave]
Cat:    RSF/user/sbader
Desc:   C-Wave Backus Averaging (See Marion et al., 1994)
DocCmd: sfbackusave | cat
Port:   stdin  rsf r req 	RSF standard input (containing deptha data)
Port:   stdout rsf w req 	RSF standard output (containing depth_bkn data)
Port:   rhob_bk rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   slow_bk rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   vel_bk rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  density string  -   -  		Density from Logs
Param:  depthsample float  -   -  		Depth Sampling
Param:  peak_f float  -   -  		Dom wavelength
Param:  ratio float  -   -  		Percent of dom wavelength
Param:  slowness string  -   -  		Slowness from Logs

