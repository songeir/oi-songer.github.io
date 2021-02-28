# 该程序的目的是将之前在typecho上的博客内容迁移到hexo上来
# 输入：
#   1. typecho中导出的dat格式备份文件
#   2. 个人备份的所有博客的markdown原文
# 输出：
#   1. 在_post文件夹下创建所有的博客，并将时间博客中的时间配置为typecho中发布的时间
# 思路：
#   枚举所有markdown文件，找到dat文件中其对应的位置，然后获取对应的时间戳，写入到新发布的博客内容中

import re
import os
import time

from absl import app, flags


flags.DEFINE_bool('force', False, 'force to rewrite output')
flags.DEFINE_bool('test', False, 'output all match results to a text file for test')
FLAGS = flags.FLAGS


def search(dat_text, title):

    content = ''
    typecho_title = ''
    try:
        title = title.replace('[', '\[')
        title = title.replace(']', '\]')
        content = re.search(title + '\ *(\[([\u4e00-\u9fa5_a-zA-Z]|\+)*\]){0,1}\ *[0-9]*<!--markdown-->', dat_text).group()
    except:
        print("Can't find content for title: {}".format(title))

    if content == '':
        try:
            content = re.search('([\u4e00-\u9fa5_a-zA-Z0-9]|\s|'+"""，"""+ ')*[0-9]*<!--markdown--># ' + title, dat_text).group().rstrip('[0-9]')
        except:
            print("Can't find content for title: {}".format(title))
                


    if typecho_title == '':
        try:
            typecho_title = re.search('([\u4e00-\u9fa5_a-zA-Z0-9]|\s|'+"""，"""+ ')*', content).group()
        except:
            typecho_title = "None"
    
    timestamp = int()
    try:
        timestamp = re.search('[0-9]{10}<!--markdown-->', content).group()[:10]
    except:
        timestamp = 0
    return title, timestamp

cates = [
    'C#',
    'Code',
    'Diary',
    'Haskell',
    'Others',
    'Server'
]
contests = [
    'Codeforces Contest',
    'kick start'
]
def file_iterator():
    base_path = '../../'
    for cate in cates:
        dir_path = base_path + cate + '/'
        for md_file in os.listdir( dir_path ):
            if md_file.endswith('.md'):
                yield md_file, cate, dir_path + md_file

        if cate=='Code':
            for contest in contests:
                deeper_dir_path = dir_path + contest + '/'
                for md_file in os.listdir( deeper_dir_path ):
                    if md_file.endswith('.md'):
                        yield md_file, cate, deeper_dir_path + md_file


def file_title(file_path):
    md_file = open(file_path, 'r')
    md_content = md_file.read()
    title = 'Error'
    try:
        title = re.search('^# ([\u4e00-\u9fa5_a-zA-Z0-9]|\ |\[|\]|\ |'+"""，"""+ ')*', md_content).group()[2:]
    except:
        print("[*] Error: Can't find tilte for {}".format(file_path))
    return title.strip(), md_content


def suc(title, timestamp):
    if title and title!='' and title!='Error' and timestamp and timestamp != 0:
        return True
    return False


def main(argv):
    dat = open('20210121_songer.xyz_60097668497b7.dat', 'r')
    dat_text = dat.read()

    test_output = None
    if FLAGS.test:
        test_output = open('test_output_suc.tsv', 'w')
        test_output.write('title\ttypecho_title\ttime\tdir\n')
        
        test_output_fail = open('test_output_fail.tsv', 'w')
        test_output_fail.write('title\ttypecho_title\ttime\tdir\n')

    skip_cnt = suc_cnt = 0
    draft_cnt = skip_draft_cnt = 0
    for md_file, cate, file_path in file_iterator():
        title, content = file_title(file_path)
        typecho_title, timestamp = search(dat_text, title)

        typecho_title = typecho_title.replace('\[', '[')
        typecho_title = typecho_title.replace('\]', ']')

        if FLAGS.test:
            output_str = "{}\t{}\t{}\t{}\n".format(
                title,
                typecho_title,
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(timestamp))),
                file_path
            )
            if suc(typecho_title, timestamp):
                test_output.write(output_str)
            else:
                test_output_fail.write(output_str)
        else:
            if suc(typecho_title, timestamp):
                output_path = '../source/_posts/{}/{}.md'.format(cate, typecho_title)
                if os.path.isfile(output_path) and not FLAGS.force:
                    skip_cnt += 1
                    continue
                output_file = open(output_path, 'w')

                output_str = '---\n' + \
                    'title: \"{}\"\n'.format(typecho_title) + \
                    'date: {}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(timestamp)))) + \
                    'tags: \n' + \
                    '---\n\n' + content.replace('https://oi-songer.github.io', '/images/')

                output_file.write(output_str)

                suc_cnt += 1
            else:
                output_path = '../source/_drafts/{}/{}.md'.format(cate, typecho_title)
                if os.path.isfile(output_path) and not FLAGS.force:
                    skip_draft_cnt += 1
                    continue
                output_file = open(output_path, 'w')

                output_str = '---\n' + \
                    'title: \"{}\"\n'.format(typecho_title) + \
                    'tags: \n' + \
                    '---\n\n' + content

                output_file.write(output_str)

                draft_cnt += 1

    print("finsiehd.")
    print("post: suc[{}], skip[{}]".format(suc_cnt, skip_cnt))
    print("draft: suc[{}], skip[{}]".format(draft_cnt, skip_draft_cnt))




if __name__=="__main__":
    app.run(main)