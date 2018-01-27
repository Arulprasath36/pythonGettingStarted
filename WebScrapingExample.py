import webbrowser,sys
#webbrowser.open("https://www.google.com/maps/place/your_address_string")

if(len(sys.argv)>1):
    #getting the address from command line
    address="".join(sys.argv[1:])
    print(address)

    #This class is incomplete and will include the rest of the logic soon.