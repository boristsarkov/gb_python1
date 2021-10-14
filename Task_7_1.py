import os

tree = {'my_project': ['sttings', 'mainapp', 'adminapp', 'authapp']}
for root, folders in tree.items():
    if os.path.exists(root):
        print(root, 'существует на данном компьютере')
    else:
        for folder in folders:
            all_dir = os.path.join(root, folder)
            os.makedirs(all_dir)
