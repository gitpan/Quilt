<!-- -*- sgml -*- -->
<!DOCTYPE spec PUBLIC "-//Ken MacLeod//DTD SPGrove Simple Spec//EN">
<spec>
  <head>
    <defaultobject>ick-none</defaultobject>
    <defaultprefix>ick-none</defaultprefix>
  <rules>
    <rule>
      <query/Quilt_Flow/
      <code><![CDATA[
my $self = shift; my $flow = shift; my $context = shift;
my $inline = $flow->inline;
#if ($inline) {
#    $builder->push_inline ($node->attributes);
#} else {
#    $builder->push_display ($node->attributes);
#}
$flow->children_accept ($self, $context, @_);
#if ($inline) {
#    $builder->pop_inline;
#} else {
#    $builder->pop_display;
#}
]]></code>

    <rule>
      <query/Quilt_Flow_Paragraph/
      <code><![CDATA[ 
my $self = shift; my $paragraph = shift; my $context = shift;
print "<P>";
$paragraph->children_accept ($self, $context, @_);
print "</P>\n\n";
]]></code>

    <rule>
      <query/Quilt_HTML_Title/
      <code><![CDATA[
my $self = shift; my $title = shift; my $context = shift;
my $level = $title->level;
print "<H$level>";
$title->children_accept ($self, $context, @_);
print "</H$level>\n\n";
]]></code>

    <rule>
      <query/Quilt_HTML_Pre/
      <code><![CDATA[
my $self = shift; my $pre = shift; my $context = shift;
print "<TABLE cellpadding='5' border='1' bgcolor='#80ffff' width='100%'>\n";
print "<TR><TD>\n";
print "<PRE>";
$pre->children_accept ($self, $context, @_);
print "</PRE>\n\n";
print "</TD></TR></TABLE>\n";
]]></code>

    <rule>
      <query/Quilt_HTML_NoFill/
      <code><![CDATA[
my $self = shift; my $pre = shift; my $context = shift;
print "<PRE>";
$pre->children_accept ($self, $context, @_);
print "</PRE>\n\n";
]]></code>

    <rule>
      <query/Quilt_HTML_List/
      <code><![CDATA[
my $self = shift; my $list = shift; my $context = shift;
my $type = $list->type;
$type = 'UL' if !defined $type;
my $continued = $list->continued ? " CONTINUED" : "";
print "<$type$continued>";
$list->children_accept ($self, $context, @_);
print "</$type>\n\n";
]]></code>

    <rule>
      <query/Quilt_HTML_List_Item/
      <code><![CDATA[
my $self = shift; my $list_item = shift; my $context = shift;
my $type = 'LI';
$type = 'DD' if ($list_item->parent->type eq 'DL');
print "<$type>";
$list_item->children_accept ($self, $context, @_);
print "</$type>\n\n";
]]></code>

    <rule>
      <query/Quilt_HTML_List_Term/
      <code><![CDATA[
my $self = shift; my $list_term = shift; my $context = shift;
print "<DT>";
$list_term->children_accept ($self, $context, @_);
print "</DT>\n\n";
]]></code>

    <rule>
      <query/Quilt_HTML_Table/
      <code><![CDATA[
my $self = shift; my $table = shift; my $context = shift;
my $border = ($table->frame =~ /none/i) ? "" : " BORDER";
print "<TABLE$border>\n";
$table->children_accept ($self, $context, @_);
print "</TABLE>\n\n";
]]></code>

    <rule>
      <query/Quilt_HTML_Table_Row/
      <code><![CDATA[
my $self = shift; my $row = shift; my $context = shift;
print "  <TR>\n";
$row->children_accept ($self, $context, @_);
print "  </TR>\n";
]]></code>

    <rule>
      <query/Quilt_HTML_Table_Data/
      <code><![CDATA[
my $self = shift; my $data = shift; my $context = shift;
print "    <TD>";
my $data_str = $data->as_string;
if ($data_str =~ /^\s*$/s) {
    print "&nbsp;";
} else {
    $data->children_accept ($self, $context, @_);
}
print "</TD>\n";
]]></code>

    <rule>
      <query/Quilt_HTML_Anchor/
      <code><![CDATA[
my $self = shift; my $anchor = shift; my $context = shift;
print ("<A url='" . $anchor->url_as_string . ">");
$anchor->children_accept ($self, $context, @_);
print "</A>\n\n";
]]></code>

    <rule>
      <query/scalar/
      <code><![CDATA[
my $self = shift; my $data = shift; my $context = shift;
print ($data->delegate);
]]></code>

    <rule>
      <query/sdata SGML_SData/
      <code><![CDATA[
my $self = shift; my $sdata = shift; my $writer = shift;

# XXX we need to move this whole thing into $writer
my $data = $sdata->data;
my $mapping = $writer->{entity_map}->lookup ($data);
if (!defined $mapping) {
    $mapping = "[[" . $data . "]]";
    if (!$writer->{warn_map}{$data}) {
        warn "no entity map for \`$data'\n";
        $writer->{warn_map}{$data} = 1;
    }
}
$mapping =~ s/&/&amp;/;
$mapping =~ s/</&lt;/;
print ($mapping);
]]></code>

  </rules>
</spec>
