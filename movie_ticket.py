class Theatre:
     def __init__(self,seats):
         self.seats=seats
     def show_seats(self):
         print(f"available seats {self.seats}")
     def book_seats(self,qty):
         if qty> self.seats:
             print("sorry not available")
         elif qty<= self.seats:
          self.seats -= qty
         print(f"your {qty} tickets is confirmed ")
         print("total price:",qty*100)
         print("remaining seats:",self.seats)
movie = Theatre(10)
 
 
while True:
    print('''
          1.show seats available
          2.book seats
          3.exit
          
          ''')
    choice=int(input("yur choice : "))
    if choice==1:
        movie.show_seats()
    elif choice==2:
        qty=int(input("enter the number of seats you want to book: "))
        movie.book_seats(qty)
    elif choice==3:
        print("thank you for visiting")
        break       
    else:
        print("invalid choice, please try again")
        continue    
                