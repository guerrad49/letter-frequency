def plot_data(x, y):
    import matplotlib.pyplot as plt
    plt.bar(x,y)
    plt.xlabel('letters')
    plt.ylabel('frequency')
    plt.title('Letter Frequency in Cipher Text')
    plt.show()


if __name__ == '__main__':
    with open('cipher.txt') as f:
        cipher = f.read()

    #generate alphabet based on ascii values
    x_axis = [chr(ascii_val) for ascii_val in range(97,123)]
    #generate letter count in cipher
    y_axis = [cipher.count(letter) for letter in x_axis]

    plot_data(x_axis,y_axis)
