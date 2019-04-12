import rsf.doc

sfdatasucjb2rsf2d = rsf.doc.rsfprog('sfdatasucjb2rsf2d','user/chengjb/Mdatasucjb2rsf2d.c','''Convert 2D cjb-SU data to RSF format.''')
sfdatasucjb2rsf2d.par('fn',rsf.doc.rsfpar('string ',desc='''setup I/O files '''))
sfdatasucjb2rsf2d.version('2.1-git')
sfdatasucjb2rsf2d.synopsis('''sfdatasucjb2rsf2d > Fo.rsf fn=''','''
Copyright (C) 2012 Tongji University, Shanghai, China 
Authors: Jiubing Cheng

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
''')
rsf.doc.progs['sfdatasucjb2rsf2d']=sfdatasucjb2rsf2d

sfkine2dvti = rsf.doc.rsfprog('sfkine2dvti','user/chengjb/Mkine2dvti.c','''2-D two-components wavefield modeling using pseudo-pure mode P-wave equation in VTI media.''')
sfkine2dvti.par('WFp',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfkine2dvti.par('WFs',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfkine2dvti.par('nx',rsf.doc.rsfpar('int','201','',''''''))
sfkine2dvti.par('nz',rsf.doc.rsfpar('int','201','',''''''))
sfkine2dvti.par('dx',rsf.doc.rsfpar('float','0.008','',''''''))
sfkine2dvti.par('dz',rsf.doc.rsfpar('float','0.008','',''''''))
sfkine2dvti.par('time',rsf.doc.rsfpar('float','0.2','','''unit: SECOND '''))
sfkine2dvti.par('da',rsf.doc.rsfpar('float','0.05','',''''''))
sfkine2dvti.par('vp0',rsf.doc.rsfpar('float','3000.0','',''''''))
sfkine2dvti.par('vs0',rsf.doc.rsfpar('float','1200.0','',''''''))
sfkine2dvti.par('eps',rsf.doc.rsfpar('float','0.2','',''''''))
sfkine2dvti.par('del',rsf.doc.rsfpar('float','0.1','',''''''))
sfkine2dvti.par('the',rsf.doc.rsfpar('float','0.0','',''''''))
sfkine2dvti.par('t0',rsf.doc.rsfpar('float','0.04','',''''''))
sfkine2dvti.par('f0',rsf.doc.rsfpar('float','20.0','',''''''))
sfkine2dvti.version('2.1-git')
sfkine2dvti.synopsis('''sfkine2dvti > Fo1.rsf WFp=Fo2.rsf WFs=Fo3.rsf nx=201 nz=201 dx=0.008 dz=0.008 time=0.2 da=0.05 vp0=3000.0 vs0=1200.0 eps=0.2 del=0.1 the=0.0 t0=0.04 f0=20.0''','''Copyright (C) 2012 Tongji University, Shanghai, China 
Authors: Jiubing Cheng and Wei Kang

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
''')
rsf.doc.progs['sfkine2dvti']=sfkine2dvti

sfort3dhomodevcK = rsf.doc.rsfprog('sfort3dhomodevcK','user/chengjb/Mort3dhomodevcK.c','''Correct projection deviation in K-domian for 3-D pseudo-pure P-wave field in homogeneous ORT media.''')
sfort3dhomodevcK.par('apvy',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfort3dhomodevcK.par('apvz',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfort3dhomodevcK.par('PseudoPurePx',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfort3dhomodevcK.par('PseudoPurePy',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfort3dhomodevcK.par('PseudoPurePz',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfort3dhomodevcK.par('PseudoPureSepP',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfort3dhomodevcK.version('2.1-git')
sfort3dhomodevcK.synopsis('''sfort3dhomodevcK < Fix.rsf apvy=Fiy.rsf apvz=Fiz.rsf PseudoPurePx=Fi1.rsf PseudoPurePy=Fi2.rsf PseudoPurePz=Fi3.rsf > Fo1.rsf PseudoPureSepP=Fo2.rsf''','''
Refernces:
Cheng et al. (15th IWSA, 2012);
Cheng and Kang (SEG Abstract, 2012);
Kang and Cheng (SEG Abstract, 2012)
Wang et al.(SEG Abstract, 2012)      

Copyright (C) 2012 Tongji University, Shanghai, China 

Authors: Jiubing Cheng, Tengfei Wang and Wei Kang

This code is first written by Tengfei Wang at Tongji University,
and then optimzied by Jiubing Cheng for Madagascar version at BEG,
University of Texas at Austin.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
''')
rsf.doc.progs['sfort3dhomodevcK']=sfort3dhomodevcK

sfort3dhomodevK = rsf.doc.rsfprog('sfort3dhomodevK','user/chengjb/Mort3dhomodevK.c','''3D three-components projection deviation correction operators calculation in''')
sfort3dhomodevK.par('apvy',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfort3dhomodevK.par('apvz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfort3dhomodevK.par('taper',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfort3dhomodevK.par('vp0',rsf.doc.rsfpar('float','3000.0','',''''''))
sfort3dhomodevK.par('vs0',rsf.doc.rsfpar('float','1500.0','',''''''))
sfort3dhomodevK.par('de1',rsf.doc.rsfpar('float','0.05','',''''''))
sfort3dhomodevK.par('de2',rsf.doc.rsfpar('float','-0.05','',''''''))
sfort3dhomodevK.par('de3',rsf.doc.rsfpar('float','0.15','',''''''))
sfort3dhomodevK.par('ep1',rsf.doc.rsfpar('float','0.2','',''''''))
sfort3dhomodevK.par('ep2',rsf.doc.rsfpar('float','0.05','',''''''))
sfort3dhomodevK.par('ga1',rsf.doc.rsfpar('float','0.1','',''''''))
sfort3dhomodevK.par('ga2',rsf.doc.rsfpar('float','0.1','',''''''))
sfort3dhomodevK.par('alpha',rsf.doc.rsfpar('float','0.','',''''''))
sfort3dhomodevK.par('the',rsf.doc.rsfpar('float','0.','',''''''))
sfort3dhomodevK.par('phi',rsf.doc.rsfpar('float','0.','',''''''))
sfort3dhomodevK.par('hnx',rsf.doc.rsfpar('int','250','',''''''))
sfort3dhomodevK.par('hny',rsf.doc.rsfpar('int','250','',''''''))
sfort3dhomodevK.par('hnz',rsf.doc.rsfpar('int','250','',''''''))
sfort3dhomodevK.par('dx',rsf.doc.rsfpar('float','10.','',''''''))
sfort3dhomodevK.par('dy',rsf.doc.rsfpar('float','10.','',''''''))
sfort3dhomodevK.par('dz',rsf.doc.rsfpar('float','10.','',''''''))
sfort3dhomodevK.par('itaper',rsf.doc.rsfpar('int','1','',''''''))
sfort3dhomodevK.version('2.1-git')
sfort3dhomodevK.synopsis('''sfort3dhomodevK > Fo1.rsf apvy=Fo2.rsf apvz=Fo3.rsf taper=Fo4.rsf vp0=3000.0 vs0=1500.0 de1=0.05 de2=-0.05 de3=0.15 ep1=0.2 ep2=0.05 ga1=0.1 ga2=0.1 alpha=0. the=0. phi=0. hnx=250 hny=250 hnz=250 dx=10. dy=10. dz=10. itaper=1''','''* homogeneous orthorhombic media
Copyright (C) 2012 Tongji University, Shanghai, China 

Authors: Jiubing Cheng and Tengfei Wang 

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
''')
rsf.doc.progs['sfort3dhomodevK']=sfort3dhomodevK

sfort3dpseudophomo = rsf.doc.rsfprog('sfort3dpseudophomo','user/chengjb/Mort3dpseudophomo.c','''3-D three-components wavefield modeling using pseudo-pure mode P-wave equation in tilted ORT media.''')
sfort3dpseudophomo.par('PseudoPurePy',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfort3dpseudophomo.par('PseudoPurePz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfort3dpseudophomo.par('ns',rsf.doc.rsfpar('int','301','',''''''))
sfort3dpseudophomo.par('ny',rsf.doc.rsfpar('int','101','',''''''))
sfort3dpseudophomo.par('nx',rsf.doc.rsfpar('int','101','',''''''))
sfort3dpseudophomo.par('nz',rsf.doc.rsfpar('int','101','',''''''))
sfort3dpseudophomo.par('dt',rsf.doc.rsfpar('float','0.001','',''''''))
sfort3dpseudophomo.par('dx',rsf.doc.rsfpar('float','0.0','',''''''))
sfort3dpseudophomo.par('dy',rsf.doc.rsfpar('float','0.0','',''''''))
sfort3dpseudophomo.par('dz',rsf.doc.rsfpar('float','0.0','',''''''))
sfort3dpseudophomo.par('vp0',rsf.doc.rsfpar('float','3000.0','',''''''))
sfort3dpseudophomo.par('vs0',rsf.doc.rsfpar('float','1500.0','',''''''))
sfort3dpseudophomo.par('epsi1',rsf.doc.rsfpar('float','0.2','',''''''))
sfort3dpseudophomo.par('epsi2',rsf.doc.rsfpar('float','0.067','',''''''))
sfort3dpseudophomo.par('del1',rsf.doc.rsfpar('float','0.1','',''''''))
sfort3dpseudophomo.par('del2',rsf.doc.rsfpar('float','-0.0422','',''''''))
sfort3dpseudophomo.par('del3',rsf.doc.rsfpar('float','0.125','',''''''))
sfort3dpseudophomo.par('gam1',rsf.doc.rsfpar('float','0.1','',''''''))
sfort3dpseudophomo.par('gam2',rsf.doc.rsfpar('float','0.047','',''''''))
sfort3dpseudophomo.par('bd',rsf.doc.rsfpar('int','20','',''''''))
sfort3dpseudophomo.version('2.1-git')
sfort3dpseudophomo.synopsis('''sfort3dpseudophomo > Fo1.rsf PseudoPurePy=Fo2.rsf PseudoPurePz=Fo3.rsf ns=301 ny=101 nx=101 nz=101 dt=0.001 dx=0.0 dy=0.0 dz=0.0 vp0=3000.0 vs0=1500.0 epsi1=0.2 epsi2=0.067 del1=0.1 del2=-0.0422 del3=0.125 gam1=0.1 gam2=0.047 bd=20''','''
Refernces:
Cheng et al. (15th IWSA, 2012);
Cheng and Kang (SEG Abstract, 2012);
Kang and Cheng (SEG Abstract, 2012)
Wang et al.(SEG Abstract, 2012)      

Copyright (C) 2012 Tongji University, Shanghai, China 

Authors: Jiubing Cheng, Tengfei Wang and Wei Kang

This code is first written by Tengfei Wang at Tongji University,
and then optimzied by Jiubing Cheng for Madagascar version at BEG,
University of Texas at Austin.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
''')
rsf.doc.progs['sfort3dpseudophomo']=sfort3dpseudophomo

sftti2desep = rsf.doc.rsfprog('sftti2desep','user/chengjb/Mtti2desep.c','''2-D two-components wavefield modeling using original elastic displacement wave equation in TTI media.''')
sftti2desep.par('vs0',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti2desep.par('epsi',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti2desep.par('del',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti2desep.par('the',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti2desep.par('Elasticz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2desep.par('apx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2desep.par('apz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2desep.par('apxs',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2desep.par('apzs',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2desep.par('apxx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2desep.par('apzz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2desep.par('apxxs',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2desep.par('apzzs',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2desep.par('ElasticSepP',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2desep.par('ElasticSepSV',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2desep.par('ns',rsf.doc.rsfpar('int','301','',''''''))
sftti2desep.par('dt',rsf.doc.rsfpar('float','0.001','',''''''))
sftti2desep.par('isep',rsf.doc.rsfpar('int','0','','''if isep=1, separate wave-modes '''))
sftti2desep.par('ihomo',rsf.doc.rsfpar('int','0','','''if ihomo=1, homogeneous medium '''))
sftti2desep.par('nstep',rsf.doc.rsfpar('int','1','','''grid step to calculate operators: 1<=nstep<=5 '''))
sftti2desep.par('tapertype',rsf.doc.rsfpar('string ',desc='''taper type'''))
sftti2desep.version('2.1-git')
sftti2desep.synopsis('''sftti2desep < Fvp0.rsf vs0=Fvs0.rsf epsi=Feps.rsf del=Fdel.rsf the=Fthe.rsf > Fo1.rsf Elasticz=Fo2.rsf apx=Fo3.rsf apz=Fo4.rsf apxs=Fo5.rsf apzs=Fo6.rsf apxx=Fo7.rsf apzz=Fo8.rsf apxxs=Fo9.rsf apzzs=Fo10.rsf ElasticSepP=Fo11.rsf ElasticSepSV=Fo12.rsf ns=301 dt=0.001 isep=0 ihomo=0 nstep=1 tapertype=''','''
Copyright (C) 2012 Tongji University, Shanghai, China 
Authors: Jiubing Cheng, Wei Kang and Tengfei Wang

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
''')
rsf.doc.progs['sftti2desep']=sftti2desep

sftti2dpseudop = rsf.doc.rsfprog('sftti2dpseudop','user/chengjb/Mtti2dpseudop.c','''2-D two-components wavefield modeling using pseudo-pure mode P-wave equation in TTI media.''')
sftti2dpseudop.par('vs0',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti2dpseudop.par('epsi',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti2dpseudop.par('del',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti2dpseudop.par('the',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti2dpseudop.par('PseudoPurePz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2dpseudop.par('PseudoPureP',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2dpseudop.par('apvx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2dpseudop.par('apvz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2dpseudop.par('apvxx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2dpseudop.par('apvzz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2dpseudop.par('PseudoPureSepP',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2dpseudop.par('ns',rsf.doc.rsfpar('int','301','',''''''))
sftti2dpseudop.par('dt',rsf.doc.rsfpar('float','0.001','',''''''))
sftti2dpseudop.par('isep',rsf.doc.rsfpar('int','0','','''if isep=1, separate wave-modes '''))
sftti2dpseudop.par('ihomo',rsf.doc.rsfpar('int','0','','''if ihomo=1, homogeneous medium '''))
sftti2dpseudop.par('nstep',rsf.doc.rsfpar('int','1','','''grid step to calculate operators: 1<=nstep<=5 '''))
sftti2dpseudop.par('tapertype',rsf.doc.rsfpar('string ',desc='''taper type'''))
sftti2dpseudop.version('2.1-git')
sftti2dpseudop.synopsis('''sftti2dpseudop < Fvp0.rsf vs0=Fvs0.rsf epsi=Feps.rsf del=Fdel.rsf the=Fthe.rsf > Fo1.rsf PseudoPurePz=Fo2.rsf PseudoPureP=Fo3.rsf apvx=Fo4.rsf apvz=Fo5.rsf apvxx=Fo6.rsf apvzz=Fo7.rsf PseudoPureSepP=Fo8.rsf ns=301 dt=0.001 isep=0 ihomo=0 nstep=1 tapertype=''','''
Copyright (C) 2012 Tongji University, Shanghai, China 
Authors: Jiubing Cheng, Wei Kang and Tengfei Wang

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
''')
rsf.doc.progs['sftti2dpseudop']=sftti2dpseudop

sftti3de = rsf.doc.rsfprog('sftti3de','user/chengjb/Mtti3de.c','''3-D three-components wavefield modeling using elasic wave equation in tilted TI media.''')
sftti3de.par('vs0',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti3de.par('epsi',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti3de.par('del',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti3de.par('gam',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti3de.par('the',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti3de.par('phi',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti3de.par('Elasticy',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti3de.par('Elasticz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti3de.par('ns',rsf.doc.rsfpar('int','301','',''''''))
sftti3de.par('dt',rsf.doc.rsfpar('float','0.001','',''''''))
sftti3de.par('bd',rsf.doc.rsfpar('int','20','',''''''))
sftti3de.version('2.1-git')
sftti3de.synopsis('''sftti3de < Fvp0.rsf vs0=Fvs0.rsf epsi=Fep.rsf del=Fde.rsf gam=Fga.rsf the=Fthe.rsf phi=Fphi.rsf > Fo1.rsf Elasticy=Fo2.rsf Elasticz=Fo3.rsf ns=301 dt=0.001 bd=20''','''
Copyright (C) 2012 Tongji University, Shanghai, China 

Authors: Jiubing Cheng, Tengfei Wang and Wei Kang

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
''')
rsf.doc.progs['sftti3de']=sftti3de

sftwolayer2dti = rsf.doc.rsfprog('sftwolayer2dti','user/chengjb/Mtwolayer2dti.c','''2-D two-components wavefield modeling using pseudo-pure mode P-wave equation in VTI media.''')
sftwolayer2dti.par('vs0',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftwolayer2dti.par('epsi',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftwolayer2dti.par('del',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftwolayer2dti.par('the',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftwolayer2dti.par('nx',rsf.doc.rsfpar('int','201','',''''''))
sftwolayer2dti.par('nz',rsf.doc.rsfpar('int','201','',''''''))
sftwolayer2dti.par('dx',rsf.doc.rsfpar('float','0.008','',''''''))
sftwolayer2dti.par('dz',rsf.doc.rsfpar('float','0.008','',''''''))
sftwolayer2dti.par('vp0_1',rsf.doc.rsfpar('float','3000.0','',''''''))
sftwolayer2dti.par('vs0_1',rsf.doc.rsfpar('float','1200.0','',''''''))
sftwolayer2dti.par('eps_1',rsf.doc.rsfpar('float','0.2','',''''''))
sftwolayer2dti.par('del_1',rsf.doc.rsfpar('float','0.1','',''''''))
sftwolayer2dti.par('the_1',rsf.doc.rsfpar('float','0.0','',''''''))
sftwolayer2dti.par('vp0_2',rsf.doc.rsfpar('float','3000.0','',''''''))
sftwolayer2dti.par('vs0_2',rsf.doc.rsfpar('float','1200.0','',''''''))
sftwolayer2dti.par('eps_2',rsf.doc.rsfpar('float','0.2','',''''''))
sftwolayer2dti.par('del_2',rsf.doc.rsfpar('float','0.1','',''''''))
sftwolayer2dti.par('the_2',rsf.doc.rsfpar('float','30.0','','''Unit: degree '''))
sftwolayer2dti.version('2.1-git')
sftwolayer2dti.synopsis('''sftwolayer2dti > Fo1.rsf vs0=Fo2.rsf epsi=Fo3.rsf del=Fo4.rsf the=Fo5.rsf nx=201 nz=201 dx=0.008 dz=0.008 vp0_1=3000.0 vs0_1=1200.0 eps_1=0.2 del_1=0.1 the_1=0.0 vp0_2=3000.0 vs0_2=1200.0 eps_2=0.2 del_2=0.1 the_2=30.0''','''Copyright (C) 2012 Tongji University, Shanghai, China 
Authors: Jiubing Cheng and Wei Kang

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
''')
rsf.doc.progs['sftwolayer2dti']=sftwolayer2dti

sftwolayer3dti = rsf.doc.rsfprog('sftwolayer3dti','user/chengjb/Mtwolayer3dti.c','''2-D two-components wavefield modeling using pseudo-pure mode P-wave equation in VTI media.''')
sftwolayer3dti.par('vs0',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftwolayer3dti.par('epsi',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftwolayer3dti.par('del',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftwolayer3dti.par('gam',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftwolayer3dti.par('the',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftwolayer3dti.par('phi',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftwolayer3dti.par('ny',rsf.doc.rsfpar('int','201','',''''''))
sftwolayer3dti.par('nx',rsf.doc.rsfpar('int','201','',''''''))
sftwolayer3dti.par('nz',rsf.doc.rsfpar('int','201','',''''''))
sftwolayer3dti.par('dy',rsf.doc.rsfpar('float','0.008','',''''''))
sftwolayer3dti.par('dx',rsf.doc.rsfpar('float','0.008','',''''''))
sftwolayer3dti.par('dz',rsf.doc.rsfpar('float','0.008','',''''''))
sftwolayer3dti.par('vp0_1',rsf.doc.rsfpar('float','3000.0','',''''''))
sftwolayer3dti.par('vs0_1',rsf.doc.rsfpar('float','1200.0','',''''''))
sftwolayer3dti.par('eps_1',rsf.doc.rsfpar('float','0.2','',''''''))
sftwolayer3dti.par('del_1',rsf.doc.rsfpar('float','0.1','',''''''))
sftwolayer3dti.par('gam_1',rsf.doc.rsfpar('float','0.0','',''''''))
sftwolayer3dti.par('the_1',rsf.doc.rsfpar('float','0.0','',''''''))
sftwolayer3dti.par('phi_1',rsf.doc.rsfpar('float','0.0','',''''''))
sftwolayer3dti.par('vp0_2',rsf.doc.rsfpar('float','3000.0','',''''''))
sftwolayer3dti.par('vs0_2',rsf.doc.rsfpar('float','1200.0','',''''''))
sftwolayer3dti.par('eps_2',rsf.doc.rsfpar('float','0.2','',''''''))
sftwolayer3dti.par('del_2',rsf.doc.rsfpar('float','0.1','',''''''))
sftwolayer3dti.par('gam_2',rsf.doc.rsfpar('float','0.0','',''''''))
sftwolayer3dti.par('the_2',rsf.doc.rsfpar('float','30.0','','''Unit: degree '''))
sftwolayer3dti.par('phi_2',rsf.doc.rsfpar('float','0.0','',''''''))
sftwolayer3dti.version('2.1-git')
sftwolayer3dti.synopsis('''sftwolayer3dti > Fo1.rsf vs0=Fo2.rsf epsi=Fo3.rsf del=Fo4.rsf gam=Fo5.rsf the=Fo6.rsf phi=Fo7.rsf ny=201 nx=201 nz=201 dy=0.008 dx=0.008 dz=0.008 vp0_1=3000.0 vs0_1=1200.0 eps_1=0.2 del_1=0.1 gam_1=0.0 the_1=0.0 phi_1=0.0 vp0_2=3000.0 vs0_2=1200.0 eps_2=0.2 del_2=0.1 gam_2=0.0 the_2=30.0 phi_2=0.0''','''Copyright (C) 2012 Tongji University, Shanghai, China 
Authors: Jiubing Cheng and Wei Kang

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
''')
rsf.doc.progs['sftwolayer3dti']=sftwolayer3dti

sfvti2desep = rsf.doc.rsfprog('sfvti2desep','user/chengjb/Mvti2desep.c','''2-D two-components wavefield modeling using original elastic displacement wave equation in VTI media.''')
sfvti2desep.par('vs0',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti2desep.par('epsi',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti2desep.par('del',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti2desep.par('Elasticz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2desep.par('apx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2desep.par('apz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2desep.par('apxs',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2desep.par('apzs',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2desep.par('apxx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2desep.par('apzz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2desep.par('apxxs',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2desep.par('apzzs',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2desep.par('ElasticSepP',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2desep.par('ElasticSepSV',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2desep.par('ns',rsf.doc.rsfpar('int','301','',''''''))
sfvti2desep.par('dt',rsf.doc.rsfpar('float','0.001','',''''''))
sfvti2desep.par('isep',rsf.doc.rsfpar('int','0','','''if isep=1, separate wave-modes '''))
sfvti2desep.par('ihomo',rsf.doc.rsfpar('int','0','','''if ihomo=1, homogeneous medium '''))
sfvti2desep.par('nstep',rsf.doc.rsfpar('int','1','','''grid step to calculate operators: 1<=nstep<=5 '''))
sfvti2desep.par('tapertype',rsf.doc.rsfpar('string ',desc='''taper type'''))
sfvti2desep.version('2.1-git')
sfvti2desep.synopsis('''sfvti2desep < Fvp0.rsf vs0=Fvs0.rsf epsi=Feps.rsf del=Fdel.rsf > Fo1.rsf Elasticz=Fo2.rsf apx=Fo3.rsf apz=Fo4.rsf apxs=Fo5.rsf apzs=Fo6.rsf apxx=Fo7.rsf apzz=Fo8.rsf apxxs=Fo9.rsf apzzs=Fo10.rsf ElasticSepP=Fo11.rsf ElasticSepSV=Fo12.rsf ns=301 dt=0.001 isep=0 ihomo=0 nstep=1 tapertype=''','''
Copyright (C) 2012 Tongji University, Shanghai, China 
Authors: Jiubing Cheng and Tengfei Wang

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
''')
rsf.doc.progs['sfvti2desep']=sfvti2desep

sfvti2dpseudop = rsf.doc.rsfprog('sfvti2dpseudop','user/chengjb/Mvti2dpseudop.c','''2-D two-components wavefield modeling using pseudo-pure mode P-wave equation in VTI media.''')
sfvti2dpseudop.par('vs0',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti2dpseudop.par('epsi',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti2dpseudop.par('del',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti2dpseudop.par('PseudoPurePz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop.par('PseudoPureP',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop.par('apvx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop.par('apvz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop.par('apvxx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop.par('apvzz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop.par('PseudoPureSepP',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop.par('ns',rsf.doc.rsfpar('int','301','',''''''))
sfvti2dpseudop.par('dt',rsf.doc.rsfpar('float','0.001','',''''''))
sfvti2dpseudop.par('isep',rsf.doc.rsfpar('int','0','','''if isep=1, separate wave-modes '''))
sfvti2dpseudop.par('ihomo',rsf.doc.rsfpar('int','0','','''if ihomo=1, homogeneous medium '''))
sfvti2dpseudop.par('itaper',rsf.doc.rsfpar('int','0','','''if itaper=1, taper the operator '''))
sfvti2dpseudop.par('nstep',rsf.doc.rsfpar('int','1','','''grid step to calculate operators: 1<=nstep<=5 '''))
sfvti2dpseudop.par('tapertype',rsf.doc.rsfpar('string ',desc='''taper type'''))
sfvti2dpseudop.version('2.1-git')
sfvti2dpseudop.synopsis('''sfvti2dpseudop < Fvp0.rsf vs0=Fvs0.rsf epsi=Feps.rsf del=Fdel.rsf > Fo1.rsf PseudoPurePz=Fo2.rsf PseudoPureP=Fo3.rsf apvx=Fo4.rsf apvz=Fo5.rsf apvxx=Fo6.rsf apvzz=Fo7.rsf PseudoPureSepP=Fo8.rsf ns=301 dt=0.001 isep=0 ihomo=0 itaper=0 nstep=1 tapertype=''','''
Copyright (C) 2012 Tongji University, Shanghai, China 
Authors: Jiubing Cheng and Wei Kang

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
''')
rsf.doc.progs['sfvti2dpseudop']=sfvti2dpseudop

sfvti2dpseudop1 = rsf.doc.rsfprog('sfvti2dpseudop1','user/chengjb/Mvti2dpseudop1.c','''2-D two-components wavefield modeling using pseudo-pure mode P-wave equation in VTI media.''')
sfvti2dpseudop1.par('vs0',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti2dpseudop1.par('epsi',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti2dpseudop1.par('del',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti2dpseudop1.par('PseudoPurePz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('PseudoPureP',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('adx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('adz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('apx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('apz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('apvx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('apvz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('adxx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('adzz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('apxx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('apzz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('apvxx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('apvzz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('PseudoPureSepP',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('ns',rsf.doc.rsfpar('int','301','',''''''))
sfvti2dpseudop1.par('dt',rsf.doc.rsfpar('float','0.001','',''''''))
sfvti2dpseudop1.par('isep',rsf.doc.rsfpar('int','0','','''if isep=1, separate wave-modes '''))
sfvti2dpseudop1.par('ihomo',rsf.doc.rsfpar('int','0','','''if ihomo=1, homogeneous medium '''))
sfvti2dpseudop1.par('itaper',rsf.doc.rsfpar('int','0','','''if itaper=1, taper the wavenumber domain p=operators'''))
sfvti2dpseudop1.par('nstep',rsf.doc.rsfpar('int','2','',''''''))
sfvti2dpseudop1.par('tapertype',rsf.doc.rsfpar('string ',desc='''taper type'''))
sfvti2dpseudop1.version('2.1-git')
sfvti2dpseudop1.synopsis('''sfvti2dpseudop1 < Fvp0.rsf vs0=Fvs0.rsf epsi=Feps.rsf del=Fdel.rsf > Fo1.rsf PseudoPurePz=Fo2.rsf PseudoPureP=Fo3.rsf adx=Fo4.rsf adz=Fo5.rsf apx=Fo6.rsf apz=Fo7.rsf apvx=Fo8.rsf apvz=Fo9.rsf adxx=Fo10.rsf adzz=Fo11.rsf apxx=Fo12.rsf apzz=Fo13.rsf apvxx=Fo14.rsf apvzz=Fo15.rsf PseudoPureSepP=Fo16.rsf ns=301 dt=0.001 isep=0 ihomo=0 itaper=0 nstep=2 tapertype=''','''
Copyright (C) 2012 Tongji University, Shanghai, China 
Authors: Jiubing Cheng, Wei Kang and Tengfei Wang

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
''')
rsf.doc.progs['sfvti2dpseudop1']=sfvti2dpseudop1

sfvti2dpseudopfvs0 = rsf.doc.rsfprog('sfvti2dpseudopfvs0','user/chengjb/Mvti2dpseudopfvs0.c','''2-D two-components wavefield modeling using pseudo-pure mode P-wave equation in VTI media.''')
sfvti2dpseudopfvs0.par('epsi',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti2dpseudopfvs0.par('del',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti2dpseudopfvs0.par('PseudoPurePz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudopfvs0.par('PseudoPureP',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudopfvs0.par('Fvs0',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudopfvs0.par('apvx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudopfvs0.par('apvz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudopfvs0.par('apvxx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudopfvs0.par('apvzz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudopfvs0.par('PseudoPureSepP',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudopfvs0.par('ns',rsf.doc.rsfpar('int','301','',''''''))
sfvti2dpseudopfvs0.par('dt',rsf.doc.rsfpar('float','0.001','',''''''))
sfvti2dpseudopfvs0.par('isep',rsf.doc.rsfpar('int','0','','''if isep=1, separate wave-modes '''))
sfvti2dpseudopfvs0.par('ihomo',rsf.doc.rsfpar('int','0','','''if ihomo=1, homogeneous medium '''))
sfvti2dpseudopfvs0.par('itaper',rsf.doc.rsfpar('int','0','','''if itaper=1, taper the operator '''))
sfvti2dpseudopfvs0.par('nstep',rsf.doc.rsfpar('int','1','','''grid step to calculate operators: 1<=nstep<=5 '''))
sfvti2dpseudopfvs0.par('tapertype',rsf.doc.rsfpar('string ',desc='''taper type'''))
sfvti2dpseudopfvs0.version('2.1-git')
sfvti2dpseudopfvs0.synopsis('''sfvti2dpseudopfvs0 < Fvp0.rsf epsi=Feps.rsf del=Fdel.rsf > Fo1.rsf PseudoPurePz=Fo2.rsf PseudoPureP=Fo3.rsf Fvs0=Fo4.rsf apvx=Fo5.rsf apvz=Fo6.rsf apvxx=Fo7.rsf apvzz=Fo8.rsf PseudoPureSepP=Fo9.rsf ns=301 dt=0.001 isep=0 ihomo=0 itaper=0 nstep=1 tapertype=''','''with finite nonzero vs0

Copyright (C) 2012 Tongji University, Shanghai, China 
Authors: Jiubing Cheng and Wei Kang

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
''')
rsf.doc.progs['sfvti2dpseudopfvs0']=sfvti2dpseudopfvs0

sfvti2dpseudosv = rsf.doc.rsfprog('sfvti2dpseudosv','user/chengjb/Mvti2dpseudosv.c','''2-D two-components wavefield modeling using pseudo-pure mode qSV-wave equation in VTI media.''')
sfvti2dpseudosv.par('vs0',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti2dpseudosv.par('epsi',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti2dpseudosv.par('del',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti2dpseudosv.par('PseudoPureSVz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudosv.par('PseudoPureSV',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudosv.par('acx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudosv.par('acz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudosv.par('asx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudosv.par('asz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudosv.par('asvx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudosv.par('asvz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudosv.par('acxx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudosv.par('aczz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudosv.par('asxx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudosv.par('aszz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudosv.par('asvxx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudosv.par('asvzz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudosv.par('PseudoPureSepSV',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudosv.par('ns',rsf.doc.rsfpar('int','301','',''''''))
sfvti2dpseudosv.par('dt',rsf.doc.rsfpar('float','0.001','',''''''))
sfvti2dpseudosv.par('isep',rsf.doc.rsfpar('int','0','','''if isep=1, separate wave-modes '''))
sfvti2dpseudosv.par('ihomo',rsf.doc.rsfpar('int','0','','''if ihomo=1, homogeneous medium '''))
sfvti2dpseudosv.par('itaper',rsf.doc.rsfpar('int','0','','''if itaper=1, taper the wavenumber domain p=operators'''))
sfvti2dpseudosv.par('nstep',rsf.doc.rsfpar('int','2','',''''''))
sfvti2dpseudosv.par('tapertype',rsf.doc.rsfpar('string ',desc='''taper type'''))
sfvti2dpseudosv.version('2.1-git')
sfvti2dpseudosv.synopsis('''sfvti2dpseudosv < Fvp0.rsf vs0=Fvs0.rsf epsi=Feps.rsf del=Fdel.rsf > Fo1.rsf PseudoPureSVz=Fo2.rsf PseudoPureSV=Fo3.rsf acx=Fo4.rsf acz=Fo5.rsf asx=Fo6.rsf asz=Fo7.rsf asvx=Fo8.rsf asvz=Fo9.rsf acxx=Fo10.rsf aczz=Fo11.rsf asxx=Fo12.rsf aszz=Fo13.rsf asvxx=Fo14.rsf asvzz=Fo15.rsf PseudoPureSepSV=Fo16.rsf ns=301 dt=0.001 isep=0 ihomo=0 itaper=0 nstep=2 tapertype=''','''
Copyright (C) 2012 Tongji University, Shanghai, China 
Authors: Jiubing Cheng, Wei Kang and Tengfei Wang

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
''')
rsf.doc.progs['sfvti2dpseudosv']=sfvti2dpseudosv

sfvti3de = rsf.doc.rsfprog('sfvti3de','user/chengjb/Mvti3de.c','''3-D three-components wavefield modeling using elasic wave equation in VTI media.''')
sfvti3de.par('vs0',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti3de.par('epsi',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti3de.par('del',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti3de.par('gam',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti3de.par('Elasticy',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti3de.par('Elasticz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti3de.par('ns',rsf.doc.rsfpar('int','301','',''''''))
sfvti3de.par('dt',rsf.doc.rsfpar('float','0.001','',''''''))
sfvti3de.par('bd',rsf.doc.rsfpar('int','20','',''''''))
sfvti3de.version('2.1-git')
sfvti3de.synopsis('''sfvti3de < Fvp0.rsf vs0=Fvs0.rsf epsi=Fep.rsf del=Fde.rsf gam=Fga.rsf > Fo1.rsf Elasticy=Fo2.rsf Elasticz=Fo3.rsf ns=301 dt=0.001 bd=20''','''
Copyright (C) 2012 Tongji University, Shanghai, China 

Authors: Jiubing Cheng, Tengfei Wang and Wei Kang

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
''')
rsf.doc.progs['sfvti3de']=sfvti3de

sfvti3dpseudosh = rsf.doc.rsfprog('sfvti3dpseudosh','user/chengjb/Mvti3dpseudosh.c','''3-D three-components wavefield modeling using pure mode SH-wave equation in 3D VTI media.''')
sfvti3dpseudosh.par('vs0',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti3dpseudosh.par('epsi',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti3dpseudosh.par('del',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti3dpseudosh.par('gam',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti3dpseudosh.par('SHy',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti3dpseudosh.par('SH',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti3dpseudosh.par('ns',rsf.doc.rsfpar('int','301','',''''''))
sfvti3dpseudosh.par('dt',rsf.doc.rsfpar('float','0.001','',''''''))
sfvti3dpseudosh.par('bd',rsf.doc.rsfpar('int','20','',''''''))
sfvti3dpseudosh.version('2.1-git')
sfvti3dpseudosh.synopsis('''sfvti3dpseudosh < Fvp0.rsf vs0=Fvs0.rsf epsi=Fep.rsf del=Fde.rsf gam=Fga.rsf > Fo1.rsf SHy=Fo2.rsf SH=Fo3.rsf ns=301 dt=0.001 bd=20''','''* Note: The z-components of pure-mode qSV-wave are zero.

Refernces:
Cheng et al. (15th IWSA, 2012);
Cheng and Kang (SEG Abstract, 2012);
Kang and Cheng (SEG Abstract, 2012)
Wang et al.(SEG Abstract, 2012)

Copyright (C) 2012 Tongji University, Shanghai, China

Authors: Jiubing Cheng, Tengfei Wang and Wei Kang

This code is first written by Tengfei Wang at Tongji University,
and then optimzied by Jiubing Cheng for Madagascar version at BEG,
University of Texas at Austin.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
''')
rsf.doc.progs['sfvti3dpseudosh']=sfvti3dpseudosh

sfvti3dpseudosv = rsf.doc.rsfprog('sfvti3dpseudosv','user/chengjb/Mvti3dpseudosv.c','''3-D three-components wavefield modeling using pseudo-pure mode SV-wave equation in 3D VTI media.''')
sfvti3dpseudosv.par('vs0',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti3dpseudosv.par('epsi',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti3dpseudosv.par('del',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti3dpseudosv.par('PseudoPureSVz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti3dpseudosv.par('PseudoPureSV',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti3dpseudosv.par('ns',rsf.doc.rsfpar('int','301','',''''''))
sfvti3dpseudosv.par('dt',rsf.doc.rsfpar('float','0.001','',''''''))
sfvti3dpseudosv.par('bd',rsf.doc.rsfpar('int','20','',''''''))
sfvti3dpseudosv.version('2.1-git')
sfvti3dpseudosv.synopsis('''sfvti3dpseudosv < Fvp0.rsf vs0=Fvs0.rsf epsi=Fep.rsf del=Fde.rsf > Fo1.rsf PseudoPureSVz=Fo2.rsf PseudoPureSV=Fo3.rsf ns=301 dt=0.001 bd=20''','''* Note: The x- and y-components of pseudo-pure-mode qSV-wave are summed thus the
* 2nd-order system only consist of two equations.

Refernces:
Cheng et al. (15th IWSA, 2012);
Cheng and Kang (SEG Abstract, 2012);
Kang and Cheng (SEG Abstract, 2012)
Wang et al.(SEG Abstract, 2012)

Copyright (C) 2012 Tongji University, Shanghai, China

Authors: Jiubing Cheng, Tengfei Wang and Wei Kang

This code is first written by Tengfei Wang at Tongji University,
and then optimzied by Jiubing Cheng for Madagascar version at BEG,
University of Texas at Austin.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
''')
rsf.doc.progs['sfvti3dpseudosv']=sfvti3dpseudosv

sftwolayer3dort = rsf.doc.rsfprog('sftwolayer3dort','user/chengjb/Mtwolayer3dort.c','''3-D three-components wavefield modeling using general anisotropy''')
sftwolayer3dort.par('vs0',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftwolayer3dort.par('eps1',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftwolayer3dort.par('eps2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftwolayer3dort.par('del1',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftwolayer3dort.par('del2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftwolayer3dort.par('del3',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftwolayer3dort.par('gam1',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftwolayer3dort.par('gam2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftwolayer3dort.par('the',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftwolayer3dort.par('phi',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftwolayer3dort.par('ny',rsf.doc.rsfpar('int','201','',''''''))
sftwolayer3dort.par('nx',rsf.doc.rsfpar('int','201','',''''''))
sftwolayer3dort.par('nz',rsf.doc.rsfpar('int','201','',''''''))
sftwolayer3dort.par('dy',rsf.doc.rsfpar('float','0.008','',''''''))
sftwolayer3dort.par('dx',rsf.doc.rsfpar('float','0.008','',''''''))
sftwolayer3dort.par('dz',rsf.doc.rsfpar('float','0.008','',''''''))
sftwolayer3dort.par('vp0_1',rsf.doc.rsfpar('float','3000.0','',''''''))
sftwolayer3dort.par('vs0_1',rsf.doc.rsfpar('float','1200.0','',''''''))
sftwolayer3dort.par('eps1_1',rsf.doc.rsfpar('float','0.2','',''''''))
sftwolayer3dort.par('eps2_1',rsf.doc.rsfpar('float','0.2','',''''''))
sftwolayer3dort.par('del1_1',rsf.doc.rsfpar('float','0.1','',''''''))
sftwolayer3dort.par('del2_1',rsf.doc.rsfpar('float','0.1','',''''''))
sftwolayer3dort.par('del3_1',rsf.doc.rsfpar('float','0.1','',''''''))
sftwolayer3dort.par('gam1_1',rsf.doc.rsfpar('float','0.0','',''''''))
sftwolayer3dort.par('gam2_1',rsf.doc.rsfpar('float','0.0','',''''''))
sftwolayer3dort.par('the_1',rsf.doc.rsfpar('float','0.0','',''''''))
sftwolayer3dort.par('phi_1',rsf.doc.rsfpar('float','0.0','',''''''))
sftwolayer3dort.par('vp0_2',rsf.doc.rsfpar('float','3000.0','',''''''))
sftwolayer3dort.par('vs0_2',rsf.doc.rsfpar('float','1200.0','',''''''))
sftwolayer3dort.par('eps1_2',rsf.doc.rsfpar('float','0.2','',''''''))
sftwolayer3dort.par('eps2_2',rsf.doc.rsfpar('float','0.2','',''''''))
sftwolayer3dort.par('del1_2',rsf.doc.rsfpar('float','0.1','',''''''))
sftwolayer3dort.par('del2_2',rsf.doc.rsfpar('float','0.1','',''''''))
sftwolayer3dort.par('del3_2',rsf.doc.rsfpar('float','0.1','',''''''))
sftwolayer3dort.par('gam1_2',rsf.doc.rsfpar('float','0.0','',''''''))
sftwolayer3dort.par('gam2_2',rsf.doc.rsfpar('float','0.0','',''''''))
sftwolayer3dort.par('the_2',rsf.doc.rsfpar('float','30.0','',''''''))
sftwolayer3dort.par('phi_2',rsf.doc.rsfpar('float','0.0','',''''''))
sftwolayer3dort.version('2.1-git')
sftwolayer3dort.synopsis('''sftwolayer3dort > Fo1.rsf vs0=Fo2.rsf eps1=Fo3.rsf eps2=Fo4.rsf del1=Fo5.rsf del2=Fo6.rsf del3=Fo7.rsf gam1=Fo8.rsf gam2=Fo9.rsf the=Fo10.rsf phi=Fo11.rsf ny=201 nx=201 nz=201 dy=0.008 dx=0.008 dz=0.008 vp0_1=3000.0 vs0_1=1200.0 eps1_1=0.2 eps2_1=0.2 del1_1=0.1 del2_1=0.1 del3_1=0.1 gam1_1=0.0 gam2_1=0.0 the_1=0.0 phi_1=0.0 vp0_2=3000.0 vs0_2=1200.0 eps1_2=0.2 eps2_2=0.2 del1_2=0.1 del2_2=0.1 del3_2=0.1 gam1_2=0.0 gam2_2=0.0 the_2=30.0 phi_2=0.0''','''elastic equation in ort media.
Copyright (C) 2015 Tongji University, Shanghai, China 
Authors: Jiubing Cheng and Peng Zou

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
''')
rsf.doc.progs['sftwolayer3dort']=sftwolayer3dort

sfresamp = rsf.doc.rsfprog('sfresamp','user/chengjb/Mresamp.c','''2D data resampling. ''')
sfresamp.par('o1',rsf.doc.rsfpar('float','o[0]','','''first sample sample on 1st axis '''))
sfresamp.par('d1',rsf.doc.rsfpar('float','d[0]','','''sample interval on 1st axis '''))
sfresamp.par('o2',rsf.doc.rsfpar('float','o[1]','','''first sample on 2nd axis '''))
sfresamp.par('d2',rsf.doc.rsfpar('float','d[1]','','''sample interval on 2nd axis '''))
sfresamp.version('2.1-git')
sfresamp.synopsis('''sfresamp < in.rsf > out.rsf o1=o[0] d1=d[0] o2=o[1] d2=d[1]''','''''')
rsf.doc.progs['sfresamp']=sfresamp

sfort3de = rsf.doc.rsfprog('sfort3de','user/chengjb/Mort3de.c','''3-D three-components wavefield modeling using elastic wave equation in tilted ORT media.''')
sfort3de.par('vs0',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfort3de.par('epsi1',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfort3de.par('epsi2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfort3de.par('del1',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfort3de.par('del2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfort3de.par('del3',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfort3de.par('gam1',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfort3de.par('gam2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfort3de.par('the',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfort3de.par('the',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfort3de.par('phi',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfort3de.par('FDElasticy',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfort3de.par('FDElasticz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfort3de.par('ns',rsf.doc.rsfpar('int','301','',''''''))
sfort3de.par('dt',rsf.doc.rsfpar('float','0.001','',''''''))
sfort3de.version('2.1-git')
sfort3de.synopsis('''sfort3de < Fvp0.rsf vs0=Fvs0.rsf epsi1=Fep1.rsf epsi2=Fep2.rsf del1=Fde1.rsf del2=Fde2.rsf del3=Fde3.rsf gam1=Fga1.rsf gam2=Fga2.rsf the=Falpha.rsf the=Fthe.rsf phi=Fphi.rsf > Fo1.rsf FDElasticy=Fo2.rsf FDElasticz=Fo3.rsf ns=301 dt=0.001''','''
Copyright (C) 2012 Tongji University, Shanghai, China 

Authors: Jiubing Cheng and Tengfei Wang

This code is first written by Tengfei Wang at Tongji University,
and then optimzied by Jiubing Cheng for Madagascar version at BEG,
University of Texas at Austin.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
''')
rsf.doc.progs['sfort3de']=sfort3de

sftti2de = rsf.doc.rsfprog('sftti2de','user/chengjb/Mtti2de.c','''2-D two-components wavefield modeling using original elastic displacement wave equation in TTI media.''')
sftti2de.par('vs0',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti2de.par('epsi',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti2de.par('del',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti2de.par('the',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti2de.par('Elasticz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2de.par('ns',rsf.doc.rsfpar('int','301','',''''''))
sftti2de.par('dt',rsf.doc.rsfpar('float','0.001','',''''''))
sftti2de.version('2.1-git')
sftti2de.synopsis('''sftti2de < Fvp0.rsf vs0=Fvs0.rsf epsi=Feps.rsf del=Fdel.rsf the=Fthe.rsf > Fo1.rsf Elasticz=Fo2.rsf ns=301 dt=0.001''','''
Copyright (C) 2012 Tongji University, Shanghai, China 
Authors: Jiubing Cheng, Wei Kang and Tengfei Wang

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
''')
rsf.doc.progs['sftti2de']=sftti2de

sftti2delrdecomp = rsf.doc.rsfprog('sftti2delrdecomp','user/chengjb/Mtti2delrdecomp.cc','''None''')
sftti2delrdecomp.par('ElasticPx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdecomp.par('ElasticPz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdecomp.par('ElasticSVx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdecomp.par('ElasticSVz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdecomp.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sftti2delrdecomp.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sftti2delrdecomp.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sftti2delrdecomp.par('ns',rsf.doc.rsfpar('','','',''''''))
sftti2delrdecomp.par('dt',rsf.doc.rsfpar('','','',''''''))
sftti2delrdecomp.version('2.1-git')
sftti2delrdecomp.synopsis('''sftti2delrdecomp < vp0.rsf > Elasticx.rsf ElasticPx=ElasticPx.rsf ElasticPz=ElasticPz.rsf ElasticSVx=ElasticSVx.rsf ElasticSVz=ElasticSVz.rsf seed=time(NULL eps=1.e-6 npk=20 ns= dt=''','''''')
rsf.doc.progs['sftti2delrdecomp']=sftti2delrdecomp

sftti2delrdecomp2p = rsf.doc.rsfprog('sftti2delrdecomp2p','user/chengjb/Mtti2delrdecomp2p.cc','''None''')
sftti2delrdecomp2p.par('Errdecxp1',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdecomp2p.par('Errdecxp2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdecomp2p.par('Decompxp1',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdecomp2p.par('Decompxp2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdecomp2p.par('Errdecxzp1',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdecomp2p.par('Errdecxzp2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdecomp2p.par('Decompxzp1',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdecomp2p.par('Decompxzp2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdecomp2p.par('Errdeczp1',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdecomp2p.par('Errdeczp2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdecomp2p.par('Decompzp1',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdecomp2p.par('Decompzp2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdecomp2p.par('ElasticPx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdecomp2p.par('ElasticPz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdecomp2p.par('ElasticSVx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdecomp2p.par('ElasticSVz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdecomp2p.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sftti2delrdecomp2p.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sftti2delrdecomp2p.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sftti2delrdecomp2p.par('ns',rsf.doc.rsfpar('','','',''''''))
sftti2delrdecomp2p.par('dt',rsf.doc.rsfpar('','','',''''''))
sftti2delrdecomp2p.par('ireconstruct',rsf.doc.rsfpar('','','',''''''))
sftti2delrdecomp2p.par('xrec1',rsf.doc.rsfpar('','','',''''''))
sftti2delrdecomp2p.par('zrec1',rsf.doc.rsfpar('','','',''''''))
sftti2delrdecomp2p.par('xrec2',rsf.doc.rsfpar('','','',''''''))
sftti2delrdecomp2p.par('zrec2',rsf.doc.rsfpar('','','',''''''))
sftti2delrdecomp2p.version('2.1-git')
sftti2delrdecomp2p.synopsis('''sftti2delrdecomp2p < vp0.rsf Errdecxp1=Errdecxp1.rsf Errdecxp2=Errdecxp2.rsf Decompxp1=Decompxp1.rsf Decompxp2=Decompxp2.rsf Errdecxzp1=Errdecxzp1.rsf Errdecxzp2=Errdecxzp2.rsf Decompxzp1=Decompxzp1.rsf Decompxzp2=Decompxzp2.rsf Errdeczp1=Errdeczp1.rsf Errdeczp2=Errdeczp2.rsf Decompzp1=Decompzp1.rsf Decompzp2=Decompzp2.rsf > ElasticX.rsf ElasticPx=ElasticPx.rsf ElasticPz=ElasticPz.rsf ElasticSVx=ElasticSVx.rsf ElasticSVz=ElasticSVz.rsf seed=time(NULL eps=1.e-6 npk=20 ns= dt= ireconstruct= xrec1= zrec1= xrec2= zrec2=''','''''')
rsf.doc.progs['sftti2delrdecomp2p']=sftti2delrdecomp2p

sftti2delrsep = rsf.doc.rsfprog('sftti2delrsep','user/chengjb/Mtti2delrsep.cc','''None''')
sftti2delrsep.par('ElasticSepP',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrsep.par('ElasticSepSV',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrsep.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sftti2delrsep.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sftti2delrsep.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sftti2delrsep.par('ns',rsf.doc.rsfpar('','','',''''''))
sftti2delrsep.par('dt',rsf.doc.rsfpar('','','',''''''))
sftti2delrsep.version('2.1-git')
sftti2delrsep.synopsis('''sftti2delrsep < vp0.rsf > Elasticx.rsf ElasticSepP=ElasticSepP.rsf ElasticSepSV=ElasticSepSV.rsf seed=time(NULL eps=1.e-6 npk=20 ns= dt=''','''''')
rsf.doc.progs['sftti2delrsep']=sftti2delrsep

sftti2delrsep2p = rsf.doc.rsfprog('sftti2delrsep2p','user/chengjb/Mtti2delrsep2p.cc','''None''')
sftti2delrsep2p.par('Errpolxp1',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrsep2p.par('Errpolxp2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrsep2p.par('Polxp1',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrsep2p.par('Polxp2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrsep2p.par('Errpolzp1',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrsep2p.par('Errpolzp2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrsep2p.par('Polzp1',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrsep2p.par('Polzp2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrsep2p.par('ElasticSepP',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrsep2p.par('ElasticSepSV',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrsep2p.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sftti2delrsep2p.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sftti2delrsep2p.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sftti2delrsep2p.par('ns',rsf.doc.rsfpar('','','',''''''))
sftti2delrsep2p.par('dt',rsf.doc.rsfpar('','','',''''''))
sftti2delrsep2p.par('ireconstruct',rsf.doc.rsfpar('','','',''''''))
sftti2delrsep2p.par('xrec1',rsf.doc.rsfpar('','','',''''''))
sftti2delrsep2p.par('zrec1',rsf.doc.rsfpar('','','',''''''))
sftti2delrsep2p.par('xrec2',rsf.doc.rsfpar('','','',''''''))
sftti2delrsep2p.par('zrec2',rsf.doc.rsfpar('','','',''''''))
sftti2delrsep2p.version('2.1-git')
sftti2delrsep2p.synopsis('''sftti2delrsep2p < vp0.rsf Errpolxp1=Errpolxp1.rsf Errpolxp2=Errpolxp2.rsf Polxp1=Polxp1.rsf Polxp2=Polxp2.rsf Errpolzp1=Errpolzp1.rsf Errpolzp2=Errpolzp2.rsf Polzp1=Polzp1.rsf Polzp2=Polzp2.rsf > Elasticx.rsf ElasticSepP=ElasticSepP.rsf ElasticSepSV=ElasticSepSV.rsf seed=time(NULL eps=1.e-6 npk=20 ns= dt= ireconstruct= xrec1= zrec1= xrec2= zrec2=''','''''')
rsf.doc.progs['sftti2delrsep2p']=sftti2delrsep2p

sftti2dpseudoplrsep = rsf.doc.rsfprog('sftti2dpseudoplrsep','user/chengjb/Mtti2dpseudoplrsep.cc','''None''')
sftti2dpseudoplrsep.par('PseudoPureSepPx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2dpseudoplrsep.par('PseudoPureSepPz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2dpseudoplrsep.par('PseudoPureP',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2dpseudoplrsep.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sftti2dpseudoplrsep.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sftti2dpseudoplrsep.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sftti2dpseudoplrsep.par('ns',rsf.doc.rsfpar('','','',''''''))
sftti2dpseudoplrsep.par('dt',rsf.doc.rsfpar('','','',''''''))
sftti2dpseudoplrsep.version('2.1-git')
sftti2dpseudoplrsep.synopsis('''sftti2dpseudoplrsep < vp0.rsf > PseudoPurePx.rsf PseudoPureSepPx=PseudoPureSepPx.rsf PseudoPureSepPz=PseudoPureSepPz.rsf PseudoPureP=PseudoPureP.rsf seed=time(NULL eps=1.e-6 npk=20 ns= dt=''','''''')
rsf.doc.progs['sftti2dpseudoplrsep']=sftti2dpseudoplrsep

sftti3delrsepP = rsf.doc.rsfprog('sftti3delrsepP','user/chengjb/Mtti3delrsepP.cc','''None''')
sftti3delrsepP.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sftti3delrsepP.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sftti3delrsepP.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sftti3delrsepP.par('iflagvti',rsf.doc.rsfpar('','','',''''''))
sftti3delrsepP.version('2.1-git')
sftti3delrsepP.synopsis('''sftti3delrsepP < vp0.rsf seed=time(NULL eps=1.e-6 npk=20 iflagvti=''','''''')
rsf.doc.progs['sftti3delrsepP']=sftti3delrsepP

sftti3delrsepSH = rsf.doc.rsfprog('sftti3delrsepSH','user/chengjb/Mtti3delrsepSH.cc','''None''')
sftti3delrsepSH.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sftti3delrsepSH.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sftti3delrsepSH.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sftti3delrsepSH.par('iflagvti',rsf.doc.rsfpar('','','',''''''))
sftti3delrsepSH.version('2.1-git')
sftti3delrsepSH.synopsis('''sftti3delrsepSH < vp0.rsf seed=time(NULL eps=1.e-6 npk=20 iflagvti=''','''''')
rsf.doc.progs['sftti3delrsepSH']=sftti3delrsepSH

sftti3delrsepSV = rsf.doc.rsfprog('sftti3delrsepSV','user/chengjb/Mtti3delrsepSV.cc','''None''')
sftti3delrsepSV.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sftti3delrsepSV.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sftti3delrsepSV.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sftti3delrsepSV.par('iflagvti',rsf.doc.rsfpar('','','',''''''))
sftti3delrsepSV.version('2.1-git')
sftti3delrsepSV.synopsis('''sftti3delrsepSV < vp0.rsf seed=time(NULL eps=1.e-6 npk=20 iflagvti=''','''''')
rsf.doc.progs['sftti3delrsepSV']=sftti3delrsepSV

sfvti3delrsepP = rsf.doc.rsfprog('sfvti3delrsepP','user/chengjb/Mvti3delrsepP.cc','''None''')
sfvti3delrsepP.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfvti3delrsepP.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sfvti3delrsepP.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sfvti3delrsepP.version('2.1-git')
sfvti3delrsepP.synopsis('''sfvti3delrsepP < vp0.rsf seed=time(NULL eps=1.e-6 npk=20''','''''')
rsf.doc.progs['sfvti3delrsepP']=sfvti3delrsepP

sfvti3delrsepSH = rsf.doc.rsfprog('sfvti3delrsepSH','user/chengjb/Mvti3delrsepSH.cc','''None''')
sfvti3delrsepSH.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfvti3delrsepSH.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sfvti3delrsepSH.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sfvti3delrsepSH.version('2.1-git')
sfvti3delrsepSH.synopsis('''sfvti3delrsepSH < vp0.rsf seed=time(NULL eps=1.e-6 npk=20''','''''')
rsf.doc.progs['sfvti3delrsepSH']=sfvti3delrsepSH

sfvti3delrsepSV = rsf.doc.rsfprog('sfvti3delrsepSV','user/chengjb/Mvti3delrsepSV.cc','''None''')
sfvti3delrsepSV.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfvti3delrsepSV.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sfvti3delrsepSV.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sfvti3delrsepSV.version('2.1-git')
sfvti3delrsepSV.synopsis('''sfvti3delrsepSV < vp0.rsf seed=time(NULL eps=1.e-6 npk=20''','''''')
rsf.doc.progs['sfvti3delrsepSV']=sfvti3delrsepSV

sftti2dpseudosvlrsep = rsf.doc.rsfprog('sftti2dpseudosvlrsep','user/chengjb/Mtti2dpseudosvlrsep.cc','''None''')
sftti2dpseudosvlrsep.par('PseudoPureSepSVx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2dpseudosvlrsep.par('PseudoPureSepSVz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2dpseudosvlrsep.par('PseudoPureSV',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2dpseudosvlrsep.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sftti2dpseudosvlrsep.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sftti2dpseudosvlrsep.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sftti2dpseudosvlrsep.par('ns',rsf.doc.rsfpar('','','',''''''))
sftti2dpseudosvlrsep.par('dt',rsf.doc.rsfpar('','','',''''''))
sftti2dpseudosvlrsep.version('2.1-git')
sftti2dpseudosvlrsep.synopsis('''sftti2dpseudosvlrsep < vp0.rsf > PseudoPureSVx.rsf PseudoPureSepSVx=PseudoPureSepSVx.rsf PseudoPureSepSVz=PseudoPureSepSVz.rsf PseudoPureSV=PseudoPureSV.rsf seed=time(NULL eps=1.e-6 npk=20 ns= dt=''','''''')
rsf.doc.progs['sftti2dpseudosvlrsep']=sftti2dpseudosvlrsep

sftti2delr = rsf.doc.rsfprog('sftti2delr','user/chengjb/Mtti2delr.cc','''None''')
sftti2delr.par('Elasticz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delr.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sftti2delr.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sftti2delr.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sftti2delr.par('ns',rsf.doc.rsfpar('','','',''''''))
sftti2delr.par('dt',rsf.doc.rsfpar('','','',''''''))
sftti2delr.version('2.1-git')
sftti2delr.synopsis('''sftti2delr < vp0.rsf > Elasticx.rsf Elasticz=Elasticz.rsf seed=time(NULL eps=1.e-6 npk=20 ns= dt=''','''''')
rsf.doc.progs['sftti2delr']=sftti2delr

sftti2dekspacelr = rsf.doc.rsfprog('sftti2dekspacelr','user/chengjb/Mtti2dekspacelr.cc','''None''')
sftti2dekspacelr.par('Elasticz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2dekspacelr.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sftti2dekspacelr.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sftti2dekspacelr.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sftti2dekspacelr.par('ns',rsf.doc.rsfpar('','','',''''''))
sftti2dekspacelr.par('dt',rsf.doc.rsfpar('','','',''''''))
sftti2dekspacelr.version('2.1-git')
sftti2dekspacelr.synopsis('''sftti2dekspacelr < vp0.rsf > Elasticx.rsf Elasticz=Elasticz.rsf seed=time(NULL eps=1.e-6 npk=20 ns= dt=''','''''')
rsf.doc.progs['sftti2dekspacelr']=sftti2dekspacelr

sftti2dekspacelrsource = rsf.doc.rsfprog('sftti2dekspacelrsource','user/chengjb/Mtti2dekspacelrsource.cc','''None''')
sftti2dekspacelrsource.par('Elasticz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2dekspacelrsource.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sftti2dekspacelrsource.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sftti2dekspacelrsource.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sftti2dekspacelrsource.par('ns',rsf.doc.rsfpar('','','',''''''))
sftti2dekspacelrsource.par('dt',rsf.doc.rsfpar('','','',''''''))
sftti2dekspacelrsource.version('2.1-git')
sftti2dekspacelrsource.synopsis('''sftti2dekspacelrsource < vp0.rsf > Elasticx.rsf Elasticz=Elasticz.rsf seed=time(NULL eps=1.e-6 npk=20 ns= dt=''','''''')
rsf.doc.progs['sftti2dekspacelrsource']=sftti2dekspacelrsource

sftti2devectorlrsvd = rsf.doc.rsfprog('sftti2devectorlrsvd','user/chengjb/Mtti2devectorlrsvd.cc','''None''')
sftti2devectorlrsvd.par('Elasticz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2devectorlrsvd.par('ElasticPx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2devectorlrsvd.par('ElasticPz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2devectorlrsvd.par('ElasticSx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2devectorlrsvd.par('ElasticSz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2devectorlrsvd.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sftti2devectorlrsvd.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sftti2devectorlrsvd.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sftti2devectorlrsvd.par('ns',rsf.doc.rsfpar('','','',''''''))
sftti2devectorlrsvd.par('dt',rsf.doc.rsfpar('','','',''''''))
sftti2devectorlrsvd.version('2.1-git')
sftti2devectorlrsvd.synopsis('''sftti2devectorlrsvd < vp0.rsf > Elasticx.rsf Elasticz=Elasticz.rsf ElasticPx=ElasticPx.rsf ElasticPz=ElasticPz.rsf ElasticSx=ElasticSx.rsf ElasticSz=ElasticSz.rsf seed=time(NULL eps=1.e-6 npk=20 ns= dt=''','''''')
rsf.doc.progs['sftti2devectorlrsvd']=sftti2devectorlrsvd

sftti2delrdec = rsf.doc.rsfprog('sftti2delrdec','user/chengjb/Mtti2delrdec.cc','''None''')
sftti2delrdec.par('ElasticPx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdec.par('ElasticPz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdec.par('ElasticSx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdec.par('ElasticSz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdec.par('Orthog',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdec.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sftti2delrdec.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sftti2delrdec.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sftti2delrdec.version('2.1-git')
sftti2delrdec.synopsis('''sftti2delrdec < vp0.rsf ElasticPx=ElasticPx.rsf ElasticPz=ElasticPz.rsf ElasticSx=ElasticSx.rsf ElasticSz=ElasticSz.rsf Orthog=Orthog.rsf seed=time(NULL eps=1.e-6 npk=20''','''''')
rsf.doc.progs['sftti2delrdec']=sftti2delrdec

sftti2devectorlrsvd_double = rsf.doc.rsfprog('sftti2devectorlrsvd_double','user/chengjb/Mtti2devectorlrsvd_double.cc','''None''')
sftti2devectorlrsvd_double.par('Elasticz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2devectorlrsvd_double.par('ElasticPx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2devectorlrsvd_double.par('ElasticPz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2devectorlrsvd_double.par('ElasticSx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2devectorlrsvd_double.par('ElasticSz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2devectorlrsvd_double.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sftti2devectorlrsvd_double.par('eps',rsf.doc.rsfpar('','1.e-8','','''tolerance'''))
sftti2devectorlrsvd_double.par('npk',rsf.doc.rsfpar('','60','','''maximum rank'''))
sftti2devectorlrsvd_double.par('ns',rsf.doc.rsfpar('','','',''''''))
sftti2devectorlrsvd_double.par('dt',rsf.doc.rsfpar('','','',''''''))
sftti2devectorlrsvd_double.version('2.1-git')
sftti2devectorlrsvd_double.synopsis('''sftti2devectorlrsvd_double < vp0.rsf > Elasticx.rsf Elasticz=Elasticz.rsf ElasticPx=ElasticPx.rsf ElasticPz=ElasticPz.rsf ElasticSx=ElasticSx.rsf ElasticSz=ElasticSz.rsf seed=time(NULL eps=1.e-8 npk=60 ns= dt=''','''''')
rsf.doc.progs['sftti2devectorlrsvd_double']=sftti2devectorlrsvd_double

sftti2devectorlrsvdkspace_double = rsf.doc.rsfprog('sftti2devectorlrsvdkspace_double','user/chengjb/Mtti2devectorlrsvdkspace_double.cc','''None''')
sftti2devectorlrsvdkspace_double.par('Elasticz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2devectorlrsvdkspace_double.par('ElasticPx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2devectorlrsvdkspace_double.par('ElasticPz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2devectorlrsvdkspace_double.par('ElasticSx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2devectorlrsvdkspace_double.par('ElasticSz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2devectorlrsvdkspace_double.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sftti2devectorlrsvdkspace_double.par('eps',rsf.doc.rsfpar('','1.e-8','','''tolerance'''))
sftti2devectorlrsvdkspace_double.par('npk',rsf.doc.rsfpar('','60','','''maximum rank'''))
sftti2devectorlrsvdkspace_double.par('ns',rsf.doc.rsfpar('','','',''''''))
sftti2devectorlrsvdkspace_double.par('dt',rsf.doc.rsfpar('','','',''''''))
sftti2devectorlrsvdkspace_double.version('2.1-git')
sftti2devectorlrsvdkspace_double.synopsis('''sftti2devectorlrsvdkspace_double < vp0.rsf > Elasticx.rsf Elasticz=Elasticz.rsf ElasticPx=ElasticPx.rsf ElasticPz=ElasticPz.rsf ElasticSx=ElasticSx.rsf ElasticSz=ElasticSz.rsf seed=time(NULL eps=1.e-8 npk=60 ns= dt=''','''''')
rsf.doc.progs['sftti2devectorlrsvdkspace_double']=sftti2devectorlrsvdkspace_double

sftti2devectorlrsvdkspace_double_stiffness = rsf.doc.rsfprog('sftti2devectorlrsvdkspace_double_stiffness','user/chengjb/Mtti2devectorlrsvdkspace_double_stiffness.cc','''None''')
sftti2devectorlrsvdkspace_double_stiffness.par('Elasticz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2devectorlrsvdkspace_double_stiffness.par('ElasticPx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2devectorlrsvdkspace_double_stiffness.par('ElasticPz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2devectorlrsvdkspace_double_stiffness.par('ElasticSx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2devectorlrsvdkspace_double_stiffness.par('ElasticSz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2devectorlrsvdkspace_double_stiffness.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sftti2devectorlrsvdkspace_double_stiffness.par('eps',rsf.doc.rsfpar('','1.e-8','','''tolerance'''))
sftti2devectorlrsvdkspace_double_stiffness.par('npk',rsf.doc.rsfpar('','60','','''maximum rank'''))
sftti2devectorlrsvdkspace_double_stiffness.par('ns',rsf.doc.rsfpar('','','',''''''))
sftti2devectorlrsvdkspace_double_stiffness.par('dt',rsf.doc.rsfpar('','','',''''''))
sftti2devectorlrsvdkspace_double_stiffness.version('2.1-git')
sftti2devectorlrsvdkspace_double_stiffness.synopsis('''sftti2devectorlrsvdkspace_double_stiffness < vp0.rsf > Elasticx.rsf Elasticz=Elasticz.rsf ElasticPx=ElasticPx.rsf ElasticPz=ElasticPz.rsf ElasticSx=ElasticSx.rsf ElasticSz=ElasticSz.rsf seed=time(NULL eps=1.e-8 npk=60 ns= dt=''','''''')
rsf.doc.progs['sftti2devectorlrsvdkspace_double_stiffness']=sftti2devectorlrsvdkspace_double_stiffness

sfort3devectorlrkspace_double = rsf.doc.rsfprog('sfort3devectorlrkspace_double','user/chengjb/Mort3devectorlrkspace_double.cc','''None''')
sfort3devectorlrkspace_double.par('Elasticy',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfort3devectorlrkspace_double.par('Elasticz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfort3devectorlrkspace_double.par('ElasticPx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfort3devectorlrkspace_double.par('ElasticPy',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfort3devectorlrkspace_double.par('ElasticPz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfort3devectorlrkspace_double.par('ElasticSx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfort3devectorlrkspace_double.par('ElasticSy',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfort3devectorlrkspace_double.par('ElasticSz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfort3devectorlrkspace_double.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfort3devectorlrkspace_double.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sfort3devectorlrkspace_double.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sfort3devectorlrkspace_double.par('ns',rsf.doc.rsfpar('','','',''''''))
sfort3devectorlrkspace_double.par('dt',rsf.doc.rsfpar('','','',''''''))
sfort3devectorlrkspace_double.version('2.1-git')
sfort3devectorlrkspace_double.synopsis('''sfort3devectorlrkspace_double < vp0.rsf > Elasticx.rsf Elasticy=Elasticy.rsf Elasticz=Elasticz.rsf ElasticPx=ElasticPx.rsf ElasticPy=ElasticPy.rsf ElasticPz=ElasticPz.rsf ElasticSx=ElasticSx.rsf ElasticSy=ElasticSy.rsf ElasticSz=ElasticSz.rsf seed=time(NULL eps=1.e-6 npk=20 ns= dt=''','''''')
rsf.doc.progs['sfort3devectorlrkspace_double']=sfort3devectorlrkspace_double

