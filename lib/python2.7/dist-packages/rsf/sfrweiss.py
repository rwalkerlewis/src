import rsf.doc

sfadjgradient2d_coupled_gpu = rsf.doc.rsfprog('sfadjgradient2d_coupled_gpu','user/rweiss/Madjgradient2d_coupled_gpu.cu','''2D ISOTROPIC wave-equation finite-difference migration on GPU ''')
sfadjgradient2d_coupled_gpu.par('vel2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfadjgradient2d_coupled_gpu.par('xig1',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfadjgradient2d_coupled_gpu.par('xig2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfadjgradient2d_coupled_gpu.par('us1',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfadjgradient2d_coupled_gpu.par('ur1',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfadjgradient2d_coupled_gpu.par('us2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfadjgradient2d_coupled_gpu.par('ur2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfadjgradient2d_coupled_gpu.par('grd2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfadjgradient2d_coupled_gpu.par('nxtap',rsf.doc.rsfpar('int','40','','''TAPER size '''))
sfadjgradient2d_coupled_gpu.par('hzero',rsf.doc.rsfpar('int','5','','''Number of near offsets to zero '''))
sfadjgradient2d_coupled_gpu.par('verbose',rsf.doc.rsfpar('bool','n','','''VERBOSITY flag '''))
sfadjgradient2d_coupled_gpu.par('epsDSO',rsf.doc.rsfpar('float','1.f','','''Weighting for DSO penalty '''))
sfadjgradient2d_coupled_gpu.par('eps4D',rsf.doc.rsfpar('float','0.f','','''Weighting for 4D penalty '''))
sfadjgradient2d_coupled_gpu.par('gpu',rsf.doc.rsfpar('int','0','','''ID of the GPU to be used '''))
sfadjgradient2d_coupled_gpu.version('2.1-git')
sfadjgradient2d_coupled_gpu.synopsis('''sfadjgradient2d_coupled_gpu < Fvel1.rsf vel2=Fvel2.rsf xig1=Fxig1.rsf xig2=Fxig2.rsf us1=Fus1.rsf ur1=Fur1.rsf us2=Fus2.rsf ur2=Fur2.rsf > Fgrd1.rsf grd2=Fgrd2.rsf nxtap=40 hzero=5 verbose=n epsDSO=1.f eps4D=0.f gpu=0''','''''')
rsf.doc.progs['sfadjgradient2d_coupled_gpu']=sfadjgradient2d_coupled_gpu

sfewefd2d_gpu = rsf.doc.rsfprog('sfewefd2d_gpu','user/rweiss/Mewefd2d_gpu.cu','''2D elastic time-domain FD modeling with GPU''')
sfewefd2d_gpu.par('ccc',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd2d_gpu.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd2d_gpu.par('sou',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd2d_gpu.par('rec',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd2d_gpu.par('wfl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfewefd2d_gpu.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfewefd2d_gpu.par('snap',rsf.doc.rsfpar('bool','n','','''wavefield snapshots flag '''))
sfewefd2d_gpu.par('free',rsf.doc.rsfpar('bool','n','','''free surface flag '''))
sfewefd2d_gpu.par('ssou',rsf.doc.rsfpar('bool','n','','''stress source '''))
sfewefd2d_gpu.par('dabc',rsf.doc.rsfpar('bool','n','','''absorbing BC '''))
sfewefd2d_gpu.par('gpu',rsf.doc.rsfpar('int','0','','''ID of the GPU to be used '''))
sfewefd2d_gpu.par('nbell',rsf.doc.rsfpar('int','5','','''bell size '''))
sfewefd2d_gpu.par('jdata',rsf.doc.rsfpar('int','1','','''extract receiver data every jdata time steps '''))
sfewefd2d_gpu.par('jsnap',rsf.doc.rsfpar('int','nt','','''save wavefield every jsnap time steps '''))
sfewefd2d_gpu.version('2.1-git')
sfewefd2d_gpu.synopsis('''sfewefd2d_gpu < Fwav.rsf ccc=Fccc.rsf den=Fden.rsf sou=Fsou.rsf rec=Frec.rsf > Fdat.rsf wfl=Fwfl.rsf verb=n snap=n free=n ssou=n dabc=n gpu=0 nbell=5 jdata=1 jsnap=nt''','''''')
rsf.doc.progs['sfewefd2d_gpu']=sfewefd2d_gpu

sfewefd3d_gpu_p2p = rsf.doc.rsfprog('sfewefd3d_gpu_p2p','user/rweiss/Mewefd3d_gpu_p2p.cu','''3D elastic time-domain FD modeling with GPU (For use in single node with one or more GPUs)''')
sfewefd3d_gpu_p2p.par('ccc',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd3d_gpu_p2p.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd3d_gpu_p2p.par('sou',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd3d_gpu_p2p.par('rec',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd3d_gpu_p2p.par('wfl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfewefd3d_gpu_p2p.par('ngpu',rsf.doc.rsfpar('int','1','','''how many local GPUs to use '''))
sfewefd3d_gpu_p2p.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfewefd3d_gpu_p2p.par('snap',rsf.doc.rsfpar('bool','n','','''wavefield snapshots flag '''))
sfewefd3d_gpu_p2p.par('free',rsf.doc.rsfpar('bool','n','','''free surface flag '''))
sfewefd3d_gpu_p2p.par('ssou',rsf.doc.rsfpar('bool','n','','''stress source '''))
sfewefd3d_gpu_p2p.par('dabc',rsf.doc.rsfpar('bool','n','','''absorbing BC '''))
sfewefd3d_gpu_p2p.par('interp',rsf.doc.rsfpar('bool','y','','''perform linear interpolation on receiver data '''))
sfewefd3d_gpu_p2p.par('nbell',rsf.doc.rsfpar('int','5','','''bell size '''))
sfewefd3d_gpu_p2p.par('jdata',rsf.doc.rsfpar('int','1','','''extract receiver data every jdata time steps '''))
sfewefd3d_gpu_p2p.par('jsnap',rsf.doc.rsfpar('int','nt','','''save wavefield every jsnap time steps '''))
sfewefd3d_gpu_p2p.version('2.1-git')
sfewefd3d_gpu_p2p.synopsis('''sfewefd3d_gpu_p2p < Fwav.rsf ccc=Fccc.rsf den=Fden.rsf sou=Fsou.rsf rec=Frec.rsf wfl=Fwfl.rsf > Fdat.rsf ngpu=1 verb=n snap=n free=n ssou=n dabc=n interp=y nbell=5 jdata=1 jsnap=nt''','''''')
rsf.doc.progs['sfewefd3d_gpu_p2p']=sfewefd3d_gpu_p2p

sfwem2d_gpu = rsf.doc.rsfprog('sfwem2d_gpu','user/rweiss/Mwem2d_gpu.cu','''2D ISOTROPIC wave-equation finite-difference migration on GPU ''')
sfwem2d_gpu.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwem2d_gpu.par('swf',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwem2d_gpu.par('rwf',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwem2d_gpu.par('swfout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfwem2d_gpu.par('rwfout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfwem2d_gpu.par('sillum',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfwem2d_gpu.par('rillum',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfwem2d_gpu.par('gpu',rsf.doc.rsfpar('int','0','','''ID of the GPU to be used '''))
sfwem2d_gpu.par('nxtap',rsf.doc.rsfpar('int','40','','''TAPER size '''))
sfwem2d_gpu.par('verbose',rsf.doc.rsfpar('bool','n','','''VERBOSITY flag '''))
sfwem2d_gpu.par('wantwf',rsf.doc.rsfpar('bool','n','','''Want output wavefields '''))
sfwem2d_gpu.par('wantillum',rsf.doc.rsfpar('bool','n','','''Want output wavefields '''))
sfwem2d_gpu.par('nh',rsf.doc.rsfpar('int','0','',''''''))
sfwem2d_gpu.version('2.1-git')
sfwem2d_gpu.synopsis('''sfwem2d_gpu vel=Fvel.rsf < Fxig.rsf swf=Fswf.rsf rwf=Frwf.rsf > Fxigo.rsf swfout=Fswfo.rsf rwfout=Frwfo.rsf sillum=Fsillum.rsf rillum=Frillum.rsf gpu=0 nxtap=40 verbose=n wantwf=n wantillum=n nh=0''','''''')
rsf.doc.progs['sfwem2d_gpu']=sfwem2d_gpu

sfwem3d_gpu = rsf.doc.rsfprog('sfwem3d_gpu','user/rweiss/Mwem3d_gpu.cu','''3D ISOTROPIC wave-equation finite-difference migration on GPU ''')
sfwem3d_gpu.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwem3d_gpu.par('swf',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwem3d_gpu.par('rwf',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwem3d_gpu.par('swfout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfwem3d_gpu.par('rwfout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfwem3d_gpu.par('kxmap',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfwem3d_gpu.par('gpu',rsf.doc.rsfpar('int','0','','''ID of the GPU to be used '''))
sfwem3d_gpu.par('nxtap',rsf.doc.rsfpar('int','40','','''TAPER size '''))
sfwem3d_gpu.par('nytap',rsf.doc.rsfpar('int','40','','''TAPER size '''))
sfwem3d_gpu.par('verbose',rsf.doc.rsfpar('bool','n','','''VERBOSITY flag '''))
sfwem3d_gpu.par('wantwf',rsf.doc.rsfpar('bool','n','','''Want output wavefields '''))
sfwem3d_gpu.version('2.1-git')
sfwem3d_gpu.synopsis('''sfwem3d_gpu < Fxig.rsf vel=Fvel.rsf swf=Fswf.rsf rwf=Frwf.rsf swfout=Fswfo.rsf rwfout=Frwfo.rsf kxmap=Fkxmap.rsf > Fxigo.rsf gpu=0 nxtap=40 nytap=40 verbose=n wantwf=n''','''''')
rsf.doc.progs['sfwem3d_gpu']=sfwem3d_gpu

sfadjgradient2d_gpu = rsf.doc.rsfprog('sfadjgradient2d_gpu','user/rweiss/Madjgradient2d_gpu.cu','''2D ISOTROPIC wave-equation finite-difference migration on GPU ''')
sfadjgradient2d_gpu.par('xig',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfadjgradient2d_gpu.par('swf',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfadjgradient2d_gpu.par('rwf',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfadjgradient2d_gpu.par('nxtap',rsf.doc.rsfpar('int','40','','''TAPER size '''))
sfadjgradient2d_gpu.par('verbose',rsf.doc.rsfpar('bool','n','','''VERBOSITY flag '''))
sfadjgradient2d_gpu.par('gpu',rsf.doc.rsfpar('int','0','','''ID of the GPU to be used '''))
sfadjgradient2d_gpu.version('2.1-git')
sfadjgradient2d_gpu.synopsis('''sfadjgradient2d_gpu < Fvel.rsf xig=Fxig.rsf swf=Fswf.rsf rwf=Frwf.rsf > Fgrd.rsf nxtap=40 verbose=n gpu=0''','''''')
rsf.doc.progs['sfadjgradient2d_gpu']=sfadjgradient2d_gpu

sfewefd2d_gpu_dev = rsf.doc.rsfprog('sfewefd2d_gpu_dev','user/rweiss/Mewefd2d_gpu_dev.cu','''2D elastic time-domain FD modeling with GPU (with experimental functionalities)''')
sfewefd2d_gpu_dev.par('ccc',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd2d_gpu_dev.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd2d_gpu_dev.par('sou',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd2d_gpu_dev.par('rec',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd2d_gpu_dev.par('wfl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfewefd2d_gpu_dev.par('um',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd2d_gpu_dev.par('uo',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd2d_gpu_dev.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfewefd2d_gpu_dev.par('snap',rsf.doc.rsfpar('bool','n','','''wavefield snapshots flag '''))
sfewefd2d_gpu_dev.par('free',rsf.doc.rsfpar('bool','n','','''free surface flag '''))
sfewefd2d_gpu_dev.par('ssou',rsf.doc.rsfpar('bool','n','','''stress source '''))
sfewefd2d_gpu_dev.par('dabc',rsf.doc.rsfpar('bool','n','','''absorbing BC '''))
sfewefd2d_gpu_dev.par('wavSrc',rsf.doc.rsfpar('bool','y','','''if yes, look for a source wavelet.  if no, look for initial displacement fields (uo and um) '''))
sfewefd2d_gpu_dev.par('gpu',rsf.doc.rsfpar('int','0','','''ID of the GPU to be used '''))
sfewefd2d_gpu_dev.par('nbell',rsf.doc.rsfpar('int','5','','''bell size '''))
sfewefd2d_gpu_dev.par('jdata',rsf.doc.rsfpar('int','1','','''extract receiver data every jdata time steps '''))
sfewefd2d_gpu_dev.par('jsnap',rsf.doc.rsfpar('int','nt','','''save wavefield every jsnap time steps '''))
sfewefd2d_gpu_dev.version('2.1-git')
sfewefd2d_gpu_dev.synopsis('''sfewefd2d_gpu_dev < Fwav.rsf ccc=Fccc.rsf den=Fden.rsf sou=Fsou.rsf rec=Frec.rsf wfl=Fwfl.rsf > Fdat.rsf um=Fum.rsf uo=Fuo.rsf verb=n snap=n free=n ssou=n dabc=n wavSrc=y gpu=0 nbell=5 jdata=1 jsnap=nt''','''''')
rsf.doc.progs['sfewefd2d_gpu_dev']=sfewefd2d_gpu_dev

sfewefd3d_gpu_mpi = rsf.doc.rsfprog('sfewefd3d_gpu_mpi','user/rweiss/Mewefd3d_gpu_mpi.cu','''3D elastic time-domain FD modeling with multiple GPUs coordinated via MPI''')
sfewefd3d_gpu_mpi.par('wav',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd3d_gpu_mpi.par('ccc',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd3d_gpu_mpi.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd3d_gpu_mpi.par('sou',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd3d_gpu_mpi.par('rec',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd3d_gpu_mpi.par('wfl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfewefd3d_gpu_mpi.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfewefd3d_gpu_mpi.par('snap',rsf.doc.rsfpar('bool','n','','''wavefield snapshots flag '''))
sfewefd3d_gpu_mpi.par('free',rsf.doc.rsfpar('bool','n','','''free surface flag '''))
sfewefd3d_gpu_mpi.par('ssou',rsf.doc.rsfpar('bool','n','','''stress source '''))
sfewefd3d_gpu_mpi.par('dabc',rsf.doc.rsfpar('bool','n','','''absorbing BC '''))
sfewefd3d_gpu_mpi.par('interp',rsf.doc.rsfpar('bool','y','','''perform linear interpolation on receiver locations '''))
sfewefd3d_gpu_mpi.par('ngpu',rsf.doc.rsfpar('int','1','','''Number of GPUs in each node, must be set to lowest common number of GPUs'''))
sfewefd3d_gpu_mpi.par('nbell',rsf.doc.rsfpar('int','5','','''bell size '''))
sfewefd3d_gpu_mpi.par('jdata',rsf.doc.rsfpar('int','1','','''extract receiver data every jdata time steps '''))
sfewefd3d_gpu_mpi.par('jsnap',rsf.doc.rsfpar('int','nt','','''save wavefield every jsnap time steps '''))
sfewefd3d_gpu_mpi.version('2.1-git')
sfewefd3d_gpu_mpi.synopsis('''sfewefd3d_gpu_mpi wav=Fwav.rsf ccc=Fccc.rsf den=Fden.rsf sou=Fsou.rsf rec=Frec.rsf wfl=Fwfl.rsf > Fdat.rsf verb=n snap=n free=n ssou=n dabc=n interp=y ngpu=1 nbell=5 jdata=1 jsnap=nt''','''''')
rsf.doc.progs['sfewefd3d_gpu_mpi']=sfewefd3d_gpu_mpi

sfewefd3d_multiNode = rsf.doc.rsfprog('sfewefd3d_multiNode','user/rweiss/Mewefd3d_multiNode.cu','''3D elastic time-domain FD modeling with multiple GPUs coordinated via MPI and p2p''')
sfewefd3d_multiNode.par('wav',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd3d_multiNode.par('ccc',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd3d_multiNode.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd3d_multiNode.par('sou',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd3d_multiNode.par('rec',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd3d_multiNode.par('wfl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfewefd3d_multiNode.par('um',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd3d_multiNode.par('uo',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefd3d_multiNode.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfewefd3d_multiNode.par('snap',rsf.doc.rsfpar('bool','n','','''wavefield snapshots flag '''))
sfewefd3d_multiNode.par('free',rsf.doc.rsfpar('bool','n','','''free surface flag '''))
sfewefd3d_multiNode.par('ssou',rsf.doc.rsfpar('bool','n','','''stress source '''))
sfewefd3d_multiNode.par('dabc',rsf.doc.rsfpar('bool','n','','''absorbing BC '''))
sfewefd3d_multiNode.par('interp',rsf.doc.rsfpar('bool','y','','''perform linear interpolation on receiver locations '''))
sfewefd3d_multiNode.par('wavSrc',rsf.doc.rsfpar('bool','y','','''if yes, look for a source wavelet.  if no, look for initial displacement fields (uo and um) '''))
sfewefd3d_multiNode.par('ngpu',rsf.doc.rsfpar('int','1','','''Number of GPUs in each node, must be set to lowest common number of GPUs'''))
sfewefd3d_multiNode.par('nbell',rsf.doc.rsfpar('int','5','','''bell size '''))
sfewefd3d_multiNode.par('jdata',rsf.doc.rsfpar('int','1','','''extract receiver data every jdata time steps '''))
sfewefd3d_multiNode.par('jsnap',rsf.doc.rsfpar('int','nt','','''save wavefield every jsnap time steps '''))
sfewefd3d_multiNode.version('2.1-git')
sfewefd3d_multiNode.synopsis('''sfewefd3d_multiNode wav=Fwav.rsf ccc=Fccc.rsf den=Fden.rsf sou=Fsou.rsf rec=Frec.rsf wfl=Fwfl.rsf > Fdat.rsf um=Fum.rsf uo=Fuo.rsf verb=n snap=n free=n ssou=n dabc=n interp=y wavSrc=y ngpu=1 nbell=5 jdata=1 jsnap=nt''','''''')
rsf.doc.progs['sfewefd3d_multiNode']=sfewefd3d_multiNode

