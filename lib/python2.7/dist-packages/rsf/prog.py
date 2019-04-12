import sys, os

import rsf.doc

import rsf.sfplot
import rsf.sflibplot
import rsf.sfplplot
import rsf.sfpens
import rsf.sfsumain
import rsf.sfsuplot
import rsf.sfseismic
import rsf.sfmain
import rsf.sfgeneric
import rsf.sfcdacosta
import rsf.sfbrowaeys
import rsf.sfrweiss
import rsf.sfjun
import rsf.sfzdzhang
import rsf.sfslim
import rsf.sfsbader
import rsf.sfpfd
import rsf.sfxuxin
import rsf.sfmlai
import rsf.sfchenyk
import rsf.sfmccowan
import rsf.sffangg
import rsf.sfzhiguang
import rsf.sfjmonsegny
import rsf.sfjyan
import rsf.sfcwp
import rsf.sfdellinger
import rsf.sfpoulsonj
import rsf.sfkregimbal
import rsf.sfpyang
import rsf.sftsai
import rsf.sfjeff
import rsf.sfgee
import rsf.sffbroggin
import rsf.sfcram
import rsf.sftariq
import rsf.sfpsava
import rsf.sfeffsilva
import rsf.sfguojian
import rsf.sfivlad
import rsf.sfzgeng
import rsf.sfchen
import rsf.sfkourkina
import rsf.sfjsun
import rsf.sflcasasan
import rsf.sfhzhu
import rsf.sfparvaneh
import rsf.sfditthara
import rsf.sfgodwinj
import rsf.sfuwaheed
import rsf.sfzedong
import rsf.sfhpcss
import rsf.sfyunzhi
import rsf.sfediazp
import rsf.sfsongxl
import rsf.sfsalah
import rsf.sfhwang
import rsf.sfaklokov
import rsf.sfcuda
import rsf.sfkarl
import rsf.sfsgreer
import rsf.sfroman
import rsf.sfjingwei
import rsf.sfbash
import rsf.sfridder
import rsf.sfsaragiotis
import rsf.sffperrone
import rsf.sfsparse
import rsf.sfzone
import rsf.sfpwd
import rsf.sfmehdi
import rsf.sfchengjb
import rsf.sfharlan
import rsf.sfrlwalker
import rsf.sfjunyan
import rsf.sfllisiw
import rsf.sfpetsc
import rsf.sfluke
import rsf.sfdmerzlikin
import rsf.sfgchliu
import rsf.sflexing
import rsf.sfurdaneta
import rsf.sfseisinv
import rsf.sfrickettj
import rsf.sfjennings
import rsf.sfseplib_compat
import rsf.sfyliu
import rsf.sffomels
import rsf.sfbase
import rsf.sftrace
import rsf.sfgrid
import rsf.sfacd
import rsf.sfasg
import rsf.sfseq

import rsf.vpplot


try:
    import rsf.use
except:
    pass

RSFROOT="/home/raptor/rsfsrc"

def selfdoc():
    'Display man page'
    prognm = os.path.basename(sys.argv[0])
    if prognm[0] == 'M' and prognm[-3:] == '.py':
        # User testing code in his local directory
        prognm = 'sf' + prognm[1:-3]
        msg = 'Self-doc may be out of synch, do "scons install" in RSFSRC'
        sys.stderr.write(msg+'\n')

    prog = rsf.doc.progs.get(prognm)
    if prog != None:
        prog.document(25,RSFROOT)
    else:
        sys.stderr.write('No installed man page for ' + prognm+'\n')
