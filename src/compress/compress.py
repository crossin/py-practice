# -*- coding: utf-8 -*-


from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals


import zipfile
import os


def compress_dir(source_dir, zip_name='temp.zip'):
    f = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(source_dir):
        # 遍历整个目录，将目录下所有文件都压缩进去，
        # 这个遍历方法是不是很熟悉？
        for filename in filenames:
            f.write(os.path.join(dirpath, filename))
    f.close()
    # 最后别忘了关闭文件，否则只要程序不终止，将永远占据这个文件。


def decompress_dir(zip_name, target_dir='.'):
    # 将给定文件解压到给定地方，默认解压到当前文件夹
    if not os.path.isdir(target_dir):
        # 如果要解压的文件夹不存在的话，要新建文件夹
        os.mkdir(target_dir)

    source_zip = zipfile.ZipFile(zip_name)
    source_zip.extractall(target_dir)
    # 和压缩相比，解压就相对容易得多，可以直接将文件全部提取。
    # 如果你只想解压部分文件，你可以读取namelist，然后选择想要的文件解压。
    source_zip.close()


if __name__ == '__main__':
    compress_dir('test/', 'temp.zip')
    # 先将test文件夹全部压缩，压缩文件名为`temp.zip`
    decompress_dir('temp.zip', 'out')
    # 在将此文件解压，为避免冲突，我们将其解压到out文件夹内。
