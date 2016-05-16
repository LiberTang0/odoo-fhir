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

##View
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
<record id="view_sale_order_calendar" model="ir.ui.view">
            <field name="name">sale.order.calendar</field>
            <field name="model">sale.order</field>
            <field name="arch" type="xml">
                <calendar string="Sales Orders" color="state" date_start="date_order">
                    <field name="partner_id"/>
                    <field name="amount_total" widget="monetary"/>
                </calendar>
            </field>
        </record>
```



