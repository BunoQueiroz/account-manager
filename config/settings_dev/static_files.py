import os
from .main import BASE_DIR


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, '../static/')
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, '../style/')]
