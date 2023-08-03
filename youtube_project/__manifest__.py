# -*- coding: utf-8 -*-

{
    'name': "Youtube Project",
    'category': "Social",
    'version': "16.0.0.0.1",
    'installable': True,
    'application': True,
    'sequence': 1,

    'license': "OEEL-1",
    'author': "MrFaBemol",
    'website': "https://www.codoo.academy",

    'depends': ['project', 'social_youtube', 'timesheet_subtask'],
    "assets": {
        "web.assets_backend": [],
    },

    'data': [
        # Security
        'security/ir.model.access.csv',

        # Data
        'data/project_task_type.xml',

        # Views
        'views/project_project.xml',
        'views/project_task.xml',
        'views/project_task_type.xml',

        # Menu Items
        'data/menuitem.xml',
    ],

    'qweb': [],
}
