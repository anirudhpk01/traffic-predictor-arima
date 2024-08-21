import csv

# Provided data
#l1 = ['Minute', 'Cars', 'Buses', 'Motorcycles', 'Bicycles', 
      #[[0, 59, 1, 15, 0], [1, 30, 2, 10, 0], [2, 53, 1, 15, 0], [3, 29, 5, 7, 0], [4, 23, 3, 11, 1], [5, 49, 9, 9, 0], [6, 22, 4, 10, 0], [7, 50, 17, 13, 1], [8, 23, 4, 12, 0], [9, 43, 14, 9, 0], [10, 31, 6, 7, 1], [11, 38, 5, 12, 0], [12, 36, 2, 5, 0], [13, 45, 1, 15, 0], [14, 48, 4, 17, 0]], 
     # [[15, 19, 1, 6, 0], [16, 46, 5, 18, 0], [17, 21, 1, 4, 0], [18, 7, 1, 6, 0], [19, 0, 0, 0, 0], [20, 0, 0, 0, 0], [21, 0, 0, 0, 0], [22, 0, 0, 0, 0], [23, 0, 0, 0, 0], [24, 0, 0, 0, 0], [25, 0, 0, 0, 0], [26, 0, 0, 0, 0], [27, 0, 0, 0, 0], [28, 0, 0, 0, 0], [29, 0, 0, 0, 0]]]

#l1= ['Minute', 'Cars', 'Buses', 'Motorcycles', 'Bicycles', [[1, 59, 1, 15, 0], [2, 30, 2, 10, 0], [3, 53, 1, 14, 0], [4, 29, 5, 7, 0], [5, 23, 3, 11, 1], [6, 49, 9, 9, 0], [7, 22, 4, 10, 0], [8, 50, 17, 13, 1], [9, 23, 4, 12, 0], [10, 43, 14, 9, 0], [11, 31, 6, 7, 1], [12, 38, 5, 12, 0], [13, 36, 2, 5, 0], [14, 45, 1, 15, 0], [15, 48, 4, 17, 0]], [[16, 19, 1, 6, 0], [17, 46, 5, 18, 0], [18, 21, 1, 4, 0], [19, 39, 7, 22, 0], [20, 41, 5, 6, 0], [21, 29, 0, 8, 1], [22, 53, 1, 17, 0], [23, 57, 3, 11, 0], [24, 22, 4, 6, 0], [25, 54, 7, 9, 1], [26, 32, 5, 12, 0], [27, 57, 1, 16, 2], [28, 40, 6, 34, 1], [29, 37, 5, 8, 0], [30, 46, 3, 23, 1]], [[31, 34, 1, 6, 1], [32, 53, 5, 22, 0], [33, 57, 3, 19, 0], [34, 18, 4, 10, 1], [35, 59, 2, 7, 0], [36, 40, 4, 9, 0], [37, 46, 3, 15, 0], [38, 53, 2, 10, 0], [39, 33, 2, 13, 0], [40, 52, 2, 23, 0], [41, 46, 3, 21, 1], [42, 38, 6, 26, 1], [43, 56, 2, 26, 0], [44, 32, 2, 12, 0], [45, 60, 2, 25, 0]], [[46, 46, 5, 16, 0], [47, 39, 2, 17, 2], [48, 60, 1, 16, 0], [49, 26, 6, 26, 0], [50, 44, 4, 15, 0], [51, 46, 3, 27, 0], [52, 36, 2, 17, 0], [53, 70, 2, 10, 0], [54, 39, 1, 4, 0], [55, 39, 2, 28, 0], [56, 50, 0, 22, 0], [57, 47, 4, 16, 0], [58, 44, 0, 12, 0], [59, 84, 1, 5, 0], [60, 25, 5, 15, 1]], [[61, 66, 4, 24, 1], [62, 68, 4, 17, 0], [63, 37, 3, 17, 1], [64, 32, 3, 19, 1], [65, 48, 8, 32, 0], [66, 32, 3, 16, 0], [67, 42, 5, 14, 0], [68, 82, 1, 19, 0], [69, 34, 9, 18, 0], [70, 66, 3, 36, 0], [71, 78, 0, 16, 0], [72, 32, 5, 22, 0], [73, 65, 2, 21, 0], [74, 53, 2, 17, 0], [75, 53, 2, 13, 3]], [[76, 77, 5, 21, 0], [77, 40, 5, 30, 4], [78, 46, 2, 15, 0], [79, 53, 1, 12, 2], [80, 22, 5, 16, 0], [81, 73, 2, 46, 0], [82, 59, 3, 51, 0], [83, 20, 7, 15, 0], [84, 65, 1, 34, 0], [85, 46, 6, 10, 0], [86, 40, 3, 7, 0], [87, 90, 1, 28, 0], [88, 41, 6, 30, 0], [89, 48, 4, 25, 2], [90, 79, 0, 44, 0]]]
# Extract header and data
#l1 = ['Minute', 'Cars', 'Buses', 'Motorcycles', 'Bicycles', [[1, 59, 1, 15, 0], [2, 30, 2, 10, 0], [3, 53, 1, 14, 0], [4, 29, 5, 7, 0], [5, 23, 3, 11, 1], [6, 49, 9, 9, 0], [7, 22, 4, 10, 0], [8, 50, 17, 13, 1], [9, 23, 4, 12, 0], [10, 43, 14, 9, 0], [11, 31, 6, 7, 1], [12, 38, 5, 12, 0], [13, 36, 2, 5, 0], [14, 45, 1, 15, 0], [15, 48, 4, 17, 0]], [[16, 19, 1, 6, 0], [17, 46, 5, 18, 0], [18, 21, 1, 4, 0], [19, 39, 7, 22, 0], [20, 41, 5, 6, 0], [21, 29, 0, 8, 1], [22, 53, 1, 17, 0], [23, 57, 3, 11, 0], [24, 22, 4, 6, 0], [25, 54, 7, 9, 1], [26, 32, 5, 12, 0], [27, 57, 1, 16, 2], [28, 40, 6, 34, 1], [29, 37, 5, 8, 0], [30, 46, 3, 23, 1]], [[31, 34, 1, 6, 1], [32, 53, 5, 22, 0], [33, 57, 3, 19, 0], [34, 18, 4, 10, 1], [35, 59, 2, 7, 0], [36, 40, 4, 9, 0], [37, 46, 3, 15, 0], [38, 53, 2, 10, 0], [39, 33, 2, 13, 0], [40, 52, 2, 23, 0], [41, 46, 3, 21, 1], [42, 38, 6, 26, 1], [43, 56, 2, 26, 0], [44, 32, 2, 12, 0], [45, 60, 2, 25, 0]], [[46, 46, 5, 16, 0], [47, 39, 2, 17, 2], [48, 60, 1, 16, 0], [49, 26, 6, 26, 0], [50, 44, 4, 15, 0], [51, 46, 3, 27, 0], [52, 36, 2, 17, 0], [53, 70, 2, 10, 0], [54, 39, 1, 4, 0], [55, 39, 2, 28, 0], [56, 50, 0, 22, 0], [57, 47, 4, 16, 0], [58, 44, 0, 12, 0], [59, 84, 1, 5, 0], [60, 25, 5, 15, 1]], [[61, 66, 4, 24, 1], [62, 68, 4, 17, 0], [63, 37, 3, 17, 1], [64, 32, 3, 19, 1], [65, 48, 8, 32, 0], [66, 32, 3, 16, 0], [67, 42, 5, 14, 0], [68, 82, 1, 19, 0], [69, 34, 9, 18, 0], [70, 66, 3, 36, 0], [71, 78, 0, 16, 0], [72, 32, 5, 22, 0], [73, 65, 2, 21, 0], [74, 53, 2, 17, 0], [75, 53, 2, 13, 3]], [[76, 77, 5, 21, 0], [77, 40, 5, 30, 4], [78, 46, 2, 15, 0], [79, 53, 1, 12, 2], [80, 22, 5, 16, 0], [81, 73, 2, 46, 0], [82, 59, 3, 51, 0], [83, 20, 7, 15, 0], [84, 65, 1, 34, 0], [85, 46, 6, 10, 0], [86, 40, 3, 7, 0], [87, 90, 1, 28, 0], [88, 41, 6, 30, 0], [89, 48, 4, 25, 2], [90, 79, 0, 44, 0]], [[91, 43, 2, 27, 0], [92, 71, 2, 28, 0], [93, 66, 3, 10, 0], [94, 37, 6, 19, 0], [95, 55, 2, 22, 0], [96, 69, 3, 7, 0], [97, 42, 2, 19, 0], [98, 62, 6, 36, 0], [99, 63, 2, 41, 0], [100, 27, 5, 15, 2], [101, 59, 2, 14, 0], [102, 74, 4, 44, 0], [103, 40, 2, 25, 1], [104, 66, 2, 12, 0], [105, 60, 3, 15, 0]], [[106, 35, 2, 28, 0], [107, 44, 4, 26, 0], [108, 90, 3, 71, 0], [109, 58, 1, 19, 0], [110, 34, 7, 39, 1], [111, 57, 2, 37, 0], [112, 54, 1, 23, 0], [113, 42, 2, 13, 0], [114, 33, 3, 21, 0], [115, 52, 1, 11, 0], [116, 69, 2, 16, 0], [117, 60, 1, 15, 0], [118, 66, 5, 18, 0], [119, 66, 3, 23, 0], [120, 38, 4, 21, 0]], [[121, 34, 3, 23, 0], [122, 61, 2, 26, 0], [123, 52, 1, 38, 2], [124, 52, 1, 21, 0], [125, 59, 0, 40, 0], [126, 32, 4, 35, 0], [127, 55, 1, 13, 0], [128, 61, 4, 29, 0], [129, 43, 3, 17, 0], [130, 32, 3, 17, 1], [131, 72, 2, 13, 0], [132, 48, 2, 20, 0], [133, 37, 5, 28, 0], [134, 55, 1, 21, 0], [135, 40, 10, 28, 1]], [[136, 63, 1, 9, 0], [137, 70, 2, 27, 1], [138, 37, 5, 33, 1], [139, 56, 5, 23, 0], [140, 60, 4, 21, 0], [141, 35, 9, 21, 0], [142, 65, 1, 23, 0], [143, 43, 5, 20, 0], [144, 35, 3, 13, 0], [145, 52, 0, 13, 0], [146, 81, 1, 16, 0], [147, 52, 4, 26, 0], [148, 39, 4, 18, 0], [149, 72, 0, 28, 0], [150, 39, 5, 9, 0]], [[151, 40, 0, 13, 0], [152, 51, 0, 10, 0], [153, 74, 3, 20, 0], [154, 44, 3, 8, 0], [155, 41, 2, 22, 0], [156, 61, 3, 15, 0], [157, 51, 2, 19, 0], [158, 31, 3, 10, 1], [159, 65, 1, 16, 0], [160, 44, 2, 16, 0], [161, 38, 3, 21, 1], [162, 69, 1, 26, 0], [163, 51, 0, 11, 0], [164, 35, 3, 13, 0], [165, 72, 3, 15, 0]], [[166, 60, 3, 7, 0], [167, 62, 2, 12, 0], [168, 52, 6, 12, 0], [169, 44, 3, 22, 0], [170, 55, 4, 25, 0], [171, 77, 1, 21, 0], [172, 34, 1, 22, 0], [173, 46, 1, 17, 0], [174, 49, 4, 12, 0], [175, 40, 5, 22, 0], [176, 85, 3, 24, 0], [177, 38, 3, 34, 0], [178, 41, 4, 14, 0], [179, 58, 1, 16, 0], [180, 45, 3, 19, 1]]]

l1 = ['Minute', 'Cars', 'Buses', 'Motorcycles', 'Bicycles', [[1, 59, 1, 15, 0], [2, 30, 2, 10, 0], [3, 53, 1, 14, 0], [4, 29, 5, 7, 0], [5, 23, 3, 11, 1], [6, 49, 9, 9, 0], [7, 22, 4, 10, 0], [8, 50, 17, 13, 1], [9, 23, 4, 12, 0], [10, 43, 14, 9, 0], [11, 31, 6, 7, 1], [12, 38, 5, 12, 0], [13, 36, 2, 5, 0], [14, 45, 1, 15, 0], [15, 48, 4, 17, 0]], [[16, 19, 1, 6, 0], [17, 46, 5, 18, 0], [18, 21, 1, 4, 0], [19, 39, 7, 22, 0], [20, 41, 5, 6, 0], [21, 29, 0, 8, 1], [22, 53, 1, 17, 0], [23, 57, 3, 11, 0], [24, 22, 4, 6, 0], [25, 54, 7, 9, 1], [26, 32, 5, 12, 0], [27, 57, 1, 16, 2], [28, 40, 6, 34, 1], [29, 37, 5, 8, 0], [30, 46, 3, 23, 1]], [[31, 34, 1, 6, 1], [32, 53, 5, 22, 0], [33, 57, 3, 19, 0], [34, 18, 4, 10, 1], [35, 59, 2, 7, 0], [36, 40, 4, 9, 0], [37, 46, 3, 15, 0], [38, 53, 2, 10, 0], [39, 33, 2, 13, 0], [40, 52, 2, 23, 0], [41, 46, 3, 21, 1], [42, 38, 6, 26, 1], [43, 56, 2, 26, 0], [44, 32, 2, 12, 0], [45, 60, 2, 25, 0]], [[46, 46, 5, 16, 0], [47, 39, 2, 17, 2], [48, 60, 1, 16, 0], [49, 26, 6, 26, 0], [50, 44, 4, 15, 0], [51, 46, 3, 27, 0], [52, 36, 2, 17, 0], [53, 70, 2, 10, 0], [54, 39, 1, 4, 0], [55, 39, 2, 28, 0], [56, 50, 0, 22, 0], [57, 47, 4, 16, 0], [58, 44, 0, 12, 0], [59, 84, 1, 5, 0], [60, 25, 5, 15, 1]], [[61, 66, 4, 24, 1], [62, 68, 4, 17, 0], [63, 37, 3, 17, 1], [64, 32, 3, 19, 1], [65, 48, 8, 32, 0], [66, 32, 3, 16, 0], [67, 42, 5, 14, 0], [68, 82, 1, 19, 0], [69, 34, 9, 18, 0], [70, 66, 3, 36, 0], [71, 78, 0, 16, 0], [72, 32, 5, 22, 0], [73, 65, 2, 21, 0], [74, 53, 2, 17, 0], [75, 53, 2, 13, 3]], [[76, 77, 5, 21, 0], [77, 40, 5, 30, 4], [78, 46, 2, 15, 0], [79, 53, 1, 12, 2], [80, 22, 5, 16, 0], [81, 73, 2, 46, 0], [82, 59, 3, 51, 0], [83, 20, 7, 15, 0], [84, 65, 1, 34, 0], [85, 46, 6, 10, 0], [86, 40, 3, 7, 0], [87, 90, 1, 28, 0], [88, 41, 6, 30, 0], [89, 48, 4, 25, 2], [90, 79, 0, 44, 0]], [[91, 43, 2, 27, 0], [92, 71, 2, 28, 0], [93, 66, 3, 10, 0], [94, 37, 6, 19, 0], [95, 55, 2, 22, 0], [96, 69, 3, 7, 0], [97, 42, 2, 19, 0], [98, 62, 6, 36, 0], [99, 63, 2, 41, 0], [100, 27, 5, 15, 2], [101, 59, 2, 14, 0], [102, 74, 4, 44, 0], [103, 40, 2, 25, 1], [104, 66, 2, 12, 0], [105, 60, 3, 15, 0]], [[106, 35, 2, 28, 0], [107, 44, 4, 26, 0], [108, 90, 3, 71, 0], [109, 58, 1, 19, 0], [110, 34, 7, 39, 1], [111, 57, 2, 37, 0], [112, 54, 1, 23, 0], [113, 42, 2, 13, 0], [114, 33, 3, 21, 0], [115, 52, 1, 11, 0], [116, 69, 2, 16, 0], [117, 60, 1, 15, 0], [118, 66, 5, 18, 0], [119, 66, 3, 23, 0], [120, 38, 4, 21, 0]], [[121, 34, 3, 23, 0], [122, 61, 2, 26, 0], [123, 52, 1, 38, 2], [124, 52, 1, 21, 0], [125, 59, 0, 40, 0], [126, 32, 4, 35, 0], [127, 55, 1, 13, 0], [128, 61, 4, 29, 0], [129, 43, 3, 17, 0], [130, 32, 3, 17, 1], [131, 72, 2, 13, 0], [132, 48, 2, 20, 0], [133, 37, 5, 28, 0], [134, 55, 1, 21, 0], [135, 40, 10, 28, 1]], [[136, 63, 1, 9, 0], [137, 70, 2, 27, 1], [138, 37, 5, 33, 1], [139, 56, 5, 23, 0], [140, 60, 4, 21, 0], [141, 35, 9, 21, 0], [142, 65, 1, 23, 0], [143, 43, 5, 20, 0], [144, 35, 3, 13, 0], [145, 52, 0, 13, 0], [146, 81, 1, 16, 0], [147, 52, 4, 26, 0], [148, 39, 4, 18, 0], [149, 72, 0, 28, 0], [150, 39, 5, 9, 0]], [[151, 40, 0, 13, 0], [152, 51, 0, 10, 0], [153, 74, 3, 20, 0], [154, 44, 3, 8, 0], [155, 41, 2, 22, 0], [156, 61, 3, 15, 0], [157, 51, 2, 19, 0], [158, 31, 3, 10, 1], [159, 65, 1, 16, 0], [160, 44, 2, 16, 0], [161, 38, 3, 21, 1], [162, 69, 1, 26, 0], [163, 51, 0, 11, 0], [164, 35, 3, 13, 0], [165, 72, 3, 15, 0]], [[166, 60, 3, 7, 0], [167, 62, 2, 12, 0], [168, 52, 6, 12, 0], [169, 44, 3, 22, 0], [170, 55, 4, 25, 0], [171, 77, 1, 21, 0], [172, 34, 1, 22, 0], [173, 46, 1, 17, 0], [174, 49, 4, 12, 0], [175, 40, 5, 22, 0], [176, 85, 3, 24, 0], [177, 38, 3, 34, 0], [178, 41, 4, 14, 0], [179, 58, 1, 16, 0], [180,45,3,19,1]]]


header = l1[:5]  # First 5 elements are headers

data = l1[5:]  # The rest are data lists

# File path for the CSV file
file_path = 'vehicle_data.csv'

# Write data to CSV file
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(header)
    
    # Write the data
    for i in range(0,12):
        for row in data[i]:
            writer.writerow(row)

print(f'Data has been written to {file_path}')



