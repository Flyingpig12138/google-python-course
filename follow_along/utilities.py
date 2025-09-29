import sys
import os
import re
import subprocess


# # file system: print filenames in a directory
# def print_filenames(dir):
#     filenames = os.listdir(dir)
#     for filename in filenames:
#         print(filename)
#         print(os.path.join(dir, filename))  # relative to current directory
#         print(os.path.abspath(filename))    # absolute path
#         print("----------")

# # subprocess: check git status of a directory
# def list_filenames(dir):
#     cmd = "git status " + dir
#     print("command to run: ", cmd)
    




def main():
    # dir = "../babynames/"

    # file system
    # print_filenames(dir)

    # subprocess.run()
    # list_filenames(dir)
    # result = subprocess.run(["python3 ", "../hello.py ", "flyingpig"], capture_output=True, text=True)
    # result = subprocess.run(["dir"], capture_output=True, shell=True, text=True)
    # print("STDOUT:", result.stdout)
    # print("STDERR:", result.stderr)

    # example 1: ping a website, and print output in Python
    # result = subprocess.run(
    #     ["ping","localhost","-n","1"],   # commands as a list
    #     capture_output=True,  # capture output to use in python
    #     text=True            # return string instead of bytes
    # )

    # # print 
    # print("stdout: ", result.stdout)
    # print("stderr: ", result.stderr)

    # example 2: use subprocess.run() to list files
    # result = subprocess.run(
    #     "dir ..\\aintnosuchfile",  # use string if shell==True
    #     capture_output=True,  # write output to STDOUT instead of to terminal directly 
    #     text=True,
    #     shell=True            # can use string arg, if not, use list arg
    # )

    # print("output: ", result.stdout)
    # print("stderr: ", result.stderr)

    # example 3: use subprocess.Popen() to process output while command is running
    # process = subprocess.Popen(
    #     ["ping","google.com","-n","10"], 
    #     stdout=subprocess.PIPE,
    #     stderr=subprocess.PIPE,
    #     text=True
    # )

    # # print output line by line
    # for line in process.stdout:
    #     print("Ping output: ", line.strip())
    # # wait for process finish and returncode
    # process.wait()
    # print("Ping finished. Return code is: ", process.returncode)

    # mini-project: ping logger (combine run and Popen)
    hosts = ["google.com", "localhost", "www.honda.co.jp", "github.com/Flyingpig12138"]
    result = []
    success = []
    for host in hosts:
        # start a subprocess for each host
        process = subprocess.run(
            ["ping",f"{host}","-n","1"],  # pin once only
            text=True,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
        )

        # collect output
        if process.returncode:
            result.append(f"{host}: failed")
        else:
            # extract IP address
            ip_addr = re.search(r'\[.+\]', process.stdout)
            ping_time    = re.search(r'time.\d+ms', process.stdout)
            print(f"{host} with IP address: {ip_addr.group()}: success! {ping_time.group()}")






# standard boiler plate
if __name__ == "__main__":
    main()