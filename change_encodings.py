#
# @ Author Cedric Walker
#

#convert a coding project to utf8
import codecs
from shutil import copyfile
from pathlib import Path

def load_file(x):
    try:
        with codecs.open(x, 'r+', encoding='utf-8') as f:
            string = f.read()
    except UnicodeDecodeError as e:
        print("is Ascii")
        with codecs.open(x, 'r+') as f:
            string = f.read()
    return string


def copy_to_path(file, new_path):
    if(not Path(file).is_dir()):
        copyfile(file, new_path)

def get_new_parent(abs_file, new_dir, dir):
    new_path = Path(new_dir).joinpath(Path(abs_file).relative_to(dir))
    return new_path

def if_not_make_dir(path, old_path):
    if(Path(old_path).is_file()):
        Path.mkdir(Path(path).parent, parents=True, exist_ok = True)
    else:
        Path.mkdir(Path(path), parents=True, exist_ok = True)


def safe_as_utf(string, new_path):
    file = codecs.open(new_path, "w", "utf-8")
    file.write(string)
    file.close()


def copy_or_encode_copy(dir, new_dir, pattern):
    pathlist = Path(dir).glob('**/*')
    for x in pathlist:
        try:
            if(Path(x).match(pattern)):
                string = load_file(x)
                new_path = get_new_parent(x, new_dir, dir)
                if_not_make_dir(new_path,x)
                safe_as_utf(string, new_path)
            else:
                new_path = get_new_parent(x, new_dir, dir)
                if_not_make_dir(new_path,x)
                copy_to_path(x, new_path)

        except UnicodeDecodeError as e:
            print(str(e))
            print(x)


if __name__ == "__main__":
    pattern = '*.php'
    dir = 'path'
    new_dir = 'newpath' # every file gets copied here
    copy_or_encode_copy(dir, new_dir, pattern)


