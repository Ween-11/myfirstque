import streamlit as st

import numpy as np
import pandas as pd
import time

st.header("My first Python Web App")

readme = st.checkbox("readme first")

if readme:

    st.write("""
        This is a web app demo using [streamlit](https://streamlit.io/) library. It is hosted on [heroku](https://www.heroku.com/). You may get the codes via [github](https://github.com/richieyuyongpoh/myfirstapp)
        """)

    st.write ("For more info, please contact:")

    st.write("<a href='https://www.linkedin.com/in/yong-poh-yu/'>Dr. Yong Poh Yu </a>", unsafe_allow_html=True)

option = st.sidebar.selectbox(
    'Select from option below',
     ['Enter queue','map','T n C','Long Process'])


if option=='Enter queue':
  
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

    st.enter_queue(ticketSystem)

elif option=='map':
    map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

    st.map(map_data)

elif option=='T n C':

    st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
    show = st.checkbox('I agree the terms and conditions')
    if show:
        st.write(pd.DataFrame({
        'Intplan': ['yes', 'yes', 'yes', 'no'],
        'Churn Status': [0, 0, 0, 1]
        }))


else:
    'Starting a long computation...'

    
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
   
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)

    '...and now we\'re done!'
