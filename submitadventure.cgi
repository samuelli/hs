#!/usr/bin/perl

use CGI qw/:all/;
use Data::Dumper;  
use CGI::Session;

print header;
my $name = param("name");
my $gender = param("gender");
my $email = param("email");
`echo $email >> adventureemails`;
my $hs = param("highschool");
my $emergencyname = param("emergencyname");
my $emergencynumber = param("emergencynumber");
my $experience = param("experience");
my $year = param("year");
my $laptop = param("laptop");
`echo "Hi $name,\n\nThank you for applying at UNSW High School Computing Club.\n\nYou will receive additional information in the coming days. Any queries can be sent to csesoc.compclub\@cse.unsw.edu.au.\n\nRegards,\nUNSW High School Computing Club\n" | mail -aFrom:csesoc.compclub\@cse.unsw.edu.au -s "Computing Club" $email`;

my $postData = "--post-data=\'entry.0.single=$name&entry.6.group=$gender&entry.2.single=$email&entry.3.group=$year&entry.4.single=$hs&entry.5.single=$emergencyname&entry.8.single=$emergencynumber&entry.9.single=$experience&entry.11.group=$laptop\'";
my $response = `wget -q $postData https://docs.google.com/spreadsheet/formResponse?formkey=dFlhMlI2djZuMy0xRjBFbTZjUjBESWc6MA&ifq`;
