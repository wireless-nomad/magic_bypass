# magic_bypass
Inject magic bytes into your scripts to bypass filters.

Extentions supported:

image: jpeg,png,gif,tiff

compression: rar,zip,7z,tar

video: mpg,mpeg

audio: mp3,midi

documents: ppt,doc,xls,msg

database: sqlitedb

other: xml,pdf,utf-8,ps,crx,dmg,dat,cab,wasm,swf,deb,pcap,rpm 

Linux web servers detect file types by the first few bytes(magic bytes).

By injecting false magic bytes into the file, this filtering mechanism will be bypassed.
Sometimes they will also check if the file extension they are looking for is also in the file name 
, so that will also be but in for good measure.

Other filtering mechanisms may be in place, therefore the bypass will be unsuccessful.
