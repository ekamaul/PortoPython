import pandas as pd

import json




df = pd.read_csv ("F:\\10. Project\\Dashboard\\Parameter\\M_Table.csv" , sep = "\;")
dfreg = df["Region"].tolist()
regset = set(dfreg)

print(regset)

dfest = df["ESTNR"].tolist()
dfcomp = df["Company"].tolist()
dfestname = df["EstName"].tolist()

dfprov = df["Province"].tolist() #special case for province, clean the data (white space remove)

provcln = []
for pr in dfprov:
    x = pr[:-33]
    provcln.append(x)


compdict = dict(zip(dfest , dfcomp))
estnamedict = dict(zip(dfest , dfestname))
provdict = dict(zip(dfest , provcln))




reglist = {} #membuat dict 

for reg in regset: #membuat list estate region
    df = pd.read_csv ("F:\\10. Project\\Dashboard\\Parameter\\M_Table.csv" , sep = "\;")
    query = 'Region ==' +"'"+ reg +"'"
    df.query(query, inplace=True) #query
    EstList = df["ESTNR"].tolist() #membuat estate list
    reglist.update({reg : EstList}) #menambahkan satu persatu estate ke dalam dict
    
reglist.update({"Company" : compdict}) #add company dict to reglist
reglist.update({"Province" : provdict}) #and soon
reglist.update({"EstateName" : estnamedict}) #and soon


# Create json file and write list on it


jsonString = json.dumps(reglist, indent=4) #pake metode dumps dan indet = 4 biar rapih dan enak terbaca
jsonFile = open("F:\\10. Project\\Dashboard\\Parameter\\MasterData.json", "w")
jsonFile.write(jsonString)
jsonFile.close()

