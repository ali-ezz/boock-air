import random
print('made by ali ezz from helwan national universtity')
  ############## admin info ###########
admin =['ali','26','1234']
admin_info=[]
  ############# users info #############
user_info =['email','password','credit card number','credit card password','credit card balance']
users =[['ali@gmail.com','1234',5678,'911',1000]]
users.insert(0,user_info)
new_users=[]
user_login=[]
with open('users.txt', 'w') as file:
 for inner_list in users:
  line = ' | '.join(map(str, inner_list)) + '\n'
  file.write(line)
  ########### flights ##############
flights_info=['origren','destination','time','prise','id']
flight1=['cairo','new york','11/3/2028',100,1]
flights=[]
flights.insert(0,flights_info)
flights.append(flight1)
new_flight=[]
with open('flights.txt', 'w') as file:
 for inner_list in flights:
  line = "{} >> {} | {}\n".format(inner_list[0], inner_list[1], ' | '.join(map(str, inner_list[2:])))
  file.write(line)
  ########### registered flights ########
registered_flights_info=['origren','destination','seat','id of the ticket','email of the user']
registered_flights=[]
registered_flights.append(registered_flights_info)
new_registered_flights=[]
with open('registered tickets.txt', 'w') as file:
 for inner_list in registered_flights:
  line = "{} >> {} | {}\n".format(inner_list[0], inner_list[1], ' | '.join(map(str, inner_list[2:])))
  file.write(line)
  ################# user or admin cheek ################
while(True):
 user_or_admin = raw_input('are you \n1.an admin \n2.an user\n3.exit\n')
 if(user_or_admin=='3'or user_or_admin=='2' or user_or_admin=='1'):
  #################### adimn interfase  #################
  if(user_or_admin=='3'):
     print('program is off')
     break
 else:
   print('invaled input, try again')
   continue 
 #admin login#
 if(user_or_admin == '1'):
      admin_info=[]
      name_admin =raw_input('please enter you name\n')
      admin_info.append(name_admin)
      id_admin =raw_input('please enter your id number\n')
      admin_info.append(id_admin)
      passwor_admin =raw_input('please enter your password\n')
      admin_info.append(passwor_admin)
      if(admin_info == admin):
       admin_info=[]
       print('welcome back ' + name_admin + '!\n')
       while(True):
        #admin commands#
        admin_opration=raw_input('\nwhat opration do you want to do?\n1.View all registered flights\n2.Add or delete a flight\n3.Modify the flight\n4.exit\n')
        if(admin_opration=='4'):
          break 
        # seeing all the registered flights #
        elif(admin_opration=='1'):
         print('\n(you can see all the flights in the file flights)\n')
         for inner_list in registered_flights:
          formatted_inner_list = "{}>>{}|{}".format(inner_list[0], inner_list[1], '|'.join(map(str, inner_list[2:])))
          print("{}".format(formatted_inner_list))
        #adding or deleting a flight#
        elif(admin_opration=='2'):
         while(True):
          add_or_delete=raw_input('do you want to\n1.add a flight\n2.delete a flight\n3.exit\n')
          if(add_or_delete=='3'):
           break
          elif(add_or_delete=='1'):
           origren=raw_input('please enter the origren of the flight\n')
           new_flight.append(origren)
           destination=raw_input('please enter the destination of the flight\n')
           new_flight.append(destination)
           time=raw_input('please enter the time of the flight in a day/monthe/year format\n')
           if(('/') in time):
            new_flight.append(time)
            new_prise=raw_input('please enter the prise of the ticket\n')
            if new_prise.isdigit():
             new_prise = int(new_prise)
            else:
             print('Error ('+new_prise+') is not a valid prise.')
            new_flight.append(new_prise)
            new_id=random.randint(0000,9999)
            new_flight.append(new_id)
            flights.append(new_flight)
            new_flight=[]
            with open('flights.txt', 'w') as file:
             for inner_list in flights:
              line = "{} >> {} | {}\n".format(inner_list[0], inner_list[1], ' | '.join(map(str, inner_list[2:])))
              file.write(line)
           else:
            print('invaled time format')
          elif(add_or_delete=='2'):
            id_to_delet=raw_input('please enter the id of the flight you eant to delet\n')
            if id_to_delet.isdigit():
             id_to_delet = int(id_to_delet)
            else:
             print('Error (' + id_to_delet + ') is not a valid id number.')
            for sublist in flights:
             if(id_to_delet in sublist):
               flights.remove(sublist)
            with open('flights.txt', 'w') as file:
             for inner_list in flights:
              line = "{} >> {} | {}\n".format(inner_list[0], inner_list[1], ' | '.join(map(str, inner_list[2:])))
              file.write(line)
          else:
            print('invaled opration')         
        #modfing the flight#
        elif(admin_opration =='3'):
          id_modify_flight=raw_input('please enter the flight id to modify\n')
          if id_modify_flight.isdigit():
           id_modify_flight = int(id_modify_flight)
          else:
           print('Error ('+id_modify_flight+') is not a valid id for a flight.')
          flight_is_not_here=False
          for sublist in flights: 
           if(id_modify_flight in sublist):    
              flight_is_not_here=True
              break
          if(flight_is_not_here):
           while(True):
            modify_selcation=raw_input('what do you want to modify\n1.origren\n2.destination\n3.time\n4.prise\n5.exit\n')
            if(modify_selcation=='5'):
              break
            elif(modify_selcation=='1'): 
             origren_modife_incert=raw_input('please write the new origren\n')
             for inner_list in flights :
              if id_modify_flight in inner_list:
                 index = inner_list.index(id_modify_flight)
                 if index >= 0:
                  inner_list[index - 4] = origren_modife_incert  
                  with open('flights.txt', 'w') as file:
                    for inner_list in flights:
                     line = "{} >> {} | {} \n".format(inner_list[0], inner_list[1], ' | '.join(map(str, inner_list[2:])))
                     file.write(line)
                 break
            elif(modify_selcation=='2'):
              destination_modife_incert=raw_input('please write the new destination\n')
              for inner_list in flights:
                if id_modify_flight in inner_list:
                 index = inner_list.index(id_modify_flight)
                 if index >= 0:
                  inner_list[index - 3] = destination_modife_incert  
                  with open('flights.txt', 'w') as file:
                    for inner_list in flights:
                     line = "{} >> {} | {} \n".format(inner_list[0], inner_list[1], ' | '.join(map(str, inner_list[2:])))
                     file.write(line)
                 break  
            elif(modify_selcation=='3'):
              time_modife_incert=raw_input('please write the new time in day/month/year foramt\n')
              if('/' in time_modife_incert):
               for inner_list in flights:
                 if id_modify_flight in inner_list:
                  index = inner_list.index(id_modify_flight)
                  if index >= 0:
                   inner_list[index - 2] = time_modife_incert  
                   with open('flights.txt', 'w') as file:
                     for inner_list in flights:
                      line = "{} >> {} | {}\n".format(inner_list[0], inner_list[1], ' | '.join(map(str, inner_list[2:])))
                      file.write(line)
                  break  
            elif(modify_selcation=='4'):
              prise_modife_incert=raw_input('please write the new prise in numbers\n')
              if prise_modife_incert.isdigit():
               prise_modife_incert = int(prise_modife_incert)
               for inner_list in flights:
                if id_modify_flight in inner_list:
                 index = inner_list.index(id_modify_flight)
                 if index >= 0:
                  inner_list[index - 1] = prise_modife_incert  
                  with open('flights.txt', 'w') as file:
                    for inner_list in flights:
                     line = "{} >> {} | {}\n".format(inner_list[0], inner_list[1], ' | '.join(map(str, inner_list[2:])))
                     file.write(line)
                 break   
              else:
               print('Error ('+prise_modife_incert+') is not a valid integer.')  
            else:
             print('invaled opration')      
        else:
         print('invaled opration')         
      else:
       print('invalid input,please cheek your name,id and your passwor and try again\n')
    #user login#
 if(user_or_admin=='2'):
   while(True):
    login_or_register=raw_input('please do you want to\n1.login\n2.sign up\n3.exit\n')
    if(login_or_register =='3'):
      break
    if(login_or_register =='1'):
      user_email =raw_input('please enter your email\n')
      user_password =raw_input('please enter your password\n')
      cheek_user=False
      for sublist in users:
       if((user_email in sublist[0] and '@gmail.com' in user_email) and (user_password in sublist[1])):
        cheek_user=True
        break
       #user opration#
      if(cheek_user):
       print('\nwelcome back ' + user_email + '!\n')
       while(True):
        user_opration=raw_input('what opration do you want to do\n1.book or delete a flight\n2.modify personal data\n3.See past and upcoming flights and your tickets\n4.exit\n')
        if(user_opration=='4'):
          break
        #See past and upcoming flights
        elif(user_opration=='3'):
         for inner_list in registered_flights:
          if user_email in inner_list:
           all_user_flight = "{}>>{}|{}|{}|{}".format(inner_list[0], inner_list[1], inner_list[2], inner_list[3], inner_list[4])
           print(all_user_flight)
          print('if nothink has printed you did not regeterd a ticket yet\n')
        #.modify personal data#
        elif(user_opration=='2'):
          modify_user_personal_data=raw_input('what do you want to modify\n1.passoword\n2.credit card info\n3.exit\n')
          if(modify_user_personal_data=='3'):
           break
          elif(modify_user_personal_data=='1'):
           password_modife_incert=raw_input('please write the new password\n')
           for inner_list in users:
            if user_email in inner_list:
             index = inner_list.index(user_email)
             if index >= 0:
              inner_list[index + 1] = password_modife_incert  
              with open('users.txt', 'w') as file:
               for inner_list in users:
                line = ' | '.join(map(str, inner_list)) + '\n'
                file.write(line)
              break  
          elif(modify_user_personal_data=='2'):
           credit_card_number_modife_incert=raw_input('please write the new credit card number\n')
           if credit_card_number_modife_incert.isdigit():
            credit_card_number_modife_incert = int(credit_card_number_modife_incert)
           else:
            print('Error ('+credit_card_number_modife_incert+') is not a valid credit card number.')
           for inner_list in users:
            if user_email in inner_list:
             index = inner_list.index(user_email)
             if index >= 0:
              inner_list[index + 2] = credit_card_number_modife_incert  
              with open('users.txt', 'w') as file:
               for inner_list in users:
                line = ' | '.join(map(str, inner_list)) + '\n'
                file.write(line)
              break               
           credit_card_password_modife_incert=raw_input('please write the new credit card password\n')
           if credit_card_password_modife_incert.isdigit():
            credit_card_password_modife_incert = int(credit_card_password_modife_incert)
           else:
            print('Error ('+credit_card_password_modife_incert+') is not a valid credit card password.')
           for inner_list in users:
            if user_email in inner_list:
             index = inner_list.index(user_email)
             if index >= 0:
              inner_list[index + 3] = credit_card_password_modife_incert  
              with open('users.txt', 'w') as file:
               for inner_list in users:
                line = ' | '.join(map(str, inner_list)) + '\n'
                file.write(line)
              break    
           credit_card_balance_modife_incert=random.randint(100,300)
           for inner_list in users:
            if user_email in inner_list:
             index = inner_list.index(user_email)
             if index >= 0:
              inner_list[index + 4] = credit_card_balance_modife_incert  
              with open('users.txt', 'w') as file:
               for inner_list in users:
                line = ' | '.join(map(str, inner_list)) + '\n'
                file.write(line)
              break   
         #user booking and canceling a flight ticket#
        elif(user_opration=='1'):  
         while(True):
          book_or_cancel=raw_input('do you want to\n1.book a ticket\n2.cansel a ticket reservation\n(there will be a fine the seat prise + the ticket prise)\n3.exit\n')
          if(book_or_cancel=='3'):
            break
          #booking a ticket#
          elif(book_or_cancel=='1'):
           ticket_selction=raw_input('please enter the id number of the flight\n(you will find it in the tap flight)\n')
           if ticket_selction.isdigit():
            ticket_selction = int(ticket_selction)
           else:
            print('Error ('+ticket_selction+') is not a valid id for a flight.')
           ticket_is_here=False
           for sublist in flights:
            if(ticket_selction in sublist):
             ticket_is_here=True
             for inner_list in users:
              if(ticket_is_here and user_email in inner_list ):
               if(sublist[3]<=inner_list[4]):
                new_registered_flights.append(sublist[0])
                new_registered_flights.append(sublist[1])
                inner_list[4]=inner_list[4]-sublist[3]
                with open('users.txt', 'w') as file:
                 for inner_list in users:
                  line = ' | '.join(map(str, inner_list)) + '\n'
                  file.write(line)
                seat_selction=raw_input('what seat do you want\n1.first class in (a1) for 50$\n2.business class in (b1) for 30$\n3.economic class in (c1)\n')
                if(seat_selction =='1'):
                 inner_list[4]=inner_list[4]-50
                 with open('users.txt', 'w') as file:
                  for inner_list in users:
                   line = ' | '.join(map(str, inner_list)) + '\n'
                   file.write(line)
                 new_registered_flights.append('first class in (a1)')
                elif(seat_selction =='2'):
                 inner_list[4]=inner_list[4]-30
                 with open('users.txt', 'w') as file:
                  for inner_list in users:
                   line = ' | '.join(map(str, inner_list)) + '\n'
                   file.write(line)
                 new_registered_flights.append('business class in (b1)')
                elif(seat_selction =='3'):
                 new_registered_flights.append('economic class in (c1)')
                else:
                 print('invalid input')
                id_of_ticket=random.randint(0000,9999)
                new_registered_flights.append(id_of_ticket)
                new_registered_flights.append(user_email)
                registered_flights.append(new_registered_flights)
                new_registered_flights=[]
                with open('registered tickets.txt', 'w') as file:
                 for inner_list in registered_flights:
                  line = "{} >> {} | {}\n".format(inner_list[0], inner_list[1], ' | '.join(map(str, inner_list[2:])))
                  file.write(line)
          elif(book_or_cancel=='2'):
            ticket_to_delet=raw_input('please enter thr id of the ticket you want to delet\n')
            if ticket_to_delet.isdigit():
             ticket_to_delet = int(ticket_to_delet)
            else:
             print('Error ('+ticket_to_delet+') is not a valid id for a flight.')
            ticket_delet_is_here=False
            for sublist in registered_flights:
             if(ticket_to_delet in sublist):
              ticket_delet_is_here=True
              inner_list_to_remove = None
              for inner_list in registered_flights:
               if ticket_to_delet in inner_list:
                inner_list_to_remove = inner_list
                break
              if inner_list_to_remove:
               registered_flights.remove(inner_list_to_remove)
              with open('registered tickets.txt', 'w') as file:
               for inner_list in registered_flights:
                line = "{} >> {} | {}\n".format(inner_list[0], inner_list[1], ' | '.join(map(str, inner_list[2:])))
                file.write(line)
              for inner_list in users:
               if(ticket_delet_is_here and user_email in inner_list):
                 inner_list[4]=inner_list[4]
                 with open('users.txt', 'w') as file:
                  for inner_list in users:
                   line = ' | '.join(map(str, inner_list)) + '\n'
                   file.write(line)
          else:
           print('invaled input')   
        else:
         print('invaled input')    
      else:
        print('you dont have an acount,please cheek your gmail and your passwor or sign up\n')
  ############## new user sign up #########################
    if(login_or_register =='2'):
     new_users=[]
     new_user_email=raw_input('please enter your email\n')
     if('@gmail.com' in new_user_email):
      new_users.append(new_user_email)
      new_password =raw_input('please enter your password\n')
      new_users.append(new_password)
      new_credit_card_number=raw_input('please enter your credit card number\n')
      if new_credit_card_number.isdigit():
       new_credit_card_number = int(new_credit_card_number)
       new_users.append(new_credit_card_number)
       new_credit_card_password=raw_input('please enter your credit card number passoword\n')
       if new_credit_card_password.isdigit():
        new_credit_card_password = int(new_credit_card_password)
        new_users.append(new_credit_card_password)
        new_balance=random.randint(100,300)
        new_users.append(new_balance)
        user_is_here=any((new_user_email in inner_list) or (new_credit_card_number in inner_list) for inner_list in users)
        if(not user_is_here):
         users.append(new_users)
         with open('users.txt', 'w') as file:
            for inner_list in users:
             line = ' | '.join(map(str, inner_list)) + '\n'
             file.write(line)
         new_users=[]
         print('acount signed up succeeded\n')
        else:
         print('acount is alredy signed please login')
       else:
        print('Error ('+new_credit_card_password+') is not a valid prise.')
      else:
       print('Error ('+new_credit_card_number+') is not a valid prise.')
     else:
      print('invaled email\n') 