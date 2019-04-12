import rsf.doc

sffitcrs = rsf.doc.rsfprog('sffitcrs','user/roman/Mfitcrs.c','''''')
sffitcrs.par('tcrs',rsf.doc.rsfpar('string ',desc=''''''))
sffitcrs.version('2.1-git')
sffitcrs.synopsis('''sffitcrs < in.rsf > out.rsf > out_tcrs_params.rsf tcrs=''','''
Input: T[m][h][t] and its sf-file  m[], Nm h[], Nh 
Output: a(3) three CRS parameters: a(0) m + a(1)m^2 + a(2) h^2

H_11 = 2 Nx Sum(m^2)
H_12 = 2 Nx Sum(m^4)
H_13 = 2 Sum(x^2) Sum(m)

H_22 = 2 Nx Sum(m^4)
H_23 = 2 Sum(x^2) Sum(m^2)

H_33 = 2 Nm Sum(x^2)

da = - grad H^{-1}
''')
rsf.doc.progs['sffitcrs']=sffitcrs

sffitcrspicks = rsf.doc.rsfprog('sffitcrspicks','user/roman/Mfitcrspicks.c','''''')
sffitcrspicks.par('crsparams',rsf.doc.rsfpar('string ',desc=''''''))
sffitcrspicks.par('mask',rsf.doc.rsfpar('string ',desc=''''''))
sffitcrspicks.version('2.1-git')
sffitcrspicks.synopsis('''sffitcrspicks < in.rsf > out_tcrs.rsf crsparams= mask=''','''Compute fitting of Non-hyperbolic CRS to first-arrivals T[m][h].

Input: T[m][h] arrivals and in its sf-file  m[], Nm h[], Nh 
Output: 
tcrs=filname - t[m][h] crs surface
prints three CRS parameters a[3] where: t[m][h] = a(0) m + a(1)m^2 + a(2) h^2

''')
rsf.doc.progs['sffitcrspicks']=sffitcrspicks

sffitnonhcrspicks = rsf.doc.rsfprog('sffitnonhcrspicks','user/roman/Mfitnonhcrspicks.c','''''')
sffitnonhcrspicks.par('A1',rsf.doc.rsfpar('float','','',''''''))
sffitnonhcrspicks.par('A2',rsf.doc.rsfpar('float','','',''''''))
sffitnonhcrspicks.par('B',rsf.doc.rsfpar('float','','','''memory allocations '''))
sffitnonhcrspicks.version('2.1-git')
sffitnonhcrspicks.synopsis('''sffitnonhcrspicks < in.rsf > out_tcrs.rsf A1= A2= B=''','''Compute fitting of Non-hyperbolic CRS to first-arrivals T[m][h].

Input: T[m][h] arrivals and in its sf-file  m[], Nm h[], Nh 

parameters:

A1
A2
B

FF = F(t0,t02,A1,A2,m-h)*F(t0,t02,A1,A2,m+h);

t2 = 0.5 * (F(t0, t02, A1, A2, m) + (2*B+A1*A1-A2)*h*h + sqrt(FF) );

Output: 
tcrs=filname - t[m][h] crs surface
prints three CRS parameters a[3] where: t[m][h] = a(0) m + a(1)m^2 + a(2) h^2

''')
rsf.doc.progs['sffitnonhcrspicks']=sffitnonhcrspicks

sfreadsample = rsf.doc.rsfprog('sfreadsample','user/roman/Mreadsample.c','''Oriented zero-offset migration. ''')
sfreadsample.par('init',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfreadsample.par('final',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfreadsample.par('N',rsf.doc.rsfpar('int','','',''''''))
sfreadsample.par('sample',rsf.doc.rsfpar('string ',desc=''''''))
sfreadsample.version('2.1-git')
sfreadsample.synopsis('''sfreadsample > so1.rsf init=so2.rsf final=so3.rsf N= sample=''','''''')
rsf.doc.progs['sfreadsample']=sfreadsample

sfreadsampleref = rsf.doc.rsfprog('sfreadsampleref','user/roman/Mreadsampleref.c','''Oriented zero-offset migration. ''')
sfreadsampleref.par('correct',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfreadsampleref.par('init',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfreadsampleref.par('final',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfreadsampleref.par('N',rsf.doc.rsfpar('int','','',''''''))
sfreadsampleref.par('sample',rsf.doc.rsfpar('string ',desc=''''''))
sfreadsampleref.version('2.1-git')
sfreadsampleref.synopsis('''sfreadsampleref > so.rsf correct=so1.rsf init=so2.rsf final=so3.rsf N= sample=''','''''')
rsf.doc.progs['sfreadsampleref']=sfreadsampleref

sfwavegeom = rsf.doc.rsfprog('sfwavegeom','user/roman/Mwavegeom.c','''Rice HPCSS forward modeling. ''')
sfwavegeom.version('2.1-git')
sfwavegeom.synopsis('''sfwavegeom''','''''')
rsf.doc.progs['sfwavegeom']=sfwavegeom

sfrtmgeom = rsf.doc.rsfprog('sfrtmgeom','user/roman/Mrtmgeom.c','''Rice HPCSS reverse time migration. ''')
sfrtmgeom.version('2.1-git')
sfrtmgeom.synopsis('''sfrtmgeom''','''''')
rsf.doc.progs['sfrtmgeom']=sfrtmgeom

sfcigangle = rsf.doc.rsfprog('sfcigangle','user/roman/Mcigangle.c','''src-receiver to angle gathers ''')
sfcigangle.par('time',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcigangle.par('dept',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcigangle.par('data',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcigangle.par('nalpha',rsf.doc.rsfpar('int','90','',''''''))
sfcigangle.par('tolz',rsf.doc.rsfpar('float','1.f','','''surface depth '''))
sfcigangle.version('2.1-git')
sfcigangle.synopsis('''sfcigangle < dist.rsf time=time.rsf dept=dept.rsf > imag.rsf data=data.rsf nalpha=90 tolz=1.f''','''''')
rsf.doc.progs['sfcigangle']=sfcigangle

sfopsmigrk = rsf.doc.rsfprog('sfopsmigrk','user/roman/Mopsmigrk.c','''Shot-recorder Oriented prestack migration data is (shots x recs x time). ''')
sfopsmigrk.par('time',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfopsmigrk.par('dept',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfopsmigrk.par('data',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfopsmigrk.par('tolz',rsf.doc.rsfpar('float','2.0','',''''''))
sfopsmigrk.par('is_offset',rsf.doc.rsfpar('bool','n','',''''''))
sfopsmigrk.version('2.1-git')
sfopsmigrk.synopsis('''sfopsmigrk < dist.rsf time=time.rsf dept=dept.rsf > imag.rsf data=data.rsf tolz=2.0 is_offset=n''','''''')
rsf.doc.progs['sfopsmigrk']=sfopsmigrk

sfgsray2rays2d = rsf.doc.rsfprog('sfgsray2rays2d','user/roman/Mgsray2rays2d.c','''Oriented zero-offset migration. ''')
sfgsray2rays2d.par('dept',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfgsray2rays2d.par('ang',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfgsray2rays2d.par('slow',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfgsray2rays2d.par('slowz',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfgsray2rays2d.par('slowx',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfgsray2rays2d.par('ref3',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfgsray2rays2d.par('stride',rsf.doc.rsfpar('int','1','',''''''))
sfgsray2rays2d.par('tolz',rsf.doc.rsfpar('float','','',''''''))
sfgsray2rays2d.par('tolx',rsf.doc.rsfpar('float','','',''''''))
sfgsray2rays2d.par('tola',rsf.doc.rsfpar('float','','',''''''))
sfgsray2rays2d.par('ref1',rsf.doc.rsfpar('string ',desc=''''''))
sfgsray2rays2d.par('ref2',rsf.doc.rsfpar('string ',desc=''''''))
sfgsray2rays2d.par('ref3',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfgsray2rays2d.version('2.1-git')
sfgsray2rays2d.synopsis('''sfgsray2rays2d < time.rsf dept=dept.rsf ang=angl.rsf slow=slow.rsf slowz=slowz.rsf slowx=slowx.rsf ref3=fref3.rsf > imagt.rsf stride=1 tolz= tolx= tola= ref1= ref2=''','''''')
rsf.doc.progs['sfgsray2rays2d']=sfgsray2rays2d

sfgsrayvti = rsf.doc.rsfprog('sfgsrayvti','user/roman/Mgsrayvti.c','''Gauss Seidel iterative solver for phase space escape positions, angle and traveltime ''')
sfgsrayvti.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfgsrayvti.par('velz',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfgsrayvti.par('velx',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfgsrayvti.par('iq',rsf.doc.rsfpar('int','','','''switch for escape variable 0=x, 1=a, 2=t, 3=z, 4=l '''))
sfgsrayvti.par('niter',rsf.doc.rsfpar('int','50','','''number of Gauss-Seidel iterations '''))
sfgsrayvti.par('tol',rsf.doc.rsfpar('float','0.000002*nx*nz','','''accuracy tolerance '''))
sfgsrayvti.par('vti_eps',rsf.doc.rsfpar('float','0.0','',''''''))
sfgsrayvti.par('vti_gamma',rsf.doc.rsfpar('float','0.0','',''''''))
sfgsrayvti.par('vti_delta',rsf.doc.rsfpar('float','0.0','','''VTI constants Thomsen  '''))
sfgsrayvti.par('vti',rsf.doc.rsfpar('string ',desc='''what to compute (p=qP, v=qSV, h=SH) '''))
sfgsrayvti.version('2.1-git')
sfgsrayvti.synopsis('''sfgsrayvti < in.rsf > out.rsf vel=slow.rsf velz=slowz.rsf velx=slowx.rsf iq= niter=50 tol=0.000002*nx*nz vti_eps=0.0 vti_gamma=0.0 vti_delta=0.0 vti=''','''''')
rsf.doc.progs['sfgsrayvti']=sfgsrayvti

sftraveltimelen = rsf.doc.rsfprog('sftraveltimelen','user/roman/Mtraveltimelen.c','''Oriented zero-offset migration. ''')
sftraveltimelen.par('time',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftraveltimelen.par('dept',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftraveltimelen.par('len',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftraveltimelen.par('xsrc',rsf.doc.rsfpar('float','','',''''''))
sftraveltimelen.par('tolz',rsf.doc.rsfpar('float','','',''''''))
sftraveltimelen.par('tolx',rsf.doc.rsfpar('float','','',''''''))
sftraveltimelen.par('interpolate',rsf.doc.rsfpar('int','','',''''''))
sftraveltimelen.par('timez0',rsf.doc.rsfpar('string ',desc=''''''))
sftraveltimelen.version('2.1-git')
sftraveltimelen.synopsis('''sftraveltimelen < dist.rsf time=time.rsf dept=dept.rsf len=lent.rsf > imagt.rsf xsrc= tolz= tolx= interpolate= timez0=''','''''')
rsf.doc.progs['sftraveltimelen']=sftraveltimelen

sftraveltime2d = rsf.doc.rsfprog('sftraveltime2d','user/roman/Mtraveltime2d.c','''Oriented zero-offset migration. ''')
sftraveltime2d.par('time',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftraveltime2d.par('dept',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftraveltime2d.par('len',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftraveltime2d.par('xsrc',rsf.doc.rsfpar('float','','',''''''))
sftraveltime2d.par('tolz',rsf.doc.rsfpar('float','','',''''''))
sftraveltime2d.par('tolx',rsf.doc.rsfpar('float','','',''''''))
sftraveltime2d.par('frontt0',rsf.doc.rsfpar('float','','',''''''))
sftraveltime2d.par('frontdt',rsf.doc.rsfpar('float','','',''''''))
sftraveltime2d.par('frontnt',rsf.doc.rsfpar('int','','',''''''))
sftraveltime2d.par('fronteps',rsf.doc.rsfpar('float','','',''''''))
sftraveltime2d.par('interpolate',rsf.doc.rsfpar('int','','','''first arrivals '''))
sftraveltime2d.par('timez0',rsf.doc.rsfpar('string ',desc=''''''))
sftraveltime2d.par('minpath',rsf.doc.rsfpar('string ',desc=''''''))
sftraveltime2d.par('front',rsf.doc.rsfpar('string ',desc=''''''))
sftraveltime2d.par('eik',rsf.doc.rsfpar('string ',desc=''''''))
sftraveltime2d.version('2.1-git')
sftraveltime2d.synopsis('''sftraveltime2d < dist.rsf time=time.rsf dept=dept.rsf len=lent.rsf > imagt.rsf xsrc= tolz= tolx= frontt0= frontdt= frontnt= fronteps= interpolate= timez0= minpath= front= eik=''','''''')
rsf.doc.progs['sftraveltime2d']=sftraveltime2d

sftraveltimelen3d = rsf.doc.rsfprog('sftraveltimelen3d','user/roman/Mtraveltimelen3d.c','''Oriented zero-offset migration. ''')
sftraveltimelen3d.par('disty',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftraveltimelen3d.par('time',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftraveltimelen3d.par('dept',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftraveltimelen3d.par('len',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftraveltimelen3d.par('xsrc',rsf.doc.rsfpar('float','','',''''''))
sftraveltimelen3d.par('ysrc',rsf.doc.rsfpar('float','','',''''''))
sftraveltimelen3d.version('2.1-git')
sftraveltimelen3d.synopsis('''sftraveltimelen3d < dist.rsf disty=distY.rsf time=time.rsf dept=dept.rsf len=lent.rsf > imagt.rsf xsrc= ysrc=''','''''')
rsf.doc.progs['sftraveltimelen3d']=sftraveltimelen3d

