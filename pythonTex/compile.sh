#!/bin/bash
pdflatex $1
pythontex $1
pdflatex $1