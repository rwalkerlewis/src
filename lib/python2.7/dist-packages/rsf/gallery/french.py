from rsf.proj import *
import rsf.gallery 

method = rsf.gallery.method()

Fetch('french.asc','french')
Flow('french','french.asc','dd form=native | transp | scale dscale=2')

def get_refl(refl):
    Flow(refl,'french',
         '''
         remap1 n1=161 o1=0 d1=51.325 | transp |
         remap1 n1=161 o1=0 d1=51.325 | transp
         ''')

def get_zodata2d(data):
    refl = data+'-refl'

    get_refl(refl)
    refl2 = refl+'2'
    dipx2 = data+'-dip2'

    Flow(refl2,refl,'window n2=1 f2=80')
    Flow(dipx2,refl2,'smooth rect1=5 | deriv scale=y')

    Flow(data,[refl2,dipx2],
         '''
         kirmod nt=601 dt=0.010265 vel=2000
         dip=${SOURCES[1]} 
         s0=0 ds=51.325 ns=161 verb=y
         nh=1 h0=0 dh=51.325 |
         window |
         put label1=Time unit1=s
         label2=North-South unit2=m
         ''')
    
def get_zodata(data):
    refl = data+'-refl'
    dipx = data+'-dipx'
    dipy = data+'-dipy'

    get_refl(refl)
    Flow(dipx,refl,'smooth rect1=5 | deriv scale=y')
    Flow(dipy,refl,'transp | smooth rect1=5 | deriv scale=y | transp')


    Flow(data,[refl,dipx,dipy],
         '''
         kirmod3 nt=601 dt=0.010265 vel=2000
         dipx=${SOURCES[1]} dipy=${SOURCES[2]}
         s0x=0 dsx=51.325 nsx=161 verb=n
         s0y=0 dsy=51.325 nsy=161
         nhx=1 h0x=0 dhx=51.325
         nhy=1 h0y=0 dhy=51.325 freq=5 |
         window |
         put label1=Time unit1=s
         label2=North-South unit2=m
         label3=West-East   unit3=m 
         ''',split=[2,161],reduce='add')

def time_mig(image):
     Result(image,
            '''
            window max1=3 |
            byte gainpanel=all |
            grey3 title="%s" frame1=175 frame2=60 frame3=80
            screenratio=1
            ''' % method)

def depth_mig(image):
     Result(image,
            '''
            window max1=3000 |
            byte gainpanel=all |
            grey3 title="%s" frame1=175 frame2=60 frame3=80
            screenratio=1 label1=Depth unit1=m unit3=m
            ''' % method)
