
import math

measured_depth_1 = float(input("Measured Depth 1: "))
inclination_1 = float(input("Inclination 1: "))
azimuth_1 = float(input("Azimuth 1: "))
true_vertical_depth_1 = float(input("True Vertical Depth 1: "))
vertical_section_1 = float(input("Vertical Section 1: "))

measured_depth_2 = float(input("Measured Depth 2: "))
inclination_2 = float(input("Inclination 2: "))
azimuth_2 = float(input("Azimuth 2: "))

average_inclination = (float(inclination_1) + float(inclination_2))/2
average_azimuth = (float(azimuth_1) + float(azimuth_2))/2

cos_ave_inc = math.cos(math.radians(average_inclination))
sin_ave_az = math.sin(math.radians(average_azimuth))

depth_drilled = measured_depth_2 - measured_depth_1

true_vertical_depth_new = cos_ave_inc * depth_drilled + true_vertical_depth_1
vertical_section_new = sin_ave_az * depth_drilled + vertical_section_1


print (true_vertical_depth_new)
print (vertical_section_new)
