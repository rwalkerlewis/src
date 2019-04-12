import rsf.doc

sfintervalVTI = rsf.doc.rsfprog('sfintervalVTI','user/lcasasan/MintervalVTI.c','''Interval/Effective VTI parameters from Effective/Interval profiles ''')
sfintervalVTI.par('vH_out',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfintervalVTI.par('eta_out',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfintervalVTI.par('eta',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfintervalVTI.par('interval',rsf.doc.rsfpar('bool','y','','''output are interval [y] or effective [n] profiles '''))
sfintervalVTI.par('vH_out',rsf.doc.rsfpar('string ',desc='''output HOR vel(auxiliary output file name)'''))
sfintervalVTI.par('eta_out',rsf.doc.rsfpar('string ',desc='''output eta(auxiliary output file name)'''))
sfintervalVTI.par('eta',rsf.doc.rsfpar('string ',desc='''input eta(auxiliary input file name)'''))
sfintervalVTI.version('2.1-git')
sfintervalVTI.synopsis('''sfintervalVTI < vn.rsf > vn_out.rsf vH_out=vh_out.rsf eta_out=eta_out.rsf eta=eta.rsf interval=y''','''''')
rsf.doc.progs['sfintervalVTI']=sfintervalVTI

sfsmoothderLS = rsf.doc.rsfprog('sfsmoothderLS','user/lcasasan/MsmoothderLS.c','''Convert input to its derivative using LS and shaping regularization''')
sfsmoothderLS.par('dataout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsmoothderLS.par('niter',rsf.doc.rsfpar('int','100','','''maximum number of iterations '''))
sfsmoothderLS.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfsmoothderLS.par('dataout',rsf.doc.rsfpar('string ',desc='''optionally, output predicted data (auxiliary output file name)'''))
sfsmoothderLS.version('2.1-git Mdix.c 5595 2010-03-21 16:54:14Z sfomel')
sfsmoothderLS.synopsis('''sfsmoothderLS < DATA.rsf > MODEL.rsf dataout=DATA_OUT.rsf niter=100 rect#=(1,1,...)''','''* applied to causint_lop d = L m

Takes: rect1= rect2= ...

rectN defines the size of the smoothing stencil in N-th dimension.
''')
rsf.doc.progs['sfsmoothderLS']=sfsmoothderLS

sfspitz = rsf.doc.rsfprog('sfspitz','user/lcasasan/Mspitz.c','''Missing data interpolation in 2-D using F-X Prediction Error Filters''')
sfspitz.par('order',rsf.doc.rsfpar('int','3','','''linear PEF order'''))
sfspitz.par('ntraces',rsf.doc.rsfpar('int','1','','''number of traces to be interpolated '''))
sfspitz.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfspitz.par('norm',rsf.doc.rsfpar('bool','y','','''normalization flag '''))
sfspitz.version('2.1-git')
sfspitz.synopsis('''sfspitz < in.rsf > out.rsf order=3 ntraces=1 verb=n norm=y''','''based on Seismic trace interpolation in the F-X domain
S.Spitz Geophysics 56, 785(1991). 

''')
rsf.doc.progs['sfspitz']=sfspitz

sfspitzbl = rsf.doc.rsfprog('sfspitzbl','user/lcasasan/Mspitzbl.c','''Missing data interpolation in 2-D using F-X Prediction Error Filters''')
sfspitzbl.par('order',rsf.doc.rsfpar('int','3','','''linear PEF order'''))
sfspitzbl.par('ntraces',rsf.doc.rsfpar('int','1','','''number of traces to be interpolated '''))
sfspitzbl.par('f1',rsf.doc.rsfpar('float','0.0','','''lower  frequency in band limited signal >= 0.0  '''))
sfspitzbl.par('f2',rsf.doc.rsfpar('float','1.0','','''higher frequency in band limited signal <= 1.0  (normalized nyquist)'''))
sfspitzbl.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfspitzbl.par('norm',rsf.doc.rsfpar('bool','y','','''normalization flag '''))
sfspitzbl.version('2.1-git')
sfspitzbl.synopsis('''sfspitzbl < in.rsf > out.rsf order=3 ntraces=1 f1=0.0 f2=1.0 verb=n norm=y''','''based on Seismic trace interpolation in the F-X domain
S.Spitz Geophysics 56, 785(1991). 
This implementation is for bandlimited [f1 f2] signals

''')
rsf.doc.progs['sfspitzbl']=sfspitzbl

sfspitzns = rsf.doc.rsfprog('sfspitzns','user/lcasasan/Mspitzns.c','''Missing data interpolation in 2-D using F-X Prediction Error Filters''')
sfspitzns.par('w1',rsf.doc.rsfpar('int','n1','','''lenght of patch along the first dimension '''))
sfspitzns.par('w2',rsf.doc.rsfpar('int','n2','','''lenght of patch along the second dimension '''))
sfspitzns.par('k1',rsf.doc.rsfpar('int','1','','''number of patches along the first dimension '''))
sfspitzns.par('k2',rsf.doc.rsfpar('int','1','','''number of patches along the second dimension '''))
sfspitzns.par('order',rsf.doc.rsfpar('int','3','','''linear PEF order'''))
sfspitzns.par('ntraces',rsf.doc.rsfpar('int','1','','''number of traces to be interpolated '''))
sfspitzns.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfspitzns.par('norm',rsf.doc.rsfpar('bool','y','','''output normalization flag '''))
sfspitzns.version('2.1-git')
sfspitzns.synopsis('''sfspitzns < in.rsf > out.rsf w1=n1 w2=n2 k1=1 k2=1 order=3 ntraces=1 verb=n norm=y''','''based on Seismic trace interpolation in the F-X domain
S.Spitz Geophysics 56, 785(1991). 

Uses 2D Patching. 
''')
rsf.doc.progs['sfspitzns']=sfspitzns

sfspitzblns = rsf.doc.rsfprog('sfspitzblns','user/lcasasan/Mspitzblns.c','''Missing data interpolation in 2-D using F-X Prediction Error Filters''')
sfspitzblns.par('w1',rsf.doc.rsfpar('int','n1','','''lenght of patch along the first dimension '''))
sfspitzblns.par('w2',rsf.doc.rsfpar('int','n2','','''lenght of patch along the second dimension '''))
sfspitzblns.par('k1',rsf.doc.rsfpar('int','1','','''number of patches along the first dimension '''))
sfspitzblns.par('k2',rsf.doc.rsfpar('int','1','','''number of patches along the second dimension '''))
sfspitzblns.par('order',rsf.doc.rsfpar('int','3','','''linear PEF order'''))
sfspitzblns.par('ntraces',rsf.doc.rsfpar('int','1','','''number of traces to be interpolated '''))
sfspitzblns.par('f1',rsf.doc.rsfpar('float','0.0','','''lower  frequency in band limited signal >= 0.0  '''))
sfspitzblns.par('f2',rsf.doc.rsfpar('float','1.0','','''higher frequency in band limited signal <= 1.0  (normalized nyquist)'''))
sfspitzblns.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfspitzblns.par('norm',rsf.doc.rsfpar('bool','y','','''output normalization flag '''))
sfspitzblns.version('2.1-git')
sfspitzblns.synopsis('''sfspitzblns < in.rsf > out.rsf w1=n1 w2=n2 k1=1 k2=1 order=3 ntraces=1 f1=0.0 f2=1.0 verb=n norm=y''','''based on Seismic trace interpolation in the F-X domain
S.Spitz Geophysics 56, 785(1991). 

Uses 2D Patching. 
''')
rsf.doc.progs['sfspitzblns']=sfspitzblns

sfpwdnorm = rsf.doc.rsfprog('sfpwdnorm','user/lcasasan/Mpwdnorm.c','''3-D plane wave destruction. ''')
sfpwdnorm.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpwdnorm.par('n4',rsf.doc.rsfpar('int','2','','''what to compute in 3-D. 0: in-line, 1: cross-line, 2: both '''))
sfpwdnorm.par('order',rsf.doc.rsfpar('int','1','','''accuracy '''))
sfpwdnorm.par('nj1',rsf.doc.rsfpar('int','1','','''in-line aliasing '''))
sfpwdnorm.par('nj2',rsf.doc.rsfpar('int','1','','''cross-line aliasing '''))
sfpwdnorm.par('norm',rsf.doc.rsfpar('bool','y','','''filter normalization '''))
sfpwdnorm.version('2.1-git Mpwd.c 5367 2010-02-16 00:33:09Z sfomel')
sfpwdnorm.synopsis('''sfpwdnorm < in.rsf dip=dip.rsf > out.rsf n4=2 order=1 nj1=1 nj2=1 norm=y''','''''')
rsf.doc.progs['sfpwdnorm']=sfpwdnorm

sfsmoothder1 = rsf.doc.rsfprog('sfsmoothder1','user/lcasasan/Msmoothder1.c','''Convert input to its derivative using LS and shaping regularization''')
sfsmoothder1.par('dataout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsmoothder1.par('niter',rsf.doc.rsfpar('int','100','','''maximum number of iterations '''))
sfsmoothder1.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfsmoothder1.par('dataout',rsf.doc.rsfpar('string ',desc='''optionally, output predicted data (auxiliary output file name)'''))
sfsmoothder1.version('2.1-git Mdix.c 5595 2010-03-21 16:54:14Z sfomel')
sfsmoothder1.synopsis('''sfsmoothder1 < DATA.rsf > MODEL.rsf dataout=DATA_OUT.rsf niter=100 rect#=(1,1,...)''','''* applied to causint_lop d = L m

Takes: rect1= rect2= ...

rectN defines the size of the smoothing stencil in N-th dimension.
''')
rsf.doc.progs['sfsmoothder1']=sfsmoothder1

sfsmoothder2 = rsf.doc.rsfprog('sfsmoothder2','user/lcasasan/Msmoothder2.c','''Convert input to its derivative using LS and shaping regularization''')
sfsmoothder2.par('dataout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsmoothder2.par('eps',rsf.doc.rsfpar('float','1.0','','''dumping factor'''))
sfsmoothder2.par('niter',rsf.doc.rsfpar('int','100','','''maximum number of iterations '''))
sfsmoothder2.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfsmoothder2.par('dataout',rsf.doc.rsfpar('string ',desc='''optionally, output predicted data (auxiliary output file name)'''))
sfsmoothder2.version('2.1-git Mdix.c 5595 2010-03-21 16:54:14Z sfomel')
sfsmoothder2.synopsis('''sfsmoothder2 < DATA.rsf > MODEL.rsf dataout=DATA_OUT.rsf eps=1.0 niter=100 rect#=(1,1,...)''','''* applied to causint_lop d = L m

Takes: rect1= rect2= ...

rectN defines the size of the smoothing stencil in N-th dimension.
''')
rsf.doc.progs['sfsmoothder2']=sfsmoothder2

sfsmoothcur = rsf.doc.rsfprog('sfsmoothcur','user/lcasasan/Msmoothcur.c','''Convert input slope and time derivative''')
sfsmoothcur.par('dipt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsmoothcur.par('dataout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsmoothcur.par('eps',rsf.doc.rsfpar('float','1.0','','''dumping factor'''))
sfsmoothcur.par('niter',rsf.doc.rsfpar('int','100','','''maximum number of iterations '''))
sfsmoothcur.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfsmoothcur.par('dataout',rsf.doc.rsfpar('string ',desc='''optionally, output predicted data (auxiliary output file name)'''))
sfsmoothcur.version('2.1-git Mdix.c 5595 2010-03-21 16:54:14Z sfomel')
sfsmoothcur.synopsis('''sfsmoothcur < DATA.rsf dipt=DIPT.rsf > MODEL.rsf dataout=DATA_OUT.rsf eps=1.0 niter=100 rect#=(1,1,...)''','''* to its curvature field using LS and shaping regularization
* applied to causint_lop d = L m

Takes: rect1= rect2= ...

rectN defines the size of the smoothing stencil in N-th dimension.
''')
rsf.doc.progs['sfsmoothcur']=sfsmoothcur

sfpmig1 = rsf.doc.rsfprog('sfpmig1','user/lcasasan/Mpmig1.c','''Slope-based prestack (t,xs,h) time migration . ''')
sfpmig1.par('sdip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpmig1.par('hdip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpmig1.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfpmig1.par('nw',rsf.doc.rsfpar('int','4','','''interpolator size (2,3,4,6,8) '''))
sfpmig1.par('mzo',rsf.doc.rsfpar('bool','n','','''do migration to zero offset '''))
sfpmig1.version('2.1-git Mpmig.c 4796 2009-09-29 19:39:07Z ivlad')
sfpmig1.synopsis('''sfpmig1 < csg.rsf sdip=sdip.rsf hdip=hdip.rsf > mig.rsf half=y nw=4 mzo=n''','''''')
rsf.doc.progs['sfpmig1']=sfpmig1

sfjoiner = rsf.doc.rsfprog('sfjoiner','user/lcasasan/Mjoiner.c','''Join two selected points along the first dimension ''')
sfjoiner.par('index',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfjoiner.par('nw',rsf.doc.rsfpar('int','','','''length of joining window '''))
sfjoiner.version('2.1-git')
sfjoiner.synopsis('''sfjoiner < in.rsf index=index_FILE.rsf > out.rsf nw=''','''''')
rsf.doc.progs['sfjoiner']=sfjoiner

sffindmax1 = rsf.doc.rsfprog('sffindmax1','user/lcasasan/Mfindmax1.c','''Find max value and its sampled position along fast dimension ''')
sffindmax1.par('max_val',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffindmax1.par('shift',rsf.doc.rsfpar('int','0','','''shift '''))
sffindmax1.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sffindmax1.par('max_val',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffindmax1.version('2.1-git')
sffindmax1.synopsis('''sffindmax1 < in.rsf > out.rsf max_val=max_val.rsf shift=0 verb=n''','''''')
rsf.doc.progs['sffindmax1']=sffindmax1

sffindintval = rsf.doc.rsfprog('sffindintval','user/lcasasan/Mfindintval.c','''Find a certain integer value position in an array [n1]''')
sffindintval.par('val',rsf.doc.rsfpar('int','','',''''''))
sffindintval.par('val2',rsf.doc.rsfpar('int','val','',''''''))
sffindintval.par('type',rsf.doc.rsfpar('string ',desc='''type of comparison eq (=) leq (<=) geq(>=) '''))
sffindintval.version('2.1-git')
sffindintval.synopsis('''sffindintval < in.rsf > out.rsf val= val2=val type=''','''''')
rsf.doc.progs['sffindintval']=sffindintval

sfmultmask = rsf.doc.rsfprog('sfmultmask','user/lcasasan/Mmultmask.c','''Create a data mask using multiple muting curve from MRKE ''')
sfmultmask.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmultmask.par('start',rsf.doc.rsfpar('bool','n','','''mask from starting sample to index value in mask '''))
sfmultmask.par('smooth',rsf.doc.rsfpar('bool','n','','''smoothed mask [raised cosine] '''))
sfmultmask.par('nw',rsf.doc.rsfpar('int','0','','''smoothing window length must be odd'''))
sfmultmask.par('shift',rsf.doc.rsfpar('bool','n','','''shift '''))
sfmultmask.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfmultmask.version('2.1-git')
sfmultmask.synopsis('''sfmultmask < in.rsf mask=mask.rsf > out.rsf start=n smooth=n nw=0 shift=n verb=n''','''''')
rsf.doc.progs['sfmultmask']=sfmultmask

sfmatch1d = rsf.doc.rsfprog('sfmatch1d','user/lcasasan/Mmatch1d.c','''1D Least-Sqaure Adaptive Matched-Filter for Multiple Suppression ''')
sfmatch1d.par('multiple',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmatch1d.par('w1',rsf.doc.rsfpar('int','9','','''data window length along 1st dimentions (time/depth) '''))
sfmatch1d.par('order',rsf.doc.rsfpar('int','w1-2','','''matchied-filter order '''))
sfmatch1d.par('w2',rsf.doc.rsfpar('int','3','','''data window length along 1st dimentions (time/depth) '''))
sfmatch1d.par('eps',rsf.doc.rsfpar('float','0.01','','''dumping parameter  '''))
sfmatch1d.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfmatch1d.par('transient',rsf.doc.rsfpar('bool','n','','''transient convolution [y/n] '''))
sfmatch1d.par('multiple',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfmatch1d.par('method',rsf.doc.rsfpar('string ',desc='''method to use (old,new) '''))
sfmatch1d.version('2.1-git')
sfmatch1d.synopsis('''sfmatch1d < in.rsf > out.rsf multiple=multiple.rsf w1=9 order=w1-2 w2=3 eps=0.01 verb=n transient=n method=''','''	x = argmin || d - M x ||^2 

	The Program uses internal (icaf.c) or transient convolution (tcaf.c)
''')
rsf.doc.progs['sfmatch1d']=sfmatch1d

sflomatch = rsf.doc.rsfprog('sflomatch','user/lcasasan/Mlomatch.c','''Local Matched filter for coherent noise removal (1-D, 2-D, and 3-D). ''')
sflomatch.par('match',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflomatch.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflomatch.par('w',rsf.doc.rsfpar('ints','','','''window size  [dim1]'''))
sflomatch.par('a',rsf.doc.rsfpar('ints','','','''filter size  [dim1]'''))
sflomatch.par('k',rsf.doc.rsfpar('ints','','','''number of windows  [dim1]'''))
sflomatch.par('gap',rsf.doc.rsfpar('ints','','','''filter gap  [dim1]'''))
sflomatch.par('center',rsf.doc.rsfpar('ints','','','''filter center  [dim1]'''))
sflomatch.par('niter',rsf.doc.rsfpar('int','1','','''number of POCS iterations: =1 L2 norm ; >1 L1 norm '''))
sflomatch.par('perc',rsf.doc.rsfpar('float','90.0','','''percentage for sharpening [L1 norm]'''))
sflomatch.par('eps',rsf.doc.rsfpar('float','0.01','','''dumping parameter x=(M'M+eps*I)M'd '''))
sflomatch.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sflomatch.par('dim',rsf.doc.rsfpar('int','dim','','''matched filter  dimensionality '''))
sflomatch.par('liter',rsf.doc.rsfpar('int','aa->nh','','''number of linear iteration'''))
sflomatch.par('match',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sflomatch.par('lag',rsf.doc.rsfpar('string ',desc='''output file for filter lags '''))
sflomatch.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sflomatch.version('2.1-git')
sflomatch.synopsis('''sflomatch < dat.rsf > mcf.rsf match=mat.rsf mask=known.rsf w= a= k= gap= center= niter=1 perc=90.0 eps=0.01 verb=n dim=dim liter=aa->nh lag=''','''''')
rsf.doc.progs['sflomatch']=sflomatch

sfTestcdstep = rsf.doc.rsfprog('sfTestcdstep','user/lcasasan/MTestcdstep.c','''None''')
sfTestcdstep.version('2.1-git')
sfTestcdstep.synopsis('''sfTestcdstep''','''''')
rsf.doc.progs['sfTestcdstep']=sfTestcdstep

sftest1_matchl1 = rsf.doc.rsfprog('sftest1_matchl1','user/lcasasan/Mtest1_matchl1.c','''L1 1D matched filter ''')
sftest1_matchl1.par('filt',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftest1_matchl1.par('mult',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftest1_matchl1.par('nb',rsf.doc.rsfpar('int','3','','''matched-filter order '''))
sftest1_matchl1.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sftest1_matchl1.par('niter',rsf.doc.rsfpar('int','100','','''number of POCS iterations '''))
sftest1_matchl1.par('perc',rsf.doc.rsfpar('float','90.0','','''percentage for sharpening '''))
sftest1_matchl1.par('mult',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sftest1_matchl1.version('2.1-git')
sftest1_matchl1.synopsis('''sftest1_matchl1 < inp.rsf filt=filt.rsf > out.rsf mult=mult.rsf nb=3 verb=n niter=100 perc=90.0''','''''')
rsf.doc.progs['sftest1_matchl1']=sftest1_matchl1

sftest2_matchl1 = rsf.doc.rsfprog('sftest2_matchl1','user/lcasasan/Mtest2_matchl1.c','''L1 1D matched filter ''')
sftest2_matchl1.par('filt',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftest2_matchl1.par('mult',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftest2_matchl1.par('nb',rsf.doc.rsfpar('int','3','','''matched-filter order '''))
sftest2_matchl1.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sftest2_matchl1.par('niter',rsf.doc.rsfpar('int','100','','''number of POCS iterations '''))
sftest2_matchl1.par('liter',rsf.doc.rsfpar('int','nb','','''number of CG iterations '''))
sftest2_matchl1.par('perc',rsf.doc.rsfpar('float','90.0','','''percentage for sharpening '''))
sftest2_matchl1.par('mult',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sftest2_matchl1.version('2.1-git')
sftest2_matchl1.synopsis('''sftest2_matchl1 < inp.rsf filt=filt.rsf > out.rsf mult=mult.rsf nb=3 verb=n niter=100 liter=nb perc=90.0''','''''')
rsf.doc.progs['sftest2_matchl1']=sftest2_matchl1

sfbil1_new = rsf.doc.rsfprog('sfbil1_new','user/lcasasan/Mbil1_new.c','''L1 regression 0 ~= d - G * m''')
sfbil1_new.par('reg',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfbil1_new.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfbil1_new.par('niter',rsf.doc.rsfpar('int','10','','''number of POCS iterations '''))
sfbil1_new.par('Liter',rsf.doc.rsfpar('int','10','','''number of CG iterations '''))
sfbil1_new.par('perc',rsf.doc.rsfpar('float','90.0','','''percentage for sharpening '''))
sfbil1_new.version('2.1-git')
sfbil1_new.synopsis('''sfbil1_new < inp.rsf reg=reg.rsf > out.rsf verb=n niter=10 Liter=10 perc=90.0''','''*
* adapted from sfbil1
* ''')
rsf.doc.progs['sfbil1_new']=sfbil1_new

sflpfL1 = rsf.doc.rsfprog('sflpfL1','user/lcasasan/MlpfL1.c','''Local prediction filter (n-dimensional) in L1 norm. ''')
sflpfL1.par('match',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflpfL1.par('pred',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sflpfL1.par('liter',rsf.doc.rsfpar('int','10','','''number of CG iterations '''))
sflpfL1.par('niter',rsf.doc.rsfpar('int','25','','''number of POCS iterations [L1]'''))
sflpfL1.par('perc',rsf.doc.rsfpar('float','90.0','','''percentage for sharpening [L1]'''))
sflpfL1.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sflpfL1.par('pred',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sflpfL1.par('pef',rsf.doc.rsfpar('string ',desc='''signal PEF file (optional) '''))
sflpfL1.par('lag',rsf.doc.rsfpar('string ',desc='''file with PEF lags (optional) '''))
sflpfL1.version('2.1-git')
sflpfL1.synopsis('''sflpfL1 < dat.rsf match=mat.rsf > flt.rsf pred=pre.rsf liter=10 niter=25 perc=90.0 verb=y pef= lag=''','''''')
rsf.doc.progs['sflpfL1']=sflpfL1

