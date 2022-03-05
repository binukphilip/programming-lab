col=input("enter the color of traffic signal light:")
if col == 'red' or col == 'RED':
    print("STOP")
elif col == 'orange' or col =='ORANGE':
    print("WAIT")
elif col == 'green' or col =='GREEN':
    print("GO")
else:
    print("invalid choice")