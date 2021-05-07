#!/usr/bin/python3

import subprocess
import sys

def banner():
    print(""" 
           (                                                
   (     )\ )    (      (         )                       
   )\   (()/(  ( )\     )\     ( /(    (         (   (    
((((_)(  /(_)) )((_) ((((_)(   )\())  ))\  (    ))\  )(   
 )\ _ )\(_))_ ((_)_   )\ _ )\ ((_)\  /((_) )\  /((_)(()\  
 (_)_\(_)|   \ | _ )  (_)_\(_)| |(_)(_))( ((_)(_))   ((_) 
  / _ \  | |) || _ \   / _ \  | '_ \| || |(_-</ -_) | '_| 
 /_/ \_\ |___/ |___/  /_/ \_\ |_.__/ \_,_|/__/\___| |_|           

            Developer: NobodyAtall   
            YouTube  : https://www.youtube.com/c/nobodyatall
            GitHub   : https://github.com/nobodyatall648                                                           
    """)

def help():
    print(""" 
        =========
        HELP MENU
        =========

        connect         connect remote ADB via IP (eg: connect "192.168.0.144:5555")
        showdev         show ADB device list
        seldev          select the ADB ID (eg: seldev 1AM761214LB616NV / seldev "192.168.0.144:5555")
        showseldev      show selected ADB ID
        shell           spawn ADB shell      
        ......
        disconnect      disconnect all connected devices
        help            show help menu
        exit            exit ADB Abuser 
        
    """)

def adbAbuserShell():
    while(True):
        #init
        cmd = ""
        arg = ""

        cmd = input("Abuser > ")            
        #spliting command and argument  
        cmd = cmd.strip()        
        splitLine = cmd.split(" ")   

        if(len(splitLine) > 1):                             
            cmd,arg = splitLine[0],splitLine[1]        
        else:
            cmd = splitLine[0]
                
        commands(cmd, arg)    

def commands(cmd, arg):
    try:        
        global ADB_ID

        if(cmd == "connect"):
            output_res = subprocess.run("adb connect " + arg.strip().replace("\"", "").replace("\'", ""), stdout=subprocess.PIPE)
            print(output_res.stdout.decode()) 
        elif(cmd == "showdev"):
            output_res = subprocess.run("adb devices", stdout=subprocess.PIPE)
            print(output_res.stdout.decode()) 
        elif(cmd == "seldev"):
            if(arg != ""):
                #check the device id/IP available in the adb devices list
                output_res = subprocess.run("adb devices", stdout=subprocess.PIPE)
                if(arg.replace("\"", "").replace("\'", "") in output_res.stdout.decode()):
                    ADB_ID = arg.strip().replace("\"", "").replace("\'", "")    
                    print("[*] ADB ID Selected: " + ADB_ID)
                else:
                    print("[!] The device is not available in ADB devices list!")
            else:
                print("[!] Please enter an ADB ID")
        elif(cmd == "showseldev"):
            if(ADB_ID != ""):
                print("[*] ADB ID Selected: " + ADB_ID)
            else:
                print("[*] No ADB ID Selected")
        elif(cmd == "shell"):
            if(ADB_ID != ""):
                output_res = subprocess.run("adb -s " + ADB_ID + " shell", shell=True)             
            else:
                print("[!] Please use seldev command to select an ADB Device")
        elif(cmd == "disconnect"):
            output_res = subprocess.run("adb disconnect", stdout=subprocess.PIPE)
            print(output_res.stdout.decode()) 
        elif(cmd == "help"):            
            help()
        elif(cmd == "exit"):            
            sys.exit(0)
        else:
            print("[!] Command Not Found")
        
        print("")
    except Exception as e:
        print("Something went wrong")
        print(e)

def main():    
    global ADB_ID    
    ADB_ID = ""

    #print banner
    banner()

    #start adb abuser shell
    adbAbuserShell()

if __name__ == "__main__":
    main()