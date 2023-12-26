import wifi_manager

wifi_mgr = wifi_manager.WifiManager()

wlan = wifi_mgr.get_connection()

if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass  # you shall not pass :D


# Main Code goes here, wlan is a working network.WLAN(STA_IF) instance.
print("ESP OK")
