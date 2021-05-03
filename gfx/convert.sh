#/bin/bash
for f in *.pdf; do 
 echo "Processing $f file.."; 
 pdf2svg $f $f.svg "all"
done
