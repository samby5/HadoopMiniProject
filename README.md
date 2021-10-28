# HadoopMiniProject
Generate a post-sale report for a car sale
## Scripts
There are 4 python files. Here are the details:
- autoinc_mapper1.py - reads the input data and propagates key as vin_number, and the value as the incident type, make, and year.

- autoinc_reducer1.py - reads the output from above mapper script and outputs the accident records with year and make of the car

- autoinc_mapper2.py - reads the output from above reducer script and outputs the composite key made up of the concatenation of vehicle make and
year.

- autoinc_reducer2.py - reads the output from above mapper script and outputs combination of make and year with total count for that key

The shell script(run.sh) pipes the results from one script to the next.

## Result
The shell script which calls the python scrip was run in the big data env by moving all the files from local to hadoop file system. The result screenshot  is in the Output.docx
