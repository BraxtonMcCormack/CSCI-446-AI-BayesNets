'''alarm'''
alarmQ = ['HYPOVOLEMIA', 'LVFAILURE', 'ERRLOWOUTPUT']

alarmE1 = {
    'HRBP': 'HIGH',
    'CO': 'LOW',
    'BP': 'HIGH'
}

alarmE2 = {
    'HRBP': 'HIGH',
    'CO': 'LOW',
    'BP': 'HIGH',
    'HRSAT': 'LOW',
    'HREKG': 'LOW',
    'HISTORY': 'TRUE'
}
'''child'''
childQ = ['Disease']

childE1 = {
    'LowerBodyO2': '<5',
    'RUQO2': '>=12',
    'CO2Report': '>=7.5',
    'XrayReport': 'Asy/Patchy'
}

childE2 = {
    'LowerBodyO2': '<5',
    'RUQO2': '>=12',
    'CO2Report': '>=7.5',
    'XrayReport': 'Asy/Patchy',
    'GruntingReport': 'Yes',
    'LVHReport': 'Yes',
    'Age': '11-30 Days'
}
'''hailfinder'''
hfQ = ['SatContMoist', 'LLIW']

hfE1 = {
    'RSFcst': 'XNIL',
    'N32StarFcst': 'XNIL',
    'MountainFcst': 'XNIL',
    'AreaMoDryAir': 'VeryWet'
}

hfE2 = {
    'RSFcst': 'XNIL',
    'N32StarFcst': 'XNIL',
    'MountainFcst': 'XNIL',
    'AreaMoDryAir': 'VeryWet',
    'CombVerMo': 'Down',
    'AreaMeso_ALS': 'Down',
    'CurPropConv': 'Strong'
}
'''insurance'''
insuranceQ = ['MedCost', 'ILiCost', 'PropCost']

insuranceE1 = {
    'Age': 'Adolescent',
    'GoodStudent': 'False',
    'SeniorTrain': 'False',
    'DrivQuality': 'Poor'
}

insuranceE2 = {
    'Age': 'Adolescent',
    'GoodStudent': 'False',
    'SeniorTrain': 'False',
    'DrivQuality': 'Poor',
    'MakeModel': 'Luxury',
    'CarValue': 'FiftyThousand',
    'DrivHistory': 'Zero'
}

'''win95pts'''
winQ = ['Problem1', 'Problem2', 'Problem3', 'Problem4', 'Problem5', 'Problem6']

winE1 = {
    'Problem1': 'No_Output'
}

winE2 = {
    'Problem2': 'Too_Long'
}

winE3 = {
    'Problem3': 'No'
}

winE4 = {
    'Problem4': 'No'
}

winE5 = {
    'Problem5': 'No'
}

winE6 = {
    'Problem6': 'Yes'
}