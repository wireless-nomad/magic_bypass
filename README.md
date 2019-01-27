# magic_bypass
Inject magic bytes into your scripts to bypass filters

Extentions supported:
image: jpeg,png,gif,tiff 
compression: rar,zip,7z,tar 
video: mpg,mpeg 
audio: mp3,midi 
documents: ppt,doc,xls,msg 
database: sqlitedb 
other: xml,pdf,utf-8,ps,crx,dmg,dat,cab,wasm,swf,deb,pcap,rpm 

Linux webservers detect file types by the first few bytes(magic bytes)
Depending on the setup by injection a false magic bytes, hopefully we can by pass this.
Sometimes they will also check if the file they are looking for is also in the file name 
so that will also be but in for good measure.
