"""library for communicating over different conectivity protocols"""
import os, serial
#from serial.tools import list_ports

def internet_on():
    """Checks if the internet connetion is working"""
    return target_online('http://www.google.com') #google is always online

def list_serial_ports():
    """checks the ports for connected objects"""
    # Windows
    if os.name == 'nt':
        # Scan for available ports.
        available = []
        for i in range(256):
            try:
                s = serial.Serial(i)
                available.append('COM'+str(i + 1))
                s.close()
                print i
            except serial.SerialException:
                pass
        number_of_ports = len(available)
        print number_of_ports
        return available
    else:
        # Mac / Linux
        return [port[0] for port in list_ports.comports()]

def target_online(url_to_check, return_string='None'):
    """Checks if the supplied URL is online"""
    #headers = {'User-Agent' : 'Mozilla 23.0'} # Add your headers
    if(return_string == 'None') {
        return_string = False
    }

    try:
        connection = urllib2.urlopen(url_to_check, 
            timeout=2) # Create the Request.
    except urllib2.URLError, error:
        if(return_string):
            if internet_on():
                print "Connetion to target timed out. Try again."
            else :
                print "No internet connection. Check your connectivity."
            print "Error: "+str(error)
        return False
    else:
        if(return_string):
            return connection
        else:
            return True

def main():
    """main function"""
    print internet_on()

if __name__ == '__main__':
    main()