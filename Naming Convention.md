##References
* [Odoo Guidelines 9.0] (https://www.odoo.com/documentation/9.0/reference/guidelines.html)
* [Python Guidelines] (https://www.python.org/dev/peps/pep-0008/)

##Module Name
```
Pattern: hc_[FHIR_resource_name]
FHIR_resource_name in https://hl7-fhir.github.io/resourcelist.html

Example: hc_patient
```

##View ID
```
Pattern: [module_name].[object_name]_view_[view_type]
Where view_type is {tree,form,kanban,search,calendar,qweb,diagram,gantt,graph,pivot}

Example: hc_base.hc_address_view_tree
```

##View Name
```
Pattern: [object_description] [view_type]
Where view_type is {tree,form,kanban,search,calendar,qweb,diagram,gantt,graph,pivot}

Example: Address Tree
```

##Action ID
```
Pattern for main action: [module_name].[object_name]_action
Pattern for other actions: [module_name].[object_name]_action_[detail]

Example: hc_base.hc_address_action
```

##Action Name
```
Pattern: [Action Word] [object_description]
Example: Configure Address
```

##Menu Item ID
```
Pattern: [module_name]_menu_[short_menu_object_name]
Example: hc_base_menu_clinic
```

##Menu Item Name
```
Pattern: [object_description] plural form
Example: Addresses
```

##Tree (List) View
```
<!-- List View -->
<record id="[View ID]" model="ir.ui.view">
  <field name="name">[View Name]</field>
  <field name="model">[Object Name]</field>
  <field name="arch" type="xml">
    <tree colors="gray:is_done==True">
      <!-- Content goes here -->
      <field name="[field_name]"/>
      <field name="[field_name]"/>
    </tree>
```
##Form View
```
<!-- Form View -->
<record id="[View ID]" model="ir.ui.view">
  <field name="name">[View Name]</field>
  <field name="model">[Object Name]</field>
  <field name="arch" type="xml">
  
    <form string="[Object Description]">
      <sheet>
        <group>
          <group>
            <!-- Content goes here -->
            <field name="[field_name]"/>
            <field name="[field_name]"/>
          </group>
          <group>
            <!-- Content goes here -->
            <field name="[field_name]"/>
            <field name="[field_name]"/>
          </group>
        </group>
      </sheet>
    </form>

  </field>
</record>
```
##Business Document Form View
```
<!-- Business Document Form View -->
<form>
  <header>
  <!-- Buttons go here -->
  </header>
  <sheet>
    <!-- Content goes here -->
    <field name="[field_name]"/>
    <field name="[field_name]"/>
  </sheet>
</form>
```
##Button Name
```
Pattern: do_[action]_done
Example: do_toggle_done
Example: do_clear_done
```

##Action Button
```
<header>
  <button name="[button_name]" 
    type="object" 
    string="[Display Label]" 
    class="oe_highlight"/>
</header>
```

##Kanban View
```
<!-- Kanban View  -->
<record id="[View ID]" model="ir.ui.view">
  <field name="name">[View Name]</field>
  <field name="model">[Object Name]</field>
  <field name="arch" type="xml">
 
    <kanban class="o_kanban_mobile">
      <!-- Content goes here -->
      <field name="[field_name]"/>
      <field name="[field_name]"/>
      <field name="name"/>
      <templates>
        <t t-name="kanban-box">
          <div t-attf-class="oe_kanban_card oe_kanban_global_click">
              
              <div class="row">
                  <div class="col-xs-6">
                      <strong><span><t t-esc="record.partner_id.value"/></span></strong>
                  </div>
                  <div class="col-xs-6 pull-right text-right">
                      <strong><field name="[field_name]" widget="monetary"/></strong>
                  </div>
              </div>
              
              <div class="row">
                  <div class="col-xs-6 text-muted">
                      <span><t t-esc="record.name.value"/> <t t-esc="record.date_order.value"/></span>
                  </div>
                  <div class="col-xs-6">
                      <span t-attf-class="pull-right text-right label #{['draft', 'cancel'].indexOf(record.state.raw_value) > -1 ? 'label-default' : ['done'].indexOf(record.state.raw_value) > -1 ? 'label-success' : 'label-primary'}"><t t-esc="record.state.value"/></span>
                  </div>
              </div>
          
          </div>
        </t>
      </templates>
    </kanban>
    
  </field>
</record>
```

##Calendar View
```
<!-- Calendar View -->
<record id="view_[object_name]_calendar" model="ir.ui.view">
<field name="name">[object.name].calendar</field>
<field name="model">[object.name]</field>
<field name="arch" type="xml">

  <calendar string="[Object Name]" color="state" date_start="date_order">
    <!-- Content goes here -->
    <field name="[field_name]"/>
    <field name="[field_name]" widget="monetary"/>
  </calendar>

</field>
</record>
```

##Graph View
```
<!-- Graph View -->
<record id="view_[object_name]_graph" model="ir.ui.view">
<field name="name">[object.name].graph</field>
<field name="model">sale.order</field>
<field name="arch" type="xml">
  
  <graph string="[Object Name]">
    <!-- Content goes here -->
    <field name="[field_name]"/>
    <field name="[field_name]" type="measure"/>
  </graph>

</field>
</record>
```

##Pivot View
```
<!-- Pivot View -->
<record model="ir.ui.view" id="view_sale_order_pivot">
  <field name="name">sale.order.pivot</field>
  <field name="model">sale.order</field>
  <field name="arch" type="xml">
  
    <pivot string="[Object Name]">
      <!-- Content goes here -->
      <field name="[field_name]" type="row"/>
      <field name="[field_name]" type="measure"/>
    </pivot>
    
  </field>
</record>
```

##Group Name
```
Pattern: [model_name]_group_[group_name]
Where group_name may be {user,manager,administrator, etc.}
Example: hc_base_group_user
```
