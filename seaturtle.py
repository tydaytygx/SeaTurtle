import requests
import urllib
import urllib.request
import re
import os
import shutil
import xlwt


def tab_setter():
    global wbk
    global sheet
    # sheet_count = 0  # sheet control
    head_list = []
    wbk = xlwt.Workbook(encoding='ascii')
    sheet = wbk.add_sheet('sheet 1', cell_overwrite_ok=True)
    head_list.append('Name')
    head_list.append('Spices')
    head_list.append('Life Stage')
    head_list.append('Release Date')
    head_list.append('Days Transmitted')
    head_list.append('Straight Line Distance Travelled')
    head_list.append('Total Distance Travelled')
    for v in range(7):
        sheet.write(1, v, head_list[v])


def file_picker(path):
    global file_list
    sheet_count = 2
    file_detail = ''
    folder_path = os.getcwd()
    file_list = []

    for v in range(len(folder_path)):
        file_list = os.listdir(folder_path + '\\' + path)

    # for v in range(len(file_list)):
    #     Output_object_detail(file_list[v], sheet_count)
    #     sheet_count = sheet_count + 1


def createFile(filePath):
    if os.path.exists(filePath):  # If folder exists
        shutil.rmtree(filePath)
    else:  # File doesn't exist
        print('No such file:%s' % filePath)

    if os.path.exists(filePath):
        print('%s: exists' % filePath)
    else:
        try:
            os.mkdir(filePath)
            print('New folder：%s' % filePath)
        except Exception as e:
            os.makedirs(filePath)
            print('New multi-sub-folder：%s' % filePath)


# def File_Checker(): # Check if output files exist or not

#     if(os.path.exists('seaturtle.html')):
#         os.remove('seaturtle.html') # Check html file
#     elif(os.path.exists('seaturtle_out.md')):
#         os.remove('seaturtle_out.md') # Check output file


def File_Checker(project_name):  # Check if output files exist or not
    if(os.path.exists(project_name + '.html')):
        os.remove(project_name + '.html')  # Check html file
    elif(os.path.exists(project_name + '_out.md')):
        os.remove(project_name + '_out.md')  # Check output file

# Turtle project


def Turtle_Spider(project_name_url):
    page = 0  # This loop may not suit this site, use when necessary
    while(page < 1):

        url = project_name_url  # Project page

        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

        r = requests.get(url)
        r = requests.get(url, headers=header)

        content = r.text

        f = open('seaturtle.html', 'w', encoding='UTF-8', errors='ignore')
        print(r.text, file=f)

        f.close()
        print('Completed with ' + r.encoding)  # Site 's HTML encoding
        page = page + 1


def Turtle_Inside_Spider(project_name_url, project_name):
    object_count = 0  # This loop may not suit this site, use when necessary
    while(object_count < 1):

        url = project_name_url  # Project page

        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

        r = requests.get(url)
        r = requests.get(url, headers=header)

        content = r.text

        f = open('html\seaturtle_%s.html' % project_name,
                 'w', encoding='UTF-8', errors='ignore')
        print(r.text, file=f)

        f.close()
        print('Completed with ' + r.encoding)  # Site 's HTML encoding
        object_count = object_count + 1


def getNonRepeatList(data):  # No-repeat tool
    return [i for n, i in enumerate(data) if i not in data[:n]]


def Output_object():
    sheet_count_object = 2
    count = 0
    seaturtle_name = []

    with open('seaturtle.html', 'r', encoding='UTF-8', errors='ignore') as f2:
        line = f2.readline()
        list1 = []

        while line:

            try:
                line = f2.readline()

                if '#999' in line:
                    # Link

                    print(re.findall(
                        r'<tr style="color:#999"><th><a\shref="(.+?)">.*</a>', line)[0])
                    # Name
                    print('Names: ' + re.findall(
                        r'<tr style="color:#999"><th><a\shref=".*">(.+?)</a>', line)[0])
                    sheet.write(sheet_count_object, 0, re.findall(
                        r'<tr style="color:#999"><th><a\shref=".*">(.+?)</a>', line)[0])

                    # Species
                    print('Species: ' + re.findall(
                        r'</th><td>(.+?)</td><td>.*</td><td>.*</td><td>.*</td><td>.*</td></tr>', line)[0])
                    sheet.write(sheet_count_object, 1, re.findall(
                        r'</th><td>(.+?)</td><td>.*</td><td>.*</td><td>.*</td><td>.*</td></tr>', line)[0])

                    # Life Stage
                    print('Life Stage: ' + re.findall(
                        r'</th><td>.*</td><td>(.+?)</td><td>.*</td><td>.*</td><td>.*</td></tr>', line)[0])
                    sheet.write(sheet_count_object, 2, re.findall(
                        r'</th><td>.*</td><td>(.+?)</td><td>.*</td><td>.*</td><td>.*</td></tr>', line)[0])

                    # Release Date
                    print('Release Date: ' + re.findall(
                        r'</th><td>.*</td><td>.*</td><td>(.+?)</td><td>.*</td><td>.*</td></tr>', line)[0])
                    sheet.write(sheet_count_object, 3, re.findall(
                        r'</th><td>.*</td><td>.*</td><td>(.+?)</td><td>.*</td><td>.*</td></tr>', line)[0])

                    # Last Location
                    # print('Last Location: ' + re.findall(
                    #     r'</th><td>.*</td><td>.*</td><td>.*</td><td>(.+?)</td><td>.*</td></tr>', line)[0])
                    # sheet.write(sheet_count_object, 3, re.findall(
                    #     r'</th><td>.*</td><td>.*</td><td>.*</td><td>(.+?)</td><td>.*</td></tr>', line)[0])

                    # Days transmitted
                    print('Days transmitted: ' + re.findall(
                        r'</th><td>.*</td><td>.*</td><td>.*</td><td>.*</td><td>(.+?)</td></tr>', line)[0])
                    sheet.write(sheet_count_object, 4, re.findall(
                        r'</th><td>.*</td><td>.*</td><td>.*</td><td>.*</td><td>(.+?)</td></tr>', line)[0])

                    seaturtle_name.append(re.findall(
                        r'<tr style="color:#999"><th><a\shref=".*">(.+?)</a>', line)[0])
                    # seaturtle_name.append('http://www.seaturtle.org' + re.findall(r'<tr style="color:#999"><th><a\shref=".*">(.+?)</a>', line)[0])
                    Turtle_Inside_Spider(r'http://www.seaturtle.org' + re.findall(r'<tr style="color:#999"><th><a\shref="(.+?)">.*</a>', line)[
                                         0], re.findall(r'<tr style="color:#999"><th><a\shref=".*">(.+?)</a>', line)[0])
                    count = count + 1
                    print('NO.' + str(count))
                    print(
                        '----------------------------------------------------------------->>>')
                    sheet_count_object = sheet_count_object + 1
            except OSError:
                pass

    print('done')


# def Output_object_detail(file_list_inside, sheet_count):
#     seaturtle_name = []
#     with open('html' + '\\' + file_list_inside, 'r', encoding='UTF-8', errors='ignore') as f2:
#         line = f2.readline()
#         list1 = []

#         while line:

#             try:
#                 line = f2.readline()
#                 # print(line)
#                 if '<h2 align="center">' in line:
#                     print('Name: ' + re.findall(
#                         r'<h2 align="center">(.+?)</h2>', line)[0])
#                     sheet.write(sheet_count, 0, re.findall(
#                         r'<h2 align="center">(.+?)</h2>', line)[0])
#                 if '<b>Species:</b>' in line:
#                     print(
#                         'Species: ' + re.findall(r'<b>Species:</b>\s(.+?)<br\s/>', line)[0])
#                     sheet.write(sheet_count, 1, re.findall(
#                         r'<b>Species:</b>\s(.+?)<br\s/>', line)[0])
#                 if '<b>Life Stage:</b>' in line:
#                     print(
#                         'Life Stage: ' + re.findall(r'<b>Life\sStage:</b>\s(.+?)<br\s/>', line)[0])
#                     sheet.write(sheet_count, 2, re.findall(
#                         r'<b>Life\sStage:</b>\s(.+?)<br\s/>', line)[0])
#                 if '<b>Gender:</b>' in line:
#                     print(
#                         'Gender: ' + re.findall(r'<b>Gender:</b>\s(.+?)<br\s/>', line)[0])

#                 if '<b>Release Date:</b>' in line:
#                     print(
#                         'Release Date: ' + re.findall(r'<b>Release Date:</b>\s(.+?)<br\s/>', line)[0])
#                     sheet.write(sheet_count, 3, re.findall(
#                         r'<b>Release Date:</b>\s(.+?)<br\s/>', line)[0])

#                 if '<b>Release Location:</b>' in line:
#                     print(
#                         'Release Location: ' + re.findall(r'<b>Release Location:</b>\s(.+?)<br\s/>', line)[0])

#                 # if '<b>Last Location:</b>' in line:
#                 #     print(
#                 #         'Last Location: ' + re.findall(r'<b>Last Location:</b>\s(.+?)</p>', line)[0])

#                 # <b>Last Location:</b> 2017-12-31 00:00:00</p>

#                     print(
#                         '----------------------------------------------------------------->>>')

#             except OSError:
#                 pass

#     print('done')


if __name__ == '__main__':
    tab_setter()
    # createFile(os.getcwd() + '\img')
    # createFile(os.getcwd() + '\html')
    # File_Checker('seaturtle')
    Turtle_Spider('http://www.seaturtle.org/tracking/?project_id=687')
    Output_object()
    # file_picker('html')
    wbk.save("test.csv")
