# -*- coding: utf-8 -*-

{
    'name': "Timesheet for subtasks",
    'category': "Services/Timesheets",
    'description': """
        This module adds the possibility to use the timesheet timer directly in the subtasks tab.
""",
    'version': "16.0.1.0.0",
    'installable': True,
    'application': False,
    'sequence': 1,

    'license': "GPL-3",
    'author': "MrFaBemol",
    'website': "https://www.codoo.academy",

    'depends': ['timesheet_grid'],
    'data': [
        # Views
        'views/project_task.xml',
    ],
}
