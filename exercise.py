import multiprocessing
from mower import Mower
import os


manager = multiprocessing.Manager()
global_mowers_position = manager.dict()
mowers_final_postion = manager.dict()


def mower_shifting(upper_right_corner, initial_position, shifting_list):
    """
    This function creates a new mower and will give its final position.

    Parameter:
    ----------
    upper_right_corner : list int, upper right corner
    initial_position : list int, initial position
    shifting_list : list, shifting list

    Return:
    -------
    None
    """

    mower = Mower(
        int(initial_position[0]), int(initial_position[1]),
        initial_position[2], upper_right_corner[0], upper_right_corner[1])

    for i in shifting_list:
        if i == "L":
            mower.move_to_left(mower.orientation)
        elif i == "R":
            mower.move_to_rigth(mower.orientation)
        elif i == "F":
            mower.move_forward(global_mowers_position)
        global_mowers_position[multiprocessing.current_process()._identity[0]] = (mower.X, mower.Y)

    mowers_final_postion[multiprocessing.current_process()._identity[0]] = mower.get_mower_position()


if __name__ == '__main__':
    processes = []
    input_file_name = 'input'
    output_file_name = 'output'
    dirname = os.getcwd()
    input_path_file = "{}/{}".format(dirname, input_file_name)
    output_path_file = "{}/{}".format(dirname, output_file_name)

    with open(input_path_file, 'r') as reader:
        upper_right_corner = list(map(int, reader.readline().split()))
        file_content = reader.readlines()

        for i in range(len(file_content)):
            if i % 2 == 0:
                initial_position = file_content[i].split()

            else:
                shifting_list = [j for j in file_content[i] if j != '\n']
                p = multiprocessing.Process(
                    target=mower_shifting,
                    args=(upper_right_corner,
                         initial_position, shifting_list,))
                processes.append(p)
                p.start()

        for process in processes:
            process.join()

        final_positions = sorted(
            [(key, value) for key, value in mowers_final_postion.items()],
            key=lambda x: x[1])
        f = open(output_path_file, "w")
        print("*********** ouput ***************\n")
        for i in final_positions:
            f.write("{}{}{}\n".format(i[1][0], i[1][1], i[1][2]))
            print("{}{}{}\n".format(i[1][0], i[1][1], i[1][2]))
        f.close()
