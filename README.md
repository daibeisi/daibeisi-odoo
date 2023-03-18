daibeisi-odoo
----

This is odoo repository for daibeisi.

项目结构
-------------------------
mini-program
├── bin                   用于保存各类帮助可执行shell脚本
├── cron                  用于保存定时任务脚本
├── filestore             用于文件存储
├── local-addons          用于保存自己开发的插件
├── logs                  用于存储服务日志文件
├── src                   用于存储Odoo项目以及一些第三方插件项目
├── venv                  项目环境
├── .gitignore            Git忽略提交规则
├── odoo.cfg              系统配置文件
├── README.md             项目手册
└── requirement.txt       系统依赖包

Getting started with daibeisi-odoo
-------------------------

python ./src/odoo/odoo-bin --config=odoo.conf