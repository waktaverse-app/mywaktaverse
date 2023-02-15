import shutil
import os
import glob

app_title = "마이 왁타버스"

# overwrite 폴더 안의 파일들을 현재 경로로 복사함.
src_dir = "overwrite"
for file_name in os.listdir(src_dir):
    if os.path.isfile(os.path.join(src_dir, file_name)):
        shutil.copy(os.path.join(src_dir, file_name), ".")

def replace_file(file_path, old_string, new_string, count):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        new_content = file_content.replace(old_string, new_string, count)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

replace_file("index.html", "/manifest.json", "manifest.json", 1)
replace_file("index.html", "</title>", '</title><link rel="icon" type="image/x-icon" href="favicon.ico">', 1)

for file_path in glob.glob("**/*.html", recursive=True):
    replace_file(file_path, "<title>AppGyver</title>", f"<title>{app_title}</title>", 1)

for file_path in glob.glob("_next/static/chunks/pages/_app-*.js"):
    replace_file(file_path, '("title",null,"AppGyver")', f'("title",null,"{app_title}")', 1)
