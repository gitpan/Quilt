#
# Copyright (C) 1997 Ken MacLeod
# See the file COPYING for distribution terms.
#
# $Id: XRef.pm,v 1.1 1997/12/07 01:02:51 ken Exp $
#

package Quilt::XRef;

use strict;
use vars qw{$singleton};

my $singleton = undef;

sub new {
    my ($type) = @_;

    return ($singleton)
	if (defined $singleton);

    my ($self) = {};

    bless ($self, $type);

    $singleton = $self;

    return $self;
}

sub visit_scalar {
}

sub visit_SGML_SData {
}

sub AUTOLOAD {
    my $self = shift;
    my $element = shift;
    return if !defined $element;
    my $context = shift;

    my $id;
    eval { $id = $element->id };

    if (defined $id) {
	$context->{'references'}{$id} = $element;
    }

    # XXX test specifically for undefined method
    eval {$element->children_accept ($self, $context, @_)};
}

1;
