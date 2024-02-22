import os
from dotenv import load_dotenv


load_dotenv()

version = os.getenv('VERSION')

os.system(
    f'docker pull bunoqueiroz/account-manager \
    && docker tag bunoqueiroz/account-manager bunoqueiroz/account-manager:1.5.{version} \
    && docker push bunoqueiroz/account-manager:1.5.{version} \
    && docker build -t account-manager . \
    && docker tag account-manager bunoqueiroz/account-manager \
    && docker push bunoqueiroz/account-manager'
)
