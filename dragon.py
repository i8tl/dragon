from fileinput import nextfile
import marshal
from msilib.schema import Error 
import os
import time 
from time import sleep
import base64

BBlack="\033[1;30m"       # Black
BRed="\033[1;31m"         # Red
BGreen="\033[1;32m"       # Green
BYellow="\033[1;33m"      # Yellow
BBlue="\033[1;34m"        # Blue
BPurple="\033[1;35m"      # Purple
BCyan="\033[1;36m"        # Cyan
BWhite="\033[1;37m"       # White
while True :
    print(BRed,"""

                                  ______________
                            ,===:'.,            `-._
    Tik:i8tl                      `:.`---.__         `-._
        FaReS                         `:.     `--.         `.
                                        \.        `.         `.
                                (,,(,    \.         `.   ____,-`.,
                            (,'     `\    \.   ,--.___`.'
                        , ,'  ,--. `, \    \.;'         `
                         `{D, {     \  :    \;
                            V,,'    /  /    //
                            j;;    /  ,' ,-//.    ,---.      ,
                            \;'   /  ,' /  _  \  /  _  \   ,'/
                                  \   `'  / \  `'  / \  `.' /
                                   `.___,'   `.__,'   `.__,'  """,BYellow,"""iG:i._KNiGHT
    """)



    print(BBlue,"---------------------")
    print(BBlue,"|",BGreen,"marshal > > [1]",BBlue,"|")
    print(BBlue,"|-------------------|")
    print(BBlue,"|",BGreen,"base64 > >  [2]",BBlue,"|")
    print(BBlue,"|-------------------|")
    print(BBlue,"|",BGreen,"CAESAR > >  [3]",BBlue,"|")
    print(BBlue,"|-------------------|")
    print(BBlue,"|",BGreen,"TXET > >    [4]",BBlue,"|")
    print(BBlue,"|-------------------|")
    print(BBlue,"|",BGreen,"photo > >   [5]",BBlue,"|")
    print(BBlue,"|-------------------|")
    print(BBlue,"|",BGreen,"EXIT > >    [0]",BBlue,"|")
    print(BBlue,"---------------------")


    print(BWhite)




    
    try :    
        x=input("ENTER NUMBER >>")
        if x=="1":
                os.system('cls' if os.name == 'nt' else 'clear')
                print(BYellow+"""
                *           (           )        (     
                (  `          )\ )     ( /(        )\ )  
                )\))(      ) (()/(     )\())    ) (()/(  """+BRed+"""
                ((_)()\  ( /(  /(_))(  ((_)\  ( /(  /(_)) 
                (_()((_) )(_))(_))  )\  _((_) )(_))(_))   """+BWhite+"""
                |  \/  |((_)_ | _ \((_)| || |((_)_ | |    
                | |\/| |/ _` ||   /(_-<| __ |/ _` || |__  
                |_|  |_|\__,_||_|_\/__/|_||_|\__,_||____| 
        
                """)
                while True :
                    
                    print(BPurple,"""
                ----------------------
                | START  > >     [1] |
                |--------------------|
                | EXIT   > >     [0] |
                ----------------------       
                
                
                """,BWhite)
                    m=input("Enter number :")
                    if m=="1":
                        file=input("Enter filw name >>")
                        rd=open(file).read()
                        nname=input("Enter new name file :")
                        om=compile(rd,"","exec")
                        ento= marshal.dumps(om )
                        nfi=open(nname,"w")
                        nfi.write("import marshal \n")
                        nfi.write("exec(marshal.loads({0}))".format(repr(ento)))
                        nfi.close()
                        print("[                    ] 0% ", end="\r")
                        time.sleep(0.5)
                        print("[=====               ] 25%", end="\r")
                        time.sleep(0.5)
                        print("[==========          ] 50%", end="\r")
                        time.sleep(0.5)
                        print("[===============     ] 75%", end="\r")
                        time.sleep(0.5)
                        print("[====================] 100%", end="\r")
                        time.sleep(0.25)
                        print("Done !")
                    elif m=="0":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(BWhite)
                        break

        elif x=="2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(BGreen,"""
            
           '########:::::'###:::::'######::'########:""",BPurple,""":'#######::'##::::::::""",BGreen,"""
            ##.... ##:::'## ##:::'##... ##: ##.....::""",BPurple,"""'##.... ##: ##:::'##::""",BGreen,"""
            ##:::: ##::'##:. ##:: ##:::..:: ##:::::::""",BPurple,""" ##::::..:: ##::: ##::""",BGreen,"""
            ########::'##:::. ##:. ######:: ######:::""",BPurple,""" ########:: ##::: ##::""",BGreen,"""
            ##.... ##: #########::..... ##: ##...::::""",BPurple,""" ##.... ##: #########:""",BGreen,"""
            ##:::: ##: ##.... ##:'##::: ##: ##:::::::""",BPurple,""" ##:::: ##:...... ##::""",BGreen,"""
            ########:: ##:::: ##:. ######:: ########:""",BPurple,""". #######:::::::: ##::""",BGreen,"""
            ........:::..:::::..:::......:::........:::.""",BPurple,"""......:::::::::..:::
            """)
            while True :

                print("""
                |------------|
                | Encode | 1 |
                |--------|---|
                | Decode | 2 |
                |------------|

                """)

                code=input("Enter Number :")

                if code == "1":
                    
                    print("""
                    
                    -----------
                    |Type |id |
                    |-----|---|
                    | b85 | 1 |
                    | b64 | 2 |
                    | b32 | 3 |
                    | b16 | 4 |
                    | a85 | 5 |
                    | EXT | 0 |
                    -----------

                    """)
                    te=input("Enter id :")
                    if te=="1":
                        text=input("Enter TexT :")
                        b85=base64.b85encode(text.encode("UTF-8")).decode("ascii")
                        print(BWhite,b85,BPurple)

                    elif te=="2":
                        text=input("Enter TexT :")
                        b64=base64.b64encode(text.encode("UTF-8")).decode("ascii")
                        print(BWhite,b64,BPurple)
                    elif te=="3":
                        text=input("Enter TexT :")
                        b32=base64.b32encode(text.encode("UTF-8")).decode("ascii")
                        print(BWhite,b32,BPurple)

                    elif te=="4":
                        text=input("Enter TexT :")
                        b16=base64.b16encode(text.encode("UTF-8")).decode("ascii")
                        print(BWhite,b16,BPurple)

                    elif te=="5":
                        text=input("Enter TexT :")
                        a85=base64.a85encode(text.encode("UTF-8")).decode("ascii")
                        print(BWhite,a85,BPurple)

                    elif te=="0":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(BWhite)
                        break
                    else :
                        print("Not Fuond !")

                elif code == "2":
                    print("""
                    
                    -----------
                    |Type |id |
                    |-----|---|
                    | b85 | 1 |
                    | b64 | 2 |
                    | b32 | 3 |
                    | b16 | 4 |
                    | a85 | 5 |
                    | EXT | 0 |
                    -----------

                    """)

                    te=input("Enter id :")

                    if te == "1":
                        decode_txt = input("ENter Ur TxT Decode:")
                        decode_hash = base64.b85decode(decode_txt)
                        decodeit = decode_hash.decode("ascii")
                        print(BWhite,decodeit,BPurple)
                       

                    elif te == "2":
                        decode_txt = input("ENter Ur TxT Decode:")
                        decode_hash = base64.b64decode(decode_txt)
                        decodeit = decode_hash.decode("UTF-8")
                        print(BWhite,decodeit,BPurple)


                    elif te == "3":
                        decode_txt = input("ENter Ur TxT Decode:")
                        decode_hash = base64.b32decode(decode_txt)
                        decodeit = decode_hash.decode("UTF-8")
                        print(BWhite,decodeit,BPurple)


                    elif te == "4":
                        decode_txt = input("ENter Ur TxT Decode:")
                        decode_hash = base64.b16decode(decode_txt)
                        decodeit = decode_hash.decode("UTF-8")
                        print(BWhite,decodeit,BPurple)


                    elif te == "5":
                        decode_txt = input("ENter Ur TxT Decode:")
                        decode_hash = base64.a85decode(decode_txt)
                        decodeit = decode_hash.decode("UTF-8")
                        print(BWhite,decodeit,BPurple)
                    

                    elif te=="0":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(BWhite)
                        break

                    else :
                        print("Not Fuond !")
                        


        elif x=="3":
            
            os.system("cls" if os.name == "nt" else "clear")
            print("""
                
              ______                             
             / _____)                            
            | /      ____  ____  ___  ____  ____ 
            | |     / _  |/ _  )/___)/ _  |/ ___)
            | \____( ( | ( (/ /|___ ( ( | | |    
             \______)_||_|\____|___/ \_||_|_|    
            """)
            while True :
                print(BPurple+"""
                
                    ----------------------
                    |encryption  > > [1] |
                    |--------------------|
                    |dencryption > > [2] |
                    |--------------------|
                    |     EXIT   > > [0] |
                    ---------------------- 
                
                """,BWhite)
                abcCSR="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
                xyzCSR="DEFGHIJKLMNOPQRSTUVWXYZABCdefghijklmnopqrstuvwxyzabc"

                tCSR=input("Enter Number :")

                if tCSR == "1":
                    def encCSR(txt):
                        enctCSR=""
                        for char in txt:
                            if char in abcCSR :
                                ind=abcCSR.index(char)
                                enctCSR+=xyzCSR[ind]
                            else:
                                enctCSR+=char 
                        return enctCSR 
                    txt=input("Enter Your TxT :")
                    txt=encCSR(txt)
                    print(txt)

                elif tCSR == "2":
                    def denctxt(txt):
                        enctCSR=""
                        for char in txt :
                            if char in abcCSR :
                                ind=xyzCSR.index(char)
                                enctCSR+=abcCSR[ind]
                            else :
                                enctCSR+=char
                        return enctCSR 
                    txt=input("Enter Your TxT :")
                    txt=denctxt(txt)
                    print(txt)
                elif tCSR == "0":
                    os.system("cls" if os.name == "nt" else "clear")
                    break
                else :
                    print("NoN")


        elif x=="4":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(BGreen,"""
            **********  ********  **     **  **********
            /////**///  /**/////  //**   **  /////**/// 
                /**     /**        //** **       /**    
                /**     /*******    //***        /**    
                /**     /**////      **/**       /**    
                /**     /**         ** //**      /**    
                /**     /********  **   //**     /**    
                //      ////////  //     //      //     
    
    """)
            while True :
                print(BPurple,"""
                ----------------------
                |encryption  > > [1] |
                |--------------------|
                |dencryption > > [2] |
                |--------------------|
                |      EXIT > >  [0] |
                ----------------------       
                
                
                """,BWhite)
                abc="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1357924680"
                cba="ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba0864213579"
                
                t=input("Enter number :")
                if   t=="1":
                    def enctxt(txt):
                        enct=""
                        for char in txt:
                            if char in abc:
                                ind=abc.index(char)
                                enct+=cba[ind]
                            else:
                                enct+=char
                        return enct
                    txt=input("Enter TxT :")
                    txt=enctxt(txt)
                    print(txt)


                elif t=="2":
                    def denctxt(txt):
                        enct=""
                        for char in txt:
                            if char in abc:
                                ind=cba.index(char)
                                enct+=abc[ind]
                            else:
                                enct+=char
                        return enct
                    txt=input("Enter TxT :")
                    txt=denctxt(txt)
                    print(txt)
                elif t=="0":
                    print(BWhite)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                    
                else :
                    print("non!")
                    
        elif x=="5":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(BYellow,"""
          
                    **               **********         
            ****** /**              /////**///          
            /**///**/**       ******     /**      ****** 
            /**  /**/******  **////**    /**     **////**
            /****** /**///**/**   /**    /**    /**   /**
            /**///  /**  /**/**   /**    /**    /**   /**
            /**     /**  /**//******     /**    //****** 
            //      //   //  //////      //      //////  
                                                         
            """)
            while True :
                print(BPurple,"""
                    ----------------------
                    |encryption  > > [1] |
                    |--------------------|
                    |dencryption > > [2] |
                    |--------------------|
                    |      EXIT > >  [0] |
                    ----------------------       
                                            """,BWhite)
                p=input("EnTer NumBer :")
                
                if p=="1":
                    
                    # nphot=input("Enter nnew object Fail >> ")
                    phot=input("Enter object File >> ")
                    def encfile(phot):
                        
                        with open(r"C:\Users\f\Desktop\kali.jfi","rb") as fimg:

                            img=fimg.read()

                        print(type(img))
                        txt=img.decode("ansi")
                        print(type(txt))
                    
                        txt=enctxt(txt)

                        img=txt.encode("ansi")

                        with open(phot,"wb") as fimg:
                            fimg.write(img)
                    nphot=input("Enter new object file :")
                    encfile(r"C:\Users\f\Desktop\kalii.jfi")   

                elif p=="2":
                    phot=input("Enter object File >> ")
                    nphot=input("Enter nnew object Fail >> ")
                    def dencfile(phot):
                        with open(phot,"rb") as fimg:

                            img=fimg.read()

                        print(type(img))
                        txt=img.decode("ansi")
                        print(type(txt))
                    
                        txt=denctxt(txt)

                        img=txt.encode("ansi")


                        with open(phot,"wb") as fimg:
                            fimg.write(img)
                    dencfile(nphot)
                elif p=="0":
                    print(BWhite)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
        elif x=="0":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        
    except:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(BRed+"""
         _______                       
        (_______)                      
         _____    ____ ____ ___   ____ 
        |  ___)  / ___) ___) _ \ / ___)
        | |_____| |  | |  | |_| | |    
        |_______)_|  |_|   \___/|_|    
                               
        
        """)
        print(Error)
        print(BWhite)
        sleep(3)
