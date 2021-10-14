import os
import shutil

main_dir = 'task_7_3'
if not os.path.exists(main_dir):
    os.mkdir(main_dir)

folder = r'my_project'
files = []

for r, d, f in os.walk(folder):
    for file in f:
        if '.html' in file:
            files.append(os.path.join(r, file))

for path in files:
    folder = os.path.join(main_dir, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder):
        os.mkdir(folder)
    save_path = os.path.join(folder, os.path.basename(path))
    shutil.copy(path,save_path)