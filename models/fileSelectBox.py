from tkinter import filedialog

class Path:
    def __init__(self):
        self.filePath = ""
        self.folderPath = ""

    def selectFolder(self, initialdir):
        path = filedialog.askdirectory(initialdir=initialdir)
        # パスに値がある場合のみ上書き。キャンセルされた場合などは上書きしない。
        if path:
            self.folderPath = path

    def selectFile(self, filetypes, initialdir):
        path = filedialog.askopenfilename(filetypes=filetypes, initialdir=initialdir)
        if path:
            self.filePath = path
