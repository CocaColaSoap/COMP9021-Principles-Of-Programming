# Uses National Data on the relative frequency of given names in the population of U.S. births,
# stored in a directory "names", in files named "yobxxxx.txt with xxxx being the year of birth.
#
# Prompts the user for a first name, and finds out the first year
# when this name was most popular in terms of frequency of names being given,
# as a female name and as a male name.
#
# Written by *** and Eric Martin for COMP9021


import os


first_name = input('Enter a first name: ')
directory = 'names'
min_male_frequency = 0
male_first_year = None
min_female_frequency = 0
female_first_year = None

# Replace this comment with your code
for filename in (os.listdir(directory)):
    if filename.endswith('.txt') :
        female_sum = 0
        male_sum = 0
        male_number = 0
        female_number = 0
        year = int(filename[3:7])
        with open(directory +'/' + filename) as data_file:
            for line in data_file:
                line = line.strip('\n').split(',')
                if str(line[1])=='F':
                    female_sum += int(line[2])
                else:
                    male_sum +=int(line[2])
                if(first_name==str(line[0]) and str(line[1])=='M'):
                    male_number = int(line[2])
                if(first_name==str(line[0]) and line[1]=='F'):
                    female_number = int(line[2])
            if(male_sum!=0):
                if(min_male_frequency<((male_number/male_sum)*100)):
                    min_male_frequency=(male_number/male_sum)*100
                    male_first_year=year
            if(female_sum!=0):
                if(min_female_frequency<((female_number/female_sum)*100)):
                    min_female_frequency=female_number/female_sum*100
                    female_first_year=year
if not female_first_year:
    print(f'In all years, {first_name} was never given as a female name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a female name first in the year {female_first_year}.\n'
          f'  It then accounted for {min_female_frequency:.2f}% of all female names.'
         )
if not male_first_year:
    print(f'In all years, {first_name} was never given as a male name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a male name first in the year {male_first_year}.\n'
          f'  It then accounted for {min_male_frequency:.2f}% of all male names.'
         )

