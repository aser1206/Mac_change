import subprocess
import re

#ifconfig eth0 down
#ifconfig eth0 hw ether 00:11:22:33:44:55
#ifconfig eth0 up

class MAC_Changer():
    def __init__(self):
        self.MAC = ""

    def getMAC(self, iface):
        output = subprocess.run(["ifconfig",iface], shell = False, capture_output = True)
        cmd_result=output.stdout.decode('utf-8')
        #print(cmd_result)

        #pattern to match the ether0 regex
        pattern = r'ether\s[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}'

        regex = re.compile(pattern)

       
        ans = regex.search(cmd_result)
        current_MAC = ans.group().split(" ")[1] #split the matching string i two tokens based on the space
        self.MAC = current_MAC
        return current_MAC
    def change_MAC(self,iface,new_MAC):
        print("[+] Current MAC" + self.getMAC(iface))

        #ifconfig eth0 down
        output = subprocess.run(["ifconfig", iface, "down"],shell = False, capture_output = True)
        print(output.stderr.decode('utf-8'))

        #ifconfig eth0 hw ether 00:11:22:33:44:55
        output = subprocess.run(["ifconfig", iface, "hw","ether",new_MAC],shell = False, capture_output = True)
        print(output.stderr.decode('utf-8'))

        #ifconfig eth0 up
        output = subprocess.run(["ifconfig", iface, "up"],shell = False, capture_output = True)
        print(output.stderr.decode('utf-8'))

        print("[+] Updated MAC",self.getMAC(iface))

        return self.getMAC(iface)