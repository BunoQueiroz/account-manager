import os


os.system(
    'docker pull bunoqueiroz/account-manager \
    && docker tag bunoqueiroz/account-manager bunoqueiroz/account-manager:${{ github.run_number }} \
    && docker push bunoqueiroz/account-manager:${{ github.run_number }} \
    && docker build -t account-manager . \
    && docker tag account-manager bunoqueiroz/account-manager \
    && docker push bunoqueiroz/account-manager'
)
