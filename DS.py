import pandas as pd
import numpy as np

pic ='C:\\Users\\obanl\\Downloads\\HashCode\\a_example.txt'

pics = open (pic, 'r')
text = pics.read()
pics.close()

print(text)