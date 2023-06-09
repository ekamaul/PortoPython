
import arcpy
import os
from DataEstate import CCline, CCpoint, CCpoly, DataCC, KodeEstate, Region4, Region5, Region3



class utama:
    
    def Input1():

        global Estatelist
        Estatelist = str(input("Masukan Kode Estate = ")).split(", ")
        return Estatelist

    
    def copydata_N():
        
        arcpy.env.overwriteOutput = True
        arcpy.env.workspace = PathGabungCloud
        DataIn1 = [LUSC]
        arcpy.FeatureClassToGeodatabase_conversion(DataIn1, PathGabungLocal)

    def copydata_Y():
        
        arcpy.env.overwriteOutput = True
        arcpy.env.workspace = PathGabungCloud
        DataIn1 = [LUSC, PTAC, BLNC, IRDC, HCVC, HCMC]
        arcpy.FeatureClassToGeodatabase_conversion(DataIn1, PathGabungLocal)

    def copydata_CC():
        
        arcpy.env.overwriteOutput = True
        arcpy.env.workspace = PathGabungCloud
        DataIn1 = [dataclaim]
        arcpy.FeatureClassToGeodatabase_conversion(DataIn1, PathGabungLocal)

    def dissolvedata():
        arcpy.env.overwriteOutput = True
        arcpy.env.workspace = PathGabungLocal
        DataOutBDY = os.path.join(PathGabungLocal, BDY)
        DataOutBLK = os.path.join(PathGabungLocal, BLK)
        DataOutSBK = os.path.join(PathGabungLocal, SBK)
        DissFieldBDY = ["ESTNR", "Owner", "InOut"]
        DissFieldBLK = ["ESTNR", "Owner", "InOut", "Block"]
        DissFieldSBK = ["ESTNR", "Owner", "InOut", "SubBlock"]
        arcpy.Dissolve_management (LUS, DataOutBDY, DissFieldBDY, None, MP, None, None)
        arcpy.Dissolve_management (LUS, DataOutBLK, DissFieldBLK, None, MP, None, None)
        arcpy.Dissolve_management (LUS, DataOutSBK, DissFieldSBK, None, MP, None, None)

    def select():
        arcpy.env.overwriteOutput = True
        arcpy.env.workspace = CartographPathReg4

        query = str("ESTNR <>" + "'"+ Estate + "'")

        DataOutBLK = os.path.join(TempPath, "BLK_Select")
        DataOutSBK = os.path.join(TempPath, "SBK_Select")
        DataOutBDY = os.path.join(TempPath, "BDY_Select")

        arcpy.Select_analysis("Block", DataOutBLK, query)
        arcpy.Select_analysis("SubBlock", DataOutSBK, query)
        arcpy.Select_analysis("Boundary", DataOutBDY, query)

    def append():
        
        arcpy.env.workspace = PathGabungLocal

        targetBLK = os.path.join(TempPath, "BLK_Select")
        targetSBK = os.path.join(TempPath, "SBK_Select")
        targetBDY = os.path.join(TempPath, "BDY_Select")

        arcpy.Append_management(BLK, targetBLK, "NO_TEST", "", "")
        arcpy.Append_management(SBK, targetSBK, "NO_TEST", "", "")
        arcpy.Append_management(BDY, targetBDY, "NO_TEST", "", "")

    def copydata_afterappend():
        
        arcpy.env.overwriteOutput = True
        arcpy.env.workspace = TempPath
        arcpy.FeatureClassToFeatureClass_conversion("BLK_Select", CartographPathReg4, "Block")
        arcpy.FeatureClassToFeatureClass_conversion("SBK_Select", CartographPathReg4, "SubBlock")
        arcpy.FeatureClassToFeatureClass_conversion("BDY_Select", CartographPathReg4, "Boundary")
        
 
     

            
    def ceklockfile():
        
        def setreg():
            global Estate
            global setdata
            jf = []
            for Estate in Estatelist:
                ut.listvar()
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
        
    


    def listvar():

        global RegRep, RegLocal, RegCloud, EstateCloud, TempPath, CartographPathReg4
        global PathGabungLocal, PathGabungCloud, PathGabungRep
        global BDY, BLK, SBK, LUS, IRD, PTA, BLN, HCV, HCM
        global IRDC, LUSC, PTAC, BLNC, MP, HCVC, HCMC
        global chooseEstC
        


        
        Reg3R = "REGION03_REP.gdb"
        Reg4R = "REGION04_REP.gdb"
        Reg5R = "REGION05_REP.gdb"

        Reg3L = "CopyCloud_REGION03.gdb"
        Reg4L = "CopyCloud_REGION04.gdb"
        Reg5L = "CopyCloud_REGION05.gdb"

        Reg3C = "REGION03_Cloud.sde"
        Reg4C = "REGION04_Cloud.sde"
        Reg5C = "REGION05_Cloud.sde"

        est3C = "REGION003.REGION003."
        est4C = "REGION004.REGION004."
        est5C = "REGION005.REGION005."

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

        def chooseEstC():
            if Estate in Region3:
                return est3C
            elif Estate in Region4:
                return est4C
            elif Estate in Region5:
                return est5C




        RegRep = "F:\\16. DatabaseCopyCloud\\" + str(chooseRegR())
        RegLocal = "F:\\16. DatabaseCopyCloud\\" + str(chooseRegL())
        RegCloud = "F:\\ArcGISPro Project\\OpenSDE\\" + str(chooseRegC())
        
        TempPath = "C:\\Temp"
        CartographPathReg4 = "F:\\3. Cartograph\\1. Data\\CartographDatabase.gdb\\INV_KalbarUTM49N"

        EstateCloud = str(chooseEstC() + Estate)

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
        
        

        

        IRDC = chooseEstC() + IRD
        PTAC = chooseEstC() + PTA
        BLNC = chooseEstC() + BLN
        LUSC = chooseEstC() + LUS
        HCVC = chooseEstC() + HCV
        HCMC = chooseEstC() + HCM


        MP = "Multi_Part"

ut = utama



def startinput_inventory():

    ut.Input1()

    ap = []
    
    for est in Estatelist:
        KodeTrue = est in KodeEstate
        ap.append(KodeTrue)
        

    print(ap)


    if False not in ap:
        ut.ceklockfile()

        if ut.ceklockfile() is False:

            def startinput2():
            
                Input2 = str(input("Apakah Beserta Data PTA, BLN, IRD, HCV, HCM ? (Y/N) = "))
                

                if (Input2 == "N" or Input2 == "n"):
                    global Estate
                    for Estate in Estatelist:
                        ut.listvar()
                        ut.copydata_N()
                    
                                   
                elif (Input2 == "Y" or Input2 == "y"):
                    
                    for Estate in Estatelist:
                        ut.listvar()
                        ut.copydata_Y()
                    
              
                else :
                    print ("Salah Kode, Silahakan Coba Lagi!")
                    startinput2()

                ap = []
                for Estate in Estatelist:
                    ut.listvar()
                    ut.dissolvedata()
                    if Estate in Region4:
                        ut.select()
                        ut.append()
                        ut.copydata_afterappend()
                    ap.append(Estate)
                
                print(str(ap) + " Selesai")

            startinput2()

        else :
            print("Terdapat Lock File di Database Copy Local, Silahakn Tutup Aplikasi yang terkait")

    else :
        print("Terdapat Kode Estate yang Tidak Ditemukan, Silahkan Coba Lagi!")
        startinput_inventory()

def startinput_contractclaim():
    ut.Input1()

    ap = []
    
    for est in Estatelist:
        KodeTrue = est in KodeEstate
        ap.append(KodeTrue)

    print(ap)

    if False not in ap:
        ut.ceklockfile()

        if ut.ceklockfile() is False:

            def startinput2():
                
                InputCC = str(input("Input data Contract Claim yang akan diunduh, contoh : DRN, RFM, CVT, dll  = ")).split(", ")
                apc = []
                for cekInputCC in InputCC:
                    CCtrue = cekInputCC in DataCC
                    apc.append(CCtrue)

                print(apc)


                if False not in apc:

                    ap = []

                    global Estate

                    for Estate in Estatelist:
                        ut.listvar()
                        global CCfor
                        for CCfor in InputCC:
                            global dataclaim
                            def CCforwhat():
                                if CCfor in CCline:
                                    return "2"
                                elif CCfor in CCpoint:
                                    return "1"
                                elif CCfor in CCpoly:
                                    return "3"
        
                            dataclaim =  chooseEstC() + Estate + "1" + CCfor + CCforwhat()

                            ut.copydata_CC()
                        ap.append(Estate)

                    print(str(ap) + " Selesai")

              
                else :
                    print ("Salah Kode, Silahakan Coba Lagi!")
                    startinput2()

                

            startinput2()

        else :
            print("Terdapat Lock File di Database Copy Local, Silahakn Tutup Aplikasi yang terkait")

    else :
        print("Terdapat Kode Estate yang Tidak Ditemukan, Silahkan Coba Lagi!")
        startinput_inventory()

choose_data = str(input("Pilih tipe data (Inventory (I) / ContractClaim (C))= "))

if (choose_data == "I" or choose_data == "i"):
    startinput_inventory()
elif (choose_data == "C" or choose_data == "c"):
    startinput_contractclaim()























 

