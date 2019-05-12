# -*- coding: utf-8 -*-

import re

with open('writer_name_no_repeat.txt') as file:
    lst = file.readlines()
japanese = u'[一-龥ぁ-んァ-ヶ]'
pre_finder = re.compile('^japanese+( )japanese+')
pre2_finder = re.compile('^japanese+')
with open('auto_complete_list.txt', 'w')as file:
    for line in lst:
        print(line)
        pre = pre_finder.search(line).group(1)
        pre2 = pre2_finder.search(line)
        print(pre)
        print(pre2)
        if not pre:

            b = 0
            for i in pre:
                if b >= 1:
                    a = line[0:b]
                    str1 = "'" + a + "': [{id: '" + line + "',text: '" + line + "',highlight: '<strong>" + a + "</strong>" + line[
                                                                                                                             len(
                                                                                                                                 a):] + "'}],"
                    file.write(str1)
                    file.write('\n')
                    '''file.write("'{}': [".format(i))

                file.write("{")

                file.write(
                    "\nid: '{}',\ntext: '{}',\nhighlight: '<strong>{}</strong>{}'\n".format(pre, pre, i, pre[len(a):]))
                file.write("}],")'''

                else:
                    str1 = "'" + i + "': [{id: '" + line + "',text: '" + line + "',highlight: '<strong>" + line + "</strong>" + line[
                                                                                                                                1:] + "'}],"

                    file.write(str1)
                    file.write('\n')

                ''' file.write("'{}': [".format(i))

                file.write("{")

                file.write(
                    "\nid: '{}',\ntext: '{}',\nhighlight: '<strong>{}</strong>{}'\n".format(pre, pre, i, pre[1:]))
                file.write("}],")'''
                b = b + 1
        if not pre2:

            b = 0
            for i in pre:
                if b >= 1:
                    a = pre[0:b]
                    str1 = "'" + a + "': [{id: '" + pre + "',text: '" + pre + "',highlight: '<strong>" + a + "</strong>" + pre[
                                                                                                                           len(
                                                                                                                               a):] + "'}],"
                    file.write(str1)
                    file.write('\n')
                    '''file.write("'{}': [".format(i))
  
                    file.write("{")
  
                    file.write(
                        "\nid: '{}',\ntext: '{}',\nhighlight: '<strong>{}</strong>{}'\n".format(pre, pre, i, pre[len(a):]))
                    file.write("}],")'''

                else:
                    str1 = "'" + i + "': [{id: '" + pre + "',text: '" + pre + "',highlight: '<strong>" + i + "</strong>" + pre[
                                                                                                                           1:] + "'}],"

                    file.write(str1)
                    file.write('\n')

                ''' file.write("'{}': [".format(i))
  
                    file.write("{")
  
                    file.write(
                        "\nid: '{}',\ntext: '{}',\nhighlight: '<strong>{}</strong>{}'\n".format(pre, pre, i, pre[1:]))
                    file.write("}],")'''
                b = b + 1

        else:
            print('failed')

    '''
        '夏目': [
                {
                    id: '夏目　漱石',
                    text: '夏目　漱石',
                    highlight: '<strong>夏目</strong>　漱石'
                }
                ],
                '''
