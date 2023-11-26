{
    'name': "Youtube Project",
    'category': "Social",
    'version': "17.0.0.0.1",
    'installable': True,
    'application': True,
    'sequence': 1,

    'license': "LGPL-3",
    'author': "Gautier «MrFaBemol» Casabona",
    'website': "https://www.codoo.academy",

    'depends': ['project', 'social_youtube'],
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
        'views/social_account.xml',

        # Menu Items
        'data/menuitem.xml',
    ],

    'qweb': [],
}
