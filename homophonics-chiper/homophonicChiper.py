# Declare a dictionary 
dict = [{'codes': ['10', '48', '22', '36', '24', '13', '42', '06'], 'current_index': 0, 'total': 8},
        {'codes': ['37'], 'current_index': 0, 'total': 1},
        {'codes': ['57', '77', '92'], 'current_index': 0, 'total': 3},
        {'codes': ['99', '56', '96', '30'], 'current_index': 0, 'total': 4},
        {'codes': ['89', '85', '47', '28', '91', '63', '55', '09', '07', '11', '51', '08'], 'current_index': 0, 'total': 12},
        {'codes': ['02', '01'], 'current_index': 0, 'total': 2},
        {'codes': ['52', '16'], 'current_index': 0, 'total': 2},
        {'codes': ['05', '66', '54', '32', '29', '33'], 'current_index': 0, 'total': 6},
        {'codes': ['81', '67', '00', '74', '58', '72', '71'], 'current_index': 0, 'total': 7},
        {'codes': ['69'], 'current_index': 0, 'total': 1},
        {'codes': ['25'], 'current_index': 0, 'total': 1},
        {'codes': ['76', '17', '95', '46'], 'current_index': 0, 'total': 4},
        {'codes': ['50', '15'], 'current_index': 0, 'total': 2},
        {'codes': ['04', '98', '34', '70', '53', '97'], 'current_index': 0, 'total': 6},
        {'codes': ['90', '64', '40', '18', '62', '73', '49'], 'current_index': 0, 'total': 7},
        {'codes': ['38', '93'], 'current_index': 0, 'total': 2},
        {'codes': ['31'], 'current_index': 0, 'total': 1},
        {'codes': ['78', '20', '59', '39', '21', '26'], 'current_index': 0, 'total': 6},
        {'codes': ['88', '65', '79', '94', '83', '27'], 'current_index': 0, 'total': 6},
        {'codes': ['41', '35', '68', '19', '87', '82', '60', '23', '14', '43'], 'current_index': 0, 'total': 10},
        {'codes': ['12', '61', '84'], 'current_index': 0, 'total': 3},
        {'codes': ['44'], 'current_index': 0, 'total': 1},
        {'codes': ['86', '45'], 'current_index': 0, 'total': 2},
        {'codes': ['80'], 'current_index': 0, 'total': 1},
        {'codes': ['03'], 'current_index': 0, 'total': 1},
        {'codes': ['75'], 'current_index': 0, 'total': 1}
        ]


#string for encryption
#Arabic knowledge of cryptography was fully set forth in a section on cryptology in an enormous fourteen-volume encyclopedia written
#to afford the secretary class a systematic survey of all the important branches of knowledge
s="Arabic knowledge of cryptography was fully set forth in a section on cryptology in an enormous fourteen-volume encyclopedia written to afford the secretary class a systematic survey of all the important branches of knowledge"
s=s.lower()
encryption=""

for ch in s:
    if(97<= ord(ch)<=122):
        ind=(ord(ch)-97)%26
        if(dict[ind]['current_index']>=dict[ind]['total']):
            dict[ind]['current_index']=0
        c=dict[ind]['current_index']
        encryption+=dict[ind]['codes'][c]
        dict[ind]['current_index']+=1
        
print(encryption)
