Summary: Perl 5 module for transforming and formatting SGML/XML documents.
Name: Quilt
Version: @VERSION@
Release: 1
Source: ftp://ftp.uu.net/vendor/bitsko/gdo/Quilt-@VERSION@.tar.gz
Copyright: distributable
Group: Applications/Publishing/SGML
URL: http://www.bitsko.slc.ut.us/
Packager: ken@bitsko.slc.ut.us (Ken MacLeod)
BuildRoot: /tmp/Quilt

#
# $Id: Quilt.spec,v 1.2 1997/10/25 21:49:28 ken Exp $
#

%description
Quilt is a framework for loading SGML/XML documents or document
fragments, manipulating them in interesting ways, and displaying
or formatting them.

Quilt can also be used from code to generate document-like items
before formatting them -- tables for example.

There are specs for reading DocBook, LinuxDoc, and TEI Lite
documents, and formatters for plain Ascii and HTML (mostly 2.0).
There's a quick and dirty frontend script for formatting
documents.

%prep
%setup

perl Makefile.PL INSTALLDIRS=perl

%build

make

%install

make PREFIX="${RPM_ROOT_DIR}/usr" pure_install

%files

%doc README Changes test.pl

/usr/lib/perl5/Quilt.pm
/usr/lib/perl5/Quilt/DO/Document.pm
/usr/lib/perl5/Quilt/DO/Inline.pm
/usr/lib/perl5/Quilt/DO/Author.pm
/usr/lib/perl5/Quilt/DO/Struct.pm
/usr/lib/perl5/Quilt/DO/XRef.pm
/usr/lib/perl5/Quilt/DO/Block.pm
/usr/lib/perl5/Quilt/DO/List.pm
/usr/lib/perl5/Quilt/Writer/HTML.pm
/usr/lib/perl5/Quilt/Writer/Ascii.pm
/usr/lib/perl5/Quilt/Context.pm
/usr/lib/perl5/Quilt/HTML.pm
/usr/lib/perl5/Quilt/Flow/Inline.pm
/usr/lib/perl5/Quilt/Flow/Display.pm
/usr/lib/perl5/Quilt/Flow/Table.pm
