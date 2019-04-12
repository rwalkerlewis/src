[sftahread]
Cat:    RSF/user/karl
Desc:   Read Trace And Header from separate files, combine, write to pipe
DocCmd: sftahread | cat
Port:   stdin  rsf r req 	RSF standard input (containing infile data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  headers string  -   -  		
LDesc:  
LDesc:       Trace header file name.  Default is the input data file
LDesc:       name, with the final .rsf changed to _hdr.rsf 
LDesc:    
Param:  input string  -   -  		
LDesc:  
LDesc:       Input file for traces amplitudes.  You can list a file here, has the 
LDesc:       input file name will be used to compute the name of the header files.
LDesc:  
LDesc:       The input trace amplitudes can also be read from standard input by
LDesc:       just supplying standard input and omitting this paramater,  This 
LDesc:       is useful it you wish to do sopme initial processing of the input
LDesc:       rsf file containing the trace amplitudes.  This is useful if you need 
LDesc:       to change input axis labels to use the makeheader=yes.
LDesc:    
Param:  makeheader enum-bool  -  n 		
LDesc:  
LDesc:       Option to load headers using the input file axis labels.  If axis 
LDesc:       label2 through label9 match a header key then that coordinate is
LDesc:       loaded to the traces header.  This can be used to load the source
LDesc:       coordinate to the sx header location.  This may require changing
LDesc:       the axis label because Madagascar axis labels are not the same as
LDesc:       segy trace headers.  for example axis 2 coordiante can be loaded in
LDesc:       sx trace header by:
LDesc:          <spike.rsf sfput label2=sx \
LDesc:             | sftahread headers=spike_hdr.rsf makeheader=y \ 
LDesc:             | sftahgethw key=sx >/dev/null
LDesc:   
Param:  verbose int  -  1 		
LDesc:  
LDesc:       flag to control amount of print
LDesc:       0 terse, 1 informative, 2 chatty, 3 debug
LDesc:    

