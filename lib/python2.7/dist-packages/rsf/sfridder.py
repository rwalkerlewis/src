import rsf.doc

sfspecfac = rsf.doc.rsfprog('sfspecfac','user/ridder/Mspecfac.f90','''(MD) Spectral Factorization or (MD) Autocorrelation using Helix Transform. ''')
sfspecfac.par('acfile',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfspecfac.version('2.1-git')
sfspecfac.synopsis('''sfspecfac < in.rsf > out.rsf acfile=acfile.rsf''','''(Maximum dimension is 3)
$  Copyright (C) 2009 Stanford University
$  
$  This program is free software; you can redistribute it and/or modify
$  it under the terms of the GNU General Public License as published by
$  the Free Software Foundation; either version 2 of the License, or
$  (at your option) any later version.
$  
$  This program is distributed in the hope that it will be useful,
$  but WITHOUT ANY WARRANTY; without even the implied warranty of
$  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
$  GNU General Public License for more details.
$  
$  You should have received a copy of the GNU General Public License
$  along with this program; if not, write to the Free Software
$  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA''')
rsf.doc.progs['sfspecfac']=sfspecfac

