#
# Copyright (C) 1997 Ken MacLeod
# See the file COPYING for distribution terms.
#
# $Id: Author.pm,v 1.1.1.1 1997/10/22 21:35:09 ken Exp $
#

#
# `Author' is based loosely on the `vCard' specification,
# http://www.versit.com/
#

use Quilt;

use strict;

package Quilt::DO::Author;

sub name {
    my ($self) = @_;

    if ($self->{'formatted_name'}) {
	return ($self->{'formatted_name'}->as_string);
    } elsif ($self->{'given_name'} || $self->{'family_name'}) {
	my (@names);
	push (@names, $self->{'given_name'}->as_string)
	    if ($self->{'givenname'});
	push (@names, $self->{'family_name'}->as_string)
	    if ($self->{'family_name'});
	return (join (" ", @names));
    } elsif ($self->{'other_name'}) {
	return ($self->{'other_name'}->as_string);
    } elsif ($self->{'content'}) {
	return ($self->as_string);
    }

    return undef;
}

sub address {
    my ($self) = @_;
    my ($str) = undef;

    $str .= $self->{'postoffice_address'}->as_string() . "\n"
	if (defined $self->{'postoffice_address'});

    $str .= $self->{'street'}->as_string() . "\n"
	if (defined $self->{'street'});

    my ($locality, $region, $postalcode);
    $locality = $self->{'locality'}->as_string
	if (defined $self->{'locality'});
    $region = $self->{'region'}->as_string
	if (defined $self->{'region'});
    $postalcode = $self->{'postal_code'}->as_string
	if (defined $self->{'postal_code'});

    $str .= $locality   if (defined $locality);
    $str .= ", "        if (defined $locality && defined $region);
    $str .= $region     if (defined $region);
    $str .= "  "        if (defined $locality || defined $region);
    $str .= $postalcode if (defined $postalcode);
    $str .= "\n"        if (defined $locality || defined $region
			    || defined $postalcode);

    $str .= $self->{'country'}->as_string() . "\n"
	if (defined $self->{'country'});

    return $str;
}

1;
