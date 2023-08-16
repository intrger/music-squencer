from structural.mainwindow import Window


if __name__ == '__main__':
    handle = Window()
    handle2 = Window()
    handle2.title('Daw')
    handle.title('Daw2')
    handle2.geometry('1280x720')
    handle.geometry('1280x720')

    assert(handle is handle2)

    handle2.mainloop()
    handle.mainloop()









