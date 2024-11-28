import time
import machine
import ntptime
import network

# Connect to wifi
def connect_wifi(proxy, ssid, password):
    # enter your wifi name and password
    proxy.active(True)
    proxy.connect(ssid, password)

def set_time():
    try:
        # Set the RTC using NTP
        ntptime.settime()
        print("RTC successfully set from NTP")
        # idk why but the time is odd by one day// 4 hours
        print(time.localtime())
    except OSError as e:
        print("Failed to set time from NTP:", e)

def main():
    mywifi = network.WLAN(network. STA_IF)
    connect_wifi(mywifi, 'NETGEAR67', 'noisycoconut718')
    set_time()


if __name__ == '__main__':
    main()  