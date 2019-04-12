[sfpgreywfl]
Cat:    RSF/user/cdacosta
Desc:   Plot wavefields over a background image
DocCmd: sfpgreywfl | cat
Param:  absclip enum-bool  -  n 		Clipping is done for all gathers rather than per frame (y/n)
Param:  aspect int  -  1 		Aspect ratio
Param:  barlabel string  -   -  		Colorbar label
Param:  bg string  -   -  		Background for animation. Zero if not supplied
LDesc:  (defaults to: None)
Param:  bgcmap string  -   -  		Background colormap. See https://matplotlib.org/users/colormaps.html
LDesc:  (defaults to: viridis)
Param:  dpi float  -  90 		DPI
Param:  figx float  -  10 		Figure x size in inches
Param:  figy float  -  8 		Figure y size in inches
Param:  fontsize float  -  16 		Font size
Param:  fps float  -  15 		Frames per second (when saving file)
Param:  jsnap int  -  1 		Number of timesteps at which to plot wavefield
Param:  pclip float  -  100 		Clip amplitude percentage from (0-100)
Param:  savefile string  -   -  		Save animation to file. If not present, display animation.
Param:  scalebar enum-bool  -  y 		Colorbar
Param:  speedup float  -  10 		Delay between frames (in milliseconds) will be speedup*dt
Param:  timetext enum-bool  -  y 		Time text
Param:  title string  -   -  		Plot title
Param:  tmax float  -  None 		Maximum time
Param:  tmin float  -  None 		Minimum time
Param:  verb enum-bool  -  n 		Verbosity flag
Param:  wflcmap string  -   -  		Wavefield colormap (should be sequential)
LDesc:  (defaults to: gray)
Param:  xints int  -  None 		Max number of x intervals
Param:  yints int  -  None 		Max number of y intervals

