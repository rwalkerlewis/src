import rsf.doc

sfwarpscanw = rsf.doc.rsfprog('sfwarpscanw','user/sbader/Mwarpscanw.c','''Multicomponent data registration analysis. ''')
sfwarpscanw.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwarpscanw.par('renergy',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwarpscanw.par('denergy',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwarpscanw.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfwarpscanw.par('cheb',rsf.doc.rsfpar('bool','n','','''use Chebyshev scan '''))
sfwarpscanw.par('sign',rsf.doc.rsfpar('bool','n','','''use signed similarity '''))
sfwarpscanw.par('ren',rsf.doc.rsfpar('bool','n','','''use reference energy '''))
sfwarpscanw.par('den',rsf.doc.rsfpar('bool','n','','''use data energy '''))
sfwarpscanw.par('ng',rsf.doc.rsfpar('int','1','','''number of gamma values '''))
sfwarpscanw.par('g0',rsf.doc.rsfpar('float','','','''gamma origin '''))
sfwarpscanw.par('dg',rsf.doc.rsfpar('float','g0','','''gamma sampling '''))
sfwarpscanw.par('rect1',rsf.doc.rsfpar('int','1','','''vertical smoothing '''))
sfwarpscanw.par('rect2',rsf.doc.rsfpar('int','1','','''gamma smoothing '''))
sfwarpscanw.par('rect3',rsf.doc.rsfpar('int','1','','''in-line smoothing '''))
sfwarpscanw.par('rect4',rsf.doc.rsfpar('int','1','','''cross-line smoothing '''))
sfwarpscanw.par('niter',rsf.doc.rsfpar('int','10','','''number of iterations '''))
sfwarpscanw.par('shift',rsf.doc.rsfpar('bool','n','','''use shift instead of stretch '''))
sfwarpscanw.par('accuracy',rsf.doc.rsfpar('int','','[1-4]','''interpolation accuracy '''))
sfwarpscanw.version('2.1-git Mwarpscan.c 744 2004-08-17 18:46:07Z fomels')
sfwarpscanw.synopsis('''sfwarpscanw < in.rsf > warped.rsf other=other.rsf renergy=renergy.rsf denergy=denergy.rsf verb=y cheb=n sign=n ren=n den=n ng=1 g0= dg=g0 rect1=1 rect2=1 rect3=1 rect4=1 niter=10 shift=n accuracy=''','''''')
rsf.doc.progs['sfwarpscanw']=sfwarpscanw

sfbackusave = rsf.doc.rsfprog('sfbackusave','user/sbader/Mbackusave.py','''C-Wave Backus Averaging (See Marion et al., 1994)''')
sfbackusave.par('vel_bk',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfbackusave.par('slow_bk',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfbackusave.par('rhob_bk',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfbackusave.par('slowness',rsf.doc.rsfpar('string','','','''Slowness from Logs'''))
sfbackusave.par('density',rsf.doc.rsfpar('string','','','''Density from Logs'''))
sfbackusave.par('ratio',rsf.doc.rsfpar('float','','','''Percent of dom wavelength'''))
sfbackusave.par('peak_f',rsf.doc.rsfpar('float','','','''Dom wavelength'''))
sfbackusave.par('depthsample',rsf.doc.rsfpar('float','','','''Depth Sampling'''))
sfbackusave.version('2.1-git')
sfbackusave.synopsis('''sfbackusave < deptha.rsf < slowa.rsf < rhoba.rsf > depth_bkn.rsf vel_bk=vel_bkn.rsf slow_bk=slow_bkn.rsf rhob_bk=rhob_bkn.rsf slowness= density= ratio= peak_f= depthsample=''','''''')
rsf.doc.progs['sfbackusave']=sfbackusave

sfmqrbf = rsf.doc.rsfprog('sfmqrbf','user/sbader/Mmqrbf.py','''''')
sfmqrbf.par('xl',rsf.doc.rsfpar('int','','','''n2 location of source'''))
sfmqrbf.par('il',rsf.doc.rsfpar('int','','','''n3 location of source'''))
sfmqrbf.par('eps',rsf.doc.rsfpar('float','','','''Scalar factor'''))
sfmqrbf.par('boundary',rsf.doc.rsfpar('int','','','''Scalar factor'''))
sfmqrbf.par('other',rsf.doc.rsfpar('string','','','''Boundary map'''))
sfmqrbf.version('2.1-git')
sfmqrbf.synopsis('''sfmqrbf < cubea.rsf > rbf_out.rsf < othera.rsf xl= il= eps= boundary= other=''','''Inverse Multiquadratic Radial Basis Function

1/sqrt(1 + (eps*r)^2) where r is distance from source
''')
rsf.doc.progs['sfmqrbf']=sfmqrbf

sfsbclip1 = rsf.doc.rsfprog('sfsbclip1','user/sbader/Msbclip1.py','''''')
sfsbclip1.par('value',rsf.doc.rsfpar('float','','','''Output if log is less than clip'''))
sfsbclip1.par('clip',rsf.doc.rsfpar('float','','','''Clipping value'''))
sfsbclip1.version('2.1-git')
sfsbclip1.synopsis('''sfsbclip1 < logrefa.rsf > logref_co.rsf value= clip=''','''One-sided data clipping

Built for log data manipulation - remove extraneous values introduced from LSIM shifting
''')
rsf.doc.progs['sfsbclip1']=sfsbclip1

sfsbslice = rsf.doc.rsfprog('sfsbslice','user/sbader/Msbslice.py','''''')
sfsbslice.par('depth_c',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsbslice.par('log1_c',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsbslice.par('log2_c',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsbslice.par('log3_c',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsbslice.par('log4_c',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsbslice.par('log5_c',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsbslice.par('log6_c',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsbslice.par('depth',rsf.doc.rsfpar('string','','',''''''))
sfsbslice.par('log1',rsf.doc.rsfpar('string','','',''''''))
sfsbslice.par('log2',rsf.doc.rsfpar('string','','',''''''))
sfsbslice.par('log3',rsf.doc.rsfpar('string','','',''''''))
sfsbslice.par('log4',rsf.doc.rsfpar('string','','',''''''))
sfsbslice.par('log5',rsf.doc.rsfpar('string','','',''''''))
sfsbslice.par('log6',rsf.doc.rsfpar('string','','',''''''))
sfsbslice.version('2.1-git')
sfsbslice.synopsis('''sfsbslice < logrefa.rsf < deptha.rsf < log1a.rsf < log2a.rsf < log3a.rsf < log4a.rsf < log5a.rsf < log6a.rsf > logref_co.rsf depth_c=depth_co.rsf log1_c=log1_co.rsf log2_c=log2_co.rsf log3_c=log3_co.rsf log4_c=log4_co.rsf log5_c=log5_co.rsf log6_c=log6_co.rsf depth= log1= log2= log3= log4= log5= log6=''','''Multiple 1D inputs clipped to length of reference input

Built for log data manipulation - clips six input logs to the length of the reference well log
''')
rsf.doc.progs['sfsbslice']=sfsbslice

sfsbslice2 = rsf.doc.rsfprog('sfsbslice2','user/sbader/Msbslice2.py','''''')
sfsbslice2.par('depth_c',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsbslice2.par('log1_c',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsbslice2.par('log2_c',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsbslice2.par('log3_c',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsbslice2.par('log4_c',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsbslice2.par('depth',rsf.doc.rsfpar('string','','',''''''))
sfsbslice2.par('log1',rsf.doc.rsfpar('string','','',''''''))
sfsbslice2.par('log2',rsf.doc.rsfpar('string','','',''''''))
sfsbslice2.par('log3',rsf.doc.rsfpar('string','','',''''''))
sfsbslice2.par('log4',rsf.doc.rsfpar('string','','',''''''))
sfsbslice2.version('2.1-git')
sfsbslice2.synopsis('''sfsbslice2 < logrefa.rsf < deptha.rsf < log1a.rsf < log2a.rsf < log3a.rsf < log4a.rsf > logref_co.rsf depth_c=depth_co.rsf log1_c=log1_co.rsf log2_c=log2_co.rsf log3_c=log3_co.rsf log4_c=log4_co.rsf depth= log1= log2= log3= log4=''','''Multiple 1D inputs clipped to length of reference input

Built for log data manipulation - clips six input logs to the length of the reference well log
''')
rsf.doc.progs['sfsbslice2']=sfsbslice2

sfgenmask = rsf.doc.rsfprog('sfgenmask','user/sbader/Mgenmask.py','''beg''')
sfgenmask.par('beg',rsf.doc.rsfpar('int','','',''''''))
sfgenmask.par('end',rsf.doc.rsfpar('int','','',''''''))
sfgenmask.version('2.1-git')
sfgenmask.synopsis('''sfgenmask < dataa.rsf > log_eo.rsf beg= end=''','''''')
rsf.doc.progs['sfgenmask']=sfgenmask

sfconstraint = rsf.doc.rsfprog('sfconstraint','user/sbader/Mconstraint.py','''''')
sfconstraint.par('value',rsf.doc.rsfpar('float','','','''Location of hard constraint'''))
sfconstraint.par('wind',rsf.doc.rsfpar('int','','','''Number of samples of hard constraint'''))
sfconstraint.version('2.1-git')
sfconstraint.synopsis('''sfconstraint < logrefa.rsf > logref_co.rsf value= wind=''','''Hard constraint 2D map

For use with LSIM if a specific alignment location is desired.
Use with reference and real datasets and scale LSIM scan by output
''')
rsf.doc.progs['sfconstraint']=sfconstraint

sfenergy = rsf.doc.rsfprog('sfenergy','user/sbader/Menergy.py','''''')
sfenergy.par('wind',rsf.doc.rsfpar('int','','','''Rolling window size'''))
sfenergy.version('2.1-git')
sfenergy.synopsis('''sfenergy < input.rsf > log_eo.rsf wind=''','''Estimate energy of input

E(t) = \sum\limits_{k=(t-\frac{R}{2})}^{(t+\frac{R}{2})}A(k)^2
''')
rsf.doc.progs['sfenergy']=sfenergy

sfextend = rsf.doc.rsfprog('sfextend','user/sbader/Mextend.py','''''')
sfextend.par('switch',rsf.doc.rsfpar('int','','','''(0 = Two-sided axis extension by first and last non-zero sample in dataset); (2 = Two-sided axis reduction); (3 = Matches starting value and number of samples between input and reference well log); (else = pad data to dataset size by first and last nonzero sample); (4 = Testing)'''))
sfextend.par('val',rsf.doc.rsfpar('int','','','''Sample manipulation (switch=0/2)'''))
sfextend.par('reflog',rsf.doc.rsfpar('string','','','''Reference log (switch=3)'''))
sfextend.version('2.1-git')
sfextend.synopsis('''sfextend < loga.rsf > log_eo.rsf < refa.rsf switch= val= reflog=''','''Dataset padding/clipping

Built for log data manipulation - Before and after LSIM alignments to deal with edge-effects and extraneous values introduced from LSIM shifting
''')
rsf.doc.progs['sfextend']=sfextend

sfextend1 = rsf.doc.rsfprog('sfextend1','user/sbader/Mextend1.py','''''')
sfextend1.par('num',rsf.doc.rsfpar('int','','','''Number of samples'''))
sfextend1.version('2.1-git')
sfextend1.synopsis('''sfextend1 < loga.rsf > log_eo.rsf num=''','''Dataset padding - maintains dataset dims.

Pads dataset by first and last nonzero sample. This helps reduce artifacts introduced by PP well log interpolation.
''')
rsf.doc.progs['sfextend1']=sfextend1

sfinterp = rsf.doc.rsfprog('sfinterp','user/sbader/Minterp.py','''''')
sfinterp.version('2.1-git')
sfinterp.synopsis('''sfinterp < logrefa.rsf > logref_co.rsf''','''1D linear missing data interpolation

Linear interpolation of missing data (0 values) based on nearest nonzero samples
''')
rsf.doc.progs['sfinterp']=sfinterp

sflogzero = rsf.doc.rsfprog('sflogzero','user/sbader/Mlogzero.py','''''')
sflogzero.par('switch',rsf.doc.rsfpar('int','','',''''''))
sflogzero.version('2.1-git')
sflogzero.synopsis('''sflogzero < loga.rsf > log_eo.rsf switch=''','''1D dataset windowing

Built for log data manipulation - Clips padded values at the beginning and end of well log data to zero
''')
rsf.doc.progs['sflogzero']=sflogzero

sfrealign = rsf.doc.rsfprog('sfrealign','user/sbader/Mrealign.py','''''')
sfrealign.par('log1',rsf.doc.rsfpar('string','','',''''''))
sfrealign.version('2.1-git')
sfrealign.synopsis('''sfrealign < logrefa.rsf < log1a.rsf > log1_co.rsf log1=''','''Residual well log realignment

Built for log data manipulation - algined axis (o1/d1/n1) with reference well log
''')
rsf.doc.progs['sfrealign']=sfrealign

sfreplace = rsf.doc.rsfprog('sfreplace','user/sbader/Mreplace.py','''''')
sfreplace.par('loc',rsf.doc.rsfpar('int','','','''Location of value used to replace'''))
sfreplace.par('num',rsf.doc.rsfpar('int','','','''Number of values to replace at beginning of dataset'''))
sfreplace.version('2.1-git')
sfreplace.synopsis('''sfreplace < loga.rsf > log_eo.rsf loc= num=''','''1D dataset padding 

Built for time-depth relationship manipulation. LSIM scan/pick is smooth intoducing non-real updates at top of pick.
''')
rsf.doc.progs['sfreplace']=sfreplace

sftdr = rsf.doc.rsfprog('sftdr','user/sbader/Mtdr.py','''''')
sftdr.par('sonicFo',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftdr.par('ms',rsf.doc.rsfpar('int','','','''(0 = Units of sonic in s); (1 = Units of sonic in ms)'''))
sftdr.par('stretch',rsf.doc.rsfpar('float','','','''(0 = Output TDR from input sonic log); (1 = Output updated sonic and TDR)'''))
sftdr.par('dels',rsf.doc.rsfpar('float','','','''Depth step (units of m or ft)'''))
sftdr.par('tdrNew',rsf.doc.rsfpar('string','','',''''''))
sftdr.version('2.1-git')
sftdr.synopsis('''sftdr < sonica.rsf > tdrFo.rsf < tdrNewa.rsf sonicFo=sonicFo.rsf ms= stretch= dels= tdrNew=''','''Update sonic well log 

Use the initial sonic well log and an updated TDR to generate and updated sonic log and TDR
''')
rsf.doc.progs['sftdr']=sftdr

