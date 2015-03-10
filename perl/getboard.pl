#Author: Haggen So
#Last Modify Date: 19 March 2004
#Language: Perl v5.0

#Utility to backup mypaper board

#This program is licensed under General Public License (GPL)
#Please refers to http://www.fsf.org/licenses/gpl.txt
#Or http://www.slat.org/project/legal/GNU_GPL_Chinese 
#for Chinese Version

$|++;       # Turn on autoflush
use 5.004;  # We will use "for my"

use HTTP::Request;
use LWP::UserAgent;
use URI::URL;   

my $userid ='adam888';
my $dest='http://mypaper.pchome.com.tw/board/index.htm?s_id='.$userid.'&Page=';
#my $proxy='http://proxy.rmit.edu.au:8080/';

my($Ua, $title);

sub ChkLink {
	($url, $id) = @_;

	print "$url, $id";
	#return 0;

#print $url,"\n";
	my $req = HTTP::Request->new (GET => $url);

	# Temporarily turn off warnings.  The bowels of LWP are returning
	# an obscure error here, which I don't know how to troubleshoot. 
	#
	$^W = 0;

        my $res = $Ua->simple_request($req,$id.'.htm');

	#my $res = $Ua->simple_request($req);
	#my $content = $res->content;

	$^W = 1;   # Turn warnings back on again

	if ($res->is_error()) {
		print "error in URL.\n";
		return 1;
	}

return 0;
}

srand();
# Set up a browser  
#
$Ua = LWP::UserAgent->new;
$Ua->agent("Mozilla (compatible: LWP $LWP::VERSION)");
$Ua->timeout(100);
#$Ua->proxy('http', $proxy);

for ($id=10;$id < 11; $id++) {
	ChkLink($dest.$id, $id);
}

