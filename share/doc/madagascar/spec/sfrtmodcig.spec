[sfrtmodcig]
Cat:    RSF/user/pyang
Desc:   RTM output ODCIG with extended images
DocCmd: sfrtmodcig | cat
Port:   stdin  rsf r req 	RSF standard input (containing vmodl data)
Port:   stdout rsf w req 	RSF standard output (containing Fodcig data)
Port:   vel1stlayer rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  amp float  -  1. 		maximum amplitude of ricker wavelet
Param:  csdgather enum-bool  -  y 		default, common shot-gather; if n, record at every point
Param:  dt float  -   -  		time interval 
Param:  fm float  -   -  		dominant freq of ricker 
Param:  gxbeg int  -   -  		x-begining index of receivers, starting from 0 
Param:  gzbeg int  -   -  		z-begining index of receivers, starting from 0 
Param:  jgx int  -  1 		receiver x-axis jump interval 
Param:  jgz int  -  0 		receiver z-axis jump interval 
Param:  jsx int  -   -  		source x-axis  jump interval  
Param:  jsz int  -  0 		source z-axis jump interval  
Param:  kt int  -  200 		record poynting vector at kt 
Param:  nb int  -  20 		thickness of split PML 
Param:  ng int  -   -  		total receivers in each shot 
Param:  nh int  -  30 		number of points in offset coordinate
Param:  ns int  -   -  		total shots 
Param:  nt int  -   -  		total modeling time steps 
Param:  sxbeg int  -   -  		x-begining index of sources, starting from 0 
Param:  szbeg int  -   -  		z-begining index of sources, starting from 0 
Param:  tdmute int  -   -  		number of deleyed time samples to mute 
LDesc:  (defaults to: 2./(fm*dt))
Param:  vmute float  -  1500 		muting velocity to remove the low-freq noise, unit=m/s

