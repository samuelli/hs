#!/usr/bin/perl

use CGI qw/:all/;
use Data::Dumper;  
use CGI::Session;

print header;
my $email = param("email");
my $year = param("year");
my $experience = param("experience");
`echo "Someone registered to the no list." | mail -aFrom:no-reply\@cse.unsw.edu.au -s "Computing Club" csesoc.computerclub\@cse.unsw.edu.au`;

my $postData = "--post-data=\'entry.0.single=$email&entry.1.single=$year&entry.2.single=$experience\'";
my $response = `wget -q $postData https://docs.google.com/spreadsheet/formResponse?formkey=dG9HaFVZb1ItZ1lJVDUyOWdGeEM0alE6MQ&ifq`;
