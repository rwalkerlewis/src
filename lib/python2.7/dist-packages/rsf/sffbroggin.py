import rsf.doc

sfautofocusing = rsf.doc.rsfprog('sfautofocusing','user/fbroggin/Mautofocusing.c','''Marchenko-Wapenaar-Broggini iterative scheme''')
sfautofocusing.par('refl',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfautofocusing.par('Gm',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfautofocusing.par('G',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfautofocusing.par('H',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfautofocusing.par('p',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfautofocusing.par('q',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfautofocusing.par('window',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfautofocusing.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfautofocusing.par('conj',rsf.doc.rsfpar('bool','n','','''complex conjugation (time-reversal) flag '''))
sfautofocusing.par('twin',rsf.doc.rsfpar('bool','n','','''returns the timewindow as one of the outputs '''))
sfautofocusing.par('pandq',rsf.doc.rsfpar('bool','n','','''pandq=true: returns p and q '''))
sfautofocusing.par('Gtot',rsf.doc.rsfpar('bool','n','','''Gtot=true: returns G=Gp+Gm '''))
sfautofocusing.par('Htot',rsf.doc.rsfpar('bool','n','','''Htot=true: returns H=Gp-Gm '''))
sfautofocusing.par('niter',rsf.doc.rsfpar('int','1','','''number of iterations '''))
sfautofocusing.par('nshots',rsf.doc.rsfpar('int','1','','''number of shots '''))
sfautofocusing.par('scale',rsf.doc.rsfpar('float','1.0','','''scale factor '''))
sfautofocusing.par('eps',rsf.doc.rsfpar('float','1e-4','','''threshold for the timewindow '''))
sfautofocusing.par('shift',rsf.doc.rsfpar('int','5','','''shift in samples for the timewindow '''))
sfautofocusing.par('refl',rsf.doc.rsfpar('string ',desc='''000.rsf are 7 characters (auxiliary input file name)'''))
sfautofocusing.version('2.1-git')
sfautofocusing.synopsis('''sfautofocusing < Fplus.rsf refl=FRefl.rsf > FGp.rsf Gm=FGm.rsf G=FG.rsf H=FH.rsf p=Fp.rsf q=Fq.rsf window=Ftwin.rsf verb=n conj=n twin=n pandq=n Gtot=n Htot=n niter=1 nshots=1 scale=1.0 eps=1e-4 shift=5''','''
sfmarchenko < downgoing.rsf refl=REFL_000.rsf conj=y verb=n Gtot=y niter=21 nshots=401 scale=1 eps=1e-4 shift=5 Gm=Gm.rsf G=G.rsf> Gp.rsf

======= INPUTS ============

p0plus.rsf: initial downgoing wavefield

REFL_000.rsf: Fourier transform of the reflection response

======= PARAMETERS ========

conj  = [y]/n	- complex-conjugation of the first input (corresponds to time-reversal in time)
verb = y/[n]	- verbosity flag
twin  = y/[n]	- returns the timewindow as one of the outputs (window=window.rsf)
pandq  = y/[n]	- pandq=true: returns p and q, pandq=false returns Gp and Gm
Gtot  = y/[n]	- Gtot=true returns G=Gp+Gm
Htot  = y/[n]	- Htot=true returns H=Gp-Gm
niter  = 1		- number of iterations
nshots  = 1		- number of shots in the reflection response
scale  = 1.0	- scale factor (often due to resampling)
eps  = 1e-4		- threshold for the timewindow
shift  = 5		- shift in samples for the timewindow
''')
rsf.doc.progs['sfautofocusing']=sfautofocusing

sfmarchenko = rsf.doc.rsfprog('sfmarchenko','user/fbroggin/Mmarchenko.c','''Marchenko-Wapenaar-Broggini iterative scheme''')
sfmarchenko.par('refl',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmarchenko.par('Gm',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmarchenko.par('G',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmarchenko.par('H',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmarchenko.par('p',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmarchenko.par('q',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmarchenko.par('window',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmarchenko.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfmarchenko.par('conj',rsf.doc.rsfpar('bool','n','','''complex conjugation (time-reversal) flag '''))
sfmarchenko.par('twin',rsf.doc.rsfpar('bool','n','','''returns the timewindow as one of the outputs '''))
sfmarchenko.par('pandq',rsf.doc.rsfpar('bool','n','','''pandq=true: returns p and q '''))
sfmarchenko.par('Gtot',rsf.doc.rsfpar('bool','n','','''Gtot=true: returns G=Gp+Gm '''))
sfmarchenko.par('Htot',rsf.doc.rsfpar('bool','n','','''Htot=true: returns H=Gp-Gm '''))
sfmarchenko.par('niter',rsf.doc.rsfpar('int','1','','''number of iterations '''))
sfmarchenko.par('ntaper',rsf.doc.rsfpar('int','101','','''tapering widht '''))
sfmarchenko.par('scale',rsf.doc.rsfpar('float','1.0','','''scale factor '''))
sfmarchenko.par('eps',rsf.doc.rsfpar('float','1e-4','','''threshold for the timewindow '''))
sfmarchenko.par('shift',rsf.doc.rsfpar('int','5','','''shift in samples for the timewindow '''))
sfmarchenko.version('2.1-git')
sfmarchenko.synopsis('''sfmarchenko < Fplus.rsf refl=FRefl.rsf > FGp.rsf Gm=FGm.rsf G=FG.rsf H=FH.rsf p=Fp.rsf q=Fq.rsf window=Ftwin.rsf verb=n conj=n twin=n pandq=n Gtot=n Htot=n niter=1 ntaper=101 scale=1.0 eps=1e-4 shift=5''','''
sfmarchenko < downgoing.rsf refl=REFL_000.rsf conj=y verb=n Gtot=y niter=21 nshots=401 scale=1 eps=1e-4 shift=5 Gm=Gm.rsf G=G.rsf> Gp.rsf

======= INPUTS ============

p0plus.rsf: initial downgoing wave field

REFL_000.rsf: Fourier transform of the reflection response

======= PARAMETERS ========

conj  = [y]/n	- complex-conjugation of the first input (corresponds to time-reversal in time)
verb = y/[n]	- verbosity flag
twin  = y/[n]	- returns the timewindow as one of the outputs (window=window.rsf)
pandq  = y/[n]	- pandq=true: returns p and q, pandq=false returns Gp and Gm
Gtot  = y/[n]	- Gtot=true returns G=Gp+Gm
Htot  = y/[n]	- Htot=true returns H=Gp-Gm
niter  = 1		- number of iterations
ntaper  = 101	- tapering width for each side
scale  = 1.0	- scale factor (often due to resampling)
eps  = 1e-4		- threshold for the timewindow
shift  = 5		- shift in samples for the timewindow
''')
rsf.doc.progs['sfmarchenko']=sfmarchenko

sfawefd2d_fo = rsf.doc.rsfprog('sfawefd2d_fo','user/fbroggin/Mawefd2d_fo.c','''Finite-difference time-domain (FDTD) wave propagation modeling in lossless acoustic 2D media.''')
sfawefd2d_fo.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawefd2d_fo.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawefd2d_fo.par('sou',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawefd2d_fo.par('rec',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawefd2d_fo.par('datvz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfawefd2d_fo.par('wfl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfawefd2d_fo.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfawefd2d_fo.par('snap',rsf.doc.rsfpar('bool','n','','''wavefield snapshots flag '''))
sfawefd2d_fo.par('free',rsf.doc.rsfpar('bool','n','','''free surface flag '''))
sfawefd2d_fo.par('expl',rsf.doc.rsfpar('bool','n','','''exploding reflector '''))
sfawefd2d_fo.par('dabc',rsf.doc.rsfpar('bool','n','','''absorbing BC '''))
sfawefd2d_fo.par('recvz',rsf.doc.rsfpar('bool','n','','''vertical particle velocity data '''))
sfawefd2d_fo.par('srctype',rsf.doc.rsfpar('int','1','','''------------------------------------------------------------'''))
sfawefd2d_fo.par('jdata',rsf.doc.rsfpar('int','1','',''''''))
sfawefd2d_fo.par('jsnap',rsf.doc.rsfpar('int','nt','',''''''))
sfawefd2d_fo.par('nqz',rsf.doc.rsfpar('int','sf_n(az)','',''''''))
sfawefd2d_fo.par('nqx',rsf.doc.rsfpar('int','sf_n(ax)','',''''''))
sfawefd2d_fo.par('oqz',rsf.doc.rsfpar('float','sf_o(az)','',''''''))
sfawefd2d_fo.par('oqx',rsf.doc.rsfpar('float','sf_o(ax)','',''''''))
sfawefd2d_fo.version('2.1-git')
sfawefd2d_fo.synopsis('''sfawefd2d_fo < Fwav.rsf vel=Fvel.rsf den=Fden.rsf sou=Fsou.rsf rec=Frec.rsf > Fdat.rsf datvz=Fdatvz.rsf wfl=Fwfl.rsf verb=n snap=n free=n expl=n dabc=n recvz=n srctype=1 jdata=1 jsnap=nt nqz=sf_n(az) nqx=sf_n(ax) oqz=sf_o(az) oqx=sf_o(ax)''','''
This program fdelmodc can be used to model waves conforming the 2D wave equation in different media.
This program computes a solution of the 2D acoustic wave equation
defined through the first-order linearized systems of Newton's and Hooke's law.''')
rsf.doc.progs['sfawefd2d_fo']=sfawefd2d_fo

