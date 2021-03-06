# -*- coding: utf-8 -*-
{
    'name': "Related Person",

    'summary': """
        Information about a person that is involved in the care for a patient, but who is not the target of healthcare, nor has a formal responsibility in the care process.
        """,

    'description': """
        RelatedPersons typically have a personal or non-healthcare-specific professional relationship to the patient. A RelatedPerson resource is primarily used for attribution of information, since RelatedPersons are often a source of information about the patient. For keeping information about people for contact purposes for a patient, use a Patient's Contact element. Some individuals may serve as both a Patient's Contact and a Related Person.

        Example RelatedPersons are:

        * A patient's wife or husband
        * A patient's relatives or friends
        * A neighbor bringing a patient to the hospital
        * The owner or trainer of a horse
        * A patient's attorney or guardian
        * A Guide Dog
        """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/relatedperson.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hc_person', 'hc_patient'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}