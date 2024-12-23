import time
import tracemalloc


def measure_performance(function, *args, **kwargs):
    start_time = time.perf_counter()
    tracemalloc.start()

    result = function(*args, **kwargs)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    peak_memory_megabytes = peak / 10 ** 6

    print(f"Execution time: {elapsed_time:.6f} seconds")
    print(f"Peak memory usage: {peak_memory_megabytes:.6f} MB")

    return result, elapsed_time, peak_memory_megabytes


def file_read(input_file_path='../txtf/input.txt'):
    with open(input_file_path, 'r') as file:
        lines = [list(map(int, line.split())) for line in file]
        print('Input:')
        for line in lines:
            print(*line)
    return tuple(lines)


def file_write(writing, output_file_path='../txtf/output.txt'):
    with open(output_file_path, 'w') as file:
        output = " ".join(map(str, writing))
        file.write(output)
        print('Output:', output, sep='\n')
