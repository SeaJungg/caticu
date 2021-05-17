DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'capston', 
        'USER': 'admin',
        'PASSWORD': 'caticu123',
        'HOST': 'caticu-db-1.cj8g7hzwpwh8.ap-northeast-2.rds.amazonaws.com',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        },

    }
}
