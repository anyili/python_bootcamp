"""
    Copyright (c) 2019, 2020, Memorial Sloan Kettering Cancer Center (MSKCC)
    All rights reserved.
    Unauthorized copying of this file, via any medium is strictly prohibited.
    MSKCC PROPRIETARY/CONFIDENTIAL. Use is subject to license terms.
 
"""

# variable and type

age = 20
name = 'python'
is_patient = True

print(age)
print(name)
print(is_patient)

# dict
person = {
    'age': 20,
    'name': 'python',
    'is_patient': False
}
print(person['age'])

# list
teams = ['Team A', 'Team B', 'Team R']
print(teams[2])
print(teams[1])

# control

if len(teams) > 1:
    print('more than 1 team')
if 'Team B' in teams:
    print('there is Team B')

# loop
for team in teams:
    print(team)

# list comprehension

teams_lower = [team.lower() for team in teams]
for team in teams_lower:
    print(team)
    print(team + '?')


# method
def reformat(p):
    str_formatted = 'name: {}, age: {}'.format(p['name'], p['age'])
    return str_formatted

print(reformat(person))
