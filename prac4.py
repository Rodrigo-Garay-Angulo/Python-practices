import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import utils_prac4 as up4

sample = up4.generate_sample(10)

print(sample)

print(up4.summary(sample))