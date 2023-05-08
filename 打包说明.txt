## 模块打包

在根目录下执行Python setup.py sdist bdist_wheel

## 模块上传

python -m pip install --upgrade twine

pip install --upgrade twine

发布

python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

twine upload --repository-url https://upload.pypi.org/legacy/  dist/*
