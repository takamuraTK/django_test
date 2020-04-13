# git clone時にSECRET_KEYを生成するためのファイル
# git clone後にsetting.pyと同じディレクトリで
# $ python generate_secretkey_setting.py > local_settings.py
# を実行することで生成可能
from django.core.management.utils import get_random_secret_key

secret_key = get_random_secret_key()
text = 'SECRET_KEY = \'{0}\''.format(secret_key)
print(text)