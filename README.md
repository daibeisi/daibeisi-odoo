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
├── daibeisi-odoo.cfg              系统配置文件
├── README.md             项目手册
└── requirement.txt       系统依赖包

部署
-------------------------
1. 准备Ubuntu系统且安装git
2. 下载本项目`git clone -b master --single-branch --depth 1 https://github.com/daibeisi/daibeisi-odoo`
3. 打开到项目中src目录下，下载Odoo项目`git clone -b 16.0 --single-branch --depth 1 https://github.com/odoo/odoo`
4. 安装项目所需依赖包`env/bin/python3 install -r src/odoo/requirements.txt`
5. 修改系统配置文件daibeisi-odoo.cfg
6. 打开到项目中bin目录下，让daibeisi-odoo脚本可执行`chmod +x daibeisi-odoo`
7. 运行项目`odoo`

Getting started with daibeisi-odoo
-------------------------

python ./src/odoo/odoo-bin --config=daibeisi-odoo.cfg