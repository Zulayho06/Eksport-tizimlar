# -*- coding: utf-8 -*-
"""Untitled63.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sr7PAOKcOb5OVp4CruiKkXI6AmwDvjw5
"""

def kasallik_tashxisi(belgi):
  if belgi == "Istima":
    return "Parasetamol iching"
  elif belgi== "Bosh og'rig'i":
    return "Bolnol"
  elif belgi == "Tish og'rig'i":
    return "Senepar"
  else:
    return "Shifokorga murjaat qiling"
belgi=input("Kasallik belgisini kiriting ")
natija=kasallik_tashxisi(belgi)
print(natija)