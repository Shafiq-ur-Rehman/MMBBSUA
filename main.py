import csv
import math


# import os,sys


def data_copy():
    # file to store average movement
    file = open("human-data.csv", "w")
    # tile of data
    data = ["X", ",", "Y", ",", "Time", ",", "Tx", ",", "Ty", "\n"]
    # writing line
    file.writelines(data)
    # file1.close()

    oTx = '2117'  # old target time x-axis
    oTy = '531'  # old target time y-axis
    # reading human mouse movement data
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # reading title of human mouse movement data
        next(csv_reader)
        template = 1
        try:
            for line in csv_reader:
                x = line[0]
                y = line[1]
                time = line[2]
                ntx = line[3]
                nty = line[4]
                if ntx != oTx and nty != oTy:
                    template += 1
                if template != 280:
                    data = [x, ",", y, ",", time, ",", ntx, ",", nty, "\n"]
                # writing line
                file.writelines(data)

                oTx = ntx
                oTy = nty

        except:
            print("Exception Occurred: ")

        finally:
            file.close()
            print("File is ended: ")


# calculate the avg-duration of each mouse movement
def average_duration():
    N = 0  # number of movements
    movement_time = 0  # movement time of each movement
    oTx = 2117  # old target time x-axis
    oTy = 531  # old target time y-axis

    # file to store total movement of each movement
    # total_movement_file = open("total-duration.csv", "w")
    # tile of data
    # total_movement_data = ["total time\n"]
    # writing line
    # total_movement_file.writelines(total_movement_data)

    # file to store average movement time of each movement
    avg_movement_file = open("avg-duration.csv", "w")
    # tile of data
    avg_movement_data = ["average time\n"]
    # writing line
    avg_movement_file.writelines(avg_movement_data)

    # reading human mouse movement data
    with open('human-data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # reading title of human mouse movement data
        next(csv_reader)
        try:
            for line in csv_reader:
                x = int(line[0])
                y = int(line[1])
                time = int(line[2])
                ntx = int(line[3])
                nty = int(line[4])

                # checking either movement is ended or not
                if ntx != oTx and nty != oTy:
                    # file to store total mouse movement
                    # total_movement_data = [str(movement_time), "\n"]
                    # total_movement_file.writelines(total_movement_data)

                    # average time of each mouse movement
                    average_time = movement_time / N
                    # file to store average mouse movement
                    avg_movement_data = [str(average_time), "\n"]
                    avg_movement_file.writelines(avg_movement_data)
                    # set the counter to zero for counting step of next mouse movement
                    N = 0
                # calculating movement time of each mouse movement
                movement_time = movement_time + time
                # counter of each movement step
                N = N + 1
                oTx = ntx
                oTy = nty

        except:
            print("Exception Occurred: ")

        finally:
            avg_movement_file.close()
            # total_movement_file.close()
            print("File is ended: ")


def average_distance():
    x1 = 0  # previous mouse movement step x-axis
    x2 = 0  # next mouse movement step x-axis
    y1 = 0  # next mouse movement step y-axis
    y2 = 0  # next mouse movement step y-axis
    oTx = 2117  # old target time x-axis
    oTy = 531  # old target time y-axis
    avg_distance = 0  # average distance of each mouse movement
    check = True  # to copy the first value of x
    xaxis_sum = 0.0
    yaxis_sum = 0.0
    count = 0

    # file to store average of x-axis and y-axis for each movement
    xy_file = open("xaxis and yaxis average-value.csv", "w")
    # tile of data
    xy_data = ["X-axis", ",", "Y-axis", "\n"]
    # writing line
    xy_file.writelines(xy_data)
    # file1.close()

    # file to store average distance
    file = open("avg-distance.csv", "w")
    # tile of data
    data = ["average distance\n"]
    # writing line
    file.writelines(data)
    # file1.close()

    # reading human mouse movement data from human-data files
    with open('human-data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # reading title of human mouse movement data
        next(csv_reader)
        try:
            for line in csv_reader:
                x2 = int(line[0])
                y2 = int(line[1])
                time = int(line[2])
                ntx = int(line[3])
                nty = int(line[4])

                if check:
                    x1 = x2
                    y1 = y2
                    check = False
                else:
                    if ntx != oTx and nty != oTy:
                        xaxis_avg = xaxis_sum / count
                        yaxis_avg = yaxis_sum / count
                        xy_data = [str(xaxis_avg), ",", str(yaxis_avg), "\n"]
                        xy_file.writelines(xy_data)
                        xaxis_sum = 0.0
                        yaxis_sum = 0.0

                        # file1 = open("avg-distance.txt", "a")
                        data = [str(avg_distance), "\n"]
                        file.writelines(data)
                        # file1.close()
                        check = True
                        # reset the variable average distance
                        avg_distance = 0
                        count = 0
                        # print(count)
                    else:
                        avg_distance += math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

                xaxis_sum += x2
                yaxis_sum += y2
                oTx = ntx
                oTy = nty
                count += 1


        except:
            print("Exception Occurred: ")

        finally:
            xy_file.close()
            file.close()
            print("File is ended: ")


def average_speed():
    # opening the file avg-distance file
    distance_file = open("avg-distance.csv", "r")

    # creating list to store the value of distance
    avg_distance = list()

    # counter is used to calculate the number of values in the file
    count = 0
    # skip the title row
    next(distance_file)
    # reading value from the file and storing in the list
    try:
        for distance in distance_file.read().split('\n'):
            if distance != "":
                # print(float(distance))
                avg_distance.append(float(distance))
            count += 1
            # print("{}, {}".format(count, distance.strip()))
            # print(count)
    except ValueError as e:
        print(count)
        print("Error : ", e)
    finally:
        print("File is ended: ")

    # opening the file avg-duration file
    duration_file = open("avg-duration.csv", "r")

    # creating list to store the value of duration and distance
    avg_duration = list()

    # skip the title row
    next(duration_file)

    # counter is used to calculate the number of values in the file
    count = 0
    # reading value from the file and storing in the list
    try:
        for duration in duration_file.read().split('\n'):
            if duration != "":
                # print(float(duration))
                avg_duration.append(float(duration))
            count += 1
            # print("{}, {}".format(count, distance.strip()))
            # print(count)
    except ValueError as e:
        print(count)
        print("Error : ", e)
    finally:
        print("File is ended: ")

    # file to store variance distance
    file = open("avg-speed.csv", "w")
    # tile of data
    data = ["Average Speed", "\n"]
    # writing line
    file.writelines(data)

    avg_speed = list()
    # formula to calculate the average speed is = distance/time
    try:
        for i in range(count - 1):
            speed = avg_distance[i] / avg_duration[i]
            data = [str(speed), "\n"]
            file.writelines(data)
            avg_speed.append(speed)
            print(avg_distance[i] / avg_duration[i])

    except ValueError as e:
        print("Error : ", e)
    finally:
        file.close()
        print("Function is ended ")


def variance_duration():
    # opening the file avg-duration file
    duration_file = open("avg-duration.csv", "r")

    # creating list to store the value of average duration
    avg_duration = list()

    # skip the title row
    next(duration_file)

    # reading average movement time value from the file and storing in the list
    try:
        for duration in duration_file.read().split('\n'):
            if duration != "":
                # average duration from function 1
                avg_duration.append(float(duration))
    except ValueError as e:
        print("Error : ", e)
    finally:
        duration_file.close()
        # print("File is ended: ")

    # file to store variance distance
    file = open("variance-duration.csv", "w")
    # tile of data
    data = ["Variance Duration", "\n"]
    # writing line
    file.writelines(data)

    N = 0  # number of movements
    movement_time = 0.0  # movement time of each movement
    oTx = 2117  # old target time x-axis
    oTy = 531  # old target time y-axis

    var_duration = list()
    total_duration = 0.0

    # counter to read every value from the avg_duration list
    count = 0
    # reading the first value of avg_duration from the list
    avg_movement_time = avg_duration[count]
    # print(len(avg_duration))
    # reading human mouse movement data
    with open('human-data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # reading title of human mouse movement data
        next(csv_reader)
        try:
            for line in csv_reader:
                x = int(line[0])
                y = int(line[1])
                time = int(line[2])
                ntx = int(line[3])
                nty = int(line[4])
                # checking either movement is ended or not
                if ntx != oTx and nty != oTy:
                    data = [str(total_duration), "\n"]
                    # writing line
                    file.writelines(data)
                    # storing the sum of each mouse movement (t- u)^2
                    var_duration.append(total_duration)
                    total_duration = 0.0
                    count += 1
                    # print(count)
                    if count < len(avg_duration):
                        # average time of each mouse movement
                        avg_movement_time = avg_duration[count]
                # calculating movement time of each mouse movement (t- u)
                movement_time = avg_movement_time - time
                # calculating movement time of each mouse movement (t- u)^2
                total_duration += pow(movement_time, 2)
                # counter of each movement step
                N = N + 1
                oTx = ntx
                oTy = nty

        except ValueError as e:
            print("Error : ", e)
        finally:
            file.close()
            csv_file.close()
            print("File is ended: ")


def variance_distance():
    x_axis = list()
    y_axis = list()

    # opening the file avg-distance file
    with open('xaxis and yaxis average-value.csv', 'r') as xy_file:
        xy_reader = csv.reader(xy_file)
        # reading title of human mouse movement data
        next(xy_reader)
        try:
            for line in xy_reader:
                x = float(line[0])
                y = float(line[1])
                x_axis.append(x)
                y_axis.append(y)

        except ValueError as e:
            print("Error : ", e)
        finally:
            xy_file.close()
            print("File is ended: ")

    # file to store variance distance
    file = open("variance-distance.csv", "w")
    # tile of data
    data = ["Variance Distance", "\n"]
    # writing line
    file.writelines(data)
    # file1.close()

    N = 0  # number of movements
    movement_time = 0.0  # movement time of each movement
    oTx = 2117  # old target time x-axis
    oTy = 531  # old target time y-axis
    xaxis_sub = 0.0  # subtraction of x-axis value
    yaxis_sub = 0.0  # subtraction of y-axis value
    var_distance = []  # list to store variance distance
    total_duration = 0.0

    # counter to read every value from the avg_duration list
    count = 0

    # reading human mouse movement data
    with open('human-data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # reading title of human mouse movement data
        next(csv_reader)
        try:
            for line in csv_reader:
                x = int(line[0])
                y = int(line[1])
                time = int(line[2])
                ntx = int(line[3])
                nty = int(line[4])

                # checking either movement is ended or not
                if ntx != oTx and nty != oTy:
                    distance = (xaxis_sub * yaxis_sub) / (N - 1)
                    data = [str(distance), "\n"]
                    file.writelines(data)
                    var_distance.append(distance)
                    xaxis_sub = 0.0
                    yaxis_sub = 0.0
                    count += 1
                    N = 0
                    # print(count)
                # counter of each movement step
                if count < len(x_axis):
                    xaxis_sub += x - x_axis[count]
                    yaxis_sub += y - y_axis[count]
                N = N + 1
                oTx = ntx
                oTy = nty

        except ValueError as e:
            print("Error : ", e)
        finally:
            # print(var_distance)
            file.close()
            csv_file.close()
            print("File is ended: ")


def variance_speed():
    # opening the file avg-distance file
    vari_distance_file = open("variance-distance.csv", "r")

    # creating list to store the value of distance
    vari_distance = list()

    # counter is used to calculate the number of values in the file
    count = 0
    # skip the title row
    next(vari_distance_file)
    # reading value from the file and storing in the list
    try:
        for distance in vari_distance_file.read().split('\n'):
            if distance != "":
                # print(float(distance))
                vari_distance.append(float(distance))
            count += 1
            # print("{}, {}".format(count, distance.strip()))
            # print(count)
    except ValueError as e:
        print(count)
        print("Error : ", e)
    finally:
        print("File is ended: ")

    # opening the file avg-duration file
    vari_duration_file = open("variance-duration.csv", "r")

    # creating list to store the value of duration and distance
    vari_duration = list()

    # skip the title row
    next(vari_duration_file)

    # counter is used to calculate the number of values in the file
    count = 0
    # reading value from the file and storing in the list
    try:
        for duration in vari_duration_file.read().split('\n'):
            if duration != "":
                # print(float(duration))
                vari_duration.append(float(duration))
            count += 1
            # print("{}, {}".format(count, distance.strip()))
            # print(count)
    except ValueError as e:
        # print(count)
        print("Error : ", e)
    finally:
        print("File is ended: ")

    # file to store variance distance
    file = open("variance-speed.csv", "w")
    # tile of data
    data = ["Variance Speed", "\n"]
    # writing line
    file.writelines(data)

    vari_speed = list()
    # formula to calculate the average speed is = distance/time
    try:
        for i in range(count - 1):
            vari_speed.append(vari_distance[i] / vari_duration[i])
            data= [str((vari_distance[i] / vari_duration[i])), "\n"]
            file.writelines(data)
            # print(vari_distance[i] / vari_duration[i])

    except ValueError as e:
        print("Error : ", e)
    finally:
        file.close()
        print("Variance speed Function ended: ")


def standard_deviation_duration():
    # opening the file variance duration file
    standard_deviation_duration_file = open("variance-duration.csv", "r")

    # creating list to store the value of distance
    standard_deviation_duration = list()

    # counter is used to calculate the number of values in the file
    count = 0
    # skip the title row
    next(standard_deviation_duration_file)

    # file to store variance distance
    file = open("standard_deviation_duration.csv", "w")
    # tile of data
    data = ["Standard Deviation Duration", "\n"]
    # writing line
    file.writelines(data)

    # reading value from the file and storing in the list
    try:
        for distance in standard_deviation_duration_file.read().split('\n'):
            if distance != "":
                sdt= math.sqrt(float(distance))
                data = [str(sdt), "\n"]
                file.writelines(data)
                # standard_deviation_duration.append(float(sdt))
            count += 1
    except ValueError as e:
        print(count)
        print("Error : ", e)
    finally:
        file.close()
        print("File is ended: ")


def standard_deviation_distance():
    # opening the file avg-distance file
    standard_deviation_distance_file = open("variance-distance.csv", "r")

    # creating list to store the value of distance
    standard_deviation_distance = list()

    # counter is used to calculate the number of values in the file
    count = 0
    # skip the title row
    next(standard_deviation_distance_file)

    # file to store variance distance
    file = open("standard_deviation_distance.csv", "w")
    # tile of data
    data = ["Standard Deviation Distance", "\n"]
    # writing line
    file.writelines(data)

    # reading value from the file and storing in the list
    try:
        for distance in standard_deviation_distance_file.read().split('\n'):
            if distance != "":
                std = math.sqrt(abs(float(distance)))
                # data = [str(std), "\n"]
                # file.writelines(data)
                print(distance)
                standard_deviation_distance.append(float(distance))
            count += 1
    except ValueError as e:
        print(count)
        print("Error : ", e)
    finally:
        file.close()
        print("File is ended: ")


def standard_deviation_speed():
    # opening the file variance speed file
    standard_deviation_speed_file = open("variance-speed.csv", "r")

    # creating list to store the value of speed
    standard_deviation_speed = list()

    # counter is used to calculate the number of values in the file
    count = 0
    # skip the title row
    next(standard_deviation_speed_file)

    # file to store variance speed
    file = open("standard_deviation_speed.csv", "w")
    # tile of data
    data = ["Standard Deviation Speed", "\n"]
    # writing line
    file.writelines(data)

    # reading value from the file and storing in the list
    try:
        for speed in standard_deviation_speed_file.read().split('\n'):
            if speed != "":
                std = math.sqrt(abs(float(speed)))
                data = [str(std), "\n"]
                file.writelines(data)
                # print(speed)
                # standard_deviation_speed.append(float(speed))
            count += 1
    except ValueError as e:
        print(count)
        print("Error : ", e)
    finally:
        file.close()
        print("File is ended: ")


def main():
    # data_copy()
    # average_duration()
    # average_distance()
    # average_speed()
    # variance_duration()
    # variance_distance()
    # variance_speed()
    # standard_deviation_duration()
    # standard_deviation_distance()
    standard_deviation_speed()


if __name__ == '__main__':
    main()
