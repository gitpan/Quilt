<!-- -*- sgml -*- -->
<!DOCTYPE spec PUBLIC "-//Ken MacLeod//DTD SPGrove Simple Spec//EN">
<spec>
  <head>
    <defaultobject>ick-none</defaultobject>
    <defaultprefix>Quilt</defaultprefix>
  <rules>
    <rule>
      <query/Quilt_DO_Document/
      <code><![CDATA[
my $self = shift; my $document = shift; my $parent = shift;
my $title = $document->title;
if (defined $title) {
    my $obj = new Quilt::HTML::Title (level => 1, quadding => 'center');
    $parent->push ($obj);
    $document->children_accept_title ($self, $obj, @_);
}
my $abstract = $document->abstract;
if (defined $abstract) {
    my $obj = new Quilt::HTML::Title (level => 3, quadding => 'center');
    $parent->push ($obj);
    $obj->push ("ABSTRACT");
    my $obj = new Quilt::Flow ();
    $parent->push ($obj);
    $document->children_accept_abstract ($self, $obj, @_);
}
$document->children_accept ($self, $parent, @_);
]]></code>

    <rule>
      <query/Quilt_Flow/ <holder>

    <rule>
      <query/Quilt_DO_Struct_Section/
      <code><![CDATA[ 
my $self = shift; my $section = shift; my $parent = shift;
# XXX div
my $title = $section->title;
if (defined $title) {
    my $obj = new Quilt::HTML::Title (level => $section->level);
    $parent->push ($obj);
    $obj->push (join (".", $section->numbers) . ".");
    $obj->push (new SGML::SData ('[nbsp  ]'));
    $obj->push (new SGML::SData ('[nbsp  ]'));
    $section->children_accept_title ($self, $obj, @_);
}
$section->children_accept ($self, $parent, @_);
]]></code>

    <rule>
      <query/Quilt_DO_Struct_Formal Quilt_DO_Struct_Admonition/
      <code><![CDATA[
my $self = shift; my $formal = shift; my $parent = shift;
my $title = $formal->title;
if (defined $title) {
    my $obj = new Quilt::HTML::Title (level => 4);
    $parent->push ($obj);
    $formal->children_accept_title ($self, $obj, @_);
}
$formal->children_accept ($self, $parent, @_);
]]></code>

    <rule>
      <query/Quilt_DO_Struct_Bridge/ <make/HTML::Title (level: 4, quadding: 'center');/

    <rule>
      <query/Quilt_DO_Block_Paragraph/ <make/Flow::Paragraph/

    <rule>
      <query/Quilt_DO_Block_Screen/
      <code><![CDATA[
my $self = shift; my $screen = shift; my $parent = shift;
$self->{quoting}++;
my ($obj) = new Quilt::HTML::Pre ();
$parent->push ($obj);
$screen->children_accept ($self, $obj, @_);
$self->{quoting}--;
]]></code>

    <rule>
      <query/Quilt_DO_Block_NoFill/ <make/HTML::NoFill/

    <rule>
      <query/Quilt_DO_List/
      <code><![CDATA[
my $self = shift; my $list = shift; my $parent = shift;
my $type = { 'itemized' => 'UL', 'ordered' => 'OL',
    'variable' => 'DL' }->{$list->type};
$type = 'UL' if !defined $type;
my $obj = new Quilt::HTML::List (type => $type, continued => $list->continued);
$parent->push ($obj);
$list->children_accept ($self, $obj, @_);
]]></code>

    <rule>
      <query/Quilt_DO_List_Item/ <make/HTML::List::Item/

    <rule>
      <query/Quilt_DO_List_Term/ <make/HTML::List::Term/

    <rule>
      <query/Quilt_DO_XRef_URL/
      <code><![CDATA[
my $self = shift; my $xref = shift; my $parent = shift;
my $url = $xref->url;
my $name = $xref->as_string;

if (!defined $url) {
    my $obj = new Quilt::HTML::Anchor (url => [$name]);
    $parent->push ($obj);
    if ($name =~ /^mailto:(.*)/) {
        $obj->push ($1);
    } else {
        $xref->children_accept ($self, $obj, @_);
    }
} elsif ($name eq "" || $name eq $url) {
    my $obj = new Quilt::HTML::Anchor (url => [$url]);
    $parent->push ($obj);
    $url =~ s/^mailto://;
    $obj->push ($url);
} else {
    my $obj = new Quilt::HTML::Anchor (url => [$url]);
    $parent->push ($obj);
    $xref->children_accept ($self, $obj, @_);
}
]]></code>

    <rule>
      <query/Quilt_DO_Inline_Quote/
      <code><![CDATA[
my $self = shift; my $quote = shift; my $parent = shift;
$self->{quoting}++ or $parent->push (new SGML::SData ('[ldquo ]'));
$quote->children_accept ($self, $parent, @_);
--$self->{quoting} or $parent->push (new SGML::SData ('[rdquo ]'));
]]></code>

    <rule>
      <query/Quilt_DO_Inline_Literal/
      <code><![CDATA[
my $self = shift; my $literal = shift; my $parent = shift;
$self->{quoting}++ or $parent->push (new SGML::SData ('[lsquo ]'));
my $obj = new Quilt::Flow (font_family_name => 'iso-monospace', inline => 1);
$parent->push ($obj);
$literal->children_accept ($self, $obj, @_);
--$self->{quoting} or $parent->push (new SGML::SData ('[rsquo ]'));
]]></code>

    <rule>
      <query/Quilt_DO_Inline_Replaceable/
      <code><![CDATA[
my $self = shift; my $replaceable = shift; my $parent = shift;
$self->{quoting}++ or $parent->push (new SGML::SData ('[lsquo ]'));
my $obj = new Quilt::Flow (font_posture => 'italic', inline => 1);
$parent->push ($obj);
$replaceable->children_accept ($self, $obj, @_);
--$self->{quoting} or $parent->push (new SGML::SData ('[rsquo ]'));
]]></code>

    <rule>
      <query/Quilt_DO_Inline_Emphasis/ <make/Flow (font_posture: 'italic', inline: 1)/

    <rule><query/Quilt_Flow_Table/ <code><![CDATA[
my $self = shift; my $table = shift; my $parent = shift;
my $obj = new Quilt::HTML::Table;
$parent->push ($obj);
my $ii;
my $parts = $table->delegate->parts;
for ($ii = 0; $ii <= $#$parts; $ii ++) {
    my $iter = $parts->[$ii]->iter ($table, $parts, $ii);
    $iter->children_accept ($self, $obj, @_);
}
]]></code>

    <rule><query/Quilt_Flow_Table_Part/      <make/HTML::Table/
    <rule><query/Quilt_Flow_Table_Row/  <make/HTML::Table::Row/
    <rule><query/Quilt_Flow_Table_Cell/ <make/HTML::Table::Data/

  <rule><query/scalar/
    <code><![CDATA[
my $self = shift; my $scalar = shift; my $parent = shift;
$scalar = $scalar->delegate;
$scalar =~ tr/\r/\n/;
$scalar =~ s/&/&amp;/g;
$scalar =~ s/</&lt;/g;
$parent->push ($scalar);
    ]]></code>

  <rule><query/SGML_SData/
    <code><![CDATA[
my $self = shift; my $sdata = shift; my $parent = shift;
$parent->push ($sdata->delegate);
    ]]></code>
  </rules>
</spec>
