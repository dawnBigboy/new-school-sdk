# -*- coding: utf-8 -*-
'''
    :file: config.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2021/09/04 23:39:20
'''

# INDEX http://192.168.2.123:7899/xtgl/index_initMenu.html?jsdm=xs&_t=1643879775142

URL_ENDPOINT = {
    "HOME_URL": "/jwglxt/xtgl/login_slogin.html",
    "INDEX_URL": "/jwglxt/xtgl/index_initMenu.html",
    'LOGIN': {
        'INDEX': '/jwglxt/xtgl/login_slogin.html',
        'CAPTCHA': '/jwglxt/zfcaptchaLogin',
        'KCAPTCHA': '/jwglxt/kaptcha',
        'PUBLIC_KEY': '/jwglxt/xtgl/login_getPublicKey.html',
    },
    "SCORE_URL": "",
    "INFO_URL": "",
    "SCHEDULE": {
        "API": '/jwglxt/kbcx/xskbcx_cxXsKb.html',
    },
    "CLASS_SCHEDULE": {
        "API": '/jwglxt/kbdy/bjkbdy_cxBjKb.html'
    },
    'SCORE': {
        # cjcx_cxXsgrcj
        'API': '/jwglxt/cjcx/cjcx_cxDgXscj.html'
    },
    'INFO': {
        'API': '/jwglxt/xsxxxggl/xsgrxxwh_cxXsgrxx.html'
    }
}
