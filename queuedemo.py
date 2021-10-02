import streamlit as st
from binarysearchtree import qu
import pandas as pd

ticketSystem = Queue()


ticketNo = 1000


while True:
    print("\n\nWelcome to the RBA Ticket Booking System. You will be served soon.\n")
    print("\nFor Customer: Press 1 to queue.\n")
    print("For Customer Care Consultant: Press 2 to serve the next customer.\n")
    print("For Customer Care Consultant: Press 3 to get the list of customers in the waiting queue.\n")

    print("Press x to end the system. ")
    step = input("\nPlease enter the number.\n\n")
    if step.lower() == 'x':
        print("Thank you for using our service. ")
        break
    try:
        step = int(step)

        if step!= 1 and step!=2 and step!=3:
            print("\nYou have entered an undefined number\n")


        elif step==1:
          
            
            customerName = input("\nPlease enter your name.\n\n")
            ticketNo = ticketNo + 1
            ticketSystem.enqueue(customerName, ticketNo)
            waitingTime = 2*ticketSystem.size

            print("\nDear {}. Your ticket no is {}.".format(customerName,ticketNo))
            print("Your estimated waiting time is {} minutes.\n\n".format(waitingTime))

        elif step==2:
            counterNo = input("\nPlease enter your counterNo.\n\n")

            if ticketSystem.size >0:
                print("No # {} , counter {}".format(ticketSystem.getFirstElement()[1],counterNo))

                ticketSystem.dequeue()
            else:
                print("No one in the queue now.")
        
        else:
            ticketSystem.traverse()
         
    
    except ValueError:
        print("\nPlease enter a number.\n\n")
