#!/usr/bin/env python3
from pathlib import Path
"""
Author: emattison@gmail.com
Created: 2024-02-07
Usage: python processor.py
Description: Reads items in two files and outputs items that are unique to each list.
Note: There is some code redundancy here, but I am stressing legibility over optimization.
"""

print("Starting...")

"""
Read files in the input directory
"""
companies1_input_file_path = "./input/companies1.txt"
companies2_input_file_path = "./input/companies2.txt"

print(f"Reading File 1 here - {companies1_input_file_path}")
print(f"Reading File 2 here - {companies2_input_file_path}")

try:
    companies1_input_file = Path(companies1_input_file_path)
    companies2_input_file = Path(companies2_input_file_path)
    companies1_text = companies1_input_file.read_text()
    companies2_text = companies2_input_file.read_text()
except Exception as e:
    print("Something went wrong reading files.")
    raise e

"""
Split the contents of the files on the line separator.
Use set difference to get items that are in one list and not the other.
Note: In python, the *sorted* method converts the set object into a list.
"""
try:
    companies1_list = companies1_text.splitlines()
    companies2_list = companies2_text.splitlines()
    only_in_companies1_list = sorted(set(companies1_list) - set(companies2_list))
    only_in_companies2_list = sorted(set(companies2_list) - set(companies1_list))
except Exception as e:
    print("Something went wrong processing the data.")
    raise e

"""
Write results to files in the output directory
"""
companies1_output_file_path = "./output/only_in_companies1.txt"
companies2_output_file_path = "./output/only_in_companies2.txt"

print(f"Writing items only in list 1 here - {companies1_output_file_path}")
print(f"Writing items only in list 2 here - {companies2_output_file_path}")

try:
    only_in_companies1_output_file = Path(companies1_output_file_path)
    only_in_companies2_output_file = Path(companies2_output_file_path)
    only_in_companies1_output_file.write_text("\n".join(only_in_companies1_list))
    only_in_companies2_output_file.write_text("\n".join(only_in_companies2_list))
except Exception as e:
    print("Something went wrong writing files.")
    raise e

print("...Done.")