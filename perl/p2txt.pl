#Author: Haggen So
#Last Modify Date: 19 March 2004
#Language: Perl v5.0

#Utility to convert mypaper html pages to text files

#This program is licensed under General Public License (GPL)
#Please refers to http://www.fsf.org/licenses/gpl.txt
#Or http://www.slat.org/project/legal/GNU_GPL_Chinese 
#for Chinese Version

sub convert {
  my ($id)=@_;
  open (board, $id.'.htm');
  open (out, ">$id.txt");
  $flag=0;
  while (<board>) {
    $curline=$_;
    if ($curline =~/\<\/table/ && $flag>0) {
      if ($flag==1) {
        $buffer=~/\xA6\x57\xA1\x47\s*\n\s+(\S+)\s/s;
        $name= "\n\nName\t$1\n";
        $buffer=~/mail\xA1\x47\s\<a\shref=\"mailto:(\S+)\"/s;
        $mail= "Mail\t$1\n";
      } else {
        $buffer=~s/\<br\s\/\>\n/\n/sg;
        $buffer=~s/\<BR\>/\n/sg;

        $buffer=~/\<!--\xAF\x64\xA8\xA5\s--\>\n\s+(.+)\<!--\xAF\x64\xA8\xA5\send--\>/s;
        $temp=$1;
        $temp=~s/\<FONT\ssize=\"-2\"\scolor=\"\#FFFFFF\">//;
        $temp=~s/\<\/FONT\>\s+$//;
        $message = "$temp\n";

        $buffer=~/\<!--\xA4\xE9\xB4\xC1\s--\>\n\s+--\s\n\s+(.+\d)\s+\--\s\<\/div/s;
        $temp=$1;
        $temp=~s/\s+/\x20/;
        $date="Date\t$temp\n";

        $buffer=~/\<!--homepage\s--\>\n\s+(.+)\s+<\/a>/s;
        $temp=$1;
        $temp=~s/\s+/\x20/;
        $url="URL\t$temp\n";

        print out $name;
        print out $date;
        print out $mail;
        print out $url;
        print out "\n".$message;
      }
      $flag=0;
    }
    if ($flag>0) {$buffer.=$curline;}
    if ($curline =~/F4FBFF/) {
      $flag=1;
      undef $buffer;
    }
    if ($curline =~/\<td class=\"tb2\"\>/) {
      $flag=2;
      undef $buffer;
    }
  }
}

for ($id=10;$id <11; $id++) {
	convert ($id);
}