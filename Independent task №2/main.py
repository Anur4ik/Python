from data_input import input_worker
from calculations import *
from general import *
def main():
    worker = input_worker()
    print(worker)

    calculate_monthly_salary(worker)


    worker_names = list(worker.keys())
    print_worker_names(worker_names)

if __name__ == "__main__":
    main()
