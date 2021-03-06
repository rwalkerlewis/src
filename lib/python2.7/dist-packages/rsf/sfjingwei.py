import rsf.doc

sfinmo3_ort = rsf.doc.rsfprog('sfinmo3_ort','user/jingwei/Minmo3_ort.c','''3-D Inverse normal moveout using orthogonal parametrization''')
sfinmo3_ort.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfinmo3_ort.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second and third axes are half-offset instead of full offset '''))
sfinmo3_ort.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfinmo3_ort.par('extend',rsf.doc.rsfpar('int','8','','''trace extension '''))
sfinmo3_ort.version('2.1-git')
sfinmo3_ort.synopsis('''sfinmo3_ort < cmp.rsf > nmod.rsf velocity=vel.rsf half=y eps=0.01 extend=8''','''
velocity file contains slowness squared with n2=3 (Wavg,Wcos,Wsin)
''')
rsf.doc.progs['sfinmo3_ort']=sfinmo3_ort

sfradon2 = rsf.doc.rsfprog('sfradon2','user/jingwei/Mradon2.cc','''2to2 Radon transform (using 2to2 butterfly)''')
sfradon2.par('ntau',rsf.doc.rsfpar('','','',''''''))
sfradon2.par('np',rsf.doc.rsfpar('','','',''''''))
sfradon2.par('tau0',rsf.doc.rsfpar('','','',''''''))
sfradon2.par('dtau',rsf.doc.rsfpar('','','',''''''))
sfradon2.par('p0',rsf.doc.rsfpar('','','',''''''))
sfradon2.par('dp',rsf.doc.rsfpar('','','',''''''))
sfradon2.par('N',rsf.doc.rsfpar('','','','''number of partitions'''))
sfradon2.version('2.1-git')
sfradon2.synopsis('''sfradon2 < input.rsf > output.rsf ntau= np= tau0= dtau= p0= dp= N=''','''''')
rsf.doc.progs['sfradon2']=sfradon2

sfradon3 = rsf.doc.rsfprog('sfradon3','user/jingwei/Mradon3.cc','''3to3 Radon transform (using 3to3 butterfly)''')
sfradon3.par('ntau',rsf.doc.rsfpar('','','',''''''))
sfradon3.par('np',rsf.doc.rsfpar('','','',''''''))
sfradon3.par('nq',rsf.doc.rsfpar('','','',''''''))
sfradon3.par('tau0',rsf.doc.rsfpar('','','',''''''))
sfradon3.par('dtau',rsf.doc.rsfpar('','','',''''''))
sfradon3.par('p0',rsf.doc.rsfpar('','','',''''''))
sfradon3.par('dp',rsf.doc.rsfpar('','','',''''''))
sfradon3.par('q0',rsf.doc.rsfpar('','','',''''''))
sfradon3.par('dq',rsf.doc.rsfpar('','','',''''''))
sfradon3.par('N',rsf.doc.rsfpar('','','','''number of partitions'''))
sfradon3.version('2.1-git')
sfradon3.synopsis('''sfradon3 < input.rsf > output.rsf ntau= np= nq= tau0= dtau= p0= dp= q0= dq= N=''','''''')
rsf.doc.progs['sfradon3']=sfradon3

sfradon32 = rsf.doc.rsfprog('sfradon32','user/jingwei/Mradon32.cc','''azimuthally isotropic 3to2 Radon transform (using 2to2 butterfly)''')
sfradon32.par('ntau',rsf.doc.rsfpar('','','',''''''))
sfradon32.par('np',rsf.doc.rsfpar('','','',''''''))
sfradon32.par('tau0',rsf.doc.rsfpar('','','',''''''))
sfradon32.par('dtau',rsf.doc.rsfpar('','','',''''''))
sfradon32.par('p0',rsf.doc.rsfpar('','','',''''''))
sfradon32.par('dp',rsf.doc.rsfpar('','','',''''''))
sfradon32.par('N',rsf.doc.rsfpar('','','','''number of partitions'''))
sfradon32.version('2.1-git')
sfradon32.synopsis('''sfradon32 < input.rsf > output.rsf ntau= np= tau0= dtau= p0= dp= N=''','''''')
rsf.doc.progs['sfradon32']=sfradon32

sfapradon2 = rsf.doc.rsfprog('sfapradon2','user/jingwei/Mapradon2.cc','''apex shifted 2to3 Radon transform (using 2to2 butterfly)''')
sfapradon2.par('ntau',rsf.doc.rsfpar('','','',''''''))
sfapradon2.par('np',rsf.doc.rsfpar('','','',''''''))
sfapradon2.par('tau0',rsf.doc.rsfpar('','','',''''''))
sfapradon2.par('dtau',rsf.doc.rsfpar('','','',''''''))
sfapradon2.par('p0',rsf.doc.rsfpar('','','',''''''))
sfapradon2.par('dp',rsf.doc.rsfpar('','','',''''''))
sfapradon2.par('N',rsf.doc.rsfpar('','','','''number of partitions'''))
sfapradon2.version('2.1-git')
sfapradon2.synopsis('''sfapradon2 < input.rsf > output.rsf ntau= np= tau0= dtau= p0= dp= N=''','''''')
rsf.doc.progs['sfapradon2']=sfapradon2

sfradon34 = rsf.doc.rsfprog('sfradon34','user/jingwei/Mradon34.cc','''azimuthally anisotropic 3to4 Radon transform (using 3to3 butterfly)''')
sfradon34.par('ntau',rsf.doc.rsfpar('','','',''''''))
sfradon34.par('np',rsf.doc.rsfpar('','','',''''''))
sfradon34.par('nq',rsf.doc.rsfpar('','','',''''''))
sfradon34.par('ns',rsf.doc.rsfpar('','','',''''''))
sfradon34.par('tau0',rsf.doc.rsfpar('','','',''''''))
sfradon34.par('dtau',rsf.doc.rsfpar('','','',''''''))
sfradon34.par('p0',rsf.doc.rsfpar('','','',''''''))
sfradon34.par('dp',rsf.doc.rsfpar('','','',''''''))
sfradon34.par('q0',rsf.doc.rsfpar('','','',''''''))
sfradon34.par('dq',rsf.doc.rsfpar('','','',''''''))
sfradon34.par('s0',rsf.doc.rsfpar('','','',''''''))
sfradon34.par('ds',rsf.doc.rsfpar('','','',''''''))
sfradon34.par('N',rsf.doc.rsfpar('','','','''number of partitions'''))
sfradon34.version('2.1-git')
sfradon34.synopsis('''sfradon34 < input.rsf > output.rsf ntau= np= nq= ns= tau0= dtau= p0= dp= q0= dq= s0= ds= N=''','''''')
rsf.doc.progs['sfradon34']=sfradon34

sfdiradon2 = rsf.doc.rsfprog('sfdiradon2','user/jingwei/Mdiradon2.cc','''direct 2to2 hyper Radon transform (single integral, nearest point interpolation)''')
sfdiradon2.par('ntau',rsf.doc.rsfpar('','','',''''''))
sfdiradon2.par('np',rsf.doc.rsfpar('','','',''''''))
sfdiradon2.par('tau0',rsf.doc.rsfpar('','','',''''''))
sfdiradon2.par('dtau',rsf.doc.rsfpar('','','',''''''))
sfdiradon2.par('p0',rsf.doc.rsfpar('','','',''''''))
sfdiradon2.par('dp',rsf.doc.rsfpar('','','',''''''))
sfdiradon2.version('2.1-git')
sfdiradon2.synopsis('''sfdiradon2 < input.rsf > output.rsf ntau= np= tau0= dtau= p0= dp=''','''''')
rsf.doc.progs['sfdiradon2']=sfdiradon2

sfdiiradon2 = rsf.doc.rsfprog('sfdiiradon2','user/jingwei/Mdiiradon2.cc','''direct 2to2 hyper Radon transform (double integral, exact)''')
sfdiiradon2.par('ntau',rsf.doc.rsfpar('','','',''''''))
sfdiiradon2.par('np',rsf.doc.rsfpar('','','',''''''))
sfdiiradon2.par('tau0',rsf.doc.rsfpar('','','',''''''))
sfdiiradon2.par('dtau',rsf.doc.rsfpar('','','',''''''))
sfdiiradon2.par('p0',rsf.doc.rsfpar('','','',''''''))
sfdiiradon2.par('dp',rsf.doc.rsfpar('','','',''''''))
sfdiiradon2.version('2.1-git')
sfdiiradon2.synopsis('''sfdiiradon2 < input.rsf > output.rsf ntau= np= tau0= dtau= p0= dp=''','''''')
rsf.doc.progs['sfdiiradon2']=sfdiiradon2

sfadiradon2 = rsf.doc.rsfprog('sfadiradon2','user/jingwei/Madiradon2.cc','''direct adjoint 2to2 hyper Radon transform (single integral, nearest point interpolation)''')
sfadiradon2.par('nt',rsf.doc.rsfpar('','','',''''''))
sfadiradon2.par('nx',rsf.doc.rsfpar('','','',''''''))
sfadiradon2.par('t0',rsf.doc.rsfpar('','','',''''''))
sfadiradon2.par('dt',rsf.doc.rsfpar('','','',''''''))
sfadiradon2.par('x0',rsf.doc.rsfpar('','','',''''''))
sfadiradon2.par('dx',rsf.doc.rsfpar('','','',''''''))
sfadiradon2.version('2.1-git')
sfadiradon2.synopsis('''sfadiradon2 < input.rsf > output.rsf nt= nx= t0= dt= x0= dx=''','''''')
rsf.doc.progs['sfadiradon2']=sfadiradon2

sfdiradon32 = rsf.doc.rsfprog('sfdiradon32','user/jingwei/Mdiradon32.cc','''direct azimuthally isotropic 3to2 hyper Radon transform''')
sfdiradon32.par('ntau',rsf.doc.rsfpar('','','',''''''))
sfdiradon32.par('np',rsf.doc.rsfpar('','','',''''''))
sfdiradon32.par('tau0',rsf.doc.rsfpar('','','',''''''))
sfdiradon32.par('dtau',rsf.doc.rsfpar('','','',''''''))
sfdiradon32.par('p0',rsf.doc.rsfpar('','','',''''''))
sfdiradon32.par('dp',rsf.doc.rsfpar('','','',''''''))
sfdiradon32.version('2.1-git')
sfdiradon32.synopsis('''sfdiradon32 < input.rsf > output.rsf ntau= np= tau0= dtau= p0= dp=''','''''')
rsf.doc.progs['sfdiradon32']=sfdiradon32

sfdiradon3 = rsf.doc.rsfprog('sfdiradon3','user/jingwei/Mdiradon3.cc','''direct 3to3 reflection/diffraction Radon transform''')
sfdiradon3.par('fi',rsf.doc.rsfpar('','','',''''''))
sfdiradon3.par('ntau',rsf.doc.rsfpar('','','',''''''))
sfdiradon3.par('np',rsf.doc.rsfpar('','','',''''''))
sfdiradon3.par('nq',rsf.doc.rsfpar('','','',''''''))
sfdiradon3.par('tau0',rsf.doc.rsfpar('','','',''''''))
sfdiradon3.par('dtau',rsf.doc.rsfpar('','','',''''''))
sfdiradon3.par('p0',rsf.doc.rsfpar('','','',''''''))
sfdiradon3.par('dp',rsf.doc.rsfpar('','','',''''''))
sfdiradon3.par('q0',rsf.doc.rsfpar('','','',''''''))
sfdiradon3.par('dq',rsf.doc.rsfpar('','','',''''''))
sfdiradon3.version('2.1-git')
sfdiradon3.synopsis('''sfdiradon3 < input.rsf > output.rsf fi= ntau= np= nq= tau0= dtau= p0= dp= q0= dq=''','''''')
rsf.doc.progs['sfdiradon3']=sfdiradon3

sfdiradon34 = rsf.doc.rsfprog('sfdiradon34','user/jingwei/Mdiradon34.cc','''direct azimuthally anisotropic 3to4 full Radon transform (double integral, nearest point interpolation)''')
sfdiradon34.par('fi',rsf.doc.rsfpar('','','',''''''))
sfdiradon34.par('ntau',rsf.doc.rsfpar('','','',''''''))
sfdiradon34.par('np',rsf.doc.rsfpar('','','',''''''))
sfdiradon34.par('nq',rsf.doc.rsfpar('','','',''''''))
sfdiradon34.par('ns',rsf.doc.rsfpar('','','',''''''))
sfdiradon34.par('tau0',rsf.doc.rsfpar('','','',''''''))
sfdiradon34.par('dtau',rsf.doc.rsfpar('','','',''''''))
sfdiradon34.par('p0',rsf.doc.rsfpar('','','',''''''))
sfdiradon34.par('dp',rsf.doc.rsfpar('','','',''''''))
sfdiradon34.par('q0',rsf.doc.rsfpar('','','',''''''))
sfdiradon34.par('dq',rsf.doc.rsfpar('','','',''''''))
sfdiradon34.par('s0',rsf.doc.rsfpar('','','',''''''))
sfdiradon34.par('ds',rsf.doc.rsfpar('','','',''''''))
sfdiradon34.version('2.1-git')
sfdiradon34.synopsis('''sfdiradon34 < input.rsf > output.rsf fi= ntau= np= nq= ns= tau0= dtau= p0= dp= q0= dq= s0= ds=''','''''')
rsf.doc.progs['sfdiradon34']=sfdiradon34

sfsum = rsf.doc.rsfprog('sfsum','user/jingwei/Msum.cc','''adjoint test ''')
sfsum.par('input2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsum.par('input3',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsum.par('input4',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsum.version('2.1-git')
sfsum.synopsis('''sfsum < input1.rsf input2=input2.rsf input3=input3.rsf input4=input4.rsf > output.rsf''','''''')
rsf.doc.progs['sfsum']=sfsum

sfsum3 = rsf.doc.rsfprog('sfsum3','user/jingwei/Msum3.cc','''adjoint test''')
sfsum3.par('input2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsum3.par('input3',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsum3.par('input4',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsum3.version('2.1-git')
sfsum3.synopsis('''sfsum3 < input1.rsf input2=input2.rsf input3=input3.rsf input4=input4.rsf > output.rsf''','''''')
rsf.doc.progs['sfsum3']=sfsum3

sfsthres = rsf.doc.rsfprog('sfsthres','user/jingwei/Msthres.cc','''soft thresholding function''')
sfsthres.par('miu',rsf.doc.rsfpar('','','',''''''))
sfsthres.version('2.1-git')
sfsthres.synopsis('''sfsthres < input.rsf > output.rsf miu=''','''''')
rsf.doc.progs['sfsthres']=sfsthres

sfrankonetest = rsf.doc.rsfprog('sfrankonetest','user/jingwei/Mrankonetest.cc','''Test rank-1 approximation for lowrank decomposition matrices''')
sfrankonetest.par('nz',rsf.doc.rsfpar('','','',''''''))
sfrankonetest.par('dz',rsf.doc.rsfpar('','','',''''''))
sfrankonetest.par('z0',rsf.doc.rsfpar('','','',''''''))
sfrankonetest.par('nx',rsf.doc.rsfpar('','','',''''''))
sfrankonetest.par('dx',rsf.doc.rsfpar('','','',''''''))
sfrankonetest.par('x0',rsf.doc.rsfpar('','','',''''''))
sfrankonetest.par('npk',rsf.doc.rsfpar('','','','''maximum sample rows/columns'''))
sfrankonetest.version('2.1-git')
sfrankonetest.synopsis('''sfrankonetest < fft.rsf > alpha.rsf nz= dz= z0= nx= dx= x0= npk=''','''''')
rsf.doc.progs['sfrankonetest']=sfrankonetest

sfsvdtest = rsf.doc.rsfprog('sfsvdtest','user/jingwei/Msvdtest.cc','''Singular value decomposition to select rank-1 approximation''')
sfsvdtest.par('nz',rsf.doc.rsfpar('','','',''''''))
sfsvdtest.par('nx',rsf.doc.rsfpar('','','',''''''))
sfsvdtest.par('nkz',rsf.doc.rsfpar('','','',''''''))
sfsvdtest.par('nkx',rsf.doc.rsfpar('','','',''''''))
sfsvdtest.version('2.1-git')
sfsvdtest.synopsis('''sfsvdtest < matrix.rsf > alpha.rsf nz= nx= nkz= nkx=''','''''')
rsf.doc.progs['sfsvdtest']=sfsvdtest

sfsamplowmat = rsf.doc.rsfprog('sfsamplowmat','user/jingwei/Msamplowmat.cc','''Sample the lowrank propagation matrix ''')
sfsamplowmat.par('dt',rsf.doc.rsfpar('','','',''''''))
sfsamplowmat.par('nz',rsf.doc.rsfpar('','','',''''''))
sfsamplowmat.par('dz',rsf.doc.rsfpar('','','',''''''))
sfsamplowmat.par('z0',rsf.doc.rsfpar('','','',''''''))
sfsamplowmat.par('nx',rsf.doc.rsfpar('','','',''''''))
sfsamplowmat.par('dx',rsf.doc.rsfpar('','','',''''''))
sfsamplowmat.par('x0',rsf.doc.rsfpar('','','',''''''))
sfsamplowmat.version('2.1-git')
sfsamplowmat.synopsis('''sfsamplowmat < velocity.rsf > mat.rsf dt= nz= dz= z0= nx= dx= x0=''','''''')
rsf.doc.progs['sfsamplowmat']=sfsamplowmat

sfpseudo = rsf.doc.rsfprog('sfpseudo','user/jingwei/Mpseudo.cc','''Generate rank-1 approximation for lowrank wave propagation: prop1, prop2, prop3, prop4''')
sfpseudo.par('flag',rsf.doc.rsfpar('','','',''''''))
sfpseudo.par('reg',rsf.doc.rsfpar('','','',''''''))
sfpseudo.par('nz',rsf.doc.rsfpar('','','',''''''))
sfpseudo.par('dz',rsf.doc.rsfpar('','','',''''''))
sfpseudo.par('z0',rsf.doc.rsfpar('','','',''''''))
sfpseudo.par('nx',rsf.doc.rsfpar('','','',''''''))
sfpseudo.par('dx',rsf.doc.rsfpar('','','',''''''))
sfpseudo.par('x0',rsf.doc.rsfpar('','','','''Get lowrank parameters'''))
sfpseudo.par('seed',rsf.doc.rsfpar('','','','''seed for random number generator'''))
sfpseudo.par('eps',rsf.doc.rsfpar('','','','''tolerance'''))
sfpseudo.par('npk',rsf.doc.rsfpar('','','','''maximum sample rows/columns'''))
sfpseudo.version('2.1-git')
sfpseudo.synopsis('''sfpseudo < fft.rsf > alpha.rsf flag= reg= nz= dz= z0= nx= dx= x0= seed= eps= npk=''','''''')
rsf.doc.progs['sfpseudo']=sfpseudo

sfadjtest = rsf.doc.rsfprog('sfadjtest','user/jingwei/Madjtest.cc','''Ajoint test of prop1, prop2, prop3, prop4''')
sfadjtest.par('flag',rsf.doc.rsfpar('','','',''''''))
sfadjtest.par('reg',rsf.doc.rsfpar('','','',''''''))
sfadjtest.version('2.1-git')
sfadjtest.synopsis('''sfadjtest < fft.rsf flag= reg=''','''''')
rsf.doc.progs['sfadjtest']=sfadjtest

sfadjtest1 = rsf.doc.rsfprog('sfadjtest1','user/jingwei/Madjtest1.cc','''Ajoint test of prop1Pa and prop1P, prop2Na and prop2N''')
sfadjtest1.version('2.1-git')
sfadjtest1.synopsis('''sfadjtest1 < fft.rsf''','''''')
rsf.doc.progs['sfadjtest1']=sfadjtest1

sfsamptest = rsf.doc.rsfprog('sfsamptest','user/jingwei/Msamptest.cc','''Test sample function prop1, prop2, prop3, prop4''')
sfsamptest.par('flag',rsf.doc.rsfpar('','','',''''''))
sfsamptest.par('reg',rsf.doc.rsfpar('','','',''''''))
sfsamptest.par('zx0',rsf.doc.rsfpar('','','',''''''))
sfsamptest.par('kzx0',rsf.doc.rsfpar('','','',''''''))
sfsamptest.par('nz',rsf.doc.rsfpar('','','',''''''))
sfsamptest.par('dz',rsf.doc.rsfpar('','','',''''''))
sfsamptest.par('z0',rsf.doc.rsfpar('','','',''''''))
sfsamptest.par('nx',rsf.doc.rsfpar('','','',''''''))
sfsamptest.par('dx',rsf.doc.rsfpar('','','',''''''))
sfsamptest.par('x0',rsf.doc.rsfpar('','','',''''''))
sfsamptest.version('2.1-git')
sfsamptest.synopsis('''sfsamptest < fft.rsf flag= reg= zx0= kzx0= nz= dz= z0= nx= dx= x0=''','''''')
rsf.doc.progs['sfsamptest']=sfsamptest

sfsampmat = rsf.doc.rsfprog('sfsampmat','user/jingwei/Msampmat.cc','''Sample the whole matrix prop1, prop2, prop3, prop4''')
sfsampmat.par('flag',rsf.doc.rsfpar('','','',''''''))
sfsampmat.par('reg',rsf.doc.rsfpar('','','',''''''))
sfsampmat.par('nz',rsf.doc.rsfpar('','','',''''''))
sfsampmat.par('dz',rsf.doc.rsfpar('','','',''''''))
sfsampmat.par('z0',rsf.doc.rsfpar('','','',''''''))
sfsampmat.par('nx',rsf.doc.rsfpar('','','',''''''))
sfsampmat.par('dx',rsf.doc.rsfpar('','','',''''''))
sfsampmat.par('x0',rsf.doc.rsfpar('','','',''''''))
sfsampmat.version('2.1-git')
sfsampmat.synopsis('''sfsampmat < fft.rsf > column.rsf flag= reg= nz= dz= z0= nx= dx= x0=''','''''')
rsf.doc.progs['sfsampmat']=sfsampmat

sfinvtest = rsf.doc.rsfprog('sfinvtest','user/jingwei/Minvtest.cc','''Test inverse rank-1 approximation for lowrank wave propagation: prop1, prop2, prop3, prop4''')
sfinvtest.par('flag',rsf.doc.rsfpar('','','',''''''))
sfinvtest.par('reg',rsf.doc.rsfpar('','','',''''''))
sfinvtest.par('nz',rsf.doc.rsfpar('','','',''''''))
sfinvtest.par('dz',rsf.doc.rsfpar('','','',''''''))
sfinvtest.par('z0',rsf.doc.rsfpar('','','',''''''))
sfinvtest.par('nx',rsf.doc.rsfpar('','','',''''''))
sfinvtest.par('dx',rsf.doc.rsfpar('','','',''''''))
sfinvtest.par('x0',rsf.doc.rsfpar('','','',''''''))
sfinvtest.version('2.1-git')
sfinvtest.synopsis('''sfinvtest < input.rsf > output1.rsf flag= reg= nz= dz= z0= nx= dx= x0=''','''''')
rsf.doc.progs['sfinvtest']=sfinvtest

sfinvtest1 = rsf.doc.rsfprog('sfinvtest1','user/jingwei/Minvtest1.cc','''Test inverse rank-1 approximation for lowrank wave propagation: prop1, prop2, prop3, prop4''')
sfinvtest1.par('flag',rsf.doc.rsfpar('','','',''''''))
sfinvtest1.par('nz',rsf.doc.rsfpar('','','',''''''))
sfinvtest1.par('dz',rsf.doc.rsfpar('','','',''''''))
sfinvtest1.par('z0',rsf.doc.rsfpar('','','',''''''))
sfinvtest1.par('nx',rsf.doc.rsfpar('','','',''''''))
sfinvtest1.par('dx',rsf.doc.rsfpar('','','',''''''))
sfinvtest1.par('x0',rsf.doc.rsfpar('','','',''''''))
sfinvtest1.version('2.1-git')
sfinvtest1.synopsis('''sfinvtest1 < input.rsf > output1.rsf flag= nz= dz= z0= nx= dx= x0=''','''''')
rsf.doc.progs['sfinvtest1']=sfinvtest1

sfpseudolrexp = rsf.doc.rsfprog('sfpseudolrexp','user/jingwei/Mpseudolrexp.cc','''Generate rank-1 approximation for lowrank wave propagation: lrexp''')
sfpseudolrexp.par('flag',rsf.doc.rsfpar('','','',''''''))
sfpseudolrexp.par('gpz',rsf.doc.rsfpar('','','',''''''))
sfpseudolrexp.par('nt',rsf.doc.rsfpar('','','',''''''))
sfpseudolrexp.par('dt',rsf.doc.rsfpar('','','',''''''))
sfpseudolrexp.par('t0',rsf.doc.rsfpar('','','',''''''))
sfpseudolrexp.par('nz',rsf.doc.rsfpar('','','',''''''))
sfpseudolrexp.par('dz',rsf.doc.rsfpar('','','',''''''))
sfpseudolrexp.par('z0',rsf.doc.rsfpar('','','',''''''))
sfpseudolrexp.par('nx',rsf.doc.rsfpar('','','',''''''))
sfpseudolrexp.par('dx',rsf.doc.rsfpar('','','',''''''))
sfpseudolrexp.par('x0',rsf.doc.rsfpar('','','','''Get lowrank parameters'''))
sfpseudolrexp.par('seed',rsf.doc.rsfpar('','','','''seed for random number generator'''))
sfpseudolrexp.par('eps',rsf.doc.rsfpar('','','','''tolerance'''))
sfpseudolrexp.par('npk',rsf.doc.rsfpar('','','','''maximum sample rows/columns'''))
sfpseudolrexp.version('2.1-git')
sfpseudolrexp.synopsis('''sfpseudolrexp < fft.rsf > alpha.rsf flag= gpz= nt= dt= t0= nz= dz= z0= nx= dx= x0= seed= eps= npk=''','''''')
rsf.doc.progs['sfpseudolrexp']=sfpseudolrexp

sfsamptestlrexp = rsf.doc.rsfprog('sfsamptestlrexp','user/jingwei/Msamptestlrexp.cc','''Test sample function lrexp''')
sfsamptestlrexp.par('flag',rsf.doc.rsfpar('','','',''''''))
sfsamptestlrexp.par('gpz',rsf.doc.rsfpar('','','',''''''))
sfsamptestlrexp.par('zx0',rsf.doc.rsfpar('','','',''''''))
sfsamptestlrexp.par('kzx0',rsf.doc.rsfpar('','','',''''''))
sfsamptestlrexp.par('nt',rsf.doc.rsfpar('','','',''''''))
sfsamptestlrexp.par('dt',rsf.doc.rsfpar('','','',''''''))
sfsamptestlrexp.par('t0',rsf.doc.rsfpar('','','',''''''))
sfsamptestlrexp.par('nz',rsf.doc.rsfpar('','','',''''''))
sfsamptestlrexp.par('dz',rsf.doc.rsfpar('','','',''''''))
sfsamptestlrexp.par('z0',rsf.doc.rsfpar('','','',''''''))
sfsamptestlrexp.par('nx',rsf.doc.rsfpar('','','',''''''))
sfsamptestlrexp.par('dx',rsf.doc.rsfpar('','','',''''''))
sfsamptestlrexp.par('x0',rsf.doc.rsfpar('','','',''''''))
sfsamptestlrexp.version('2.1-git')
sfsamptestlrexp.synopsis('''sfsamptestlrexp < fft.rsf flag= gpz= zx0= kzx0= nt= dt= t0= nz= dz= z0= nx= dx= x0=''','''''')
rsf.doc.progs['sfsamptestlrexp']=sfsamptestlrexp

