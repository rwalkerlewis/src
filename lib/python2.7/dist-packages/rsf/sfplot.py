import rsf.doc

sfbargraph = rsf.doc.rsfprog('sfbargraph','plot/main/bargraph.c','''Bar plot.''')
sfbargraph.par('wantframenum',rsf.doc.rsfpar('bool','(bool) (n3 > 1)','','''if y, display third axis position in the corner '''))
sfbargraph.par('pclip',rsf.doc.rsfpar('float','100.','','''clip percentile '''))
sfbargraph.par('width',rsf.doc.rsfpar('float','0.8','','''bar width '''))
sfbargraph.par('transp',rsf.doc.rsfpar('bool','n','','''if y, transpose the axes '''))
sfbargraph.version('2.1-git')
sfbargraph.synopsis('''sfbargraph < in.rsf wantframenum=(bool) (n3 > 1) pclip=100. width=0.8 transp=n > plot.vpl''','''Run "sfdoc stdplot" for more parameters.
''')
rsf.doc.progs['sfbargraph']=sfbargraph

sfbox = rsf.doc.rsfprog('sfbox','plot/main/box.c','''Draw a balloon-style label.''')
sfbox.par('lab_color',rsf.doc.rsfpar('int','VP_WHITE','','''label color '''))
sfbox.par('lab_fat',rsf.doc.rsfpar('int','0','','''label fatness '''))
sfbox.par('pscale',rsf.doc.rsfpar('float','1.','','''scale factor for width of pointer '''))
sfbox.par('pointer',rsf.doc.rsfpar('bool','y','','''if y, create arrow pointer '''))
sfbox.par('reverse',rsf.doc.rsfpar('bool','n','','''if reverse '''))
sfbox.par('lat',rsf.doc.rsfpar('float','0.','','''latitude of viewpoint in 3-D '''))
sfbox.par('long',rsf.doc.rsfpar('float','90.','','''longitude of viewpoint in 3-D '''))
sfbox.par('angle',rsf.doc.rsfpar('float','0.','','''longitude of floating label in 3-D '''))
sfbox.par('x0',rsf.doc.rsfpar('float','0.','','''x position of the pointer tip '''))
sfbox.par('y0',rsf.doc.rsfpar('float','0.','','''y position of the pointer tip '''))
sfbox.par('scale0',rsf.doc.rsfpar('float','1.','','''scale factor for x0 and y0 '''))
sfbox.par('xt',rsf.doc.rsfpar('float','2.','','''relative position of text in x '''))
sfbox.par('yt',rsf.doc.rsfpar('float','0.','','''relative position of text in y '''))
sfbox.par('x_oval',rsf.doc.rsfpar('float','0.','','''x size of the oval around pointer '''))
sfbox.par('y_oval',rsf.doc.rsfpar('float','0.','','''y size of the oval around pointer '''))
sfbox.par('boxit',rsf.doc.rsfpar('bool','y','','''if y, create a box around text '''))
sfbox.par('length',rsf.doc.rsfpar('float','','','''normalization for xt and yt '''))
sfbox.par('scalet',rsf.doc.rsfpar('float','','','''( scalet scale factor for xt and yt (if length is not set) )'''))
sfbox.par('size',rsf.doc.rsfpar('float','.25','','''text height in inches '''))
sfbox.par('font',rsf.doc.rsfpar('int','VP_NO_CHANGE','','''text font '''))
sfbox.par('label',rsf.doc.rsfpar('string ',desc='''text for label '''))
sfbox.version('2.1-git')
sfbox.synopsis('''sfbox lab_color=VP_WHITE lab_fat=0 pscale=1. pointer=y reverse=n lat=0. long=90. angle=0. x0=0. y0=0. scale0=1. xt=2. yt=0. x_oval=0. y_oval=0. boxit=y length= scalet= size=.25 font=VP_NO_CHANGE label= > out.vpl''','''May 2015 program of the month:
http://ahay.org/blog/2015/05/01/program-of-the-month-sfbox/
''')
rsf.doc.progs['sfbox']=sfbox

sfcontour = rsf.doc.rsfprog('sfcontour','plot/main/contour.c','''Contour plot.''')
sfcontour.par('c',rsf.doc.rsfpar('floats','','',''' [nc]'''))
sfcontour.par('min1',rsf.doc.rsfpar('float','o1','','''minimum on 1st axis '''))
sfcontour.par('min2',rsf.doc.rsfpar('float','o2','','''minimum on 2nd axis '''))
sfcontour.par('max1',rsf.doc.rsfpar('float','o1+(n1-1)*d1','','''maximum on 1st axis '''))
sfcontour.par('max2',rsf.doc.rsfpar('float','o2+(n2-1)*d2','','''maximum on 2nd axis '''))
sfcontour.par('nc',rsf.doc.rsfpar('int','50','','''number of contours '''))
sfcontour.par('dc',rsf.doc.rsfpar('float','','','''contour increment '''))
sfcontour.par('c0',rsf.doc.rsfpar('float','','','''first contour '''))
sfcontour.par('transp',rsf.doc.rsfpar('bool','y','','''if y, transpose the axes '''))
sfcontour.par('minval',rsf.doc.rsfpar('float','','','''minimum value for scalebar (default is the data minimum) '''))
sfcontour.par('maxval',rsf.doc.rsfpar('float','','','''maximum value for scalebar (default is the data maximum) '''))
sfcontour.par('allpos',rsf.doc.rsfpar('bool','y','','''contour positive values only '''))
sfcontour.par('cfile',rsf.doc.rsfpar('string ',desc='''contours in a file '''))
sfcontour.par('barlabel',rsf.doc.rsfpar('string ',desc='''scale bar label '''))
sfcontour.version('2.1-git')
sfcontour.synopsis('''sfcontour < in.rsf c= min1=o1 min2=o2 max1=o1+(n1-1)*d1 max2=o2+(n2-1)*d2 nc=50 dc= c0= transp=y minval= maxval= allpos=y cfile= barlabel= > plot.vpl''','''Run "sfdoc stdplot" for more parameters.

December 2011 program of the month:
http://ahay.org/blog/2011/12/03/programs-of-the-month-sfcontour/
''')
rsf.doc.progs['sfcontour']=sfcontour

sfcontour3 = rsf.doc.rsfprog('sfcontour3','plot/main/contour3.c','''Generate 3-D contour plot.''')
sfcontour3.par('c',rsf.doc.rsfpar('floats','','',''' [nc]'''))
sfcontour3.par('min1',rsf.doc.rsfpar('float','o1','',''''''))
sfcontour3.par('min2',rsf.doc.rsfpar('float','o2','',''''''))
sfcontour3.par('min3',rsf.doc.rsfpar('float','o3','',''''''))
sfcontour3.par('max1',rsf.doc.rsfpar('float','o1+(n1-1)*d1','',''''''))
sfcontour3.par('max2',rsf.doc.rsfpar('float','o2+(n2-1)*d2','',''''''))
sfcontour3.par('max3',rsf.doc.rsfpar('float','o3+(n3-1)*d3','','''data window to plot '''))
sfcontour3.par('yreverse',rsf.doc.rsfpar('bool','y','','''if y, reverse the first axis '''))
sfcontour3.par('nc',rsf.doc.rsfpar('int','50','','''number of contours '''))
sfcontour3.par('dc',rsf.doc.rsfpar('float','','','''contour increment '''))
sfcontour3.par('c0',rsf.doc.rsfpar('float','','','''first contour '''))
sfcontour3.par('point1',rsf.doc.rsfpar('float','0.5','','''fraction of the vertical axis for front face '''))
sfcontour3.par('point2',rsf.doc.rsfpar('float','0.5','','''fraction of the horizontal axis for front face '''))
sfcontour3.par('frame1',rsf.doc.rsfpar('int','0','',''''''))
sfcontour3.par('frame2',rsf.doc.rsfpar('int','n2-1','',''''''))
sfcontour3.par('frame3',rsf.doc.rsfpar('int','0','','''frame numbers for cube faces '''))
sfcontour3.par('movie',rsf.doc.rsfpar('int','0','','''0: no movie, 1: movie over axis 1, 2: axis 2, 3: axis 3 '''))
sfcontour3.par('dframe',rsf.doc.rsfpar('int','1','','''frame increment in a movie '''))
sfcontour3.par('n1pix',rsf.doc.rsfpar('int','n1/point1+n3/(1.-point1)','','''number of vertical pixels '''))
sfcontour3.par('n2pix',rsf.doc.rsfpar('int','n2/point2+n3/(1.-point2)','','''number of horizontal pixels '''))
sfcontour3.par('flat',rsf.doc.rsfpar('bool','y','','''if n, display perspective view '''))
sfcontour3.par('scalebar',rsf.doc.rsfpar('bool','n','','''if y, draw scalebar '''))
sfcontour3.par('minval',rsf.doc.rsfpar('float','','','''minimum value for scalebar (default is the data minimum) '''))
sfcontour3.par('maxval',rsf.doc.rsfpar('float','','','''maximum value for scalebar (default is the data maximum) '''))
sfcontour3.par('barreverse',rsf.doc.rsfpar('bool','n','','''if y, go from small to large on the bar scale '''))
sfcontour3.par('cfile',rsf.doc.rsfpar('string ',desc='''contours in a file '''))
sfcontour3.version('2.1-git')
sfcontour3.synopsis('''sfcontour3 < in.rsf c= min1=o1 min2=o2 min3=o3 max1=o1+(n1-1)*d1 max2=o2+(n2-1)*d2 max3=o3+(n3-1)*d3 yreverse=y nc=50 dc= c0= point1=0.5 point2=0.5 frame1=0 frame2=n2-1 frame3=0 movie=0 dframe=1 n1pix=n1/point1+n3/(1.-point1) n2pix=n2/point2+n3/(1.-point2) flat=y scalebar=n minval= maxval= barreverse=n cfile= > plot.vpl''','''''')
rsf.doc.progs['sfcontour3']=sfcontour3

sfdots = rsf.doc.rsfprog('sfdots','plot/main/dots.c','''Plot signal with lollipops.''')
sfdots.par('labels',rsf.doc.rsfpar('strings','','','''trace labels  [n2]'''))
sfdots.par('dots',rsf.doc.rsfpar('int','(n1 <= 130)? 1: 0','','''type of dots: 1 - baloon, 0 - no dots, 2 - only for non-zero data '''))
sfdots.par('seemean',rsf.doc.rsfpar('bool','(bool) (n2 <= 30)','','''if y, draw axis lines '''))
sfdots.par('strings',rsf.doc.rsfpar('bool','(bool) (n1 <= 400)','','''if y, draw strings '''))
sfdots.par('connect',rsf.doc.rsfpar('int','1','','''connection type: 1 - diagonal, 2 - bar, 4 - only for non-zero data '''))
sfdots.par('corners',rsf.doc.rsfpar('int','','','''number of polygon corners (default is 6) '''))
sfdots.par('silk',rsf.doc.rsfpar('bool','n','','''if y, silky plot '''))
sfdots.par('gaineach',rsf.doc.rsfpar('bool','y','','''if y, gain each trace independently '''))
sfdots.par('labelsz',rsf.doc.rsfpar('int','8','','''label size '''))
sfdots.par('yreverse',rsf.doc.rsfpar('bool','n','','''if y, reverse y axis '''))
sfdots.par('constsep',rsf.doc.rsfpar('bool','n','','''if y, use constant trace separation '''))
sfdots.par('seedead',rsf.doc.rsfpar('bool','n','','''if y, show zero traces '''))
sfdots.par('transp',rsf.doc.rsfpar('bool','n','','''if y, transpose the axis '''))
sfdots.par('xxscale',rsf.doc.rsfpar('float','1.','','''x scaling '''))
sfdots.par('yyscale',rsf.doc.rsfpar('float','1.','','''y scaling '''))
sfdots.par('clip',rsf.doc.rsfpar('float','-1.','','''data clip '''))
sfdots.par('overlap',rsf.doc.rsfpar('float','0.9','','''trace overlap '''))
sfdots.par('screenratio',rsf.doc.rsfpar('float','VP_SCREEN_RATIO','','''screen aspect ratio '''))
sfdots.par('screenht',rsf.doc.rsfpar('float','VP_STANDARD_HEIGHT','','''screen height '''))
sfdots.par('screenwd',rsf.doc.rsfpar('float','screenhigh / screenratio','','''screen width '''))
sfdots.par('radius',rsf.doc.rsfpar('float','dd1/3','','''dot radius '''))
sfdots.par('font',rsf.doc.rsfpar('int','-1','','''font to use in text '''))
sfdots.par('label1',rsf.doc.rsfpar('float','','','''label for the axis '''))
sfdots.par('unit1',rsf.doc.rsfpar('string','','','''unit for the axis '''))
sfdots.par('title',rsf.doc.rsfpar('string','','','''plot title '''))
sfdots.par('label1',rsf.doc.rsfpar('string ',desc='''label for the axis'''))
sfdots.par('unit1',rsf.doc.rsfpar('string ',desc='''unit for the axis'''))
sfdots.par('title',rsf.doc.rsfpar('string ',desc='''plot title'''))
sfdots.version('2.1-git')
sfdots.synopsis('''sfdots < in.rsf labels= dots=(n1 <= 130)? 1: 0 seemean=(bool) (n2 <= 30) strings=(bool) (n1 <= 400) connect=1 corners= silk=n gaineach=y labelsz=8 yreverse=n constsep=n seedead=n transp=n xxscale=1. yyscale=1. clip=-1. overlap=0.9 screenratio=VP_SCREEN_RATIO screenht=VP_STANDARD_HEIGHT screenwd=screenhigh / screenratio radius=dd1/3 font=-1 label1= unit1= title= > plot.vpl''','''The axis is displayed only if label1= is present in the input
file or the command line.  
''')
rsf.doc.progs['sfdots']=sfdots

sfgraph = rsf.doc.rsfprog('sfgraph','plot/main/graph.c','''Graph plot.''')
sfgraph.par('depth',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfgraph.par('symbolsz',rsf.doc.rsfpar('floats','','','''symbol size (default is 2)  [n2]'''))
sfgraph.par('scalebar',rsf.doc.rsfpar('bool','n','','''if y, draw scalebar '''))
sfgraph.par('wantframenum',rsf.doc.rsfpar('bool','(bool) (n3 > 1)','','''if y, display third axis position in the corner '''))
sfgraph.par('nreserve',rsf.doc.rsfpar('int','8','','''reserved colors '''))
sfgraph.par('minval',rsf.doc.rsfpar('float','','','''minimum value for scalebar (default is the data minimum) '''))
sfgraph.par('maxval',rsf.doc.rsfpar('float','','','''maximum value for scalebar (default is the data maximum) '''))
sfgraph.par('barreverse',rsf.doc.rsfpar('bool','n','','''if y, go from small to large on the bar scale '''))
sfgraph.par('pclip',rsf.doc.rsfpar('float','100.','','''clip percentile '''))
sfgraph.par('transp',rsf.doc.rsfpar('bool','n','','''if y, transpose the axes '''))
sfgraph.par('depth',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfgraph.par('color',rsf.doc.rsfpar('string ',desc='''color scheme (default is j) '''))
sfgraph.par('bar',rsf.doc.rsfpar('string ',desc='''file for scalebar data '''))
sfgraph.par('symbol',rsf.doc.rsfpar('string ',desc='''if set, plot with symbols instead of lines '''))
sfgraph.version('2.1-git')
sfgraph.synopsis('''sfgraph < in.rsf depth=depth.rsf symbolsz= scalebar=n wantframenum=(bool) (n3 > 1) nreserve=8 minval= maxval= barreverse=n pclip=100. transp=n color= bar= symbol= > plot.vpl''','''Run "sfdoc stdplot" for more parameters.

August 2011 program of the month:
http://ahay.org/blog/2011/08/09/program-of-the-month-sfgraph/
''')
rsf.doc.progs['sfgraph']=sfgraph

sfgraph3 = rsf.doc.rsfprog('sfgraph3','plot/main/graph3.c','''Generate 3-D cube plot for surfaces.''')
sfgraph3.par('orient',rsf.doc.rsfpar('int','1','','''function orientation '''))
sfgraph3.par('yreverse',rsf.doc.rsfpar('bool','n','',''''''))
sfgraph3.par('min',rsf.doc.rsfpar('float','','','''minimum function value '''))
sfgraph3.par('max',rsf.doc.rsfpar('float','','','''maximum function value '''))
sfgraph3.par('point1',rsf.doc.rsfpar('float','0.5','','''fraction of the vertical axis for front face '''))
sfgraph3.par('point2',rsf.doc.rsfpar('float','0.5','','''fraction of the horizontal axis for front face '''))
sfgraph3.par('frame1',rsf.doc.rsfpar('float','0.5*(min+max)','',''''''))
sfgraph3.par('frame2',rsf.doc.rsfpar('int','n1-1','',''''''))
sfgraph3.par('frame3',rsf.doc.rsfpar('int','0','','''frame numbers for cube faces '''))
sfgraph3.par('movie',rsf.doc.rsfpar('int','0','','''0: no movie, 1: movie over axis 1, 2: axis 2, 3: axis 3 '''))
sfgraph3.par('dframe',rsf.doc.rsfpar('float','1','','''frame increment in a movie '''))
sfgraph3.par('n1pix',rsf.doc.rsfpar('int','n1/point1+n3/(1.-point1)','','''number of vertical pixels '''))
sfgraph3.par('n2pix',rsf.doc.rsfpar('int','n2/point2+n3/(1.-point2)','','''number of horizontal pixels '''))
sfgraph3.par('flat',rsf.doc.rsfpar('bool','y','','''if n, display perspective view '''))
sfgraph3.version('2.1-git')
sfgraph3.synopsis('''sfgraph3 < in.rsf orient=1 yreverse=n min= max= point1=0.5 point2=0.5 frame1=0.5*(min+max) frame2=n1-1 frame3=0 movie=0 dframe=1 n1pix=n1/point1+n3/(1.-point1) n2pix=n2/point2+n3/(1.-point2) flat=y > plot.vpl''','''''')
rsf.doc.progs['sfgraph3']=sfgraph3

sfgrey = rsf.doc.rsfprog('sfgrey','plot/main/grey.c','''Generate raster plot.''')
sfgrey.par('transp',rsf.doc.rsfpar('bool','y','','''if y, transpose the display axes '''))
sfgrey.par('yreverse',rsf.doc.rsfpar('bool','y','','''if y, reverse the vertical axis '''))
sfgrey.par('xreverse',rsf.doc.rsfpar('bool','n','','''if y, reverse the horizontal axis '''))
sfgrey.par('gpow',rsf.doc.rsfpar('float','','',''''''))
sfgrey.par('phalf',rsf.doc.rsfpar('float','','','''percentage for estimating gpow '''))
sfgrey.par('clip',rsf.doc.rsfpar('float','','','''data clip '''))
sfgrey.par('pclip',rsf.doc.rsfpar('float','','','''data clip percentile (default is 99) '''))
sfgrey.par('gainstep',rsf.doc.rsfpar('int','0.5+n1/256.','','''subsampling for gpow and clip estimation '''))
sfgrey.par('allpos',rsf.doc.rsfpar('bool','n','','''if y, assume positive data '''))
sfgrey.par('mean',rsf.doc.rsfpar('bool','n','','''if y, bias on the mean value '''))
sfgrey.par('bias',rsf.doc.rsfpar('float','0.','','''value mapped to the center of the color table '''))
sfgrey.par('polarity',rsf.doc.rsfpar('bool','n','','''if y, reverse polarity (white is high by default) '''))
sfgrey.par('symcp',rsf.doc.rsfpar('bool','n','','''if y, assume symmetric color palette of 255 colors '''))
sfgrey.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfgrey.par('scalebar',rsf.doc.rsfpar('bool','n','','''if y, draw scalebar '''))
sfgrey.par('minval',rsf.doc.rsfpar('float','','','''minimum value for scalebar (default is the data minimum) '''))
sfgrey.par('maxval',rsf.doc.rsfpar('float','','','''maximum value for scalebar (default is the data maximum) '''))
sfgrey.par('barreverse',rsf.doc.rsfpar('bool','n','','''if y, go from small to large on the bar scale '''))
sfgrey.par('wantframenum',rsf.doc.rsfpar('bool','(bool) (n3 > 1)','','''if y, display third axis position in the corner '''))
sfgrey.par('nreserve',rsf.doc.rsfpar('int','8','','''reserved colors '''))
sfgrey.par('gpow',rsf.doc.rsfpar('float','1','','''raise data to gpow power for display '''))
sfgrey.par('gainpanel',rsf.doc.rsfpar('string ',desc='''gain reference: 'a' for all, 'e' for each, or number '''))
sfgrey.par('bar',rsf.doc.rsfpar('string ',desc='''file for scalebar data '''))
sfgrey.par('color',rsf.doc.rsfpar('string ',desc='''color scheme (default is i) '''))
sfgrey.version('2.1-git')
sfgrey.synopsis('''sfgrey < in.rsf > out.rsf > bar.rsf transp=y yreverse=y xreverse=n gpow= phalf= clip= pclip= gainstep=0.5+n1/256. allpos=n mean=n bias=0. polarity=n symcp=n verb=n scalebar=n minval= maxval= barreverse=n wantframenum=(bool) (n3 > 1) nreserve=8 gpow=1 gainpanel= bar= color= > (plot.vpl | char.rsf)''','''Can input char values.
If called "byte", outputs char values.

If called "bar", outputs scalebar data.

Run "sfdoc stdplot" for more parameters.

March 2015 program of the month:
http://ahay.org/blog/2015/03/04/program-of-the-month-sfgrey/
''')
rsf.doc.progs['sfgrey']=sfgrey

sfgrey3 = rsf.doc.rsfprog('sfgrey3','plot/main/grey3.c','''Generate 3-D cube plot.''')
sfgrey3.par('point1',rsf.doc.rsfpar('float','0.5','','''fraction of the vertical axis for front face '''))
sfgrey3.par('point2',rsf.doc.rsfpar('float','0.5','','''fraction of the horizontal axis for front face '''))
sfgrey3.par('frame1',rsf.doc.rsfpar('int','0','','''top frame number '''))
sfgrey3.par('frame2',rsf.doc.rsfpar('int','n2-1','','''side frame number '''))
sfgrey3.par('frame3',rsf.doc.rsfpar('int','0','','''front frame number '''))
sfgrey3.par('movie',rsf.doc.rsfpar('int','0','','''0: no movie, 1: movie over axis 1, 2: axis 2, 3: axis 3 '''))
sfgrey3.par('dframe',rsf.doc.rsfpar('int','1','','''frame increment in a movie '''))
sfgrey3.par('n1pix',rsf.doc.rsfpar('int','n1/point1+n3/(1.-point1)','','''number of vertical pixels '''))
sfgrey3.par('n2pix',rsf.doc.rsfpar('int','n2/point2+n3/(1.-point2)','','''number of horizontal pixels '''))
sfgrey3.par('flat',rsf.doc.rsfpar('bool','y','','''if n, display perspective view '''))
sfgrey3.par('scalebar',rsf.doc.rsfpar('bool','n','','''if y, draw scalebar '''))
sfgrey3.par('minval',rsf.doc.rsfpar('float','','','''minimum value for scalebar (default is the data minimum) '''))
sfgrey3.par('maxval',rsf.doc.rsfpar('float','','','''maximum value for scalebar (default is the data maximum) '''))
sfgrey3.par('barreverse',rsf.doc.rsfpar('bool','n','','''if y, go from small to large on the bar scale '''))
sfgrey3.par('nreserve',rsf.doc.rsfpar('int','8','','''reserved colors '''))
sfgrey3.par('bar',rsf.doc.rsfpar('string ',desc='''file for scalebar data '''))
sfgrey3.par('color',rsf.doc.rsfpar('string ',desc='''color scheme (default is i) '''))
sfgrey3.version('2.1-git')
sfgrey3.synopsis('''sfgrey3 < in.rsf point1=0.5 point2=0.5 frame1=0 frame2=n2-1 frame3=0 movie=0 dframe=1 n1pix=n1/point1+n3/(1.-point1) n2pix=n2/point2+n3/(1.-point2) flat=y scalebar=n minval= maxval= barreverse=n nreserve=8 bar= color= > plot.vpl''','''Requires an "unsigned char" input (the output of sfbyte).

April 2012 program of the month:
http://ahay.org/blog/2012/04/01/program-of-the-month-sfgrey3/
''')
rsf.doc.progs['sfgrey3']=sfgrey3

sfgrey4 = rsf.doc.rsfprog('sfgrey4','plot/main/grey4.c','''Generate movie of 3-D cube plots.''')
sfgrey4.par('point1',rsf.doc.rsfpar('float','0.5','','''fraction of the vertical axis for front face '''))
sfgrey4.par('point2',rsf.doc.rsfpar('float','0.5','','''fraction of the horizontal axis for front face '''))
sfgrey4.par('frame1',rsf.doc.rsfpar('int','0','','''top frame number '''))
sfgrey4.par('frame2',rsf.doc.rsfpar('int','n2-1','','''side frame number '''))
sfgrey4.par('frame3',rsf.doc.rsfpar('int','0','','''front frame number '''))
sfgrey4.par('n1pix',rsf.doc.rsfpar('int','n1/point1+n3/(1.-point1)','','''number of vertical pixels '''))
sfgrey4.par('n2pix',rsf.doc.rsfpar('int','n2/point2+n3/(1.-point2)','','''number of horizontal pixels '''))
sfgrey4.par('flat',rsf.doc.rsfpar('bool','y','','''if n, display perspective view '''))
sfgrey4.par('scalebar',rsf.doc.rsfpar('bool','n','','''if y, draw scalebar '''))
sfgrey4.par('minval',rsf.doc.rsfpar('float','','','''minimum value for scalebar (default is the data minimum) '''))
sfgrey4.par('maxval',rsf.doc.rsfpar('float','','','''maximum value for scalebar (default is the data maximum) '''))
sfgrey4.par('barreverse',rsf.doc.rsfpar('bool','n','','''if y, go from small to large on the bar scale '''))
sfgrey4.par('nreserve',rsf.doc.rsfpar('int','8','','''reserved colors '''))
sfgrey4.par('bar',rsf.doc.rsfpar('string ',desc='''file for scalebar data '''))
sfgrey4.par('color',rsf.doc.rsfpar('string ',desc='''color scheme (default is i) '''))
sfgrey4.version('2.1-git')
sfgrey4.synopsis('''sfgrey4 < in.rsf point1=0.5 point2=0.5 frame1=0 frame2=n2-1 frame3=0 n1pix=n1/point1+n3/(1.-point1) n2pix=n2/point2+n3/(1.-point2) flat=y scalebar=n minval= maxval= barreverse=n nreserve=8 bar= color= > plot.vpl''','''Requires an "unsigned char" input (the output of sfbyte).
''')
rsf.doc.progs['sfgrey4']=sfgrey4

sfplas = rsf.doc.rsfprog('sfplas','plot/main/plas.c','''Plot Assembler - convert ascii to vplot. ''')
sfplas.version('2.1-git')
sfplas.synopsis('''sfplas''','''
November 2015 program of the month:
http://ahay.org/blog/2015/11/16/
''')
rsf.doc.progs['sfplas']=sfplas

sfpldb = rsf.doc.rsfprog('sfpldb','plot/main/pldb.c','''Plot Debugger - convert vplot to ascii. ''')
sfpldb.version('2.1-git')
sfpldb.synopsis('''sfpldb''','''
November 2015 program of the month:
http://ahay.org/blog/2015/11/16/

See also vplotdiff. ''')
rsf.doc.progs['sfpldb']=sfpldb

sfplotrays = rsf.doc.rsfprog('sfplotrays','plot/main/plotrays.c','''Plot rays.''')
sfplotrays.par('frame',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfplotrays.par('nt',rsf.doc.rsfpar('int','n1*n2','','''maximum ray length '''))
sfplotrays.par('jr',rsf.doc.rsfpar('int','1','','''skip rays '''))
sfplotrays.par('frame',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfplotrays.version('2.1-git')
sfplotrays.synopsis('''sfplotrays frame=frame.rsf nt=n1*n2 jr=1 < rays.rsf > plot.vpl''','''Run "sfdoc stdplot" for more parameters.
''')
rsf.doc.progs['sfplotrays']=sfplotrays

sfthplot = rsf.doc.rsfprog('sfthplot','plot/main/thplot.c','''Hidden-line surface plot.''')
sfthplot.par('uflag',rsf.doc.rsfpar('bool','y','','''if y, plot upper side of the surface '''))
sfthplot.par('dflag',rsf.doc.rsfpar('bool','y','','''if y, plot down side of the surface '''))
sfthplot.par('alpha',rsf.doc.rsfpar('float','45.','','''apparent angle in degrees, |alpha| < 89 '''))
sfthplot.par('titlsz',rsf.doc.rsfpar('int','9','','''title size '''))
sfthplot.par('axissz',rsf.doc.rsfpar('int','6','','''axes size '''))
sfthplot.par('plotfat',rsf.doc.rsfpar('int','0','','''line fatness '''))
sfthplot.par('titlefat',rsf.doc.rsfpar('int','2','','''title fatness '''))
sfthplot.par('axisfat',rsf.doc.rsfpar('int','2','','''axes fatness '''))
sfthplot.par('plotcolup',rsf.doc.rsfpar('int','VP_YELLOW','','''color of the upper side '''))
sfthplot.par('plotcoldn',rsf.doc.rsfpar('int','VP_RED','','''color of the lower side '''))
sfthplot.par('wanttitle',rsf.doc.rsfpar('bool','y','',''''''))
sfthplot.par('axis',rsf.doc.rsfpar('bool','y','',''''''))
sfthplot.par('axis1',rsf.doc.rsfpar('bool','y','',''''''))
sfthplot.par('axis2',rsf.doc.rsfpar('bool','y','',''''''))
sfthplot.par('axis3',rsf.doc.rsfpar('bool','y','','''plot axis '''))
sfthplot.par('clip',rsf.doc.rsfpar('float','0.','','''data clip '''))
sfthplot.par('pclip',rsf.doc.rsfpar('float','100.','','''data clip percentile '''))
sfthplot.par('gainstep',rsf.doc.rsfpar('int','0.5+nx/256.','','''subsampling for gpow and clip estimation '''))
sfthplot.par('bias',rsf.doc.rsfpar('float','0.','','''subtract bias from data '''))
sfthplot.par('dclip',rsf.doc.rsfpar('float','1.','','''change the clip: clip *= dclip '''))
sfthplot.par('norm',rsf.doc.rsfpar('bool','y','','''normalize by the clip '''))
sfthplot.par('xc',rsf.doc.rsfpar('float','1.5','',''''''))
sfthplot.par('zc',rsf.doc.rsfpar('float','3','','''lower left corner of the plot '''))
sfthplot.par('ratio',rsf.doc.rsfpar('float','5.','','''plot adjustment '''))
sfthplot.par('zmax',rsf.doc.rsfpar('float','','',''''''))
sfthplot.par('zmin',rsf.doc.rsfpar('float','','',''''''))
sfthplot.par('sz',rsf.doc.rsfpar('float','6.','','''vertical scale '''))
sfthplot.par('title',rsf.doc.rsfpar('string ',desc=''''''))
sfthplot.version('2.1-git')
sfthplot.synopsis('''sfthplot < in.rsf uflag=y dflag=y alpha=45. titlsz=9 axissz=6 plotfat=0 titlefat=2 axisfat=2 plotcolup=VP_YELLOW plotcoldn=VP_RED wanttitle=y axis=y axis1=y axis2=y axis3=y clip=0. pclip=100. gainstep=0.5+nx/256. bias=0. dclip=1. norm=y xc=1.5 zc=3 ratio=5. zmax= zmin= sz=6. title= > plot.vpl ''','''''')
rsf.doc.progs['sfthplot']=sfthplot

sfvplotdiff = rsf.doc.rsfprog('sfvplotdiff','plot/main/vplotdiff.c','''Vplot diff - see if 2 vplot files represent "identical" plots. ''')
sfvplotdiff.version('2.1-git')
sfvplotdiff.synopsis('''sfvplotdiff''','''''')
rsf.doc.progs['sfvplotdiff']=sfvplotdiff

sfwiggle = rsf.doc.rsfprog('sfwiggle','plot/main/wiggle.c','''Plot data with wiggly traces. ''')
sfwiggle.par('xpos',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwiggle.par('xmax',rsf.doc.rsfpar('float','','','''maximum trace position (if using xpos) '''))
sfwiggle.par('xmin',rsf.doc.rsfpar('float','','','''minimum trace position (if using xpos) '''))
sfwiggle.par('poly',rsf.doc.rsfpar('bool','n','','''if draw polygons '''))
sfwiggle.par('polyneg',rsf.doc.rsfpar('bool','n','','''if polygons for negative values '''))
sfwiggle.par('fatp',rsf.doc.rsfpar('int','1','','''polygon border fatness '''))
sfwiggle.par('xmask',rsf.doc.rsfpar('int','1','','''polygon filling '''))
sfwiggle.par('ymask',rsf.doc.rsfpar('int','1','','''polygon filling '''))
sfwiggle.par('pclip',rsf.doc.rsfpar('float','98.','','''clip percentile '''))
sfwiggle.par('zplot',rsf.doc.rsfpar('float','0.75','','''vertical separation '''))
sfwiggle.par('clip',rsf.doc.rsfpar('float','0.','','''data clip (estimated from pclip by default '''))
sfwiggle.par('seemean',rsf.doc.rsfpar('bool','n','','''if y, plot mean lines of traces '''))
sfwiggle.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfwiggle.par('transp',rsf.doc.rsfpar('bool','n','','''if y, transpose the axes '''))
sfwiggle.par('yreverse',rsf.doc.rsfpar('bool','n','','''if y, reverse the vertical axis '''))
sfwiggle.par('xreverse',rsf.doc.rsfpar('bool','n','','''if y, reverse the horizontal axis '''))
sfwiggle.par('xpos',rsf.doc.rsfpar('string ',desc='''optional header file with trace positions (auxiliary input file name)'''))
sfwiggle.version('2.1-git')
sfwiggle.synopsis('''sfwiggle < in.rsf xpos=xpos.rsf xmax= xmin= poly=n polyneg=n fatp=1 xmask=1 ymask=1 pclip=98. zplot=0.75 clip=0. seemean=n verb=n transp=n yreverse=n xreverse=n > plot.vpl''','''Run "sfdoc stdplot" for more parameters.

June 2013 program of the month:
http://www.ahay.org/blog/2013/06/12/program-of-the-month-sfwiggle/
''')
rsf.doc.progs['sfwiggle']=sfwiggle

rsf.doc.progs['sfbyte']=sfgrey
rsf.doc.progs['sfbar']=sfgrey
rsf.doc.progs['sfcubeplot']=sfgrey3
