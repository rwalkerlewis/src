import rsf.doc

sfpgreywfl = rsf.doc.rsfprog('sfpgreywfl','user/cdacosta/Mpgreywfl.py','''Plot wavefields over a background image''')
sfpgreywfl.par('bg',rsf.doc.rsfpar('string','None','','''Background for animation. Zero if not supplied'''))
sfpgreywfl.par('savefile',rsf.doc.rsfpar('string','','','''Save animation to file. If not present, display animation.'''))
sfpgreywfl.par('title',rsf.doc.rsfpar('string','','','''Plot title'''))
sfpgreywfl.par('pclip',rsf.doc.rsfpar('float','100','','''Clip amplitude percentage from (0-100)'''))
sfpgreywfl.par('absclip',rsf.doc.rsfpar('bool','n','','''Clipping is done for all gathers rather than per frame (y/n)'''))
sfpgreywfl.par('scalebar',rsf.doc.rsfpar('bool','y','','''Colorbar'''))
sfpgreywfl.par('barlabel',rsf.doc.rsfpar('string','','','''Colorbar label'''))
sfpgreywfl.par('timetext',rsf.doc.rsfpar('bool','y','','''Time text'''))
sfpgreywfl.par('bgcmap',rsf.doc.rsfpar('string','viridis','','''Background colormap. See https://matplotlib.org/users/colormaps.html'''))
sfpgreywfl.par('wflcmap',rsf.doc.rsfpar('string','gray','','''Wavefield colormap (should be sequential)'''))
sfpgreywfl.par('jsnap',rsf.doc.rsfpar('int','1','','''Number of timesteps at which to plot wavefield'''))
sfpgreywfl.par('aspect',rsf.doc.rsfpar('int','1','','''Aspect ratio'''))
sfpgreywfl.par('tmin',rsf.doc.rsfpar('float','None','','''Minimum time'''))
sfpgreywfl.par('tmax',rsf.doc.rsfpar('float','None','','''Maximum time'''))
sfpgreywfl.par('figx',rsf.doc.rsfpar('float','10','','''Figure x size in inches'''))
sfpgreywfl.par('figy',rsf.doc.rsfpar('float','8','','''Figure y size in inches'''))
sfpgreywfl.par('xints',rsf.doc.rsfpar('int','None','','''Max number of x intervals'''))
sfpgreywfl.par('yints',rsf.doc.rsfpar('int','None','','''Max number of y intervals'''))
sfpgreywfl.par('fps',rsf.doc.rsfpar('float','15','','''Frames per second (when saving file)'''))
sfpgreywfl.par('speedup',rsf.doc.rsfpar('float','10','','''Delay between frames (in milliseconds) will be speedup*dt'''))
sfpgreywfl.par('dpi',rsf.doc.rsfpar('float','90','','''DPI'''))
sfpgreywfl.par('fontsize',rsf.doc.rsfpar('float','16','','''Font size'''))
sfpgreywfl.par('verb',rsf.doc.rsfpar('bool','n','','''Verbosity flag'''))
sfpgreywfl.version('2.1-git')
sfpgreywfl.synopsis('''sfpgreywfl bg=None savefile= title= pclip=100 absclip=n scalebar=y barlabel= timetext=y bgcmap=viridis wflcmap=gray jsnap=1 aspect=1 tmin=None tmax=None figx=10 figy=8 xints=None yints=None fps=15 speedup=10 dpi=90 fontsize=16 verb=n''','''Common usage examples
\t* Plot to screen using default parameters
\t\tsfpgreywfl < wavefield.rsf bg=velocity.rsf
\t* Save to file using custom parameters
\t\tsfpgreywfl < wavefield.rsf bg=velocity.rsf jsnap=10 bgcmap=gray wflcmap=seismic fps=10 verb=y savefile=output.mp4
''')
rsf.doc.progs['sfpgreywfl']=sfpgreywfl

