#
# Copyright (C) 1997 Ken MacLeod
# See the file COPYING for distribution terms.
#
# $Id: Quilt.pm,v 1.5 1997/12/07 01:02:51 ken Exp $
#

package Quilt;
use vars qw{$VERSION};

$VERSION = '0.05';

use Quilt::Objs;
use Quilt::Flow::Table;
use Quilt::DO::List;
use Quilt::DO::Struct;
use Quilt::HTML;

1;
