# -*- coding: utf-8 -*-
import os
import random
import subprocess

VIDEO_EXT = ['avi', 'mkv', 'mp4', 'wmv']
# 视频文件的扩展名，这里只列出了常见的几种格式


def rand_walk(root_dir):
    all_videos = []
    for root, dirs, files in os.walk(root_dir):
        for file_ in files:
            if 'huluwa' in root or 'xiyangyang' in file_:
                '''对于一些不想播放的视频，我们要将它排除掉，
                在这里，如果文件夹名中含有`huluwa`的文件夹，
                或者文件名中含有`xiyangyang`的文件夹，
                我们都将跳过，毕竟我们不喜欢看葫芦娃和喜羊羊不是么？
                :P
                '''
                continue
            extstr = file_.split('.')[-1].lower()
            # 提取出扩展名
            if extstr in VIDEO_EXT:
                # 如果扩展名在我们想要的列表中，则将此文件加入最后的结果
                all_videos.append(os.path.join(root, file_))

    return all_videos


if __name__ == '__main__':
    # 将你想遍历的文件夹地址作为参数传入，譬如要遍历当前文件夹，则传入 '.'
    all_videos = rand_walk('d:\\')
    # 我们得到所有视频文件

    # print(all_videos)

    for i in range(5):
        video = random.choice(all_videos)
        # 据说多随机选几次，得到的结果更随机？//哈哈其实完全是心理作用

    # print(video)
    os.startfile(video)  # Windows
    # 调用系统默认播放器播放视频，注意不要使用 `os.system`
    # subprocess.call(['open', video])  # Mac / Linux
