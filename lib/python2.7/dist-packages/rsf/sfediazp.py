import rsf.doc

sfderiv3 = rsf.doc.rsfprog('sfderiv3','user/ediazp/Mderiv3.c','''Second order derivative along axis''')
sfderiv3.par('axis',rsf.doc.rsfpar('int','1','',''''''))
sfderiv3.par('operator',rsf.doc.rsfpar('int','2','',''''''))
sfderiv3.version('2.1-git')
sfderiv3.synopsis('''sfderiv3 < in.rsf > out.rsf axis=1 operator=2''','''
int axis=[1] axis to differentiate

int operator=[2] 1 backward, 2 centered, 3 forward


''')
rsf.doc.progs['sfderiv3']=sfderiv3

sfdespike2ed = rsf.doc.rsfprog('sfdespike2-ed','user/ediazp/Mdespike2-ed.c','''Despike filter:''')
sfdespike2ed.par('window',rsf.doc.rsfpar('int','20','',''''''))
sfdespike2ed.par('sigma',rsf.doc.rsfpar('float','3.0','',''''''))
sfdespike2ed.version('2.1-git')
sfdespike2ed.synopsis('''sfdespike2-ed < in.rsf > out.rsf window=20 sigma=3.0''','''move outliers values to the tolerance
parameter.

Example:

if (a>3sigma) a=3sigma

outlier
* *              ^
*    *            |
*      *           |
*        *          *
****          * * * * *  *****



''')
rsf.doc.progs['sfdespike2-ed']=sfdespike2ed

sfdespike1ed = rsf.doc.rsfprog('sfdespike1-ed','user/ediazp/Mdespike1-ed.c','''Despike filter:''')
sfdespike1ed.par('window',rsf.doc.rsfpar('int','20','',''''''))
sfdespike1ed.par('sigma',rsf.doc.rsfpar('float','3.0','',''''''))
sfdespike1ed.version('2.1-git')
sfdespike1ed.synopsis('''sfdespike1-ed < in.rsf > out.rsf window=20 sigma=3.0''','''move outliers values to the tolerance
parameter. The mean is calculated with moving
windows 

Example:


if (a>3sigma) a=3sigma

outlier
* *              ^
*    *            |
*      *           |
*        *          *
****          * * * * *  *****



''')
rsf.doc.progs['sfdespike1-ed']=sfdespike1ed

sfvel1d = rsf.doc.rsfprog('sfvel1d','user/ediazp/Mvel1d.c','''Hungs a 1d velocity function from the Water bottom.''')
sfvel1d.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvel1d.par('wb',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvel1d.par('vel',rsf.doc.rsfpar('float','1.5','',''''''))
sfvel1d.version('2.1-git')
sfvel1d.synopsis('''sfvel1d < in.rsf mask=mask1.rsf > out.rsf wb=wbot.rsf vel=1.5''','''Should work for 2D models



stdin    1D velocity function to be used 
file mask [required]   The water bottom is read from the mask file.
1 above the WB
0 bellow the WB

stdout The output velocity model has dimensions of the mask file.
vel [1.5]    velocity to use above the horizon (usually water velocity) 





''')
rsf.doc.progs['sfvel1d']=sfvel1d

sfpicks2rsf = rsf.doc.rsfprog('sfpicks2rsf','user/ediazp/Mpicks2rsf.c','''Creates a mask from horizons:''')
sfpicks2rsf.par('ntic',rsf.doc.rsfpar('int','5','',''''''))
sfpicks2rsf.par('tmask',rsf.doc.rsfpar('bool','y','',''''''))
sfpicks2rsf.par('extend',rsf.doc.rsfpar('bool','n','',''''''))
sfpicks2rsf.par('above',rsf.doc.rsfpar('bool','n','',''''''))
sfpicks2rsf.par('picks',rsf.doc.rsfpar('string ',desc='''parameters from input file'''))
sfpicks2rsf.version('2.1-git')
sfpicks2rsf.synopsis('''sfpicks2rsf < in.rsf > out.rsf ntic=5 tmask=y extend=n above=n picks=''','''
horizon format:

x1 h1
x2 h2
x3 h3
x4 h4
.
.
.
xn hn



xn> ... >x4 >x3 >x2>x1

picks (file)  ascii file with two columns (x and h(x))
the x values must be increasing order,
you can easily achieve that by doing:

sort -k 1  unsorted_picks.txt > sorted_picks.txt

stdin             2D file from which the axes will be read
extend [false]    Extends picks to the boundaries of the axis
n Do not extend
y Extend to boundary

tmask [true]     write a mask (1 if z>h(x))
false     put a tic on the horizon

above [false] put 1 above the horizon
true   put 1 below the horizon

ntic [1]     works with tmask=false; put 1 around ntic grid points
above and below the horizon.   

stdout       It writes a file with the same dimensions as stdin 
with a mask function, 1 below the horizon 0 above 
''')
rsf.doc.progs['sfpicks2rsf']=sfpicks2rsf

sfconvkernel = rsf.doc.rsfprog('sfconvkernel','user/ediazp/Mconvkernel.c','''''')
sfconvkernel.par('filter',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfconvkernel.par('lag',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfconvkernel.par('lag2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfconvkernel.par('lag3',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfconvkernel.par('adj',rsf.doc.rsfpar('bool','n','',''''''))
sfconvkernel.par('n',rsf.doc.rsfpar('int','1','','''------------------------------------------------------------'''))
sfconvkernel.version('2.1-git')
sfconvkernel.synopsis('''sfconvkernel < Fin.rsf filter=Ffilter.rsf > Fout.rsf lag=Flag1.rsf lag2=Flag2.rsf lag3=Flag3.rsf adj=n n=1''','''Applies a 1,2, or 3D convolution kernel or its adjoint
The filter is composed by n coefficients.

example: 2d laplacian

1
1 -4  1
1 

filter: 1 1 -4 1 1
lag1 (vertical lag)  :  0  1  0  -1  0 
lag2 (horizontal lag): -1  0  0   0  1  

''')
rsf.doc.progs['sfconvkernel']=sfconvkernel

sfnderiv = rsf.doc.rsfprog('sfnderiv','user/ediazp/Mnderiv.py','''''')
sfnderiv.par('order',rsf.doc.rsfpar('int','1','','''order of the derivative, default first derivative'''))
sfnderiv.par('length',rsf.doc.rsfpar('int','5','','''filter length, the lengthier the accurate, but also gets costlier'''))
sfnderiv.par('scale',rsf.doc.rsfpar('bool','y','','''scales by 1/d^order'''))
sfnderiv.par('axis',rsf.doc.rsfpar('int','1','','''apply differentiator along axis, default is fast axis'''))
sfnderiv.version('2.1-git')
sfnderiv.synopsis('''sfnderiv < Fin.rsf > Fout.rsf order=1 length=5 scale=y axis=1''','''This program implements Fornberg, 1988
paper for digital differentiators
of arbitrary order.

So, it computes first, second, n derivative along axis 1,2 or 3.
''')
rsf.doc.progs['sfnderiv']=sfnderiv

sfnpyCorr = rsf.doc.rsfprog('sfnpyCorr','user/ediazp/MnpyCorr.py','''''')
sfnpyCorr.par('flt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnpyCorr.par('norm',rsf.doc.rsfpar('bool','n','','''normalize output'''))
sfnpyCorr.par('nc',rsf.doc.rsfpar('int','100','','''number of correlation lags'''))
sfnpyCorr.version('2.1-git')
sfnpyCorr.synopsis('''sfnpyCorr < Fa.rsf flt=Fb.rsf > Fc.rsf norm=n nc=100''','''Implements corr(a,b) along the fast axis 
a [file] : is taken from stdin
b [file] : is taken from  "flt"
Requires both files to have the same sampling interval
''')
rsf.doc.progs['sfnpyCorr']=sfnpyCorr

sfnpyConv = rsf.doc.rsfprog('sfnpyConv','user/ediazp/MnpyConv.py','''''')
sfnpyConv.par('flt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnpyConv.par('norm',rsf.doc.rsfpar('bool','n','','''normalize output'''))
sfnpyConv.par('mode',rsf.doc.rsfpar('string','same','',''''''))
sfnpyConv.version('2.1-git')
sfnpyConv.synopsis('''sfnpyConv < Fa.rsf flt=Fb.rsf > Fc.rsf norm=n mode=same''','''Implements conv(a,b) along the fast axis 
a [file] : is taken from stdin
b [file] : is taken from  "flt"
Requires both files to have the same sampling interval

mode [string]:
'full': returns an M+N-1 array, boundary effects are visible.
'same': returns a max(M,N) array, boundary effects are visible.
''')
rsf.doc.progs['sfnpyConv']=sfnpyConv

sfvelan = rsf.doc.rsfprog('sfvelan','user/ediazp/Mvelan.py','''font.size''')
sfvelan.par('cmp',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvelan.par('offset',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvelan.par('useoffset',rsf.doc.rsfpar('bool','y','','''if irregular offset, pass it'''))
sfvelan.par('half',rsf.doc.rsfpar('bool','y','','''half or full offset?'''))
sfvelan.version('2.1-git')
sfvelan.synopsis('''sfvelan < Fsemb.rsf cmp=Fcmp.rsf offset=Foff.rsf > Fout.rsf useoffset=y half=y''','''''')
rsf.doc.progs['sfvelan']=sfvelan

