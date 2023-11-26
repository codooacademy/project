{
    'name': "Project Implementation",
    'category': "Project",
    'version': "17.0.0.0.1",
    'installable': True,
    'sequence': 1,

    'license': "LGPL-3",
    'author': "Gautier «MrFaBemol» Casabona",
    'website': "https://www.codoo.academy",

    'depends': ['project', 'hr_timesheet'],

    'assets': {
        'web.assets_backend': [
            'project_implementation/static/src/components/**/*',
        ],
    },

    'data': [
        # Views
        'views/project_epic.xml',
        'views/project_epic_category.xml',
        'views/project_user_story_criteria_type.xml',

        # Security
        'security/ir.model.access.csv',

        # Data
        'data/menuitem.xml',
    ],

    'qweb': [],
}
