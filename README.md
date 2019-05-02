# Graduation_Project
## 文件夹内容
   open_reply为开题答辩的内容。
   
   paper为所读的文献资料。
   
   notes为一些重要知识以及项目日常笔记。
   
   public为一些公有链接资源。
   
**笔记**

***2019/5/1***

创建了django项目，并且实现登录界面

attempted relative import with no known parent package解决办法：
创建一个新的__init__.py文件
 解决执行下面命令生成相关用户表即可:
    python manage.py  makemigrations
    python manage.py  migrate
问题：
auth.User.groups: (fields.E304) Reverse accessor for 'User.groups' clashes with reverse accessor for 'User.groups'.
	HINT: Add or change a related_name argument to the definition for 'User.groups' or 'User.groups'.
auth.User.user_permissions: (fields.E304) Reverse accessor for 'User.user_permissions' clashes with reverse accessor for 'User.user_permissions'.
	HINT: Add or change a related_name argument to the definition for 'User.user_permissions' or 'User.user_permissions'.
users.User.groups: (fields.E304) Reverse accessor for 'User.groups' clashes with reverse accessor for 'User.groups'.
	HINT: Add or change a related_name argument to the definition for 'User.groups' or 'User.groups'.
users.User.user_permissions: (fields.E304) Reverse accessor for 'User.user_permissions' clashes with reverse accessor for 'User.user_permissions'.
	HINT: Add or change a related_name argument to the definition for 'User.user_permissions' or 'User.user_permissions'.

解决办法：
setting下# AUTH_USER_MODEL = 'users.User'   #自己加的   使用user下的User模型

***2019/5/2***

do：实现注册界面与index界面，注册界面使用的是form表单连接django内置的注册结构

todo：实现数据库的连接与用户数据表的设计，实现登录注册功能


问题：ValueError: Dependency on app with no migrations: users

错误原因： 在settings中加入了AUTH_USER_MODEL 

解决办法： 
解决执行下面命令生成相关用户表即可:

python manage.py  makemigrations

python manage.py  migrate
