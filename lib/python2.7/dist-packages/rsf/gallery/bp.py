from rsf.proj import *

velsegy = 'vel_z6.25m_x12.5m_exact.segy'
densegy = 'density_z6.25m_x12.5m.segy'

Fetch(velsegy+'.gz',dir='bpvelanal2004',
      server='https://s3.amazonaws.com',top='open.source.geoscience/open_data')
Flow(velsegy,velsegy+'.gz','gunzip -c $SOURCE',stdin=0)

Fetch(densegy+'.gz',dir='bpvelanal2004',
      server='https://s3.amazonaws.com',top='open.source.geoscience/open_data')
Flow(densegy,densegy+'.gz','gunzip -c $SOURCE',stdin=0)

def getdata(dat,segy,label,unit):
    Flow(dat,segy,
         '''
         segyread read=data |
         put label=%s unit=%s
         o1=0 d1=6.25 label1=Depth    unit1=m
         o2=0 d2=12.5 label2=Distance unit2=m
         ''' % (label,unit))

def getvel(vel):
    getdata(vel,velsegy,'Velocity','m/s')

def getden(den):
    getdata(den,densegy,'Density','')

shots = [
    'shots0001_0200',
    'shots0201_0400',
    'shots0401_0600',
    'shots0601_0800',
    'shots0801_1000',
    'shots1001_1200',
    'shots1201_1348'
    ]

for shot in shots:
    Fetch(shot+'.segy.gz',dir='bpvelanal2004',
          server='https://s3.amazonaws.com',
          top='open.source.geoscience/open_data')
    Flow(shot+'.segy',shot+'.segy.gz','gunzip -c $SOURCE',stdin=0)
    Flow([shot,'t-'+shot,shot+'.asc',shot+'.bin'],shot+'.segy',
         '''
         segyread tfile=${TARGETS[1]} hfile=${TARGETS[2]} bfile=${TARGETS[3]}
         ''')
Flow('bpshots',shots,'cat axis=2 ${SOURCES[1:%d]}' % len(shots))
Flow('tbpshots',map(lambda x: 't-'+x,shots),
     'cat axis=2 ${SOURCES[1:%d]}' % len(shots))

def getshots(data):
    Flow(data,'bpshots tbpshots',
         '''
         intbin head=${SOURCES[1]} xk=tracf yk=fldr |
         put label3=Shot   o3=0.05 d3=0.05   unit3=km
             label2=Offset o2=-15  d2=0.0125 unit2=km
         ''')

def zodata(zo):
    Flow(zo,'bpshots tbpshots',
         '''
         intbin head=${SOURCES[1]} xk=tracf yk=fldr |
         window n2=1 f2=-1 | cut max1=0.1 | 
         put label2=Distance o2=0.05 d2=0.05   unit2=km
         ''')
