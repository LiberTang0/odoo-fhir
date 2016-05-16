##View ID
```
<!-- View -->
Pattern: [module_name].[object_name>]_[viewtype]
Example: hc_person.value_set_contains_tree
```
##Action ID
```
<!-- Action -->
Pattern: open_view_[object_name>]_[viewtype]
Example: open_view_value_set_contains_tree
```
##Menu Item ID
```
<!-- Menu Item -->
Pattern: [module_name].menu_[short_object_name]
Example: hc_base.menu_clinic
```

##Form Name
```
Pattern: [object.name].form
Example: hc.address.form
```

##View Type
```
{tree,form,kanban,search,calendar,Qweb,diagram,gantt,graph,pivot}
```

##Form View
```
<!-- View -->
<record id="[View ID]" model="ir.ui.view">
  <field name="name">[Form Name]</field>
  <field name="model">[Object Name]</field>
  <field name="arch" type="xml">
  
    <form string="[Object Description]">
      <sheet>
        <group>
          <group>
            <field name="[field]"/>
          </group>
          <group>
            <field name="[field]"/>
          </group>
        </group>
      </sheet>
    </form>

  </field>
</record>
```
##View Calendar
```
<record id="view_[object_name]_calendar" model="ir.ui.view">
  <field name="name">[object.name].calendar</field>
  <field name="model">[object.name]</field>
  <field name="arch" type="xml">
    <calendar string="Object Name" color="state" date_start="date_order">
      <field name="partner_id"/>
      <field name="amount_total" widget="monetary"/>
    </calendar>
  </field>
</record>
```

##View Graph
```
<record id="view_[object_name]_graph" model="ir.ui.view">
            <field name="name">[object.name].graph</field>
            <field name="model">sale.order</field>
            <field name="arch" type="xml">
                <graph string="Sales Orders">
                    <field name="partner_id"/>
                    <field name="amount_total" type="measure"/>
                </graph>
            </field>
        </record>

