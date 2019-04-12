import rsf.doc

sfimage = rsf.doc.rsfprog('sfimage','su/plot/Ximage.c','''X IMAGE plot of a uniformly-sampled function f(x1,x2).''')
sfimage.par('curve',rsf.doc.rsfpar('strings','','','''file(s) containing points to draw curve(s)  [curve]'''))
sfimage.par('npair',rsf.doc.rsfpar('ints','','','''number(s) of pairs in each curve file  [curve]'''))
sfimage.par('curvecolor',rsf.doc.rsfpar('strings','','',''' [ncurvecolor]'''))
sfimage.par('curvecolor',rsf.doc.rsfpar('strings','','','''color(s) for curve(s)  [ncurvecolor]'''))
sfimage.par('ncurve',rsf.doc.rsfpar('int','0','','''number of curves to draw '''))
sfimage.par('ncurvecolor',rsf.doc.rsfpar('int','0','','''number of curve colors '''))
sfimage.par('clip',rsf.doc.rsfpar('float','','',''''''))
sfimage.par('clip',rsf.doc.rsfpar('float','','',''''''))
sfimage.par('perc',rsf.doc.rsfpar('float','100.0','','''percentile used to determine clip '''))
sfimage.par('balance',rsf.doc.rsfpar('bool','n','','''if false, determine bclip & wclip individually; 
	   else set them to the same abs value '''))
sfimage.par('bclip',rsf.doc.rsfpar('float','','',''''''))
sfimage.par('bperc',rsf.doc.rsfpar('float','perc','','''percentile for determining black clip value '''))
sfimage.par('wclip',rsf.doc.rsfpar('float','','',''''''))
sfimage.par('wperc',rsf.doc.rsfpar('float','100.0-perc','','''percentile for determining white clip value '''))
sfimage.par('verbose',rsf.doc.rsfpar('bool','y','','''verbose mode '''))
sfimage.par('blockinterp',rsf.doc.rsfpar('bool','n','','''whether to use block interpolation '''))
sfimage.par('legend',rsf.doc.rsfpar('bool','n','','''if display the color scale '''))
sfimage.par('blank',rsf.doc.rsfpar('float','0.0f','','''portion of the lower range to blank out '''))
sfimage.par('xbox',rsf.doc.rsfpar('int','50','','''x in pixels of upper left corner of window '''))
sfimage.par('ybox',rsf.doc.rsfpar('int','50','','''y in pixels of upper left corner of window '''))
sfimage.par('wbox',rsf.doc.rsfpar('int','550','','''width in pixels of window '''))
sfimage.par('hbox',rsf.doc.rsfpar('int','700','','''height in pixels of window '''))
sfimage.par('lwidth',rsf.doc.rsfpar('int','16','','''colorscale (legend) width in pixels '''))
sfimage.par('lheight',rsf.doc.rsfpar('int','hbox/3','','''colorscale (legend) height in pixels '''))
sfimage.par('lx',rsf.doc.rsfpar('int','3','','''colorscale (legend) x-position in pixels '''))
sfimage.par('ly',rsf.doc.rsfpar('int','(hbox-lheight)/3','','''colorscale (legend) y-position in pixels '''))
sfimage.par('x1beg',rsf.doc.rsfpar('float','x1min','','''value at which axis 1 begins '''))
sfimage.par('x1end',rsf.doc.rsfpar('float','x1max','','''value at which axis 1 ends '''))
sfimage.par('d1num',rsf.doc.rsfpar('float','0.0','','''numbered tic interval on axis 1 (0.0 for automatic) '''))
sfimage.par('f1num',rsf.doc.rsfpar('float','x1min','','''first numbered tic on axis 1 (used if d1num not 0.0) '''))
sfimage.par('n1tic',rsf.doc.rsfpar('int','1','','''number of tics per numbered tic on axis 1 '''))
sfimage.par('x2beg',rsf.doc.rsfpar('float','x2min','','''value at which axis 2 begins '''))
sfimage.par('x2end',rsf.doc.rsfpar('float','x2max','','''value at which axis 2 ends '''))
sfimage.par('d2num',rsf.doc.rsfpar('float','0.0','','''numbered tic interval on axis 2 (0.0 for automatic) '''))
sfimage.par('f2num',rsf.doc.rsfpar('float','0.0','','''first numbered tic on axis 2 (used if d2num not 0.0) '''))
sfimage.par('n2tic',rsf.doc.rsfpar('int','1','','''number of tics per numbered tic on axis 2 '''))
sfimage.par('labelsize',rsf.doc.rsfpar('float','18.0','',''''''))
sfimage.par('titlesize',rsf.doc.rsfpar('float','24.0','',''''''))
sfimage.par('mpicks',rsf.doc.rsfpar('string ',desc='''file to save mouse picks '''))
sfimage.par('cmap',rsf.doc.rsfpar('string ',desc='''colormap specification (hsv# or rgb#) '''))
sfimage.par('units',rsf.doc.rsfpar('string ',desc='''unit label for legend '''))
sfimage.par('legendfont',rsf.doc.rsfpar('string ',desc='''font name for legend '''))
sfimage.par('grid1',rsf.doc.rsfpar('string ',desc='''grid lines on axis 1 (none, dot, dash, or solid) '''))
sfimage.par('label1',rsf.doc.rsfpar('string ',desc='''label on axis 1 '''))
sfimage.par('grid2',rsf.doc.rsfpar('string ',desc='''grid lines on axis 2 (none, dot, dash, or solid) '''))
sfimage.par('label2',rsf.doc.rsfpar('string ',desc='''label on axis 2 '''))
sfimage.par('labelfont',rsf.doc.rsfpar('string ',desc='''font name for axes labels '''))
sfimage.par('title',rsf.doc.rsfpar('string ',desc='''title of plot '''))
sfimage.par('titlefont',rsf.doc.rsfpar('string ',desc='''font name for title '''))
sfimage.par('style',rsf.doc.rsfpar('string ',desc='''normal (axis 1 horizontal, axis 2 vertical) 
	or  seismic (axis 1 vertical, axis 2 horizontal) '''))
sfimage.par('titlecolor',rsf.doc.rsfpar('string ',desc='''color for title '''))
sfimage.par('labelcolor',rsf.doc.rsfpar('string ',desc='''color for axes labels '''))
sfimage.par('gridcolor',rsf.doc.rsfpar('string ',desc='''color for grid lines '''))
sfimage.par('windowtitle',rsf.doc.rsfpar('string ',desc='''title on window '''))
sfimage.version('2.1-git')
sfimage.synopsis('''sfimage < in.rsf curve= npair= curvecolor= curvecolor= ncurve=0 ncurvecolor=0 clip= clip= perc=100.0 balance=n bclip= bperc=perc wclip= wperc=100.0-perc verbose=y blockinterp=n legend=n blank=0.0f xbox=50 ybox=50 wbox=550 hbox=700 lwidth=16 lheight=hbox/3 lx=3 ly=(hbox-lheight)/3 x1beg=x1min x1end=x1max d1num=0.0 f1num=x1min n1tic=1 x2beg=x2min x2end=x2max d2num=0.0 f2num=0.0 n2tic=1 labelsize=18.0 titlesize=24.0 mpicks= cmap= units= legendfont= grid1= label1= grid2= label2= labelfont= title= titlefont= style= titlecolor= labelcolor= gridcolor= windowtitle=''','''X Functionality:							
Button 1	Zoom with rubberband box				
Button 2	Show mouse (x1,x2) coordinates while pressed		
q or Q key	Quit							
s key		Save current mouse (x1,x2) location to file		
a or page up keys		enhance clipping by 10%			
c or page down keys		reduce clipping by 10%			
up,down,left,right keys	move zoom window by half width/height	
i or +(keypad) 		zoom in by factor 2 			
o or -(keypad) 		zoom out by factor 2 			
									
... change colormap interactively					
r	     install next RGB - colormap				
R	     install previous RGB - colormap				
h	     install next HSV - colormap				
H	     install previous HSV - colormap				
H	     install previous HSV - colormap				
(Move mouse cursor out and back into window for r,R,h,H to take effect)
''')
rsf.doc.progs['sfimage']=sfimage

sfwigb = rsf.doc.rsfprog('sfwigb','su/plot/Xwigb.c','''X WIGgle-trace plot of f(x1,x2) via Bitmap.''')
sfwigb.par('x2',rsf.doc.rsfpar('floats','','','''array of sampled values in 2nd dimension  [n2]'''))
sfwigb.par('bias',rsf.doc.rsfpar('float','0.0','','''data value corresponding to location along axis 2 '''))
sfwigb.par('clip',rsf.doc.rsfpar('float','','','''data values < bias+clip and > bias-clip are clipped '''))
sfwigb.par('perc',rsf.doc.rsfpar('float','100.0','','''percentile for determining clip '''))
sfwigb.par('verbose',rsf.doc.rsfpar('bool','y','','''y for info printed on stderr (n for no info) '''))
sfwigb.par('wt',rsf.doc.rsfpar('int','1','','''=0 for no wiggle-trace; =1 for wiggle-trace '''))
sfwigb.par('va',rsf.doc.rsfpar('int','1','','''=0 for no variable-area; 
       =1 for variable-area fill;
       =2 for variable area, solid/grey fill '''))
sfwigb.par('xcur',rsf.doc.rsfpar('float','1.0','','''wiggle excursion in traces corresponding to clip '''))
sfwigb.par('wigclip',rsf.doc.rsfpar('int','0','','''If 0, the plot box is expanded to accommodate	
       the larger wiggles created by xcur>1. If this 
       flag is non-zero, the extra-large wiggles are	
       are clipped at the boundary of the plot box. '''))
sfwigb.par('xbox',rsf.doc.rsfpar('int','50','','''x in pixels of upper left corner of window '''))
sfwigb.par('ybox',rsf.doc.rsfpar('int','50','','''y in pixels of upper left corner of window '''))
sfwigb.par('wbox',rsf.doc.rsfpar('int','550','','''width in pixels of window '''))
sfwigb.par('hbox',rsf.doc.rsfpar('int','700','','''height in pixels of window '''))
sfwigb.par('x1beg',rsf.doc.rsfpar('float','x1min','','''value at which axis 1 begins '''))
sfwigb.par('x1end',rsf.doc.rsfpar('float','x1max','','''value at which axis 1 ends '''))
sfwigb.par('d1num',rsf.doc.rsfpar('float','0.0','','''numbered tic interval on axis 1 (0.0 for automatic) '''))
sfwigb.par('f1num',rsf.doc.rsfpar('float','x1min','','''first numbered tic on axis 1 (used if d1num not 0.0) '''))
sfwigb.par('n1tic',rsf.doc.rsfpar('int','1','','''number of tics per numbered tic on axis 1 '''))
sfwigb.par('x2beg',rsf.doc.rsfpar('float','x2min','','''value at which axis 2 begins '''))
sfwigb.par('x2end',rsf.doc.rsfpar('float','x2max','','''value at which axis 2 ends '''))
sfwigb.par('d2num',rsf.doc.rsfpar('float','0.0','','''numbered tic interval on axis 2 (0.0 for automatic) '''))
sfwigb.par('f2num',rsf.doc.rsfpar('float','x2min','','''first numbered tic on axis 2 (used if d2num not 0.0) '''))
sfwigb.par('n2tic',rsf.doc.rsfpar('int','1','','''number of tics per numbered tic on axis 2 '''))
sfwigb.par('labelsize',rsf.doc.rsfpar('float','18.0','',''''''))
sfwigb.par('titlesize',rsf.doc.rsfpar('float','24.0','',''''''))
sfwigb.par('endian',rsf.doc.rsfpar('int','','','''endian for display =0 little endian =1 big endian '''))
sfwigb.par('interp',rsf.doc.rsfpar('bool','n','','''if y, use interpolation '''))
sfwigb.par('mpicks',rsf.doc.rsfpar('string ',desc='''file to save mouse picks in '''))
sfwigb.par('grid1',rsf.doc.rsfpar('string ',desc='''grid lines on axis 1 - none, dot, dash, or solid '''))
sfwigb.par('label1',rsf.doc.rsfpar('string ',desc=''''''))
sfwigb.par('grid2',rsf.doc.rsfpar('string ',desc='''grid lines on axis 2 - none, dot, dash, or solid '''))
sfwigb.par('label2',rsf.doc.rsfpar('string ',desc=''''''))
sfwigb.par('labelfont',rsf.doc.rsfpar('string ',desc='''font name for axes labels '''))
sfwigb.par('title',rsf.doc.rsfpar('string ',desc=''''''))
sfwigb.par('titlefont',rsf.doc.rsfpar('string ',desc=''''''))
sfwigb.par('style',rsf.doc.rsfpar('string ',desc=''''''))
sfwigb.par('titlecolor',rsf.doc.rsfpar('string ',desc=''''''))
sfwigb.par('labelcolor',rsf.doc.rsfpar('string ',desc=''''''))
sfwigb.par('gridcolor',rsf.doc.rsfpar('string ',desc=''''''))
sfwigb.par('windowtitle',rsf.doc.rsfpar('string ',desc='''initialize zoom box parameters '''))
sfwigb.version('2.1-git')
sfwigb.synopsis('''sfwigb < in.rsf x2= bias=0.0 clip= perc=100.0 verbose=y wt=1 va=1 xcur=1.0 wigclip=0 xbox=50 ybox=50 wbox=550 hbox=700 x1beg=x1min x1end=x1max d1num=0.0 f1num=x1min n1tic=1 x2beg=x2min x2end=x2max d2num=0.0 f2num=x2min n2tic=1 labelsize=18.0 titlesize=24.0 endian= interp=n mpicks= grid1= label1= grid2= label2= labelfont= title= titlefont= style= titlecolor= labelcolor= gridcolor= windowtitle=''','''
X Functionality:							
Button 1	Zoom with rubberband box				
Button 2	Show mouse (x1,x2) coordinates while pressed		
q or Q key	Quit							
s key		Save current mouse (x1,x2) location to file		
p or P key	Plot current window with pswigb (only from disk files)	
a or page up keys		enhance clipping by 10%			
c or page down keys		reduce clipping by 10%			
up,down,left,right keys	move zoom window by half width/height	
i or +(keypad) 		zoom in by factor 2 			
o or -(keypad) 		zoom out by factor 2 			
l 				lock the zoom while moving the coursor	
u 				unlock the zoom 			
1,2,...,9	Zoom/Move factor of the window size			
									
Notes:								
	Reaching the window limits while moving within changes the zoom	
	factor in this direction. The use of zoom locking(l) disables it
''')
rsf.doc.progs['sfwigb']=sfwigb

