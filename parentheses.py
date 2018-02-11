import re


def without_regexp(line_lst):
    print('--------------- Without regexp ---------------------')
    for line in line_lst:
        print('--- initial:', line)
        dic = {}
        i = 0
        j = 0
        while i != -1:
            i = line.find('(', i + 1)
            j = line.find(')', j + 1)
            dic[i] = 'i'
            dic[j] = 'j'
        # print(dic)

        parenthesis_count = 0
        start_index = 0
        start_index2 = 0
        end_index = 0
        distance_more_than_one = False
        new_line = ''
        for k in sorted(dic.keys())[1:]:
            if dic[k] == 'i' and not parenthesis_count:
                parenthesis_count += 1
                end_index = k
                new_line += line[start_index:end_index]
                distance_more_than_one = False
                start_index = k
                continue
            elif dic[k] == 'i' and parenthesis_count >= 1:
                start_index2 = k
                parenthesis_count += 1
                continue
            elif dic[k] == 'j' and parenthesis_count == 2:
                end_index = k + 1
                if start_index2 - start_index == 1:
                    new_line += line[start_index:end_index]
                    parenthesis_count = 0
                    distance_more_than_one = False
                    start_index = k + 1
                else:
                    parenthesis_count -= 1
                    distance_more_than_one = True
                continue
            elif dic[k] == 'j' and parenthesis_count == 1:
                end_index = k + 1
                parenthesis_count -= 1
                if distance_more_than_one and parenthesis_count:
                    new_line += ''
                else:
                    new_line += line[start_index:end_index]
                start_index = k + 1
                continue
        print('+++  result:', new_line)


def sub_func(m):
    new = m.group(0)[0]
    return f'{new}'


def with_regexp(line_lst):
    print('\n--------------- With regexp ---------------------')
    for line in line_lst:
        print('--- initial:', line)
        new_line = re.sub(r'[^(]([(][a-zA-Z0-9]+.+)', sub_func, line)
        print('+++  result:', new_line)


if __name__ == '__main__':
    line_lst = [
        'abra((esdf)(esdf',
        'abra((esdf)abc((esdf)',
        'abra((esdf)abc(hjkk(vsdf))',
        'abra((esdf)abc(hjkk(vsdf)',
        'abra((esdf)abc(hjkk(vsdf',
        'abra((esdf)abc((vsdf)',
        'abra((esdf)abc((vsdf)((fgj))hjk((((ghj)'
    ]
    without_regexp(line_lst)
    with_regexp(line_lst)
