import os




Region4 = [
    "DAD01", 
    "DAD02", 
    "DAD03",
    "DAD04",
    "DIE01",
    "DDC01",
    "DAA02",
    "DIF01",
    "DBX01",
    "DBV04",
    "DPV01"
    
]

Region5 = [
    "ERA01",
    "ERA02",
    "ERA03",
    "EKD01",
    "EKD02",
    "EKD03",
    "EMD01",
    "EMD02"

]

Region3 = [
    "CBV01",
    "CBV02",
    "CBV03",
    "CMH01",
    "CMH02",
    "CAA01",
    "CTC01",
    "CTC02",
    "CTC03"


]

KodeEstate = Region3 + Region4 + Region5

CCline = [
    "RFM",
    "DRN",
    "DST",
    "RSF"
    

]

CCpoint = [
    "CVT",
    "BRD",
    "FTB"

]

CCpoly = [
    "FEL",
    "STK",
    "UBR"

]


DataCC = CCline + CCpoint + CCpoly

INV_line = [
    "BLN",
    "IRD",
    
]

INV_point = [
    "PTA",


]

INV_poly = [
    "LUS",
    

]

def Input1():

    global Estatelist
    Estatelist = str(input("Masukan Kode = ")).split(", ")
    return Estatelist



def listvar():

    global RegRep, RegLocal, RegCloud, EstateCloud, TempPath, CartographPathReg4
    global PathGabungLocal, PathGabungCloud, PathGabungRep
    global BDY, BLK, SBK, LUS, IRD, PTA, BLN, HCV, HCM
    global IRDC, LUSC, MP
    
    Reg3R = "REGION03_REP.gdb"
    Reg4R = "REGION04_REP.gdb"
    Reg5R = "REGION05_REP.gdb"

    Reg3L = "CopyCloud_REGION03.gdb"
    Reg4L = "CopyCloud_REGION04.gdb"
    Reg5L = "CopyCloud_REGION05.gdb"

    Reg3C = "REGION03_Cloud.sde"
    Reg4C = "REGION04_Cloud.sde"
    Reg5C = "REGION05_Cloud.sde"

    def chooseRegR():
        if Estate in Region4:
            return Reg4R
        elif Estate in Region5:
            return Reg5R
        elif Estate in Region3:
            return Reg3R

    def chooseRegL():
        if Estate in Region4:
            return Reg4L
        elif Estate in Region5:
            return Reg5L
        elif Estate in Region3:
            return Reg3L

    def chooseRegC():
        if Estate in Region4:
            return Reg4C
        elif Estate in Region5:
            return Reg5C
        elif Estate in Region3:
            return Reg3C

    RegRep = "F:\\16. DatabaseCopyCloud\\" + str(chooseRegR())
    RegLocal = "F:\\16. DatabaseCopyCloud\\" + str(chooseRegL())
    RegCloud = "F:\\ArcGISPro Project\\OpenSDE\\" + str(chooseRegC())
    
    TempPath = "C:\\Temp"
    CartographPathReg4 = "F:\\3. Cartograph\\1. Data\\CartographDatabase.gdb\\INV_KalbarUTM49N"
    EstateCloud = str("REGION004.REGION004." + Estate)
    PathGabungLocal = os.path.join(RegLocal, Estate)
    PathGabungCloud = os.path.join(RegCloud, EstateCloud)
    PathGabungRep = os.path.join(RegRep, Estate)

    BDY = Estate + "4BDY3"
    BLK = Estate + "4BLK3"
    SBK = Estate + "4SBK3"
    LUS = Estate + "4LUS3"
    IRD = Estate + "4IRD2"
    PTA = Estate + "4PTA1"
    BLN = Estate + "4BLN2"
    HCV = Estate + "7HCV3"
    HCM = Estate + "7HCM3"
    
    IRDC = "REGION004.REGION004." + IRD
    LUSC = "REGION004.REGION004." + LUS
    MP = "Multi_Part"



def ceklockfile():
    def setreg():
        global Estate
        global setdata
        jf = []
        for Estate in Estatelist:
            listvar()
            jf.append(RegLocal)
        setdata = set(jf)
    setreg()

    jh = []
    for dir in setdata:
        dir_list = os.listdir(dir)
        def flock():
            h = []
            for c in dir_list:
                splitup = os.path.splitext(c)
                h.append(splitup[1])    
            if ".lock" in h:
                return True
            else :
                return False
        jh.append(flock())

    
    if True in jh:
        return True
    else :
        return False
        
        





