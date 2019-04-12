import rsf.doc

sfGridDeriv = rsf.doc.rsfprog('sfGridDeriv','trip/iwave/grid/main/GridDeriv.cc','''None''')
sfGridDeriv.version('2.1-git')
sfGridDeriv.synopsis('''sfGridDeriv''','''''')
rsf.doc.progs['sfGridDeriv']=sfGridDeriv

sfstandardmodel = rsf.doc.rsfprog('sfstandardmodel','trip/iwave/grid/main/standardmodel.cc','''None''')
sfstandardmodel.version('2.1-git')
sfstandardmodel.synopsis('''sfstandardmodel''','''''')
rsf.doc.progs['sfstandardmodel']=sfstandardmodel

sfstandardmodel_elastic = rsf.doc.rsfprog('sfstandardmodel_elastic','trip/iwave/grid/main/standardmodel_elastic.cc','''None''')
sfstandardmodel_elastic.version('2.1-git')
sfstandardmodel_elastic.synopsis('''sfstandardmodel_elastic''','''''')
rsf.doc.progs['sfstandardmodel_elastic']=sfstandardmodel_elastic

