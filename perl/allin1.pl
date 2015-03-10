#Author: Haggen So
#Last Modify Date: 19 March 2004
#Language: Perl v5.0

#Utility to join multiple files into one file

#This program is licensed under General Public License (GPL)
#Please refers to http://www.fsf.org/licenses/gpl.txt
#Or http://www.slat.org/project/legal/GNU_GPL_Chinese 
#for Chinese Version

# Optimized for MSDOS only :P
$filename='allin1.txt';
$temp = "copy 1.txt $filename";
qx\$temp\;
for ($id=2;$id <173; $id++) {
  $temp = 'type '.$id.'.txt >> '.$filename;
  qx\$temp\;
}