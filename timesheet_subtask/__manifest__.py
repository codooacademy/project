{
    'name': "Timesheet for subtasks",
    'category': "Services/Timesheets",
    'description': """
        This module adds the possibility to use the timesheet timer directly in the subtasks tab.
""",
    'version': "17.0.1.0.0",
    'installable': True,
    'application': False,
    'sequence': 1,

    'license': "LGPL-3",
    'author': "Gautier «MrFaBemol» Casabona",
    'website': "https://www.codoo.academy",

    'depends': ['timesheet_grid'],
    'data': [
        # Views
        'views/project_task.xml',
    ],
}
