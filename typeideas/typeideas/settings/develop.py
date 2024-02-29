import os.path

from .base import *
DEBUG =True

DATABASES={
'default'    :{
    'ENGINE':"django.backends.sqlite3",
                                                        'NAME':os.path.join(BASE_DIR,'db_sqlite3')
}

}