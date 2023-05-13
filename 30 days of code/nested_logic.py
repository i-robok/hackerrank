
import datetime

def calculate_fine(returned_date, due_date):
    if returned_date <= due_date:
        return 0
    
    if returned_date.year > due_date.year:
        return 10000
    
    if returned_date.month > due_date.month:
        return (returned_date.month - due_date.month) * 500
    
    if returned_date.day > due_date.day:
        return (returned_date.day - due_date.day) * 15
    

def main():
    # Read returned date
    returned_day, returned_month, returned_year = str(input()).split(" ")
    returned_date = datetime.date(int(returned_year), int(returned_month), int(returned_day))
    
    # Read due date
    due_day, due_month, due_year = str(input()).split(" ")
    due_date = datetime.date(int(due_year), int(due_month), int(due_day))
    
    fine = calculate_fine(returned_date, due_date)

    print(f'{fine}')
    

if __name__ == "__main__":
    main()