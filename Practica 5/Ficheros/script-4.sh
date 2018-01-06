#!/bin/bash

for i in {25..25}; do
  # echo "Buscando ${i} ceros:" >> salida_2.txt
  for j in {1..5}; do
    python3 ejercicio_3.py text.txt ${i} >> salida_2.txt
  done
done
