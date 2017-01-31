# -*- coding: utf-8 -*-

urls = (
    '/', 'Index',
    '/blog/(.+)/', 'Blog',
    '/login/', 'Login',
    '/logout/', 'Logout',
    '/admin/', 'Admin',
    '/media/', 'Media',
    '/entry/(.+)?', 'Entry'
)
