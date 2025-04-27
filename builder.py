import os
import shutil
import subprocess

projects_base_dir = str(input("Директория проекта: "))
project_name_input = str(input("Название проекта: "))

# Базовые директории
base_dirs = ['templates', 'static']
base_static_dirs = ['css', 'img', 'js']

# Онлайн-магазин
shop_apps = ['main', 'users', 'product', 'order', 'cart', 'payment']
shop_templates = {
    'main': ['base.html', 'index.html', 'about.html', 'contact.html'],
    'users': ['register.html', 'login.html', 'logout.html', 'settings.html', 'update.html', 'profile.html'],
    'product': ['create_product.html', 'list_product.html', 'detail_product.html', 'update_product.html'],
    'order': ['order.html', 'history_order.html', 'status_order.html'],
    'cart': ['cart.html'],
    'payment': ['payment.html', 'history.html'],
}

# Блог
blog_apps = ['main', 'users', 'post']
blog_templates = {
    'main': ['base.html', 'index.html', 'about.html', 'contact.html'],
    'users': ['register.html', 'login.html', 'logout.html', 'settings.html', 'update.html', 'profile.html'],
    'post': ['create_post.html', 'list_post.html', 'detail_post.html', 'update_post.html'],
}

# Лендинг
landing_apps = ['main', 'users', 'contact']
landing_templates = {
    'main': ['base.html', 'index.html', 'about.html', 'contact.html'],
    'users': ['register.html', 'login.html', 'logout.html', 'settings.html', 'update.html', 'profile.html'],
    'contact': ['contact.html'],
}


def create_project(parent_dir, project_name):
    if not os.path.isdir(parent_dir):
        print(f"Директория {parent_dir} не найдена ")
        return
    try:
        print(f"Переходим в директорию {parent_dir}")
        os.chdir(parent_dir)
        print(f"Создайем проект {project_name}")
        subprocess.Popen(['django-admin', 'startproject', f"{project_name}"])
        print(f"Проект {project_name} успешно создан в директории {parent_dir}")
    except subprocess.CalledProcessError:
        print("Команда django-admin - не найдено ")


def create_app(apps):
    if not os.path.isdir(projects_base_dir):
        print(f"Директория {projects_base_dir} не найдена")
        return
    try:
        parent_dir = os.path.join(projects_base_dir, project_name_input)
        os.chdir(parent_dir)
        print(f"Переходим в директорию {parent_dir}")
        for app in apps:
            print(f"Создаем приложение {app}")
            subprocess.Popen(['django-admin', 'startapp', f"{app}"])
            print(f"Приложение {app} успешно создано в директории {parent_dir}")

    except subprocess.CalledProcessError:
        print("Команда django-admin - не найдено")

create_project(projects_base_dir, project_name_input)


def create_base_dirs(apps):
    for app in apps:
        app_dir = os.path.join(projects_base_dir, project_name_input, app)

        # Создаем директорию templates/app_name
        templates_dir = os.path.join(app_dir, 'templates', app)
        os.makedirs(templates_dir, exist_ok=True)
        # Создаем директорию static/app_name/css, js, img
        static_base_dir = os.path.join(app_dir, 'static', app)
        for sub_dir in base_static_dirs:
            full_static_dir = os.path.join(static_base_dir, sub_dir)
            os.makedirs(full_static_dir, exist_ok=True)

    print("Базовые директории и подпапки приложений успешно созданы")


print("Выберите тип проекта .")

print("1 . Онлайн магазин")
print("2 . Блог")
print("3 . Лендинг ")

type_project = int(input("Выберите тип проекта : "))

if type_project == 1:
    print("Создаем архитектуру онлайн магазина ...")
    create_app(shop_apps)
    print("Архитектура онлайн магазина успешно создана")
elif type_project == 2:
    print("Создаем архитектуру блога ...")
    create_app(blog_apps)
    print("Архитектура блога успешно создана")
elif type_project == 3:
    print("Создаем архитектуру лендинга ...")
    create_app(landing_apps)
    print("Архитектура лендинга успешно создана")
else:
    print("Команда не существует")


create_dirs = str(input("Хотите создать базовые директорий tempaltes & static ? (y/n) :"))

if create_dirs.lower() == 'y':
    if type_project == 1:
        create_base_dirs(shop_apps)
    elif type_project == 2:
        create_base_dirs(blog_apps)
    elif type_project == 3:
        create_base_dirs(landing_apps)