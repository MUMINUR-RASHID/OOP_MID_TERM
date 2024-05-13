
# 1 NO ANSWER
class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall:
    #2 NO ANSWER

    def __init__(self, no, rows, cols):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = no

       
        for row in range(1, self.rows + 1):
            seat_row = [0] * self.cols
            self.seats[row] = seat_row

            # 3 NO ANSWER
    def entry_show(self, movie_id, movie_name, time):
        show_info = (movie_id, movie_name, time)
        self.show_list.append(show_info)

        # 4 NO ANSWER
    @staticmethod
    def book_seats(movie_id, seat_tp):
        Check_Id=False
        for hall in Star_Cinema.hall_list:
            for show in hall.show_list:
                if show[0] == movie_id:
                    Check_Id=True
                    for seat in seat_tp:
                        seat_row, seat_col = seat
                        if seat_row in hall.seats and seat_col <= len(hall.seats[seat_row]):
                            if hall.seats[seat_row][seat_col - 1] == 0:
                                hall.seats[seat_row][seat_col - 1] = 1
                                print(f"Seat {seat_row},{seat_col} Booked Successfully")
                            else:
                                print(f"Seat {seat_row},{seat_col} is not Available")
                                return
                        else:
                            print(f"Seat {seat_row},{seat_col} is not valid")
                            return
                        
        if not Check_Id:
            print("Invalid Movie Id.")
            return
        
        # 5 NO ANSWER
    @staticmethod
    def view_show_list():
        for hall in Star_Cinema.hall_list:
            print(f"Hall: {hall.hall_no}")
            for show in hall.show_list:
                print(f"Movie: {show[1]}, Movie_Id: {show[0]}, Show_Time: {show[2]}")

        # 6 NO ANSWER
    @staticmethod
    def view_available_seats(movie_id):
        for hall in Star_Cinema.hall_list:
            for show in hall.show_list:
                if show[0] == movie_id:
                    for row, seats_row in hall.seats.items():
                        print(f"Row {row}: {seats_row}")



# 7 NO ANSWER
class Counter:
    def __init__(self):
        self.choice = None

    def display_menu(self):
        print("\n1. Show Available Seats.")
        print("2. Book Seats.")
        print("3. Show Today's Shows.")
        print("4. Exit\n")

    def get_choice(self):
        self.choice = int(input("Enter Your Choice: "))

    def process_choice(self):
        if self.choice == 1:
            movie_id = int(input("Input Movie Id: "))
            Hall.view_available_seats(movie_id)
        elif self.choice == 2:
            movie_id = int(input("Input Movie Id: "))
            num_seats = int(input("How Many Seats You Want to Book?: "))
            seat_list = []
            for _ in range(num_seats):
                row = int(input("Enter row: "))
                col = int(input("Enter col: "))
                seat_list.append((row, col))
            Hall.book_seats(movie_id, seat_list)
            Hall.view_available_seats(movie_id)
        elif self.choice == 3:
            Hall.view_show_list()
        elif self.choice == 4:
            return False
        else:
            print("Invalid Choice. Please Enter Valid Choice.")
        return True


Cinema_Center = Star_Cinema()

hall1 = Hall(1, 7, 8)
hall2 = Hall(2, 8, 9)
hall3 = Hall(3, 10, 10)

hall1.entry_show(101, "Jawan", "Morning")
hall2.entry_show(102, "DUNKI", "Evening")
hall3.entry_show(103, "Ghetu Putro", "Night")


#2  NO ANSWER
Cinema_Center.entry_hall(hall1)
Cinema_Center.entry_hall(hall2)
Cinema_Center.entry_hall(hall3)

counter = Counter()

while True:
    counter.display_menu()
    counter.get_choice()
    if not counter.process_choice():
        break
