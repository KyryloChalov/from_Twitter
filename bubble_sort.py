YELLOW_ON_BLACK = "\033[33;40;1m"
CYAN_ON_BLACK = "\033[36;40;1m"

YELLOW_ON_BLUE = "\33[44;93;1m"
BLUE_ON_YELLOW = "\33[103;34;1m"
WHITE_ON_BLACK = "\33[40;37;5m"
RESET = "\33[0m"
ITALICS = "\33[3m"
BLACK_BACK = "\33[40m"


def blanked_10(str):
    try:
        int_from_str = int(str)
    except:  # noqa - просто повертаємо вхідне значення, якщо його не можна зробити int
        return str
    result = f'{" " if int_from_str < 10 else ""}{str}'
    return result


def color_print(to_print, color_code=RESET, end=""):
    print(f"{color_code}{blanked_10(str(to_print))}{RESET}", end=end)


def print_bubbled_array(arr, j=float("inf"), m=float("inf")):  # = 2**31 - 1

    len_array = len(arr)
    if j <= len_array:
        color_print(21 * " ")

    for k in range(len_array):

        if k == j:
            color_print(f" {(arr[j])} ", YELLOW_ON_BLUE)
            color_print(f" {(arr[j+1])} ", BLUE_ON_YELLOW)

        # elif k not in [j, j + 1]:
        elif all((k!=j, k!=j+1, k<m)):
            color_print(f" {(arr[k])} ")

        elif k >= m:
            color_print(f" {(arr[k])} ", WHITE_ON_BLACK)

    print()


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # print_bubbled_array(arr, j)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print_bubbled_array(arr, j, n-i)
    return arr


def main(arr):
    color_print("    Original Array >>", ITALICS)
    print_bubbled_array(arr)

    bubble_sort(arr)

    color_print("Final Sorted array >>", WHITE_ON_BLACK + ITALICS)
    print_bubbled_array(arr, m=0)
    print("\n")


if __name__ == "__main__":

    arr = [64, 84, 91, 10, 15, 4, 22, 99, 1, 12]

    main(arr)
