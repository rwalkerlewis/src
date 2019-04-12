[sfmpicfftrtm]
Cat:    RSF/user/jsun
Desc:   Lowrank decomposition for 3-D isotropic wave propagation
DocCmd: sfmpicfftrtm | cat
Param:  cb   -   -  		abc strength
LDesc:  (defaults to: 1.0)
Param:  dabc   -   -  		absorbing boundary
LDesc:  (defaults to: false)
Param:  eps   -   -  		tolerance/accuracy
LDesc:  (defaults to: 1.e-4)
Param:  info   -   -  		verbosity of output info about revolve
LDesc:  (defaults to: 0)
Param:  jsnap   -   -  		snapshot interval
LDesc:  (defaults to: 100)
Param:  jump   -   -  		subsampling rate for lowrank decomposition
LDesc:  (defaults to: 1)
Param:  media   -   -  		media: 0-> iso, 1-> tti
LDesc:  (defaults to: 0)
Param:  migr   -   -  		adjoint(migration) flag
LDesc:  (defaults to: false)
Param:  mute   -   -  		mute first arrival (modeling or imaging)
LDesc:  (defaults to: false)
Param:  nb   -   -  		abc width
LDesc:  (defaults to: 0)
Param:  nbell   -   -  		source position z
LDesc:  (defaults to: 1)
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 20)
Param:  revolve_snaps   -   -  		maximum num of snapshots allowed to be saved
LDesc:  (defaults to: 64)
Param:  roll   -   -  		rolling v.s. fixed-spread acquisition geometry
LDesc:  (defaults to: false)
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)
Param:  sht_num   -   -  		shot number to process
LDesc:  (defaults to: sht_num_total)
Param:  sht_set   -   -  		starting shot index
LDesc:  (defaults to: 0)
Param:  sill   -   -  		source illumination for rtm
LDesc:  (defaults to: false)
Param:  snap   -   -  		output wavefield snapshots
LDesc:  (defaults to: false)
Param:  sou_t0   -   -  		source delay
LDesc:  (defaults to: 0.)
Param:  taper   -   -  		tapering interval for tti
LDesc:  (defaults to: 0)
Param:  thres   -   -  		tapering threshold for tti
LDesc:  (defaults to: 1)
Param:  vel_w   -   -  		water velocity
LDesc:  (defaults to: 1500.)
Param:  verb   -   -  		verbosity
LDesc:  (defaults to: false)

