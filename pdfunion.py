#pdfUnion.py
# Here how to use this script
#python3 /home/openSource/pdfUnion.py /home/openSource/pdfUnion/test/ outputfile.pdf PDFNR1.pdf PDFNR2.pdf

# Some import (like /copy and /include in RPG)
import sys
import os
import PyPDF2

merger = PyPDF2.PdfFileMerger()

# Here are my input parms

path = sys.argv[1]
out_file = sys.argv[2]
in_files = sys.argv[3:]  #  Una lista di PDF dal terzo parm in avanti

# Set the path for input and output files
os.chdir(path)



# Loop into in_files (two or more files)
for pdf in in_files:
    try:
        #if doc exist then merge
        if os.path.exists(pdf):
            input = PyPDF2.PdfFileReader(open(pdf,'rb'))
            merger.append((input))
        else:
            print(f"problem with file {pdf}")

    except:
            print("cant merge !! sorry")
    else:
            print(f" {pdf} Merged !!! ")

# write output file on disk
merger.write(out_file)

# end