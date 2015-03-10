#Author: Haggen So
#Last Modify Date: 19 March 2004
#Language: Perl v5.0

#Utility to join several files into one file
#e.g. 20 files into 1 file

#This program is licensed under General Public License (GPL)
#Please refers to http://www.fsf.org/licenses/gpl.txt
#Or http://www.slat.org/project/legal/GNU_GPL_Chinese 
#for Chinese Version

# Optimized for MSDOS only :P

$howmany=20;
for ($id=1;$id <173; $id+=$howmany) {
  $filename='j'.$id.'to'.($id+$howmany-1).'.txt';
  $temp = "copy $id.txt $filename";
  qx\$temp\;
  for ($i=1;$i<$howmany;$i++){
    $temp = 'type '.($id+$i).'.txt >> '.$filename;
    qx\$temp\;
  }
}