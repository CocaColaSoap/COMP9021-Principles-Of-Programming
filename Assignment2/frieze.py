import sys


class FriezeError(Exception):
    def __init__(self, message):
        self.message = message


class Frieze:
    def __init__(self, filename):
        global filename_1
        global period
        filename_1 = filename
        try:
            file = open(filename)
            count = 0
            global LL
            LL = []
            for line in file:
                line = line.split()
                if len(line) == 0:
                    continue
                if (len(line)-1 < 4) or (len(line)-1 > 50):
                    raise FriezeError('Incorrect input.')
                    sys.exit()
                if len(LL) == 0 and (len(line)-1 >= 4) and (len(line)-1 <= 50):
                    L = []
                    for item in line:
                        try:
                            item =int(item)
                        except ValueError:
                            sys.exit()
                        if 0<= item <= 15:
                            L.append(item)
                        else:
                            raise FriezeError('Incorrect input.')
                            sys.exit()
                    LL.append(L)
                    length = len(line)
                else:
                    if length != len(line):
                        raise FriezeError('Incorrect input.')
                        sys.exit()
                    else:
                        L = []
                        for item in line:
                            try:
                                item = int(item)
                            except ValueError:
                                sys.exit()
                            if 0 <= item <= 15:
                                L.append(item)
                            else:
                                raise FriezeError('Incorrect input.')
                                sys.exit()
                        LL.append(L)
                        length = len(line)
                count += 1
            if (count-1 < 2) or (count-1 > 16):
                raise FriezeError('Incorrect input.')
                sys.exit()
        except FileNotFoundError:
            sys.exit()

        if LL[0][-1] != 0:
            raise FriezeError('Input does not represent a frieze.')
            sys.exit()

        for item in (LL[-1]):
            if item >= 8:
                raise FriezeError('Input does not represent a frieze.')
                sys.exit()

        for i in range(len(LL)):
            if LL[i][-1] > 1:
                raise FriezeError('Input does not represent a frieze.')
                sys.exit()

        for i in range(len(LL[0])-1):
            if LL[0][i] != 4 and LL[0][i] != 12:
                raise FriezeError('Input does not represent a frieze.')
                sys.exit()

        for i in range(1,len(LL)-1):
            for j in range(len(LL[0])):
                List = [2, 3, 6, 7, 10, 11, 14, 15]
                if LL[i][j] >= 8 and LL[i+1][j] in List:
                    raise FriezeError('Input does not represent a frieze.')
                    sys.exit()

        # L_0 = []
        # L_last =[]
        # for i in range(len(LL[0])-1):
        #     L_0.append(LL[0][i])
        #     L_last.append(LL[-1][i])
        # # print(L_0)
        # # print(L_last)
        # flag_equal = False
        # for i in range(len(L_0)):
        #     x = L_0[0]
        #     y = L_last[0]
        #     if x == L_0[i] and y == L_last[i]:
        #         continue
        #     else:
        #         flag_equal =True
        # if flag_equal == False:
        #     count_0 = 0
        #     for i in range(1,len(LL)-1):
        #         for j in range(len(LL[0])):
        #             if LL[i][j] == 0:
        #                 count_0 +=1
        #
        #     if count_0 == (len(LL)-2) *(len(LL[0])):
        #         raise FriezeError('Input does not represent a frieze.')
        #         sys.exit()
        #
        #     count_1 = 0
        #     for i in range(1, len(LL) - 1):
        #         for j in range(len(LL[0])):
        #             if LL[i][j] == 1:
        #                 count_1 += 1
        #
        #     if count_1 == (len(LL) - 2) * (len(LL[0])):
        #         raise FriezeError('Input does not represent a frieze.')
        #         sys.exit()




        period = 0
        for size in range(2,round(len(LL[0])/2)+1):
            flag = False
            counter = 1
            ll_compare = []
            ll_compare_back = []
            for i in range(0,size):
                for j in range(0,len(LL)):
                    ll_compare.append(LL[j][i])
            for k in range(size,len(LL[0])-size,size):
                for g in range(0, size):
                    for h in range(0,len(LL)):
                        ll_compare_back.append(LL[h][k+g])
                if ll_compare == ll_compare_back:
                    counter += 1
                    if (size * counter) == (len(LL[0])-1):
                        period = size

                        flag = True
                        break
                ll_compare_back.clear()
            if flag is True:
                break
        if period < 2:
            raise FriezeError('Input does not represent a frieze.')

    def display(self):
        l_using_1 = [1, 3, 5, 7, 9, 11, 13, 15]
        l_using_2 = [2, 3, 6, 7, 10, 11, 14, 15]
        l_using_4 = [4, 5, 6, 7, 12, 13, 14, 15]
        l_using_8 = [8, 9, 10, 11, 12, 13, 14, 15]

        filename = str(filename_1.split('.txt')[0])+'.tex'
        file = open(filename,'w')
        file.write('\documentclass[10pt]{article}\n')
        file.write('\\usepackage{tikz}\n')
        file.write('\\usepackage[margin=0cm]{geometry}\n')
        file.write('\pagestyle{empty}\n')
        file.write('\n')
        file.write('\\begin{document}\n')
        file.write('\n')
        file.write('\\vspace*{\\fill}\n')
        file.write('\\begin{center}\n')
        file.write('\\begin{tikzpicture}[x=0.2cm, y=-0.2cm, thick, purple]\n')
        file.write('% North to South lines\n')
        l_north_to_south=[]
        for j in range((len(LL[0]))):
            for i in range(len(LL)):
                if LL[i][j] in l_using_1:
                    l_north_to_south.append((j, i))

        for i in range(len(l_north_to_south)):
            if(l_north_to_south[i][0],l_north_to_south[i][1]-1) in l_north_to_south:
                continue
            begin = (l_north_to_south[i][0],l_north_to_south[i][1]-1)
            end = l_north_to_south[i]
            while end in l_north_to_south:
                end = (end[0],end[1]+1)
            file.write(f'    \draw ({begin[0]},{begin[1]}) -- ({end[0]},{end[1]-1});\n')

        file.write('% North-West to South-East lines\n')
        l_northwest_to_southeast = []
        for i in range(len(LL)):
            for j in range(len(LL[0])):
                if LL[i][j] in l_using_8:
                    l_northwest_to_southeast.append((j, i))

        for i in range(len(l_northwest_to_southeast)):
            if (l_northwest_to_southeast[i][0] - 1, l_northwest_to_southeast[i][1] - 1) in l_northwest_to_southeast:
                continue
            begin = l_northwest_to_southeast[i]
            end = (l_northwest_to_southeast[i][0] + 1, l_northwest_to_southeast[i][1] + 1)
            while end in l_northwest_to_southeast:
                end = (end[0] + 1, end[1] + 1)
            file.write(f'    \draw ({begin[0]},{begin[1]}) -- ({end[0]},{end[1]});\n')

        file.write('% West to East lines\n')
        l_west_to_east = []
        for i in range(len(LL)):
            for j in range(len(LL[0])):
                if LL[i][j] in l_using_4:
                    l_west_to_east.append((j, i))

        for i in range(len(l_west_to_east)):
            if (l_west_to_east[i][0] - 1, l_west_to_east[i][1]) in l_west_to_east:
                continue
            begin = l_west_to_east[i]
            end = (l_west_to_east[i][0] + 1, l_west_to_east[i][1])
            while end in l_west_to_east:
                end = (end[0] + 1, end[1])
            file.write(f'    \draw ({begin[0]},{begin[1]}) -- ({end[0]},{end[1]});\n')

        file.write('% South-West to North-East lines\n')
        l_southwest_to_north_east = []
        for i in range(len(LL)):
            for j in range(len(LL[0])):
                if LL[i][j] in l_using_2:
                    l_southwest_to_north_east.append((j, i))

        for i in range(len(l_southwest_to_north_east)):
            if (l_southwest_to_north_east[i][0]-1, l_southwest_to_north_east[i][1]+1) in l_southwest_to_north_east:
                continue
            begin = l_southwest_to_north_east[i]
            end = (l_southwest_to_north_east[i][0]+1,l_southwest_to_north_east[i][1]-1)
            while end in l_southwest_to_north_east:
                end = (end[0]+1,end[1]-1)
            file.write(f'    \draw ({begin[0]},{begin[1]}) -- ({end[0]},{end[1]});\n')
        file.write('\end{tikzpicture}\n')
        file.write('\end{center}\n')
        file.write('\\vspace*{\\fill}\n')
        file.write('\n')
        file.write('\end{document}\n')
        file.close()

    def analyse(self):
        l_using_1 = [1, 3, 5, 7, 9, 11, 13, 15]
        l_using_2 = [2, 3, 6, 7, 10, 11, 14, 15]
        l_using_4 = [4, 5, 6, 7, 12, 13, 14, 15]
        l_using_8 = [8, 9, 10, 11, 12, 13, 14, 15]

        l_north_to_south = []
        for j in range((len(LL[0]))):
            for i in range(len(LL)):
                if LL[i][j] in l_using_1:
                    l_north_to_south.append((j, i))

        l_total = []
        for i in range(len(l_north_to_south)):
            l_total.append([l_north_to_south[i],(l_north_to_south[i][0],l_north_to_south[i][1]-1)])

        l_northwest_to_southeast = []
        for i in range(len(LL)):
            for j in range(len(LL[0])):
                if LL[i][j] in l_using_8:
                    l_northwest_to_southeast.append((j, i))
        l_8=[]
        for i in range(len(l_northwest_to_southeast)):
            l_total.append([l_northwest_to_southeast[i],(l_northwest_to_southeast[i][0]+1,l_northwest_to_southeast[i][1]+1)])

        l_west_to_east = []
        for i in range(len(LL)):
            for j in range(len(LL[0])):
                if LL[i][j] in l_using_4:
                    l_west_to_east.append((j, i))

        l_4=[]
        for i in range(len(l_west_to_east)):
            l_total.append([l_west_to_east[i],(l_west_to_east[i][0]+1,l_west_to_east[i][1])])

        l_southwest_to_north_east = []
        for i in range(len(LL)):
            for j in range(len(LL[0])):
                if LL[i][j] in l_using_2:
                    l_southwest_to_north_east.append((j, i))

        l_2=[]
        for i in range(len(l_southwest_to_north_east)):
            l_total.append([l_southwest_to_north_east[i], (l_southwest_to_north_east[i][0] + 1, l_southwest_to_north_east[i][1]-1)])


        dict = {}
        for i in range(len(l_total)):
            x=l_total[i][0]
            l_dictory = []
            for j in range(len(l_total)):
                if l_total[j][0] == x:
                    l_dictory.append(l_total[j][1])
                if l_total[j][1] == x:
                    l_dictory.append(l_total[j][0])
            dict_2 = {x:l_dictory}
            dict.update(dict_2)

        for i in range(len(l_total)):
            x=l_total[i][1]
            l_dictory = []
            for j in range(len(l_total)):
                if l_total[j][0] == x:
                    l_dictory.append(l_total[j][1])
                if l_total[j][1] == x:
                    l_dictory.append(l_total[j][0])
            dict_2 = {x:l_dictory}
            dict.update(dict_2)


        flag_horizzontal_reflection = False
        duichengzhou = (len(LL)-1) / 2
        for i in dict:
            L = dict.get(i)
            for j in range(len(L)):
                x1 = i[0]
                y1 = int(duichengzhou * 2 - i[1])
                x2 = L[j][0]
                y2 = int(duichengzhou * 2 - L[j][1])
                L_x1_y1 = dict.get((x1,y1))
                if L_x1_y1 == None:
                    flag_horizzontal_reflection = False
                    break
                else:
                    if (x2,y2) in L_x1_y1:
                        flag_horizzontal_reflection = True
                    else:
                        flag_horizzontal_reflection = False
                        break
            if flag_horizzontal_reflection == False:
                break

        flag_vertical_reflection = False
        duichengzhou = period/2
        while duichengzhou < len(LL[0]):
            a = duichengzhou - period/2 - 1
            b = duichengzhou + period/2 + 1
            for i in dict:
                if a <= i[0] and i[0] <= b:
                    L = dict.get(i)
                    for j in range(len(L)):
                        if a<= L[j][0] and L[j][0]<=b:
                            x1 = int(duichengzhou * 2 - i[0])
                            y1 = i[1]
                            x2 = int(duichengzhou * 2 - L[j][0])
                            y2 = L[j][1]
                            L_x1_y1 = dict.get((x1, y1))
                            if L_x1_y1 == None:
                                flag_vertical_reflection = False
                                break
                            else:
                                if(x2,y2) in L_x1_y1:
                                    flag_vertical_reflection = True
                                else:
                                    flag_vertical_reflection = False
                                    break
                    if flag_vertical_reflection == False:
                        break
            if flag_vertical_reflection == True:
                break
            else:
                duichengzhou += 0.5

        flag_rotation = False
        duichengzhou = period / 2
        while duichengzhou < len(LL[0]):
            a = duichengzhou - period / 2 - 1
            b = duichengzhou + period / 2 + 1
            for i in dict:
                if a<=i[0] and i[0] <=b:
                    L = dict.get(i)
                    for j in range(len(L)):
                        if a<=L[j][0] and L[j][0] <= b:
                            x1 = int(duichengzhou * 2 - i[0])
                            y1 = len(LL) - i[1]-1
                            x2 = int(duichengzhou * 2 - L[j][0])
                            y2 = len(LL) - L[j][1]-1
                            L_x1_y1 = dict.get((x1, y1))
                            if L_x1_y1 == None:
                                flag_rotation = False
                                break
                            else:
                                if (x2, y2) in L_x1_y1:
                                    flag_rotation = True
                                else:
                                    flag_rotation = False
                                    break
                    if flag_rotation == False:
                            break
            if flag_rotation == True:
                    break
            else:
                duichengzhou += 0.5


        flag_glided= False
        duichengzhou = (len(LL) - 1) / 2
        duichengzhou_2=period/2
        while duichengzhou_2 < len(LL[0]):
            a = duichengzhou_2 - period / 2
            b = duichengzhou_2 + period / 2
            for i in dict:
                if a<=i[0] and i[0] <=(b/2):
                    L = dict.get(i)
                    for j in range(len(L)):
                        if a<=L[j][0] and L[j][0] <= b:
                            y1 = int(duichengzhou * 2 - i[1])
                            y2 = int(duichengzhou * 2 - L[j][1])
                            x1 = i[0] + period / 2
                            x2 = L[j][0] + period /2
                            L_x1_y1 = dict.get((x1, y1))
                            if L_x1_y1 == None:
                                flag_glided = False
                                break
                            else:
                                if (x2, y2) in L_x1_y1:
                                    flag_glided = True
                                else:
                                    flag_glided = False
                                    break
                if flag_glided == False:
                        break

            for i in dict:
                if (b/2) <= i[0] and i[0] <= b:
                    L = dict.get(i)
                    for j in range(len(L)):
                        if (b/2) <= L[j][0] and L[j][0] <= b:
                            y1 = int(duichengzhou * 2 - i[1])
                            y2 = int(duichengzhou * 2 - L[j][1])
                            x1 = i[0] - period / 2
                            x2 = L[j][0] - period / 2
                            L_x1_y1 = dict.get((x1, y1))
                            if L_x1_y1 == None:
                                flag_glided = False
                                break
                            else:
                                if (x2, y2) in L_x1_y1:
                                    flag_glided = True
                                else:
                                    flag_glided = False
                                    break
                if flag_glided == False:
                    break
            if flag_glided == True:
                break
            else:
                duichengzhou_2 += 0.5

        # print(flag_glided)
        # print(flag_vertical_reflection)
        # print(flag_horizzontal_reflection)
        # print(flag_rotation)
        # print(period)

        if flag_glided != True and flag_vertical_reflection!= True and flag_rotation!=True and flag_horizzontal_reflection != True:
            print(f'Pattern is a frieze of period {period} that is invariant under translation only.')
        if flag_vertical_reflection == True and flag_glided!= True and flag_rotation!=True and flag_horizzontal_reflection!=True:
            print(f'Pattern is a frieze of period {period} that is invariant under translation\n        and vertical reflection only.')

        if flag_horizzontal_reflection==True and flag_glided!=True and flag_vertical_reflection!= True and flag_rotation!=True:
            print(f'Pattern is a frieze of period {period} that is invariant under translation\n        and horizontal reflection only.')

        if flag_glided == True and flag_horizzontal_reflection != True and flag_vertical_reflection != True and flag_rotation != True:
            print(f'Pattern is a frieze of period {period} that is invariant under translation\n        and glided horizontal reflection only.')
        if flag_rotation == True and flag_horizzontal_reflection != True and flag_vertical_reflection != True and flag_glided != True:
            print(f'Pattern is a frieze of period {period} that is invariant under translation\n        and rotation only.')
        if flag_rotation == True and flag_glided == True and flag_vertical_reflection == True:
            print(f'Pattern is a frieze of period {period} that is invariant under translation,\n        glided horizontal and vertical reflections, and rotation only.')
        if flag_horizzontal_reflection == True and flag_rotation == True and flag_vertical_reflection == True:
            print(f'Pattern is a frieze of period {period} that is invariant under translation,\n        horizontal and vertical reflections, and rotation only.')