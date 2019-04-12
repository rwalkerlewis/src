import rsf.doc

sfditime2d = rsf.doc.rsfprog('sfditime2d','user/aklokov/Mditime2d.c','''2D Hybrid Radon transform for diffraction imaging in the time dip-angle domain ''')
sfditime2d.par('dweight',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfditime2d.par('reflMod',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfditime2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfditime2d.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfditime2d.par('isAA',rsf.doc.rsfpar('bool','n','','''if y, apply anti-aliasing '''))
sfditime2d.par('liter',rsf.doc.rsfpar('int','100','','''number of linear iterations (for inversion) '''))
sfditime2d.par('niter',rsf.doc.rsfpar('int','0','','''number of nonlinear iterations (for inversion) '''))
sfditime2d.par('eps',rsf.doc.rsfpar('float','0.','','''regularization parameter '''))
sfditime2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfditime2d.par('invMod',rsf.doc.rsfpar('int','2','','''number of nonlinear iterations (for inversion) '''))
sfditime2d.par('dip0n',rsf.doc.rsfpar('int','','','''number of dip0 values (if adj=y) '''))
sfditime2d.par('dip0d',rsf.doc.rsfpar('float','','','''dip0 sampling (if adj=y) '''))
sfditime2d.par('dip0o',rsf.doc.rsfpar('float','','','''dip0 origin (if adj=y) '''))
sfditime2d.par('xin',rsf.doc.rsfpar('int','','','''number of xi values (if adj=y) '''))
sfditime2d.par('xid',rsf.doc.rsfpar('float','','','''xi sampling (if adj=y) '''))
sfditime2d.par('xio',rsf.doc.rsfpar('float','','','''xi origin (if adj=y) '''))
sfditime2d.par('dipn',rsf.doc.rsfpar('int','','','''number of offsets '''))
sfditime2d.par('dipo',rsf.doc.rsfpar('float','','','''offset origin '''))
sfditime2d.par('dipd',rsf.doc.rsfpar('float','','','''offset sampling '''))
sfditime2d.par('dweight',rsf.doc.rsfpar('string ',desc='''input file containing data weights (auxiliary input file name)'''))
sfditime2d.version('2.1-git')
sfditime2d.synopsis('''sfditime2d < in.rsf > out.rsf dweight=fileDweight.rsf reflMod=fileRefl.rsf verb=n adj=n isAA=n liter=100 niter=0 eps=0. verb=n invMod=2 dip0n= dip0d= dip0o= xin= xid= xio= dipn= dipo= dipd=''','''''')
rsf.doc.progs['sfditime2d']=sfditime2d

sfditime3d = rsf.doc.rsfprog('sfditime3d','user/aklokov/Mditime3d.c','''3D Hybrid Radon transform for diffraction imaging in the time dip-angle domain ''')
sfditime3d.par('dweight',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfditime3d.par('reflMod',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfditime3d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfditime3d.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfditime3d.par('isAA',rsf.doc.rsfpar('bool','n','','''if y, apply anti-aliasing '''))
sfditime3d.par('liter',rsf.doc.rsfpar('int','100','','''number of linear iterations (for inversion) '''))
sfditime3d.par('niter',rsf.doc.rsfpar('int','0','','''number of nonlinear iterations (for inversion) '''))
sfditime3d.par('eps',rsf.doc.rsfpar('float','0.','','''regularization parameter '''))
sfditime3d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfditime3d.par('invMod',rsf.doc.rsfpar('int','2','','''number of nonlinear iterations (for inversion) '''))
sfditime3d.par('dip0n',rsf.doc.rsfpar('int','','','''number of dip0 values (if adj=y) '''))
sfditime3d.par('dip0d',rsf.doc.rsfpar('float','','','''dip0 sampling (if adj=y) '''))
sfditime3d.par('dip0o',rsf.doc.rsfpar('float','','','''dip0 origin (if adj=y) '''))
sfditime3d.par('sdip0n',rsf.doc.rsfpar('int','','','''number of sdip0 values (if adj=y) '''))
sfditime3d.par('sdip0d',rsf.doc.rsfpar('float','','','''sdip0 sampling (if adj=y) '''))
sfditime3d.par('sdip0o',rsf.doc.rsfpar('float','','','''sdip0 origin (if adj=y) '''))
sfditime3d.par('xin',rsf.doc.rsfpar('int','','','''number of xi values (if adj=y) '''))
sfditime3d.par('xid',rsf.doc.rsfpar('float','','','''xi sampling (if adj=y) '''))
sfditime3d.par('xio',rsf.doc.rsfpar('float','','','''xi origin (if adj=y) '''))
sfditime3d.par('sxin',rsf.doc.rsfpar('int','','','''number of xi values (if adj=y) '''))
sfditime3d.par('sxid',rsf.doc.rsfpar('float','','','''xi sampling (if adj=y) '''))
sfditime3d.par('sxio',rsf.doc.rsfpar('float','','','''xi origin (if adj=y) '''))
sfditime3d.par('dipn',rsf.doc.rsfpar('int','','','''number of dips in x-direction '''))
sfditime3d.par('dipo',rsf.doc.rsfpar('float','','','''dip origin in x-direction '''))
sfditime3d.par('dipd',rsf.doc.rsfpar('float','','','''dip sampling in x-direction '''))
sfditime3d.par('sdipn',rsf.doc.rsfpar('int','','','''number of dips in y-direction '''))
sfditime3d.par('sdipo',rsf.doc.rsfpar('float','','','''dip origin in y-direction '''))
sfditime3d.par('sdipd',rsf.doc.rsfpar('float','','','''dip sampling in y-direction '''))
sfditime3d.par('dweight',rsf.doc.rsfpar('string ',desc='''input file containing data weights (auxiliary input file name)'''))
sfditime3d.version('2.1-git')
sfditime3d.synopsis('''sfditime3d < in.rsf > out.rsf dweight=fileDweight.rsf reflMod=fileRefl.rsf verb=n adj=n isAA=n liter=100 niter=0 eps=0. verb=n invMod=2 dip0n= dip0d= dip0o= sdip0n= sdip0d= sdip0o= xin= xid= xio= sxin= sxid= sxio= dipn= dipo= dipd= sdipn= sdipo= sdipd=''','''''')
rsf.doc.progs['sfditime3d']=sfditime3d

sfcrssemb = rsf.doc.rsfprog('sfcrssemb','user/aklokov/Mcrssemb.c','''CRS-based semblance''')
sfcrssemb.par('dataSq',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcrssemb.par('xapp',rsf.doc.rsfpar('int','1','','''number of CIGs in the inline-direction processed simultaneously '''))
sfcrssemb.par('dipapp',rsf.doc.rsfpar('int','11','','''number of traces in the x-dip direction processed simultaneously '''))
sfcrssemb.par('coher',rsf.doc.rsfpar('int','11','','''height of a vertical window for semblance calculation '''))
sfcrssemb.par('scatnum',rsf.doc.rsfpar('int','1','','''shows how many traces were stacked in the scattering angle direction; 
       if the stack was normalized use the default value 
    '''))
sfcrssemb.par('s1',rsf.doc.rsfpar('float','','',''''''))
sfcrssemb.par('s2',rsf.doc.rsfpar('float','','',''''''))
sfcrssemb.version('2.1-git')
sfcrssemb.synopsis('''sfcrssemb < inDags_.rsf dataSq=inDagsSq_.rsf > sembFile_.rsf xapp=1 dipapp=11 coher=11 scatnum=1 s1= s2=''','''
Several CIGs are used simultaneously. Dip-angle sections corresponding to the same 
dip-angle compose a subvolume. The subvolume allows calculating semblance in the
scattering-angle direction along reflection boundaries.

Input:
inDags_.rsf   - dip-angle gathers - stack in the scattering-angle direction
InDagsSq_.rsf - stack of amplitude squares in the scattering-angle direction

Working with just dip-angle gathers use default value of "scatnum" parameter

Output:
sembFile_.rsf - crs-based semblance file; has the same dimensions as the input files
''')
rsf.doc.progs['sfcrssemb']=sfcrssemb

sfcrssemb3d = rsf.doc.rsfprog('sfcrssemb3d','user/aklokov/Mcrssemb3d.c','''CRS-based semblance for 3D''')
sfcrssemb3d.par('dataSq',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcrssemb3d.par('xapp',rsf.doc.rsfpar('int','1','','''number of CIGs in the inline-direction processed simultaneously '''))
sfcrssemb3d.par('yapp',rsf.doc.rsfpar('int','1','','''number of CIGs in the crossline-direction processed simultaneously '''))
sfcrssemb3d.par('dipappx',rsf.doc.rsfpar('int','11','','''number of traces in the x-dip direction processed simultaneously '''))
sfcrssemb3d.par('dipappy',rsf.doc.rsfpar('int','11','','''number of traces in the y-dip direction processed simultaneously '''))
sfcrssemb3d.par('coher',rsf.doc.rsfpar('int','11','','''height of a vertical window for semblance calculation '''))
sfcrssemb3d.par('scatnum',rsf.doc.rsfpar('int','1','','''shows how many traces were stacked in the scattering angle direction; 
       if the stack was normalized use the default value 
    '''))
sfcrssemb3d.version('2.1-git')
sfcrssemb3d.synopsis('''sfcrssemb3d < inDags_.rsf dataSq=inDagsSq_.rsf > sembFile_.rsf xapp=1 yapp=1 dipappx=11 dipappy=11 coher=11 scatnum=1''','''Several CIGs are used simultaneously. Dip-angle sections corresponding to the same 
dip-angle compose a subvolume. The subvolume allows calculating semblance in the
scattering-angle direction along reflection boundaries.

Input:
inDags_.rsf   - 3D dip-angle gathers - stack in the scattering-angle direction
inDagsSq_.rsf - stack of amplitude squares in the scattering-angle direction

Working with just dip-angle gathers use default value of "scatnum" parameter

Output:
sembFile_.rsf - crs-based semblance file; has the same dimensions as the input files
''')
rsf.doc.progs['sfcrssemb3d']=sfcrssemb3d

sfdiptaper = rsf.doc.rsfprog('sfdiptaper','user/aklokov/Mdiptaper.c','''Aperture optimization for migrated gathers in the dip-angle domain.''')
sfdiptaper.par('dz',rsf.doc.rsfpar('float','20.f','','''half of a migrated wave length '''))
sfdiptaper.par('greyarea',rsf.doc.rsfpar('float','10.f','','''width of event tail taper (in degree) '''))
sfdiptaper.version('2.1-git')
sfdiptaper.synopsis('''sfdiptaper < dipFile.rsf > taperFile.rsf dz=20.f greyarea=10.f''','''
Estimates a constructive imaging part of a reflection event in the dip-angle domain.
Basing on the estimation defines a stacking weight for every migrated sample.

Input:
dipFile.rsf - dips esitimated in constant-dip subimages. The dips are in degree (!).
A positive dip corresponds to an ascending boundary, a negative dip - to a descending boundary.
A constant-dip subimage consists of migrated traces correspondig to the same dip-angle.

Output:
taperFile.rsf - optimal weights for the migrated samples
''')
rsf.doc.progs['sfdiptaper']=sfdiptaper

sfdvscan2d = rsf.doc.rsfprog('sfdvscan2d','user/aklokov/Mdvscan2d.c','''Diffraction velocity analysis''')
sfdvscan2d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdvscan2d.par('gn',rsf.doc.rsfpar('int','1','','''number of scanned Vm/V values  '''))
sfdvscan2d.par('go',rsf.doc.rsfpar('float','1.0','','''start of Vm/V parameter '''))
sfdvscan2d.par('gd',rsf.doc.rsfpar('float','1','','''increment of Vm/V parameter '''))
sfdvscan2d.par('coher',rsf.doc.rsfpar('int','11','','''height of a vertical window for semblance calculation '''))
sfdvscan2d.par('cigNum',rsf.doc.rsfpar('int','1','','''height of a vertical window for semblance calculation '''))
sfdvscan2d.par('dlim',rsf.doc.rsfpar('float','fabs (dipStart_)','','''defines dip-angle-window for the analysis '''))
sfdvscan2d.par('isSemb',rsf.doc.rsfpar('bool','y','','''y - output is semblance; n - stack power '''))
sfdvscan2d.par('vel',rsf.doc.rsfpar('string ',desc='''velocity model file (velocity in km/s) (auxiliary input file name)'''))
sfdvscan2d.version('2.1-git')
sfdvscan2d.synopsis('''sfdvscan2d < dataFile_.rsf vel=velFile_.rsf > sembFile_.rsf gn=1 go=1.0 gd=1 coher=11 cigNum=1 dlim=fabs (dipStart_) isSemb=y''','''
Input:
dataFile_.rsf - migrated dip-angle gathers

Output:
sembFile_.rsf - semblance spectrum
''')
rsf.doc.progs['sfdvscan2d']=sfdvscan2d

sfpick2d = rsf.doc.rsfprog('sfpick2d','user/aklokov/Mpick2d.c','''2D picking''')
sfpick2d.par('eps',rsf.doc.rsfpar('float','0','','''smoothness measure '''))
sfpick2d.par('xApp',rsf.doc.rsfpar('int','1','','''x-aperture '''))
sfpick2d.version('2.1-git')
sfpick2d.synopsis('''sfpick2d < dataFile_.rsf > outFile_.rsf eps=0 xApp=1''','''
Input:
dataFile_.rsf - parameter spectrum (semblance) panel

Output:
outFile_.rsf - picked optimal values
''')
rsf.doc.progs['sfpick2d']=sfpick2d

sfgammapick2d = rsf.doc.rsfprog('sfgammapick2d','user/aklokov/Mgammapick2d.c','''2D picking for gamma=Vm/V panels''')
sfgammapick2d.par('eps',rsf.doc.rsfpar('float','0','','''line-freedom measure '''))
sfgammapick2d.par('xApp',rsf.doc.rsfpar('int','1','','''x-aperture '''))
sfgammapick2d.version('2.1-git')
sfgammapick2d.synopsis('''sfgammapick2d < dataFile_.rsf > outFile_.rsf eps=0 xApp=1''','''
Input:
dataFile_.rsf - parameter spectrum (semblance) panel

Output:
outFile_.rsf - picked optimal values
''')
rsf.doc.progs['sfgammapick2d']=sfgammapick2d

sfpdrscan2d = rsf.doc.rsfprog('sfpdrscan2d','user/aklokov/Mpdrscan2d.c','''Velocity Scan by 2D Parametric Development of Reflections ''')
sfpdrscan2d.par('aux',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpdrscan2d.par('po',rsf.doc.rsfpar('float','shotStart_','','''start position in stack section '''))
sfpdrscan2d.par('pn',rsf.doc.rsfpar('int','recNum_','','''number of positions in stack section '''))
sfpdrscan2d.par('pd',rsf.doc.rsfpar('float','recStep_','','''increment of positions in stack section '''))
sfpdrscan2d.par('vn',rsf.doc.rsfpar('int','1','','''number of scanned velocities  '''))
sfpdrscan2d.par('vo',rsf.doc.rsfpar('float','1500','','''start velocity '''))
sfpdrscan2d.par('vd',rsf.doc.rsfpar('float','50','','''increment of velocities '''))
sfpdrscan2d.par('wh',rsf.doc.rsfpar('int','11','','''height of a vertical window for semblance calculation '''))
sfpdrscan2d.par('aux',rsf.doc.rsfpar('string ',desc='''output file containing semblance measure of CIGs stacking (auxiliary output file name)'''))
sfpdrscan2d.version('2.1-git')
sfpdrscan2d.synopsis('''sfpdrscan2d < dataFile.rsf > outFile.rsf aux=auxFile.rsf po=shotStart_ pn=recNum_ pd=recStep_ vn=1 vo=1500 vd=50 wh=11''','''''')
rsf.doc.progs['sfpdrscan2d']=sfpdrscan2d

sfpdr2d = rsf.doc.rsfprog('sfpdr2d','user/aklokov/Mpdr2d.c','''2D Parametric Development of Reflections ''')
sfpdr2d.par('aux',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpdr2d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpdr2d.par('po',rsf.doc.rsfpar('float','shotStart_','','''start position in stack section '''))
sfpdr2d.par('pn',rsf.doc.rsfpar('int','recNum_','','''number of positions in stack section '''))
sfpdr2d.par('pd',rsf.doc.rsfpar('float','recStep_','','''increment of positions in stack section '''))
sfpdr2d.par('wh',rsf.doc.rsfpar('int','11','','''height of a vertical window for semblance calculation '''))
sfpdr2d.par('aux',rsf.doc.rsfpar('string ',desc='''output file containing semblance measure of CIGs stacking (auxiliary output file name)'''))
sfpdr2d.par('vel',rsf.doc.rsfpar('string ',desc='''velocity model file (velocity in m/s) (auxiliary input file name)'''))
sfpdr2d.version('2.1-git')
sfpdr2d.synopsis('''sfpdr2d < dataFile.rsf > outFile.rsf aux=auxFile.rsf vel=velFile.rsf po=shotStart_ pn=recNum_ pd=recStep_ wh=11''','''''')
rsf.doc.progs['sfpdr2d']=sfpdr2d

sfdagap = rsf.doc.rsfprog('sfdagap','user/aklokov/Mdagap.c','''Reflection event apex protector/removal for dip-angle gathers.''')
sfdagap.par('dips',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdagap.par('ddep',rsf.doc.rsfpar('bool','y','','''if y, taper depends on depth; if n, no '''))
sfdagap.par('pwidth',rsf.doc.rsfpar('float','10.f','','''protected width (in degree) '''))
sfdagap.par('greyarea',rsf.doc.rsfpar('float','10.f','','''width of event tail taper (in degree) '''))
sfdagap.par('dz',rsf.doc.rsfpar('float','20.f','','''half of a migrated wave length '''))
sfdagap.par('dips',rsf.doc.rsfpar('string ',desc='''dips esitimated in the image domain (in degree) (auxiliary input file name)'''))
sfdagap.version('2.1-git')
sfdagap.synopsis('''sfdagap < dagFile.rsf dips=dipFile.rsf > taperFile.rsf ddep=y pwidth=10.f greyarea=10.f dz=20.f''','''
May be used for migration aperture optimization or for reflected energy
supression. For the last multiply the output on -1.

Input:
dagFile.rsf - input dip-angle gathers;
dipFile.rsf - dips esitimated in the image domain. The dips are in degree (!)

Output:
taperFile.rsf - mask for input dip-angle gathers
''')
rsf.doc.progs['sfdagap']=sfdagap

sfsumamp = rsf.doc.rsfprog('sfsumamp','user/aklokov/Msumamp.c','''Stack energy between two input horizons ''')
sfsumamp.par('top',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsumamp.par('bot',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsumamp.par('badSample',rsf.doc.rsfpar('float','99999.f','','''non-interpreted sample in the horizons '''))
sfsumamp.par('top',rsf.doc.rsfpar('string ',desc='''top horizon (auxiliary input file name)'''))
sfsumamp.par('bot',rsf.doc.rsfpar('string ',desc='''bottom horizon (auxiliary input file name)'''))
sfsumamp.version('2.1-git')
sfsumamp.synopsis('''sfsumamp < dataFile.rsf top=hTopFile.rsf bot=hBotFile.rsf > stackFile.rsf badSample=99999.f''','''''')
rsf.doc.progs['sfsumamp']=sfsumamp

sftaperedge = rsf.doc.rsfprog('sftaperedge','user/aklokov/Mtaperedge.c','''Taper based on data parameters''')
sftaperedge.par('len',rsf.doc.rsfpar('int','11','','''length of the taper function '''))
sftaperedge.version('2.1-git')
sftaperedge.synopsis('''sftaperedge < dataFile.rsf > maskFile.rsf len=11''','''Input - "inline/xline" plane
''')
rsf.doc.progs['sftaperedge']=sftaperedge

sfheal = rsf.doc.rsfprog('sfheal','user/aklokov/Mheal.c','''Heal empty traces ddd''')
sfheal.version('2.1-git')
sfheal.synopsis('''sfheal < inFile.rsf > outFile.rsf''','''Interpolation between two neighbours;
An empty trace should be horizontal => transpose input before and after 
''')
rsf.doc.progs['sfheal']=sfheal

sfrevent = rsf.doc.rsfprog('sfrevent','user/aklokov/Mrevent.c','''Compute reflection event ''')
sfrevent.par('deriv',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrevent.par('tn',rsf.doc.rsfpar('int','1001','','''number of time samples '''))
sfrevent.par('hn',rsf.doc.rsfpar('int','51','','''number of offsets '''))
sfrevent.par('sn',rsf.doc.rsfpar('int','1','','''number of sources '''))
sfrevent.par('to',rsf.doc.rsfpar('float','0.f','','''start time (in s) '''))
sfrevent.par('ho',rsf.doc.rsfpar('float','0.f','','''start offset (in s) '''))
sfrevent.par('so',rsf.doc.rsfpar('float','0.f','','''start source position (in s) '''))
sfrevent.par('td',rsf.doc.rsfpar('float','0.004f','','''step in time (in s) '''))
sfrevent.par('hd',rsf.doc.rsfpar('float','0.05f','','''step in offset (in km) '''))
sfrevent.par('sd',rsf.doc.rsfpar('float','0.025f','','''step in source position (in km) '''))
sfrevent.par('eps',rsf.doc.rsfpar('float','0.5 * hStep','','''receiver position accuracy (in km) '''))
sfrevent.par('vel',rsf.doc.rsfpar('float','2.f','','''constant velocity value (in km/s) '''))
sfrevent.par('deriv',rsf.doc.rsfpar('string ',desc='''first derivative estimated along the reflection boundary (auxiliary input file name)'''))
sfrevent.version('2.1-git')
sfrevent.synopsis('''sfrevent < reflFile.rsf deriv=derivFile.rsf > dataFile.rsf tn=1001 hn=51 sn=1 to=0.f ho=0.f so=0.f td=0.004f hd=0.05f sd=0.025f eps=0.5 * hStep vel=2.f''','''''')
rsf.doc.progs['sfrevent']=sfrevent

sfrotvol = rsf.doc.rsfprog('sfrotvol','user/aklokov/Mrotvol.c','''3D volume rotation about a vertical axis ''')
sfrotvol.par('xf',rsf.doc.rsfpar('float','0.f','','''x-coord of the vertical axis '''))
sfrotvol.par('yf',rsf.doc.rsfpar('float','0.f','','''y-coord of the vertical axis '''))
sfrotvol.par('theta',rsf.doc.rsfpar('float','0.f','','''rotation angle '''))
sfrotvol.version('2.1-git')
sfrotvol.synopsis('''sfrotvol < inFile.rsf > outFile.rsf xf=0.f yf=0.f theta=0.f''','''''')
rsf.doc.progs['sfrotvol']=sfrotvol

sfdagtaper = rsf.doc.rsfprog('sfdagtaper','user/aklokov/Mdagtaper.c','''Edge tapering for dip-angle gathers''')
sfdagtaper.par('len',rsf.doc.rsfpar('float','5.f','','''length of the taper function (in degree) '''))
sfdagtaper.version('2.1-git')
sfdagtaper.synopsis('''sfdagtaper < dataFile.rsf > outFile.rsf len=5.f''','''''')
rsf.doc.progs['sfdagtaper']=sfdagtaper

sftmigda = rsf.doc.rsfprog('sftmigda','user/aklokov/Mtmigda.cc','''3D time scattering-angle Kirchhoff migration  ''')
sftmigda.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftmigda.par('semb',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftmigda.par('dag',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftmigda.par('cig',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftmigda.par('is3d',rsf.doc.rsfpar('bool','n','','''if y, apply 3D migration '''))
sftmigda.par('axis2label',rsf.doc.rsfpar('int','0','','''0 - shot; 1 - cmp; 2 - receiver '''))
sftmigda.par('isAA',rsf.doc.rsfpar('bool','y','','''if y, apply anti-aliasing '''))
sftmigda.par('isDipAz',rsf.doc.rsfpar('bool','y','','''if y, apply dip/azimuth mode; if n, apply inline/crossline angle mode '''))
sftmigda.par('hmign',rsf.doc.rsfpar('int','dp.hNum','','''number of migrated offsets '''))
sftmigda.par('sembWindow',rsf.doc.rsfpar('int','11','','''vertical window for semblance calculation (in samples) '''))
sftmigda.par('edgeTaper',rsf.doc.rsfpar('float','5.f','','''edge taper for dip-angle gathers (in degree) '''))
sftmigda.par('itn',rsf.doc.rsfpar('int','dp.zNum','','''number of imaged times '''))
sftmigda.par('ixn',rsf.doc.rsfpar('int','dp.xNum','','''number of imaged inlines '''))
sftmigda.par('iyn',rsf.doc.rsfpar('int','rp.is3D ? vp.yNum : 1','','''number of imaged crosslines '''))
sftmigda.par('ito',rsf.doc.rsfpar('float','dp.zStart','','''first imaged time (in ms) '''))
sftmigda.par('ixo',rsf.doc.rsfpar('float','dp.xStart','','''first imaged inline '''))
sftmigda.par('iyo',rsf.doc.rsfpar('float','dp.yStart','','''first imaged crossline '''))
sftmigda.par('itd',rsf.doc.rsfpar('float','dp.zStep','','''step in imaged times  (in ms) '''))
sftmigda.par('ixd',rsf.doc.rsfpar('float','dp.xStep','','''step in imaged inlines '''))
sftmigda.par('iyd',rsf.doc.rsfpar('float','dp.yStep','','''step in imaged crosslines '''))
sftmigda.par('dipn',rsf.doc.rsfpar('int','1','','''number of dip-angles '''))
sftmigda.par('sdipn',rsf.doc.rsfpar('int','1','','''number of secondary (azimuth or crossline) angles '''))
sftmigda.par('dipo',rsf.doc.rsfpar('float','0.f','','''first dip-angle '''))
sftmigda.par('sdipo',rsf.doc.rsfpar('float','90.f','','''first secondary (azimuth or crossline) angle '''))
sftmigda.par('dipd',rsf.doc.rsfpar('float','1.f','','''step in dip-angle '''))
sftmigda.par('sdipd',rsf.doc.rsfpar('float','1.f','','''step in secondary (azimuth or crossline) angle '''))
sftmigda.par('vel',rsf.doc.rsfpar('string ',desc='''velocity model file (velocity in m/s) (auxiliary input file name)'''))
sftmigda.par('semb',rsf.doc.rsfpar('string ',desc='''output file containing semblance measure of CIGs stacking (auxiliary output file name)'''))
sftmigda.par('dag',rsf.doc.rsfpar('string ',desc='''output file containing CIGs in the dip-angle domain (auxiliary output file name)'''))
sftmigda.par('cig',rsf.doc.rsfpar('string ',desc='''output file containing CIGs in the surface-offset domain (auxiliary output file name)'''))
sftmigda.version('2.1-git')
sftmigda.synopsis('''sftmigda < dataFile.rsf vel=velFile.rsf > imageFile.rsf semb=sembFile.rsf dag=dagFile.rsf cig=cigFile.rsf is3d=n axis2label=0 isAA=y isDipAz=y hmign=dp.hNum sembWindow=11 edgeTaper=5.f itn=dp.zNum ixn=dp.xNum iyn=rp.is3D ? vp.yNum : 1 ito=dp.zStart ixo=dp.xStart iyo=dp.yStart itd=dp.zStep ixd=dp.xStep iyd=dp.yStep dipn=1 sdipn=1 dipo=0.f sdipo=90.f dipd=1.f sdipd=1.f''','''''')
rsf.doc.progs['sftmigda']=sftmigda

sfdmigda = rsf.doc.rsfprog('sfdmigda','user/aklokov/Mdmigda.cc','''2D depth scattering-angle Kirchhoff migration  ''')
sfdmigda.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdmigda.par('dag',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfdmigda.par('cig',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfdmigda.par('mcig',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfdmigda.par('esct',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfdmigda.par('escx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfdmigda.par('axis2label',rsf.doc.rsfpar('int','0','','''0 - shot; 1 - cmp; 2 - receiver '''))
sfdmigda.par('isAA',rsf.doc.rsfpar('bool','y','','''if y, apply anti-aliasing '''))
sfdmigda.par('izn',rsf.doc.rsfpar('int','dp.zNum','','''number of imaged depth samples '''))
sfdmigda.par('ixn',rsf.doc.rsfpar('int','dp.xNum','','''number of imaged inlines '''))
sfdmigda.par('iyn',rsf.doc.rsfpar('int','rp.is3D ? vp.yNum : 1','','''number of imaged crosslines '''))
sfdmigda.par('izo',rsf.doc.rsfpar('float','dp.zStart','','''first imaged depth (in meters) '''))
sfdmigda.par('ixo',rsf.doc.rsfpar('float','dp.xStart','','''first imaged inline (in meters) '''))
sfdmigda.par('iyo',rsf.doc.rsfpar('float','dp.yStart','','''first imaged crossline (in meters) '''))
sfdmigda.par('izd',rsf.doc.rsfpar('float','dp.zStep','','''step in depth (in meters) '''))
sfdmigda.par('ixd',rsf.doc.rsfpar('float','dp.xStep','','''step in inlines (in meters) '''))
sfdmigda.par('iyd',rsf.doc.rsfpar('float','dp.yStep','','''step in crosslines (in meters) '''))
sfdmigda.par('dipn',rsf.doc.rsfpar('int','161','','''number of dip-angles '''))
sfdmigda.par('dipo',rsf.doc.rsfpar('float','-80.f','','''first dip-angle '''))
sfdmigda.par('dipd',rsf.doc.rsfpar('float','1.f','','''step in dip-angle '''))
sfdmigda.par('iscatn',rsf.doc.rsfpar('int','1','','''number of scattering-angles '''))
sfdmigda.par('iscato',rsf.doc.rsfpar('float','0.f','','''first scattering-angle (in degree) '''))
sfdmigda.par('iscatd',rsf.doc.rsfpar('float','2 * gp.dipStep','','''scattering-angle increment (in degree) '''))
sfdmigda.par('ttd',rsf.doc.rsfpar('float','0.002f','','''travel-times increment '''))
sfdmigda.par('ttn',rsf.doc.rsfpar('int','(int) floor(0.001 * 0.5 * maxTime / ttStep + 1)','','''travel-times number '''))
sfdmigda.par('ttrayd',rsf.doc.rsfpar('float','gp.dipStep / 2.f','','''travel-times rays increment '''))
sfdmigda.par('ttrayo',rsf.doc.rsfpar('float','minttRay','','''travel-times rays start '''))
sfdmigda.par('ttrayn',rsf.doc.rsfpar('int','(int) floor((maxttRay - minttRay) / ttRayStep + 1)','','''travel-times rays number '''))
sfdmigda.par('vel',rsf.doc.rsfpar('string ',desc='''velocity model file (velocity in m/s) (auxiliary input file name)'''))
sfdmigda.par('dag',rsf.doc.rsfpar('string ',desc='''output file containing CIGs in the dip-angle domain (auxiliary output file name)'''))
sfdmigda.par('cig',rsf.doc.rsfpar('string ',desc='''output file containing CIGs in the scattering-angle domain (auxiliary output file name)'''))
sfdmigda.par('mcig',rsf.doc.rsfpar('string ',desc='''output file containing multi-CIGs (in the dip-angle and the scattering-angle domain both (auxiliary output file name)'''))
sfdmigda.par('esct',rsf.doc.rsfpar('string ',desc='''output file containing escqpe times (auxiliary output file name)'''))
sfdmigda.par('escx',rsf.doc.rsfpar('string ',desc='''output file containing escape positions (auxiliary output file name)'''))
sfdmigda.version('2.1-git')
sfdmigda.synopsis('''sfdmigda < dataFile.rsf vel=velFile.rsf > imageFile.rsf dag=dagFile.rsf cig=acigFile.rsf mcig=mcigFile.rsf esct=tEscFile.rsf escx=xEscFile.rsf axis2label=0 isAA=y izn=dp.zNum ixn=dp.xNum iyn=rp.is3D ? vp.yNum : 1 izo=dp.zStart ixo=dp.xStart iyo=dp.yStart izd=dp.zStep ixd=dp.xStep iyd=dp.yStep dipn=161 dipo=-80.f dipd=1.f iscatn=1 iscato=0.f iscatd=2 * gp.dipStep ttd=0.002f ttn=(int) floor(0.001 * 0.5 * maxTime / ttStep + 1) ttrayd=gp.dipStep / 2.f ttrayo=minttRay ttrayn=(int) floor((maxttRay - minttRay) / ttRayStep + 1)''','''''')
rsf.doc.progs['sfdmigda']=sfdmigda

sfdiparti = rsf.doc.rsfprog('sfdiparti','user/aklokov/Mdiparti.cc','''diparti''')
sfdiparti.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdiparti.par('semb',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfdiparti.par('apert',rsf.doc.rsfpar('float','1000','','''diffraction summation aperture '''))
sfdiparti.par('sembWindow',rsf.doc.rsfpar('int','11','','''vertical window for semblance calculation (in samples) '''))
sfdiparti.par('gamma',rsf.doc.rsfpar('float','1.f','','''velocity-model-accuracy parameter '''))
sfdiparti.par('ppn',rsf.doc.rsfpar('int','dipNum_','','''number of processed partial images '''))
sfdiparti.par('ppo',rsf.doc.rsfpar('float','dipStart_','','''first processed partial image '''))
sfdiparti.par('ppd',rsf.doc.rsfpar('float','dipStep_','','''step in processed partial images '''))
sfdiparti.par('itn',rsf.doc.rsfpar('int','tNum_','','''number of imaged depth samples '''))
sfdiparti.par('ixn',rsf.doc.rsfpar('int','xNum_','','''number of imaged positions '''))
sfdiparti.par('ito',rsf.doc.rsfpar('float','tStart_','','''first imaged time (in ms) '''))
sfdiparti.par('ixo',rsf.doc.rsfpar('float','xStart_','','''first imaged position (in m) '''))
sfdiparti.par('itd',rsf.doc.rsfpar('float','tStep_','','''step in time (in ms) '''))
sfdiparti.par('ixd',rsf.doc.rsfpar('float','xStep_','','''step in positions (in m) '''))
sfdiparti.par('vel',rsf.doc.rsfpar('string ',desc='''velocity model file (velocity in km/s) (auxiliary input file name)'''))
sfdiparti.par('semb',rsf.doc.rsfpar('string ',desc='''output file containing semblance (auxiliary output file name)'''))
sfdiparti.version('2.1-git')
sfdiparti.synopsis('''sfdiparti < piFile.rsf vel=velFile.rsf > resFile.rsf semb=sembFile.rsf apert=1000 sembWindow=11 gamma=1.f ppn=dipNum_ ppo=dipStart_ ppd=dipStep_ itn=tNum_ ixn=xNum_ ito=tStart_ ixo=xStart_ itd=tStep_ ixd=xStep_''','''''')
rsf.doc.progs['sfdiparti']=sfdiparti

sfitrace = rsf.doc.rsfprog('sfitrace','user/aklokov/Mitrace.cc','''''')
sfitrace.par('esct',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfitrace.par('zres',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfitrace.par('x0',rsf.doc.rsfpar('float','0.f','','''x-coordinate of the diffraction point '''))
sfitrace.par('z0',rsf.doc.rsfpar('float','0.f','','''z-coordinate of the diffraction point '''))
sfitrace.par('p0',rsf.doc.rsfpar('float','0.f','','''migration angle '''))
sfitrace.par('sa0',rsf.doc.rsfpar('float','0.f','','''scattering-angle '''))
sfitrace.par('dx',rsf.doc.rsfpar('float','5*xStep','','''x-range for point detection '''))
sfitrace.par('dt',rsf.doc.rsfpar('float','0.02f','','''time-range for point detection '''))
sfitrace.par('esct',rsf.doc.rsfpar('string ',desc='''escape-time file (auxiliary input file name)'''))
sfitrace.par('zres',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfitrace.version('2.1-git')
sfitrace.synopsis('''sfitrace < xEscFile.rsf esct=tEscFile.rsf > xResFile.rsf zres=zResFile.rsf x0=0.f z0=0.f p0=0.f sa0=0.f dx=5*xStep dt=0.02f''','''''')
rsf.doc.progs['sfitrace']=sfitrace

sfdbfmig = rsf.doc.rsfprog('sfdbfmig','user/aklokov/Mdbfmig.cc','''''')
sfdbfmig.par('escx',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdbfmig.par('esct',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdbfmig.par('ppn',rsf.doc.rsfpar('int','pNum','','''number of processed partial images '''))
sfdbfmig.par('ppo',rsf.doc.rsfpar('float','pStart','','''first processed partial image '''))
sfdbfmig.par('ppd',rsf.doc.rsfpar('float','pStep','','''step in processed partial images '''))
sfdbfmig.par('izn',rsf.doc.rsfpar('int','zNum','','''number of imaged depth samples '''))
sfdbfmig.par('ixn',rsf.doc.rsfpar('int','xNum','','''number of imaged positions '''))
sfdbfmig.par('izo',rsf.doc.rsfpar('float','zStart','','''first imaged depth (in meters) '''))
sfdbfmig.par('ixo',rsf.doc.rsfpar('float','xStart','','''first imaged position (in meters) '''))
sfdbfmig.par('izd',rsf.doc.rsfpar('float','zStep','','''step in depth (in meters) '''))
sfdbfmig.par('ixd',rsf.doc.rsfpar('float','xStep','','''step in positions (in meters) '''))
sfdbfmig.par('sn',rsf.doc.rsfpar('int','1','','''number of scattering-angles '''))
sfdbfmig.par('so',rsf.doc.rsfpar('float','0.f','','''first scattering-angle '''))
sfdbfmig.par('sd',rsf.doc.rsfpar('float','1.f','','''step in scattering-angles '''))
sfdbfmig.par('isAA',rsf.doc.rsfpar('bool','y','','''if y, apply anti-aliasing '''))
sfdbfmig.par('dx',rsf.doc.rsfpar('float','xStep','','''x-range for point detection '''))
sfdbfmig.par('dt',rsf.doc.rsfpar('float','0.008f','','''time-range for point detection '''))
sfdbfmig.par('xlim',rsf.doc.rsfpar('float','2 * xStep','','''maximum distance between depth-line points '''))
sfdbfmig.par('xapert',rsf.doc.rsfpar('float','xNum * xStep','','''migration aperture size '''))
sfdbfmig.par('pj',rsf.doc.rsfpar('int','1','','''jump in points '''))
sfdbfmig.par('escx',rsf.doc.rsfpar('string ',desc='''escape-positions file (auxiliary input file name)'''))
sfdbfmig.par('esct',rsf.doc.rsfpar('string ',desc='''escape-time file (auxiliary input file name)'''))
sfdbfmig.version('2.1-git')
sfdbfmig.synopsis('''sfdbfmig < piFile.rsf escx=xEscFile.rsf esct=tEscFile.rsf > resFile.rsf ppn=pNum ppo=pStart ppd=pStep izn=zNum ixn=xNum izo=zStart ixo=xStart izd=zStep ixd=xStep sn=1 so=0.f sd=1.f isAA=y dx=xStep dt=0.008f xlim=2 * xStep xapert=xNum * xStep pj=1''','''''')
rsf.doc.progs['sfdbfmig']=sfdbfmig

sfdiparti3 = rsf.doc.rsfprog('sfdiparti3','user/aklokov/Mdiparti3.cc','''diparti''')
sfdiparti3.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdiparti3.par('semb',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfdiparti3.par('apert',rsf.doc.rsfpar('float','1000','','''diffraction summation aperture '''))
sfdiparti3.par('sembWindow',rsf.doc.rsfpar('int','11','','''vertical window for semblance calculation (in samples) '''))
sfdiparti3.par('gamma',rsf.doc.rsfpar('float','1.f','','''velocity-model-accuracy parameter '''))
sfdiparti3.par('xppn',rsf.doc.rsfpar('int','dipNum_','','''number of processed partial images '''))
sfdiparti3.par('xppo',rsf.doc.rsfpar('float','dipStart_','','''first processed partial image '''))
sfdiparti3.par('xppd',rsf.doc.rsfpar('float','dipStep_','','''step in processed partial images '''))
sfdiparti3.par('yppn',rsf.doc.rsfpar('int','sdipNum_','','''number of processed partial images '''))
sfdiparti3.par('yppo',rsf.doc.rsfpar('float','sdipStart_','','''first processed partial image '''))
sfdiparti3.par('yppd',rsf.doc.rsfpar('float','sdipStep_','','''step in processed partial images '''))
sfdiparti3.par('itn',rsf.doc.rsfpar('int','tNum_','','''number of imaged depth samples '''))
sfdiparti3.par('ixn',rsf.doc.rsfpar('int','xNum_','','''number of imaged positions '''))
sfdiparti3.par('iyn',rsf.doc.rsfpar('int','yNum_','','''number of imaged positions '''))
sfdiparti3.par('ito',rsf.doc.rsfpar('float','tStart_','','''first imaged time (in ms) '''))
sfdiparti3.par('ixo',rsf.doc.rsfpar('float','xStart_','','''first imaged position (in m) '''))
sfdiparti3.par('iyo',rsf.doc.rsfpar('float','yStart_','','''first imaged position (in m) '''))
sfdiparti3.par('itd',rsf.doc.rsfpar('float','tStep_','','''step in time (in ms) '''))
sfdiparti3.par('ixd',rsf.doc.rsfpar('float','xStep_','','''step in positions (in m) '''))
sfdiparti3.par('iyd',rsf.doc.rsfpar('float','yStep_','','''step in positions (in m) '''))
sfdiparti3.par('vel',rsf.doc.rsfpar('string ',desc='''velocity model file (velocity in km/s) (auxiliary input file name)'''))
sfdiparti3.par('semb',rsf.doc.rsfpar('string ',desc='''output file containing semblance (auxiliary output file name)'''))
sfdiparti3.version('2.1-git')
sfdiparti3.synopsis('''sfdiparti3 < piFile.rsf vel=velFile.rsf > resFile.rsf semb=sembFile.rsf apert=1000 sembWindow=11 gamma=1.f xppn=dipNum_ xppo=dipStart_ xppd=dipStep_ yppn=sdipNum_ yppo=sdipStart_ yppd=sdipStep_ itn=tNum_ ixn=xNum_ iyn=yNum_ ito=tStart_ ixo=xStart_ iyo=yStart_ itd=tStep_ ixd=xStep_ iyd=yStep_''','''''')
rsf.doc.progs['sfdiparti3']=sfdiparti3

sfvsptmigda = rsf.doc.rsfprog('sfvsptmigda','user/aklokov/Mvsptmigda.cc','''3D time scattering-angle Kirchhoff migration for VSP data ''')
sfvsptmigda.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvsptmigda.par('semb',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvsptmigda.par('dag',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvsptmigda.par('cig',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvsptmigda.par('is3d',rsf.doc.rsfpar('bool','n','','''if y, apply 3D migration '''))
sfvsptmigda.par('axis2label',rsf.doc.rsfpar('int','0','','''0 - shot; 1 - cmp; 2 - receiver '''))
sfvsptmigda.par('isAA',rsf.doc.rsfpar('bool','y','','''if y, apply anti-aliasing '''))
sfvsptmigda.par('isDipAz',rsf.doc.rsfpar('bool','y','','''if y, apply dip/azimuth mode; if n, apply inline/crossline angle mode '''))
sfvsptmigda.par('hmign',rsf.doc.rsfpar('int','dp.hNum','','''number of migrated offsets '''))
sfvsptmigda.par('sembWindow',rsf.doc.rsfpar('int','11','','''vertical window for semblance calculation (in samples) '''))
sfvsptmigda.par('itn',rsf.doc.rsfpar('int','dp.zNum','','''number of imaged times '''))
sfvsptmigda.par('ixn',rsf.doc.rsfpar('int','dp.xNum','','''number of imaged inlines '''))
sfvsptmigda.par('iyn',rsf.doc.rsfpar('int','rp.is3D ? vp.yNum : 1','','''number of imaged crosslines '''))
sfvsptmigda.par('ito',rsf.doc.rsfpar('float','dp.zStart','','''first imaged time (in ms) '''))
sfvsptmigda.par('ixo',rsf.doc.rsfpar('float','dp.xStart','','''first imaged inline '''))
sfvsptmigda.par('iyo',rsf.doc.rsfpar('float','dp.yStart','','''first imaged crossline '''))
sfvsptmigda.par('itd',rsf.doc.rsfpar('float','dp.zStep','','''step in imaged times  (in ms) '''))
sfvsptmigda.par('ixd',rsf.doc.rsfpar('float','dp.xStep','','''step in imaged inlines '''))
sfvsptmigda.par('iyd',rsf.doc.rsfpar('float','dp.yStep','','''step in imaged crosslines '''))
sfvsptmigda.par('dipn',rsf.doc.rsfpar('int','1','','''number of dip-angles '''))
sfvsptmigda.par('dipo',rsf.doc.rsfpar('float','0.f','','''first dip-angle '''))
sfvsptmigda.par('dipd',rsf.doc.rsfpar('float','1.f','','''step in dip-angle '''))
sfvsptmigda.par('iscatn',rsf.doc.rsfpar('int','1','','''number of scattering-angles '''))
sfvsptmigda.par('iscato',rsf.doc.rsfpar('float','0.f','','''first scattering-angle (in degree) '''))
sfvsptmigda.par('iscatd',rsf.doc.rsfpar('float','2 * gp.dipStep','','''scattering-angle increment (in degree) '''))
sfvsptmigda.par('vel',rsf.doc.rsfpar('string ',desc='''velocity model file (velocity in m/s) (auxiliary input file name)'''))
sfvsptmigda.par('semb',rsf.doc.rsfpar('string ',desc='''output file containing semblance measure of CIGs stacking (auxiliary output file name)'''))
sfvsptmigda.par('dag',rsf.doc.rsfpar('string ',desc='''output file containing CIGs in the dip-angle domain (auxiliary output file name)'''))
sfvsptmigda.par('cig',rsf.doc.rsfpar('string ',desc='''output file containing CIGs in the surface-offset domain (auxiliary output file name)'''))
sfvsptmigda.version('2.1-git')
sfvsptmigda.synopsis('''sfvsptmigda < dataFile.rsf vel=velFile.rsf > imageFile.rsf semb=sembFile.rsf dag=dagFile.rsf cig=cigFile.rsf is3d=n axis2label=0 isAA=y isDipAz=y hmign=dp.hNum sembWindow=11 itn=dp.zNum ixn=dp.xNum iyn=rp.is3D ? vp.yNum : 1 ito=dp.zStart ixo=dp.xStart iyo=dp.yStart itd=dp.zStep ixd=dp.xStep iyd=dp.yStep dipn=1 dipo=0.f dipd=1.f iscatn=1 iscato=0.f iscatd=2 * gp.dipStep''','''''')
rsf.doc.progs['sfvsptmigda']=sfvsptmigda

