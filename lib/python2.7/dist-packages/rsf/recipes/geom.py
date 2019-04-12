try:    from rsf.cluster import *
except: from rsf.proj    import *
import math,random

random.seed(1001)
def add(x,y): return x+y
def myid(n): return '_'+reduce(add,['%d'%random.randint(0,9) for i in range(n)])
        
# ------------------------------------------------------------
# point
def point2d(cc,xcoord,zcoord,custom,par):
    Flow(cc,None,
         '''
         spike nsp=2 mag=%g,%g n1=2 o1=0 d1=1 k1=1,2 | 
         put label1="" unit1="" n2=1 o2=0 d2=1
         '''%(xcoord,zcoord) +' '+ custom)
    
def point3d(cc,xcoord,ycoord,zcoord,custom,par):
    Flow(cc,None,
         '''
         spike nsp=3 mag=%g,%g,%g n1=3 o1=0 d1=1 k1=1,2,3 n2=1 n3=1 | 
         put label1="" unit1="" n2=1 o2=0 d2=1 n3=1 o3=0 d3=1
         '''%(xcoord,ycoord,zcoord) +' '+ custom)

# ------------------------------------------------------------
def zero2d(out,custom,par):
    Flow(out,None,
         '''
         spike nsp=1 mag=0 
         n1=%(nz)d o1=%(oz)g d1=%(dz)g label1=%(lz)s unit1=%(uz)s
         n2=%(nx)d o2=%(ox)g d2=%(dx)g label2=%(lx)s unit2=%(ux)s
         '''%par + ' ' + custom)

def zero3d(out,custom,par):
    Flow(out,None,
         '''
         spike nsp=1 mag=0 
         n1=%(nz)d o1=%(oz)g d1=%(dz)g label1=%(lz)s unit1=%(uz)s
         n2=%(nx)d o2=%(ox)g d2=%(dx)g label2=%(lx)s unit2=%(ux)s
         n3=%(ny)d o3=%(oy)g d3=%(dy)g label3=%(ly)s unit3=%(uy)s         
         '''%par + ' ' + custom)
         
# ------------------------------------------------------------
# make a box
def rectangle(cc,zmin,zmax,xmin,xmax,custom,par):
    M8R='$RSFROOT/bin/sf'
    DPT=os.environ.get('TMPDATAPATH',os.environ.get('DATAPATH'))

    ccx=cc+'x'+myid(16)
    ccz=cc+'z'+myid(16)

    Flow(cc,None,
         '''
         %sspike nsp=5 mag=%g,%g,%g,%g,%g n1=5 o1=0 d1=1 k1=1,2,3,4,5 |
         transp >%s datapath=%s/;
         '''%(M8R,zmin,zmax,zmax,zmin,zmin,ccz,DPT) +
         '''
         %sspike nsp=5 mag=%g,%g,%g,%g,%g n1=5 o1=0 d1=1 k1=1,2,3,4,5 |
         transp >%s datapath=%s/;
         '''%(M8R,xmin,xmin,xmax,xmax,xmin,ccx,DPT) +
         '''
         %scat axis=1 space=n %s %s >${TARGETS[0]};
         '''%(M8R,ccx,ccz) +
         '''
         %srm %s %s
         '''%(M8R,ccx,ccz),
         stdin=0,
         stdout=0
        )

# ------------------------------------------------------------
# make a circle
def circle(cc,xcenter,zcenter,radius,sampling,custom,par):
    M8R='$RSFROOT/bin/sf'
    DPT=os.environ.get('TMPDATAPATH',os.environ.get('DATAPATH'))
    
    ccx=cc+'x'+myid(16)
    ccz=cc+'z'+myid(16)

    deg2rad = math.pi/180
    
    Flow(cc,None,
         '''
         %smath n1=%d d1=%g o1=%g output="%g+%g*cos(%g*x1)" >%s datapath=%s/;
         '''%(M8R,sampling,360./sampling,0.,xcenter,radius,deg2rad,ccx,DPT) +
         '''
         %smath n1=%d d1=%g o1=%g output="%g-%g*sin(%g*x1)" >%s datapath=%s/;
         '''%(M8R,sampling,360./sampling,0.,zcenter,radius,deg2rad,ccz,DPT) +
         '''
         %scat axis=2 space=n %s %s |
         transp |
         put label1="" unit1="" label2="" unit2="" o1=0 d1=1 o2=0 d2=1 >${TARGETS[0]};
         '''%(M8R,ccx,ccz) +
         '''
         %srm %s %s
         '''%(M8R,ccx,ccz),
         stdin=0,
         stdout=0
        )

def sphere(cc,xcenter,ycenter,zcenter,radius,nlat,nlon,custom,par):
    M8R='$RSFROOT/bin/sf'
    DPT=os.environ.get('TMPDATAPATH',os.environ.get('DATAPATH'))
    
    ccx=cc+'x'+myid(16)
    ccy=cc+'y'+myid(16)
    ccz=cc+'z'+myid(16)

    deg2rad = math.pi/180
    
    Flow(cc,None,
         '''
         %smath n1=%d d1=%g o1=%g n2=%d d2=%g o2=%g output="%g+%g*cos(%g*x2)*cos(%g*x1)" >%s datapath=%s/;
         '''%(M8R,
              nlon,360./nlon,0.,
              nlat,180./nlat,-90.,
              xcenter,radius,deg2rad,deg2rad,ccx,DPT) +
         '''
         %smath n1=%d d1=%g o1=%g n2=%d d2=%g o2=%g output="%g+%g*cos(%g*x2)*sin(%g*x1)" >%s datapath=%s/;
         '''%(M8R,
              nlon,360./nlon,0.,
              nlat,180./nlat,-90.,
              ycenter,radius,deg2rad,deg2rad,ccy,DPT) +
         '''
         %smath n1=%d d1=%g o1=%g n2=%d d2=%g o2=%g output="%g+%g*sin(%g*x2)" >%s datapath=%s/;
         '''%(M8R,
              nlon,360./nlon,0.,
              nlat,180./nlat,-90.,
              zcenter,radius,deg2rad,ccz,DPT) +
         '''
         %scat axis=2 space=n %s %s %s |
         put n1=%d n2=3 |
         transp |
         put label1="" unit1="" label2="" unit2="" o1=0 d1=1 o2=0 d2=1 o3=0 d3=1 >${TARGETS[0]};
         '''%(M8R,ccx,ccy,ccz,nlat*nlon) +
         '''
         %srm %s %s %s
         '''%(M8R,ccx,ccy,ccz),
         stdin=0,
         stdout=0
        )
    
# ------------------------------------------------------------
# make an ellipse
def ellipse(cc,xcenter,zcenter,semiA,semiB,sampling,custom,par):
    M8R='$RSFROOT/bin/sf'
    DPT=os.environ.get('TMPDATAPATH',os.environ.get('DATAPATH'))
        
    ccr=cc+'r'+myid(16)
    ccx=cc+'x'+myid(16)
    ccz=cc+'z'+myid(16)

    Flow(cc,None,
         '''
         %smath n1=%d d1=%g o1=%g
         output="((%g)*(%g))/sqrt( ((%g)*cos(%g*x1/180))^2 + ((%g)*sin(%g*x1/180))^2 )"
         >%s datapath=%s/;
         '''%(M8R,sampling,360./sampling,0.,
              semiA,semiB,semiB,math.pi,semiA,math.pi,ccr,DPT) +
         '''
         %smath <%s output='"%g+input*cos(%g*x1/180)"' >%s datapath=%s/;
         '''%(M8R,ccr,xcenter,math.pi,ccx,DPT) +
         '''
         %smath <%s output='"%g+input*sin(%g*x1/180)"' >%s datapath=%s/;
         '''%(M8R,ccr,zcenter,math.pi,ccz,DPT) +
         '''
         %scat axis=2 space=n %s %s |
         transp |
         put o1=0 d1=1 label1="" unit1="" label2="" unit2="" >${TARGETS[0]};
         '''%(M8R,ccx,ccz) +
         '''
         %srm %s %s %s
         '''%(M8R,ccr,ccx,ccz),
         stdin=0,
         stdout=0
        )

# ------------------------------------------------------------
def hsine2d(cc,base,ampl,peri,custom,par,jx=1):
    M8R='$RSFROOT/bin/sf'
    DPT=os.environ.get('TMPDATAPATH',os.environ.get('DATAPATH'))
   
    cco=cc+'o'+myid(16)
    ccz=cc+'z'+myid(16)
    ccx=cc+'x'+myid(16)
   
    Flow(cc,None,
         '''
         %smath output=0 n1=%d o1=%g d1=%g |
         window j1=%d >%s datapath=%s/;
         '''%(M8R,par['nx'],par['ox'],par['dx'],jx,cco,DPT) +
         '''
         %smath <%s output="%g+%g*sin(2*3.14*x1/%g)" >%s datapath=%s/;
         '''%(M8R,cco,base,ampl,peri,ccz,DPT) +
         '''
         %smath <%s output="x1" >%s datapath=%s/;
         '''%(M8R,cco,ccx,DPT) +
         '''
         %scat axis=2 space=n %s %s |
         transp |
         put o1=0 d1=1 label1="" unit1="" label2="" unit2="">${TARGETS[0]};
         '''%(M8R,ccx,ccz) +
         '''
         %srm %s %s %s
         '''%(M8R,cco,ccx,ccz),
              stdin=0,
              stdout=0)

# ------------------------------------------------------------
def horizontal2d(cc,zcoord,custom,par,jx=1,fx=0):
    M8R='$RSFROOT/bin/sf'
    DPT=os.environ.get('TMPDATAPATH',os.environ.get('DATAPATH'))
    
    cco=cc+'o'+myid(16)
    ccz=cc+'z'+myid(16)
    ccx=cc+'x'+myid(16)

    nx=(par['nx']-fx-1)/jx+1
        
    Flow(cc,None,
         '''
         %smath output=0 n1=%d o1=%g d1=%g |
         window f1=%d j1=%d n1=%d >%s datapath=%s/;
         '''%(M8R,
              par['nx'],par['ox'],par['dx'],
              fx,jx,nx,cco,DPT) +
         '''
         %smath <%s output="%g" >%s datapath=%s/;
         '''%(M8R,cco,zcoord,ccz,DPT) +
         '''
         %smath <%s output="x1" >%s datapath=%s/;
         '''%(M8R,cco,ccx,DPT) +
         '''
         %scat axis=2 space=n %s %s | 
         transp | 
         put o1=0 d1=1 label1="" unit1="" label2="" unit2="">${TARGETS[0]};
         '''%(M8R,ccx,ccz) +
         '''     
         %srm %s %s %s
         '''%(M8R,cco,ccx,ccz),
              stdin=0,
              stdout=0)

# ------------------------------------------------------------
def horizontal3d(cc,zcoord,custom,par,jx=1,jy=1,fx=0,fy=0):
    M8R='$RSFROOT/bin/sf'
    DPT=os.environ.get('TMPDATAPATH',os.environ.get('DATAPATH'))
    
    cco=cc+'o'+myid(16)
    ccz=cc+'z'+myid(16)
    ccy=cc+'y'+myid(16)
    ccx=cc+'x'+myid(16)

    nx=(par['nx']-fx-1)/jx+1
    ny=(par['ny']-fy-1)/jy+1
    
    Flow(cc,None,
         '''
         %smath output=0 n1=%d o1=%g d1=%g n2=%d o2=%g d2=%g |
         window f1=%d j1=%d n1=%d f2=%d j2=%d n2=%d >%s datapath=%s/;
         '''%(M8R,
              par['nx'],par['ox'],par['dx'],
              par['ny'],par['oy'],par['dy'],
              fx,jx,nx,fy,jy,ny,cco,DPT) +
         '''
         %smath <%s output="%g" | put n2=1 n1=%d >%s datapath=%s/;
         '''%(M8R,cco,zcoord,nx*ny,ccz,DPT) +
         '''
         %smath <%s output="x1" | put n2=1 n1=%d >%s datapath=%s/;
         '''%(M8R,cco,nx*ny,ccx,DPT) +
         '''
         %smath <%s output="x2" | put n2=1 n1=%d >%s datapath=%s/;
         '''%(M8R,cco,nx*ny,ccy,DPT) +
         '''
         %scat axis=2 space=n %s %s %s | 
         transp | 
         put o1=0 d1=1 o2=0 d2=1 label1="" unit1="" label2="" unit2="">${TARGETS[0]};
         '''%(M8R,ccx,ccy,ccz) +
         '''     
         %srm %s %s %s %s
         '''%(M8R,cco,ccx,ccy,ccz),
              stdin=0,
              stdout=0)
    
# constant x
def YZsheet3d(cc,xcoord,custom,par,jy=1,jz=1):
    M8R='$RSFROOT/bin/sf'
    DPT=os.environ.get('TMPDATAPATH',os.environ.get('DATAPATH'))
    
    cco=cc+'o'+myid(16)
    ccz=cc+'z'+myid(16)
    ccy=cc+'y'+myid(16)
    ccx=cc+'x'+myid(16)

    ny=(par['ny']-1)/jy+1
    nz=(par['nz']-1)/jz+1
    
    Flow(cc,None,
         '''
         %smath output=0 n1=%d o1=%g d1=%g n2=%d o2=%g d2=%g |
         window j1=%d n1=%d j2=%d n2=%d >%s datapath=%s/;
         '''%(M8R,
              par['ny'],par['oy'],par['dy'],
              par['nz'],par['oz'],par['dz'],
              jy,ny,jz,nz,cco,DPT) +
         '''
         %smath <%s output="%g" | put n2=1 n1=%d >%s datapath=%s/;
         '''%(M8R,cco,xcoord,ny*nz,ccx,DPT) +
         '''
         %smath <%s output="x1" | put n2=1 n1=%d >%s datapath=%s/;
         '''%(M8R,cco,ny*nz,ccy,DPT) +
         '''
         %smath <%s output="x2" | put n2=1 n1=%d >%s datapath=%s/;
         '''%(M8R,cco,ny*nz,ccz,DPT) +
         '''
         %scat axis=2 space=n %s %s %s | 
         transp | 
         put o1=0 d1=1 label1="" unit1="" label2="" unit2="">${TARGETS[0]};
         '''%(M8R,ccx,ccy,ccz) +
         '''     
         %srm %s %s %s %s
         '''%(M8R,cco,ccx,ccy,ccz),
              stdin=0,
              stdout=0)

# constant y
def ZXsheet3d(cc,ycoord,custom,par,jx=1,jz=1):
    M8R='$RSFROOT/bin/sf'
    DPT=os.environ.get('TMPDATAPATH',os.environ.get('DATAPATH'))
    
    cco=cc+'o'+myid(16)
    ccz=cc+'z'+myid(16)
    ccy=cc+'y'+myid(16)
    ccx=cc+'x'+myid(16)

    nx=(par['nx']-1)/jx+1
    nz=(par['nz']-1)/jz+1
    
    Flow(cc,None,
         '''
         %smath output=0 n1=%d o1=%g d1=%g n2=%d o2=%g d2=%g |
         window j1=%d n1=%d j2=%d n2=%d >%s datapath=%s/;
         '''%(M8R,
              par['nx'],par['ox'],par['dx'],
              par['nz'],par['oz'],par['dz'],
              jx,nx,jz,nz,cco,DPT) +
         '''
         %smath <%s output="%g" | put n2=1 n1=%d >%s datapath=%s/;
         '''%(M8R,cco,ycoord,nx*nz,ccy,DPT) +
         '''
         %smath <%s output="x1" | put n2=1 n1=%d >%s datapath=%s/;
         '''%(M8R,cco,nx*nz,ccx,DPT) +
         '''
         %smath <%s output="x2" | put n2=1 n1=%d >%s datapath=%s/;
         '''%(M8R,cco,nx*nz,ccz,DPT) +
         '''
         %scat axis=2 space=n %s %s %s | 
         transp | 
         put o1=0 d1=1 label1="" unit1="" label2="" unit2="">${TARGETS[0]};
         '''%(M8R,ccx,ccy,ccz) +
         '''     
         %srm %s %s %s %s
         '''%(M8R,cco,ccx,ccy,ccz),
              stdin=0,
              stdout=0)

# constant z
def XYsheet3d(cc,zcoord,custom,par,jx=1,jy=1):
    M8R='$RSFROOT/bin/sf'
    DPT=os.environ.get('TMPDATAPATH',os.environ.get('DATAPATH'))
    
    cco=cc+'o'+myid(16)
    ccz=cc+'z'+myid(16)
    ccy=cc+'y'+myid(16)
    ccx=cc+'x'+myid(16)

    nx=(par['nx']-1)/jx+1
    ny=(par['ny']-1)/jy+1
    
    Flow(cc,None,
         '''
         %smath output=0 n1=%d o1=%g d1=%g n2=%d o2=%g d2=%g |
         window j1=%d n1=%d j2=%d n2=%d >%s datapath=%s/;
         '''%(M8R,
              par['nx'],par['ox'],par['dx'],
              par['ny'],par['oy'],par['dy'],
              jx,nx,jy,ny,cco,DPT) +
         '''
         %smath <%s output="%g" | put n2=1 n1=%d >%s datapath=%s/;
         '''%(M8R,cco,zcoord,nx*ny,ccz,DPT) +
         '''
         %smath <%s output="x1" | put n2=1 n1=%d >%s datapath=%s/;
         '''%(M8R,cco,nx*ny,ccx,DPT) +
         '''
         %smath <%s output="x2" | put n2=1 n1=%d >%s datapath=%s/;
         '''%(M8R,cco,nx*ny,ccy,DPT) +
         '''
         %scat axis=2 space=n %s %s %s | 
         transp | 
         put o1=0 d1=1 label1="" unit1="" label2="" unit2="">${TARGETS[0]};
         '''%(M8R,ccx,ccy,ccz) +
         '''     
         %srm %s %s %s %s
         '''%(M8R,cco,ccx,ccy,ccz),
              stdin=0,
              stdout=0)
    
# ------------------------------------------------------------
def vertical2d(cc,xcoord,custom,par):
    M8R='$RSFROOT/bin/sf'
    DPT=os.environ.get('TMPDATAPATH',os.environ.get('DATAPATH'))
    
    cco=cc+'o'+myid(16)
    ccz=cc+'z'+myid(16)
    ccx=cc+'x'+myid(16)
    
    Flow(cc,None,
         '''
         %smath output=0 n1=%d o1=%g d1=%g >%s datapath=%s/;
         '''%(M8R,par['nz'],par['oz'],par['dz'],cco,DPT) +
         '''
         %smath <%s output="x1" >%s datapath=%s/;
         '''%(M8R,cco,ccz,DPT) +
         '''
         %smath <%s output="%g" >%s datapath=%s/;
         '''%(M8R,cco,xcoord,ccx,DPT) +
         '''
         %scat axis=2 space=n %s %s | 
         transp | 
         put o1=0 d1=1 label1="" unit1="" label2="" unit2="">${TARGETS[0]};
         '''%(M8R,ccx,ccz) +
         '''     
         %srm %s %s %s
         '''%(M8R,cco,ccx,ccz),
              stdin=0,
              stdout=0)

# ------------------------------------------------------------
def boxarray2d(cc,nz,oz,dz,nx,ox,dx,par):
    M8R='$RSFROOT/bin/sf'
    DPT=os.environ.get('TMPDATAPATH',os.environ.get('DATAPATH'))

    cco=cc+'o'+myid(16)
    ccz=cc+'z'+myid(16)
    ccx=cc+'x'+myid(16)

    Flow(cc,None,
         '''
         %smath output=1 n1=%d o1=%g d1=%g n2=%d o2=%g d2=%g >%s datapath=%s/;
         '''%(M8R,nz,oz,dz,nx,ox,dx,cco,DPT) +
         '''
         %smath <%s output="x1" | put n1=%d n2=1 >%s datapath=%s/;
         '''%(M8R,cco,nz*nx,ccz,DPT) +
         '''
         %smath <%s output="x2" | put n1=%d n2=1 >%s datapath=%s/;
         '''%(M8R,cco,nz*nx,ccx,DPT) +
         '''
         %scat axis=2 space=n %s %s | 
         transp | 
         put o1=0 d1=1 o2=0 d2=1 label1="" unit1="" label2="" unit2="">${TARGETS[0]};
         '''%(M8R,ccx,ccz) +
         '''     
         %srm %s %s %s
         '''%(M8R,cco,ccx,ccz),
              stdin=0,
              stdout=0)


def boxarray3d(cc,nz,oz,dz,nx,ox,dx,ny,oy,dy,par):
    M8R='$RSFROOT/bin/sf'
    DPT=os.environ.get('TMPDATAPATH',os.environ.get('DATAPATH'))

    cco=cc+'o'+myid(16)
    ccz=cc+'z'+myid(16)
    ccx=cc+'x'+myid(16)
    ccy=cc+'y'+myid(16)

    Flow(cc,None,
         '''
         %smath output=1 n1=%d o1=%g d1=%g n2=%d o2=%g d2=%g n3=%d o3=%g d3=%g >%s datapath=%s/;
         '''%(M8R,nz,oz,dz,nx,ox,dx,ny,oy,dy,cco,DPT) +
         '''
         %smath <%s output="x1" | put n1=%d n2=1 n3=1 >%s datapath=%s/;
         '''%(M8R,cco,nz*nx*ny,ccz,DPT) +
         '''
         %smath <%s output="x2" | put n1=%d n2=1 n3=1 >%s datapath=%s/;
         '''%(M8R,cco,nz*nx*ny,ccx,DPT) +
         '''
         %smath <%s output="x3" | put n1=%d n2=1 n3=1 >%s datapath=%s/;
         '''%(M8R,cco,nz*nx*ny,ccy,DPT) +
         '''
         %scat axis=2 space=n %s %s %s | 
         transp | 
         put o1=0 d1=1 o2=0 d2=1 o3=0 d3=1 label1="" unit1="" label2="" unit2="" label3="" unit3="" >${TARGETS[0]};
         '''%(M8R,ccx,ccz,ccy) +
         '''     
         %srm %s %s %s %s
         '''%(M8R,cco,ccx,ccy,ccz),
              stdin=0,
              stdout=0)

def segment2d(cc,
              ox,oz, # origin
              nx,nz, # normal
              ll,    # length
              n,     # sampling
              custom,par):
    M8R='$RSFROOT/bin/sf'
    DPT=os.environ.get('TMPDATAPATH',os.environ.get('DATAPATH'))

    cco=cc+'o'+myid(16)
    ccx=cc+'x'+myid(16)
    ccz=cc+'z'+myid(16)

    o=0
    d=1./n

    nn = math.sqrt(nx*nx + nz*nz);
    nx = nx / nn
    nz = nz / nn

    Flow(cc,None,
         '''
         %smath output="x1" n1=%d o1=%g d1=%g |
         scale rscale=%g >%s datapath=%s/;
         '''%(M8R,n,o,d,ll,cco,DPT) +
         '''
         %smath <%s output="%g+%g*input" >%s datapath=%s/;
         '''%(M8R,cco,ox,nx,ccx,DPT) +
         '''
         %smath <%s output="%g+%g*input" >%s datapath=%s/;
         '''%(M8R,cco,oz,nz,ccz,DPT) +
         '''
         %scat axis=2 space=n %s %s |
         transp |
         put o1=0 d1=1 label1="" unit1="" label2="" unit2="">${TARGETS[0]};
         '''%(M8R,ccx,ccz) +
         '''
         %srm %s %s %s
         '''%(M8R,cco,ccx,ccz),
              stdin=0,
              stdout=0)

def segment3d(cc,
            ox,oy,oz, # origin
            nx,ny,nz, # normal
            ll,       # length
            n,       # sampling
            custom,par):
    M8R='$RSFROOT/bin/sf'
    DPT=os.environ.get('TMPDATAPATH',os.environ.get('DATAPATH'))
    
    cco=cc+'o'+myid(16)
    ccx=cc+'x'+myid(16)
    ccy=cc+'y'+myid(16)
    ccz=cc+'z'+myid(16)

    o=0
    d=1./n

    nn = math.sqrt(nx*nx + ny*ny + nz*nz);
    nx = nx / nn
    ny = ny / nn
    nz = nz / nn
    
    Flow(cc,None,
         '''
         %smath output="x1" n1=%d o1=%g d1=%g |
         scale rscale=%g >%s datapath=%s/;
         '''%(M8R,n,o,d,ll,cco,DPT) +
         '''
         %smath <%s output="%g+%g*input" >%s datapath=%s/;
         '''%(M8R,cco,ox,nx,ccx,DPT) +
         '''
         %smath <%s output="%g+%g*input" >%s datapath=%s/;
         '''%(M8R,cco,oy,ny,ccy,DPT) +
         '''
         %smath <%s output="%g+%g*input" >%s datapath=%s/;
         '''%(M8R,cco,oz,nz,ccz,DPT) +
         '''
         %scat axis=2 space=n %s %s %s|
         transp |
         put o1=0 d1=1 label1="" unit1="" label2="" unit2="">${TARGETS[0]};
         '''%(M8R,ccx,ccy,ccz) +
         '''
         %srm %s %s %s %s
         '''%(M8R,cco,ccx,ccy,ccz),
              stdin=0,
              stdout=0)
