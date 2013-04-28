#!/usr/bin/python
import subprocess

COMPILE_COMMAND = "/usr/texbin/pdflatex -interaction=nonstopmode fixpred.tex"

process = subprocess.Popen(COMPILE_COMMAND, shell=True, stdout=subprocess.PIPE)
for line in process.stdout:
        print line
        process.wait()

OPEN_COMMAND = "open fixpred.pdf"

subprocess.Popen(OPEN_COMMAND, shell=True, stdout=subprocess.PIPE).wait()
