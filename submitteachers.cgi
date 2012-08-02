#!/usr/bin/perl

use CGI qw/:all/;
use Data::Dumper;  
use CGI::Session;

print header;
my $name = param("name");
my $email = param("email");
`echo $email >> teacheremails`;
my $hs = param("highschool");
my $city = param("city");
my $number = param("number");
`echo "Hi $name,\n\nThank you for registering your interest in UNSW High School Computing Club.\n\nAny queries you may have can be sent to csesoc.compclub\@cse.unsw.edu.au. Please do not reply to this email directly.\n\nRegards,\nUNSW High School Computing Club\n" | mail -aFrom:csesoc.compclub\@cse.unsw.edu.au -s "Computing Club" $email`;

my $postData = "--post-data=\'entry.0.single=$name&entry.1.single=$hs&entry.2.single=$number&entry.3.single=$email&entry.4.single=$city\'";
my $response = `wget -q $postData https://docs.google.com/spreadsheet/formResponse?formkey=dGVhb3E3ZkhhODRsRkFMbWJBT2JkWUE6MQ&ifq`;
