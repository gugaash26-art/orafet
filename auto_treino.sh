#!/bin/bash
cd ~/orafet
set +H
echo "ORAFET iniciando auto treino"
python treinar_sozinho.py
echo "ORAFET treinou sozinho"
python orafet_ensina.py
