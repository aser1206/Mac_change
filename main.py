from mac import MAC_Changer

if __name__=="__main__":
    mc=MAC_Changer()
    mac = mc.getMAC("eth0")
    print(mac)

    curr_MAC = mc.change_MAC("eth0","00:1d:35:72:b2:af")
    print(curr_MAC)