# -*- coding: utf-8 -*-

urls = (
    '/', 'Index',
    '/blog/(.+)/', 'Blog',
    '/login/', 'Login',
    '/admin/', 'Admin',
    '/media/', 'Media',
    '/user/', 'User',
    '/post/(.+)?', 'Post'
)
