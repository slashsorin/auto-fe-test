#-*- coding: utf-8 -*-
'''
    
    @author: Sorin

    Copyright Issuu Aps Jun 15, 2012
'''
import new
import cfg
    
def make_platform_classes(base_class, platforms=None):
    if not platforms:
        platforms = cfg.config['platforms']
        # this is a dict with all the platforms we want to test in this execution

    classes = {}
    for platfrm in cfg.config['platforms']:
        os = platfrm['os']
        browser = platfrm['browser']
        version = platfrm['browser-version']
        
        name = "%s_%s_%s_%s_" % (base_class.__name__,
                                os,
                                browser,
                                version
                                )
        
        name = name.encode('ascii')
        for x in " .-":
            name = name.replace(x, "_")
    
        d = {'__test__': True,
             'name': name,
             'os': os,
             'browser': browser,
             'version': version
             }

        if platfrm.has_key('avoid-proxy'):
            d['avoid_proxy'] = platfrm['avoid-proxy']

        classes[name] = new.classobj(name, (base_class,), d) # import new is needed
    return classes
