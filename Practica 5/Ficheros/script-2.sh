#!/bin/bash

for i in {1..25}; do
  echo "Buscando ${i} ceros:" >> salida.txt
  for j in {1..10}; do
    python3 ejercicio_1.py text.txt ${i} >> salida.txt
  done
done
