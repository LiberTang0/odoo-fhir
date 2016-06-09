##References
* [Odoo Guidelines 9.0] (https://www.odoo.com/documentation/9.0/reference/guidelines.html)
* [Python Guidelines] (https://www.python.org/dev/peps/pep-0008/)

##Model (Object) Name
* Style: lower case terms separated by a dot `.`
* Prefix: `hc.res` for all [FHIR Resources] (https://hl7-fhir.github.io/resourcelist.html)
   * Example: *Patient* has model name `hc.res.patient`
* Prefix: `hc.vs` for all [FHIR Value Set] (https://hl7-fhir.github.io/terminologies-valuesets.html) and other value sets
   * Example: *PatientContactRelationship* has model name `hc.vs.patient.contact.relationship`
* Prefix: `hc` for all [FHIR Data Types] (https://hl7-fhir.github.io/datatypes.html) objects which are not resources or value sets.
  *  Example: *Address* data type has model name `hc.address`
  *  Example: *Patient Contact* has model name `hc.patient.contact`

## Directories

* Mandatory

  * *data/* : demo and data xml
  * *models/* : models definition
  * *controllers/* : contains controllers (HTTP routes).
  * *views/* : contains the views and templates
  * *static/* : contains the web assets, separated into *css/*, *js/*, *img/*, *lib/*, ...

* Optional

  * *wizard/* : regroups the transient models (formerly osv_memory) and their views.
  * *report/* : contains the reports (RML report [deprecated], models based on SQL views (for reporting) and other complex reports). Python objects and XML views are included in this directory.
  * *tests/* : contains the Python/YML tests

##Module Name

* Pattern: `hc_[FHIR_resource_name]`
* FHIR_resource_name in https://hl7-fhir.github.io/resourcelist.html
* Example: `hc_patient`

##File Name

* Models
  * Split by sets of models.
  * models/*[main_model]*.py* (e.g., hc_address.py)
  * For example, `hc.address`, `hc.vs.country.postal.code` and `hc.vs.country.city` models are in the same file.
  * models/*[inherited_main_model]*.py (e.g., inherited_hc_address.py)

##View ID

* Pattern: `[object_name]_view_[view_type]`
* Where `view_type` is `{tree,form,kanban,search,calendar,qweb,diagram,gantt,graph,pivot}`
* Example: `hc_address_view_tree`


##View Name

* Style: Proper
* Pattern: `[object_description] [view_type]`
* Where `view_type` is `{tree,form,kanban,search,calendar,qweb,diagram,gantt,graph,pivot}`
* Examples: `Address Tree`, `Address Form`

##Action ID

* Pattern for main action: `[object_name]_action`
* Pattern for other actions: `[object_name]_action_[detail]`
* Example: `hc_base.hc_address_action`

##Action Name

Pattern: Prefix `HC` + Plural form of `[object_description]`
Example: `HC Addresses`

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
```html
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
```html
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
```html
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
```html
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
```html
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
```html
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
```html
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
```html
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

* Pattern: `[model_name]_group_[group_name]`
* Where group_name may be `{user,manager,administrator, etc.}` 
* Example: `hc_base_group_user`
