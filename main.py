import argparse
from scripts import preprocess, build_data
import time

TASKS = ["normalize-sample", "normalize", "build-data"]
def main():

    parser = argparse.ArgumentParser()    
    parser.add_argument("task", choices=TASKS, 
        metavar="task", 
        help=f"specify task: {', '.join(TASKS)}")
    parser.add_argument("data_path")   
    parser.add_argument("--data-dir")
    parser.add_argument("-n", default=10, type=int)
    args = parser.parse_args()

    start_time = time.monotonic()
    if args.task == "normalize-sample":
        preprocess.normalize_sample(args.data_path, args.n)
    elif args.task == "normalize":
        preprocess.normalize(args.data_path)
    elif args.task == "build-data":
        build_data.build_data(args.data_path, args.data_dir)
    else:
        pass
    print(f"time used: {time.monotonic()-start_time}")


if __name__ == "__main__":
    main()