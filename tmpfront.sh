use lib "/home/ken/src/SGML-SPGrove/blib/arch";
use lib "/home/ken/src/SGML-SPGrove/blib/lib";
use lib "lib";

$specs_dir = '/home/ken/src/Quilt/specs';

# XXX awaiting SPGrove classes using Class::Visitor
@SGML::SData::Iter::ISA = qw{Class::Iter};

use Getopt::Long;
use SGML::SPGrove;
use Quilt;
use Quilt::Writer::Ascii;
use Quilt::Writer::HTML;

use SGML::Simple::SpecBuilder;
use SGML::Simple::BuilderBuilder;

$| = 1;

$usage = "aack! don't grok!\n";
die "$usage" if !GetOptions("--html"         => \$to_html,
			    "--ascii"        => \$to_ascii,
			    "--linuxdoc"     => \$linuxdoc,
			    "--docbook"      => \$docbook,
			    "--teilite"      => \$teilite,
			    "--debug"        => sub { $debug ++ },
			    "--help"         => \&help,
			    "--version"      => \&version);

$debug && do {$time = localtime; warn "$time  -- loaded\n"};

my $doc_builder;
$linuxdoc && do {$doc_builder = spec_builder("$specs_dir/linuxdoc.spec")};
$docbook  && do {$doc_builder = spec_builder("$specs_dir/docbook.spec")};
$teilite  && do {$doc_builder = spec_builder("$specs_dir/teilite.spec")};
if ($to_ascii) {
    $to_ascii_builder = spec_builder("$specs_dir/toAscii.spec", 1);
    $wr_ascii_builder = spec_builder("$specs_dir/wrAscii.spec", 1);
}
if ($to_html) {
    $to_html_builder = spec_builder("$specs_dir/toHTML.spec", 1);
    $wr_html_builder = spec_builder("$specs_dir/wrHTML.spec", 1);
}
my $doc_builder_inst = $doc_builder->new;

my $doc_ot = load_doc ($ARGV[0], $doc_builder_inst);

if ($to_ascii) {
    $fot = Quilt::Flow->new();
    $fot_b = $to_ascii_builder->new;
    $doc_ot->iter->accept ($fot_b, $fot, {});
    $debug && do {$time = localtime; warn "$time  -- doc - build fot\n"};
    $out_b = $wr_ascii_builder->new;
    $fot->iter->accept ($out_b, Quilt::Writer::Ascii->new, {});
}
if ($to_html) {
    $fot = Quilt::Flow->new();
    $fot_b = $to_html_builder->new;
    $doc_ot->iter->accept ($fot_b, $fot, {});
    $debug && do {$time = localtime; warn "$time  -- doc - build fot\n"};
    $out_b = $wr_html_builder->new;
    $fot->iter->accept ($out_b, Quilt::Writer::HTML->new, {});
}

exit (0);

sub spec_builder {
    my $spec_file = shift;
    my $no_gi = shift;

    my $base_name = $spec_file;
    $base_name =~ s|.*/||;

    my $spec_grove = SGML::SPGrove->new ("$spec_file");
    $debug && do {my $time = localtime; warn "$time  -- $base_name - loaded\n"};
    my $spec = SGML::Simple::Spec->new;
    $spec_grove->accept (SGML::Simple::SpecBuilder->new, $spec);
    $debug && do {$time = localtime; warn "$time  -- $base_name - build spec\n"};
    my $builder = SGML::Simple::BuilderBuilder->new (spec => $spec, no_gi => $no_gi);
    $debug && do {$time = localtime; warn "$time  -- $base_name - build builder\n"};

    return ($builder);
}

sub load_doc {
    my $doc = shift;
    my $builder = shift;

    my $base_name = $doc;
    $base_name =~ s|.*/||;

    my $grove = SGML::SPGrove->new ($doc);
    $debug && do {$time = localtime; warn "$time  -- $base_name - loaded\n"};
    my $ot = Quilt::Flow->new();
    $grove->accept ($builder, $ot, {});
    $debug && do {$time = localtime; warn "$time  -- $base_name - build ot\n"};

    return $ot;
}

# XXX awaiting SPGrove classes using Class::Visitor
package SGML::Element;

package SGML::SData;
sub iter {
    my $iter = [@_];
    bless $iter, 'SGML::SData::Iter';
}

package SGML::PI;

package SGML::SData::Iter;

sub accept {
    my $self = shift; my $visitor = shift;

    $visitor->visit_SGML_SData ($self, @_);
}

sub data {
    my $self = shift;
    return ($self->[0]->data);
}
