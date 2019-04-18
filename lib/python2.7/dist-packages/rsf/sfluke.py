import rsf.doc

sfdagap3 = rsf.doc.rsfprog('sfdagap3','user/luke/Mdagap3.c','''Reflection event apex protector/removal for dip-angle gathers.''')
sfdagap3.par('dips',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdagap3.par('ddep',rsf.doc.rsfpar('bool','y','','''if y, taper depends on depth; if n, no '''))
sfdagap3.par('pwidth1',rsf.doc.rsfpar('float','10.f','',''''''))
sfdagap3.par('pwidth2',rsf.doc.rsfpar('float','10.f','','''protected width (in degree) '''))
sfdagap3.par('greyarea1',rsf.doc.rsfpar('float','10.f','',''''''))
sfdagap3.par('greyarea2',rsf.doc.rsfpar('float','10.f','','''width of event tail taper (in degree) '''))
sfdagap3.par('dz',rsf.doc.rsfpar('float','20.f','','''half of a migrated wave length '''))
sfdagap3.par('dips',rsf.doc.rsfpar('string ',desc='''dips esitimated in the image domain (in degree) (auxiliary input file name)'''))
sfdagap3.version('2.1-git')
sfdagap3.synopsis('''sfdagap3 < dagFile.rsf dips=dipFile.rsf > taperFile.rsf ddep=y pwidth1=10.f pwidth2=10.f greyarea1=10.f greyarea2=10.f dz=20.f''','''
May be used for migration aperture optimization or for reflected energy
supression. For the last multiply the output on -1.

Input:
dagFile.rsf - input dip-angle gathers;
dipFile.rsf - dips esitimated in the image domain. The dips are in degree (!)

Output:
taperFile.rsf - mask for input dip-angle gathers
''')
rsf.doc.progs['sfdagap3']=sfdagap3

sfdagap3e = rsf.doc.rsfprog('sfdagap3e','user/luke/Mdagap3e.c','''Reflection event apex protector/removal for dip-angle gathers.''')
sfdagap3e.par('dips',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdagap3e.par('ddep',rsf.doc.rsfpar('bool','y','','''if y, taper depends on depth; if n, no '''))
sfdagap3e.par('pwidth1',rsf.doc.rsfpar('float','10.f','',''''''))
sfdagap3e.par('pwidth2',rsf.doc.rsfpar('float','10.f','','''protected width (in degree) '''))
sfdagap3e.par('greyarea1',rsf.doc.rsfpar('float','10.f','',''''''))
sfdagap3e.par('greyarea2',rsf.doc.rsfpar('float','10.f','','''width of event tail taper (in degree) '''))
sfdagap3e.par('dz',rsf.doc.rsfpar('float','20.f','','''half of a migrated wave length '''))
sfdagap3e.par('dips',rsf.doc.rsfpar('string ',desc='''dips esitimated in the image domain (in degree) (auxiliary input file name)'''))
sfdagap3e.version('2.1-git')
sfdagap3e.synopsis('''sfdagap3e < dagFile.rsf dips=dipFile.rsf > taperFile.rsf ddep=y pwidth1=10.f pwidth2=10.f greyarea1=10.f greyarea2=10.f dz=20.f''','''
May be used for migration aperture optimization or for reflected energy
supression. For the last multiply the output on -1.

Input:
dagFile.rsf - input dip-angle gathers;
dipFile.rsf - dips esitimated in the image domain. The dips are in degree (!)

Output:
taperFile.rsf - mask for input dip-angle gathers
''')
rsf.doc.progs['sfdagap3e']=sfdagap3e

sfdagap3a = rsf.doc.rsfprog('sfdagap3a','user/luke/Mdagap3a.c','''Reflection event apex protector/removal for dip-angle gathers.''')
sfdagap3a.par('dips',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdagap3a.par('rms',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdagap3a.par('ddep',rsf.doc.rsfpar('bool','y','','''if y, taper depends on depth; if n, no '''))
sfdagap3a.par('pwidth1',rsf.doc.rsfpar('float','10.f','',''''''))
sfdagap3a.par('pwidth2',rsf.doc.rsfpar('float','10.f','','''protected width (in degree) '''))
sfdagap3a.par('drms',rsf.doc.rsfpar('bool','y','','''if y, taper depends on rms; if n, no '''))
sfdagap3a.par('fudge',rsf.doc.rsfpar('float','10.f','','''Fudge Factor '''))
sfdagap3a.par('greyarea1',rsf.doc.rsfpar('float','10.f','',''''''))
sfdagap3a.par('greyarea2',rsf.doc.rsfpar('float','10.f','','''width of event tail taper (in degree) '''))
sfdagap3a.par('dz',rsf.doc.rsfpar('float','20.f','','''half of a migrated wave length '''))
sfdagap3a.par('dips',rsf.doc.rsfpar('string ',desc='''dips esitimated in the image domain (in degree) (auxiliary input file name)'''))
sfdagap3a.par('rms',rsf.doc.rsfpar('string ',desc='''RMS input for tapering variation (auxiliary input file name)'''))
sfdagap3a.version('2.1-git')
sfdagap3a.synopsis('''sfdagap3a < dagFile.rsf dips=dipFile.rsf > taperFile.rsf rms=rmsFile.rsf ddep=y pwidth1=10.f pwidth2=10.f drms=y fudge=10.f greyarea1=10.f greyarea2=10.f dz=20.f''','''
May be used for migration aperture optimization or for reflected energy
supression. For the last multiply the output on -1.

Input:
dagFile.rsf - input dip-angle gathers;
dipFile.rsf - dips esitimated in the image domain. The dips are in degree (!)
rmsFile.rsf - input rms;

Output:
taperFile.rsf - mask for input dip-angle gathers
''')
rsf.doc.progs['sfdagap3a']=sfdagap3a

sfdagapex = rsf.doc.rsfprog('sfdagapex','user/luke/Mdagapex.c','''None''')
sfdagapex.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdagapex.par('mask',rsf.doc.rsfpar('float','','',''''''))
sfdagapex.par('gray',rsf.doc.rsfpar('float','','',''''''))
sfdagapex.par('dip',rsf.doc.rsfpar('string ',desc='''Image Dips (deg)(auxiliary input file name)'''))
sfdagapex.version('2.1-git')
sfdagapex.synopsis('''sfdagapex < gathers_in.rsf dip=dips_in.rsf > fresnel_out.rsf mask= gray=''','''''')
rsf.doc.progs['sfdagapex']=sfdagapex

sfangmig2 = rsf.doc.rsfprog('sfangmig2','user/luke/Mangmig2.c','''Angle-gather constant-velocity time migration. ''')
sfangmig2.par('semb',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfangmig2.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfangmig2.par('vin',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfangmig2.par('adj',rsf.doc.rsfpar('bool','n','','''if y modeling, if n, migration '''))
sfangmig2.par('weighting',rsf.doc.rsfpar('bool','y','','''kirchhoff weighting? '''))
sfangmig2.par('na',rsf.doc.rsfpar('int','','','''number of dip angles '''))
sfangmig2.par('amax',rsf.doc.rsfpar('float','','','''maximum dip angle '''))
sfangmig2.par('ng',rsf.doc.rsfpar('int','na','','''number of reflection angles '''))
sfangmig2.par('gmax',rsf.doc.rsfpar('float','amax','','''maximum reflection angle'''))
sfangmig2.par('nxi',rsf.doc.rsfpar('int','nx','','''output samples '''))
sfangmig2.par('xi0',rsf.doc.rsfpar('float','x0','','''output orgin '''))
sfangmig2.par('dxi',rsf.doc.rsfpar('float','dx','','''output sampling '''))
sfangmig2.par('ntau',rsf.doc.rsfpar('int','nt','','''output vertical samples '''))
sfangmig2.par('tau0',rsf.doc.rsfpar('float','t0','','''output vertical orgin '''))
sfangmig2.par('dtau',rsf.doc.rsfpar('float','dt','','''output vertical sampling '''))
sfangmig2.par('nh',rsf.doc.rsfpar('int','','','''number of offsets '''))
sfangmig2.par('h0',rsf.doc.rsfpar('float','','','''initial offset '''))
sfangmig2.par('dh',rsf.doc.rsfpar('float','','','''offset increment'''))
sfangmig2.par('ng',rsf.doc.rsfpar('int','na','','''number of reflection angles '''))
sfangmig2.par('gmax',rsf.doc.rsfpar('float','amax','','''maximum reflection angle'''))
sfangmig2.par('nx',rsf.doc.rsfpar('int','nxi','','''data domain spatial samples '''))
sfangmig2.par('x0',rsf.doc.rsfpar('float','xi0','','''data domain spatial orgin '''))
sfangmig2.par('dx',rsf.doc.rsfpar('float','dxi','','''data domain spatial increment '''))
sfangmig2.par('nt',rsf.doc.rsfpar('int','ntau','','''number time samples '''))
sfangmig2.par('t0',rsf.doc.rsfpar('float','tau0','','''time orgin '''))
sfangmig2.par('dt',rsf.doc.rsfpar('float','dtau','','''time increment '''))
sfangmig2.par('eps',rsf.doc.rsfpar('float','0.00001','','''epsilon for division in semblance calc'''))
sfangmig2.par('l2',rsf.doc.rsfpar('bool','y','','''if y use l2 norm for semb, if n, use l1 norm '''))
sfangmig2.par('semb',rsf.doc.rsfpar('string ',desc='''output file containing Semblance (auxiliary output file name)'''))
sfangmig2.par('mask',rsf.doc.rsfpar('string ',desc='''input file contining image mask locations, 0 = skip (auxiliary input file name)'''))
sfangmig2.par('vin',rsf.doc.rsfpar('string ',desc='''input velocity file (auxiliary input file name)'''))
sfangmig2.version('2.1-git')
sfangmig2.synopsis('''sfangmig2 < in.rsf > out.rsf semb=semb.rsf mask=mask.rsf vin=vin.rsf adj=n weighting=y na= amax= ng=na gmax=amax nxi=nx xi0=x0 dxi=dx ntau=nt tau0=t0 dtau=dt nh= h0= dh= ng=na gmax=amax nx=nxi x0=xi0 dx=dxi nt=ntau t0=tau0 dt=dtau eps=0.00001 l2=y''','''''')
rsf.doc.progs['sfangmig2']=sfangmig2

sfangmigM = rsf.doc.rsfprog('sfangmigM','user/luke/MangmigM.c','''Angle-gather constant-velocity time migration with mask file. ''')
sfangmigM.par('semb',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfangmigM.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfangmigM.par('vin',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfangmigM.par('adj',rsf.doc.rsfpar('bool','n','','''if y modeling, if n, migration '''))
sfangmigM.par('weighting',rsf.doc.rsfpar('bool','y','','''kirchhoff weighting? '''))
sfangmigM.par('na',rsf.doc.rsfpar('int','','','''number of dip angles '''))
sfangmigM.par('amax',rsf.doc.rsfpar('float','','','''maximum dip angle '''))
sfangmigM.par('ng',rsf.doc.rsfpar('int','na','','''number of reflection angles '''))
sfangmigM.par('gmax',rsf.doc.rsfpar('float','amax','','''maximum reflection angle'''))
sfangmigM.par('nxi',rsf.doc.rsfpar('int','nx','','''output samples '''))
sfangmigM.par('xi0',rsf.doc.rsfpar('float','x0','','''output orgin '''))
sfangmigM.par('dxi',rsf.doc.rsfpar('float','dx','','''output sampling '''))
sfangmigM.par('ntau',rsf.doc.rsfpar('int','nt','','''output vertical samples '''))
sfangmigM.par('tau0',rsf.doc.rsfpar('float','t0','','''output vertical orgin '''))
sfangmigM.par('dtau',rsf.doc.rsfpar('float','dt','','''output vertical sampling '''))
sfangmigM.par('nh',rsf.doc.rsfpar('int','','','''number of offsets '''))
sfangmigM.par('h0',rsf.doc.rsfpar('float','','','''initial offset '''))
sfangmigM.par('dh',rsf.doc.rsfpar('float','','','''offset increment'''))
sfangmigM.par('ng',rsf.doc.rsfpar('int','na','','''number of reflection angles '''))
sfangmigM.par('gmax',rsf.doc.rsfpar('float','amax','','''maximum reflection angle'''))
sfangmigM.par('nx',rsf.doc.rsfpar('int','nxi','','''data domain spatial samples '''))
sfangmigM.par('x0',rsf.doc.rsfpar('float','xi0','','''data domain spatial orgin '''))
sfangmigM.par('dx',rsf.doc.rsfpar('float','dxi','','''data domain spatial increment '''))
sfangmigM.par('nt',rsf.doc.rsfpar('int','ntau','','''number time samples '''))
sfangmigM.par('t0',rsf.doc.rsfpar('float','tau0','','''time orgin '''))
sfangmigM.par('dt',rsf.doc.rsfpar('float','dtau','','''time increment '''))
sfangmigM.par('eps',rsf.doc.rsfpar('float','0.00001','','''epsilon for division in semblance calc'''))
sfangmigM.par('l2',rsf.doc.rsfpar('bool','y','','''if y use l2 norm for semb, if n, use l1 norm '''))
sfangmigM.par('semb',rsf.doc.rsfpar('string ',desc='''output file containing Semblance (auxiliary output file name)'''))
sfangmigM.par('mask',rsf.doc.rsfpar('string ',desc='''input file contining image mask locations, 0 = skip (auxiliary input file name)'''))
sfangmigM.par('vin',rsf.doc.rsfpar('string ',desc='''input velocity file (auxiliary input file name)'''))
sfangmigM.version('2.1-git')
sfangmigM.synopsis('''sfangmigM < in.rsf > out.rsf semb=semb.rsf mask=mask.rsf vin=vin.rsf adj=n weighting=y na= amax= ng=na gmax=amax nxi=nx xi0=x0 dxi=dx ntau=nt tau0=t0 dtau=dt nh= h0= dh= ng=na gmax=amax nx=nxi x0=xi0 dx=dxi nt=ntau t0=tau0 dt=dtau eps=0.00001 l2=y''','''''')
rsf.doc.progs['sfangmigM']=sfangmigM

sfcovariance2d = rsf.doc.rsfprog('sfcovariance2d','user/luke/Mcovariance2d.c','''determine covariance from 2d data of mean zero, output is n1xn1 array ''')
sfcovariance2d.version('2.1-git')
sfcovariance2d.synopsis('''sfcovariance2d < in.rsf > out.rsf''','''''')
rsf.doc.progs['sfcovariance2d']=sfcovariance2d

sfdivnp = rsf.doc.rsfprog('sfdivnp','user/luke/Mdivnp.c','''OpenMP Parallelized  Smooth division. ''')
sfdivnp.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdivnp.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfdivnp.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sfdivnp.par('eps',rsf.doc.rsfpar('float','0.0f','','''regularization '''))
sfdivnp.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfdivnp.version('2.1-git')
sfdivnp.synopsis('''sfdivnp < fnum.rsf den=fden.rsf > frat.rsf niter=100 verb=y eps=0.0f rect#=(1,1,...)''','''
''')
rsf.doc.progs['sfdivnp']=sfdivnp

sfovczop = rsf.doc.rsfprog('sfovczop','user/luke/Movczop.c','''Post-stack 2-D oriented velocity continuation, with OpenMP Parallelism on frequency loop''')
sfovczop.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfovczop.par('nv',rsf.doc.rsfpar('int','','','''velocity steps '''))
sfovczop.par('dv',rsf.doc.rsfpar('float','','','''velocity step size '''))
sfovczop.par('v0',rsf.doc.rsfpar('float','','','''starting velocity '''))
sfovczop.version('2.1-git')
sfovczop.synopsis('''sfovczop < in.rsf > out.rsf verb=y nv= dv= v0=''','''
Axes: (Omega,k,p) -> (Omega,v,k,p)
''')
rsf.doc.progs['sfovczop']=sfovczop

sfdtw = rsf.doc.rsfprog('sfdtw','user/luke/Mdtw.c','''''')
sfdtw.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdtw.par('error',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfdtw.par('accum',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfdtw.par('shifts',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfdtw.par('maxshift',rsf.doc.rsfpar('int','','',''''''))
sfdtw.par('exp',rsf.doc.rsfpar('float','2','','''error exponent (g-f)^exp '''))
sfdtw.par('strain',rsf.doc.rsfpar('float','1.0','','''maximum strain '''))
sfdtw.par('ref',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfdtw.par('error',rsf.doc.rsfpar('string ',desc='''misfit error (auxiliary output file name)'''))
sfdtw.par('accum',rsf.doc.rsfpar('string ',desc='''accumulation errors from forward and backtracking (auxiliary output file name)'''))
sfdtw.par('shifts',rsf.doc.rsfpar('string ',desc='''output integer shifts as floats (auxiliary output file name)'''))
sfdtw.version('2.1-git')
sfdtw.synopsis('''sfdtw < _in.rsf ref=_ref.rsf > _out.rsf error=_error.rsf accum=_accum.rsf shifts=_shifts.rsf maxshift= exp=2 strain=1.0''','''program calculates the shifts to warp a matching trace (input) 
to a reference trace (ref=) of equal length and applies those shifts 
''')
rsf.doc.progs['sfdtw']=sfdtw

sfdtwapply = rsf.doc.rsfprog('sfdtw-apply','user/luke/Mdtw-apply.c','''''')
sfdtwapply.par('shifts',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdtwapply.par('shifts',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfdtwapply.version('2.1-git')
sfdtwapply.synopsis('''sfdtw-apply < _in.rsf shifts=_shifts.rsf > _out.rsf''','''program applies integer shifts (stored as floats!) to warp a matching trace.  Can match 1d shifts to a 1,2, or 3d volume , or 2d shifts to a 2, or 3 d volume, or 3d shifts to a 3d volume 
''')
rsf.doc.progs['sfdtw-apply']=sfdtwapply

sfdtwerrors = rsf.doc.rsfprog('sfdtw-errors','user/luke/Mdtw-errors.c','''''')
sfdtwerrors.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdtwerrors.par('maxshift',rsf.doc.rsfpar('int','','','''maximum shift '''))
sfdtwerrors.par('exp',rsf.doc.rsfpar('float','2','','''error exponent (g-f)^exp '''))
sfdtwerrors.par('ref',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfdtwerrors.version('2.1-git')
sfdtwerrors.synopsis('''sfdtw-errors < _in.rsf ref=_ref.rsf > _out.rsf maxshift= exp=2''','''program calculates the alignment errors 
between a reference and matching trace 
given a maximum shift (maxshift=) and an error exponent (exp=)
''')
rsf.doc.progs['sfdtw-errors']=sfdtwerrors

sfdtwaccumulate = rsf.doc.rsfprog('sfdtw-accumulate','user/luke/Mdtw-accumulate.c','''''')
sfdtwaccumulate.par('strain',rsf.doc.rsfpar('float','1','','''maximum strain '''))
sfdtwaccumulate.par('dir',rsf.doc.rsfpar('int','0','','''accumulation direction: 1 is forward, -1 is backward, 0 is both '''))
sfdtwaccumulate.version('2.1-git')
sfdtwaccumulate.synopsis('''sfdtw-accumulate < _in.rsf > _out.rsf strain=1 dir=0''','''accumulates or smooths alignment errors in the 
forward direction, subject to 
strain str=float is the maximum du/di
''')
rsf.doc.progs['sfdtw-accumulate']=sfdtwaccumulate

sfdtwtrack = rsf.doc.rsfprog('sfdtw-track','user/luke/Mdtw-track.c','''''')
sfdtwtrack.par('error',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdtwtrack.par('strain',rsf.doc.rsfpar('float','1','','''maximum strain '''))
sfdtwtrack.par('error',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfdtwtrack.version('2.1-git')
sfdtwtrack.synopsis('''sfdtw-track < _in.rsf error=_miss.rsf > _out.rsf strain=1''','''problem finds the optimal trajectory 
across accumulation errors using backtracking.  
takes the same strain strain= as the accumulation step.
''')
rsf.doc.progs['sfdtw-track']=sfdtwtrack

sfdtwflatten = rsf.doc.rsfprog('sfdtw-flatten','user/luke/Mdtw-flatten.c','''flattens a gather or similar object to its stack using dtw, optionally writes out shifts, currently set up for (time,gather,space) for 2d imaging''')
sfdtwflatten.par('shifts',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfdtwflatten.par('exp',rsf.doc.rsfpar('float','2','','''error exponent (g-f)^exp '''))
sfdtwflatten.par('strain',rsf.doc.rsfpar('float','1.0','','''maximum strain '''))
sfdtwflatten.par('maxshift',rsf.doc.rsfpar('int','','',''''''))
sfdtwflatten.par('shifts',rsf.doc.rsfpar('string ',desc='''output gather flattening shifts (auxiliary output file name)'''))
sfdtwflatten.version('2.1-git')
sfdtwflatten.synopsis('''sfdtw-flatten < _in.rsf > _out.rsf shifts=_shifts.rsf exp=2 strain=1.0 maxshift=''','''''')
rsf.doc.progs['sfdtw-flatten']=sfdtwflatten

sfdtw2 = rsf.doc.rsfprog('sfdtw2','user/luke/Mdtw2.c','''''')
sfdtw2.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdtw2.par('accum',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfdtw2.par('shifts',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfdtw2.par('maxshift',rsf.doc.rsfpar('int','','','''maximum shift to be tested '''))
sfdtw2.par('exp',rsf.doc.rsfpar('float','2','','''error exponent (g-f)^exp '''))
sfdtw2.par('strain1',rsf.doc.rsfpar('float','1.0','','''maximum strain in first axis '''))
sfdtw2.par('strain2',rsf.doc.rsfpar('float','1.0','','''maximum strain in second axis, if > 1 no strain limit '''))
sfdtw2.par('nalter',rsf.doc.rsfpar('int','2','','''number of horizontal and vertical smoothings '''))
sfdtw2.par('ref',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfdtw2.par('accum',rsf.doc.rsfpar('string ',desc='''optional output for accumulation errors (auxiliary output file name)'''))
sfdtw2.par('shifts',rsf.doc.rsfpar('string ',desc='''optional output for shifts (auxiliary output file name)'''))
sfdtw2.version('2.1-git')
sfdtw2.synopsis('''sfdtw2 < _in.rsf ref=_ref.rsf > _out.rsf accum=_accum.rsf shifts=_shifts.rsf maxshift= exp=2 strain1=1.0 strain2=1.0 nalter=2''','''program warps a 2D input image to a 2D reference image
''')
rsf.doc.progs['sfdtw2']=sfdtw2

sftranslate = rsf.doc.rsfprog('sftranslate','user/luke/Mtranslate.c','''''')
sftranslate.par('trans',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftranslate.par('adj',rsf.doc.rsfpar('bool','n','','''if y reverse translation, if n, translation '''))
sftranslate.par('x1',rsf.doc.rsfpar('float','0.','','''fixed translation in first dimension '''))
sftranslate.par('x2',rsf.doc.rsfpar('float','0.','','''fixed translation in second dimension '''))
sftranslate.par('trans',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sftranslate.version('2.1-git')
sftranslate.synopsis('''sftranslate < _in.rsf > _out.rsf trans=_trans.rsf adj=n x1=0. x2=0.''','''program translates a 2D image
''')
rsf.doc.progs['sftranslate']=sftranslate

sfconvolve = rsf.doc.rsfprog('sfconvolve','user/luke/Mconvolve.c','''''')
sfconvolve.par('ker',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfconvolve.par('adj',rsf.doc.rsfpar('bool','n','','''if y adjoint convolution, if n, convolution '''))
sfconvolve.par('wrap',rsf.doc.rsfpar('bool','n','','''if y, perform doughnut wrapping.  if n, no wrapping '''))
sfconvolve.par('ker',rsf.doc.rsfpar('string ',desc='''convolution kernel file (auxiliary input file name)'''))
sfconvolve.version('2.1-git')
sfconvolve.synopsis('''sfconvolve < _in.rsf > _out.rsf ker=_ker.rsf adj=n wrap=n''','''convolve input 2D image by kernel
''')
rsf.doc.progs['sfconvolve']=sfconvolve

sftransconv = rsf.doc.rsfprog('sftransconv','user/luke/Mtransconv.c','''''')
sftransconv.par('trans',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftransconv.par('ker',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftransconv.par('adj',rsf.doc.rsfpar('bool','n','','''if y reverse translation, if n, translation '''))
sftransconv.par('x1',rsf.doc.rsfpar('float','0.','','''fixed translation in first dimension '''))
sftransconv.par('x2',rsf.doc.rsfpar('float','0.','','''fixed translation in second dimension '''))
sftransconv.par('trans',rsf.doc.rsfpar('string ',desc='''variable translations file with same sampling as input, added ndim dimension (auxiliary input file name)'''))
sftransconv.par('ker',rsf.doc.rsfpar('string ',desc='''convolution kernel file (auxiliary input file name)'''))
sftransconv.version('2.1-git')
sftransconv.synopsis('''sftransconv < _in.rsf > _out.rsf trans=_trans.rsf ker=_ker.rsf adj=n x1=0. x2=0.''','''program translates a 2D image then convolves it with arbitrary kernel
''')
rsf.doc.progs['sftransconv']=sftransconv

sflskernel = rsf.doc.rsfprog('sflskernel','user/luke/Mlskernel.c','''''')
sflskernel.par('match',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflskernel.par('adj',rsf.doc.rsfpar('bool','n','','''if n takes kernel and outputs function, if y takes function and outputs kernel '''))
sflskernel.par('wrap',rsf.doc.rsfpar('bool','n','','''if y, perform doughnut wrapping.  if n, no wrapping '''))
sflskernel.par('nk1',rsf.doc.rsfpar('int','5','','''size of kernel in dimension 1'''))
sflskernel.par('nk2',rsf.doc.rsfpar('int','5','','''size of kernel in dimension 2 '''))
sflskernel.par('match',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sflskernel.version('2.1-git')
sflskernel.synopsis('''sflskernel < _in.rsf > _out.rsf match=_match.rsf adj=n wrap=n nk1=5 nk2=5''','''find kernel for convolution in ls sense, this is assuming 3 dimensional data and a 2d kernel
''')
rsf.doc.progs['sflskernel']=sflskernel

sfpathmin = rsf.doc.rsfprog('sfpathmin','user/luke/Mpathmin.c','''One dimensional path minimization for optimization input file has first coordinate parameter, second coordinate time ''')
sfpathmin.par('k',rsf.doc.rsfpar('float','1','','''stiffness relative to attraction'''))
sfpathmin.par('kink',rsf.doc.rsfpar('float','1','','''resistance to kinks  '''))
sfpathmin.par('lr',rsf.doc.rsfpar('float','.3','','''learning rate '''))
sfpathmin.par('g',rsf.doc.rsfpar('float','.1','','''scaling the gradient by how much '''))
sfpathmin.par('knots',rsf.doc.rsfpar('int','11','','''number of knots '''))
sfpathmin.par('niter',rsf.doc.rsfpar('int','10','',''''''))
sfpathmin.par('damp',rsf.doc.rsfpar('float','.5','','''if the path goes out of bounds, we reflect and dampen the rate of change by this much '''))
sfpathmin.par('shove',rsf.doc.rsfpar('float','1000','','''size of initial random lateral shove '''))
sfpathmin.par('aniso1',rsf.doc.rsfpar('float','D[1]/D[0]','','''aniso of 2nd axis relative to first   '''))
sfpathmin.par('dorder',rsf.doc.rsfpar('int','6','','''derivative order '''))
sfpathmin.par('srad',rsf.doc.rsfpar('int','2','','''smoothing radius for gradient '''))
sfpathmin.par('nsmooth',rsf.doc.rsfpar('int','1','','''number of gradient smoothings  '''))
sfpathmin.par('eps',rsf.doc.rsfpar('float','0.','','''if the change and gradient are simultaneously lower than this, terminate  early '''))
sfpathmin.version('2.1-git')
sfpathmin.synopsis('''sfpathmin < _in.rsf > _out.rsf k=1 kink=1 lr=.3 g=.1 knots=11 niter=10 damp=.5 shove=1000 aniso1=D[1]/D[0] dorder=6 srad=2 nsmooth=1 eps=0.''','''''')
rsf.doc.progs['sfpathmin']=sfpathmin

