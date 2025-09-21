def print_worker_names(worker_names, index=0):
    if index < len(worker_names):
        print(worker_names[index])

        print_worker_names(worker_names, index + 1)


