# ShowCodeTemplates

> 自用项目结构

## 功能模块

- LOG日志
- Pusher功能
  - 钉钉机器人
  - pushplus
  - serverchan
- **[pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)**提交检查
- sqlalchemy数据库(可选)
- Dockfile(可选)
- pipenv环境(可选)

## 项目结构

```
.
├── docker-entrypoint.sh
├── Dockerfile
├── .gitignore
├── base
│        ├── dbs.py
│        ├── decorators.py
│        ├── enums.py
│        ├── exceptions.py
│        ├── ext.py
│        ├── __init__.py
│        ├── logger.py
│        ├── runner.py
│        ├── settings.py
│        └── utils
│            ├── fileu.py
│            ├── __init__.py
│            ├── pusher.py
│            ├── stringu.py
│            └── timeu.py
├── LICENSE
├── logs
├── main.py
├── push_config.ini
├── Readme.md
├── requirements.txt
└── tests
```

## 鸣谢

Created by: [cookiecutter](https://cookiecutter.readthedocs.io/)

