#
# Copyright (C) 1997 Ken MacLeod
# See the file COPYING for distribution terms.
#
# $Id: HTML.pm,v 1.2 1997/10/24 18:54:11 ken Exp $
#

use Class::Visitor;

use strict;

visitor_class 'Quilt::HTML', 'Quilt', {};

visitor_class 'Quilt::HTML::Title', 'Quilt', {
    contents => '@',
    level => '$',
    quadding => '$',
};

visitor_class 'Quilt::HTML::Pre', 'Quilt::Flow', {};
visitor_class 'Quilt::HTML::NoFill', 'Quilt::Flow', {};
visitor_class 'Quilt::HTML::List', 'Quilt::Flow', {
    type => '$',
    continued => '$',
};
visitor_class 'Quilt::HTML::List::Item', 'Quilt::Flow', {};
visitor_class 'Quilt::HTML::List::Term', 'Quilt::Flow', {};
visitor_class 'Quilt::HTML::Anchor', 'Quilt::Flow', {
    url => '@',
};

visitor_class 'Quilt::HTML::Table', 'Quilt::Flow', {};
visitor_class 'Quilt::HTML::Table::Row', 'Quilt::Flow', {};
visitor_class 'Quilt::HTML::Table::Data', 'Quilt::Flow', {};

1;
