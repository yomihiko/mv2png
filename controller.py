import tkinter
from tkinter import Entry
from models.fileSelectBox import Path
from models.mv2png import Mv2Png

# コントローラー
class Controller:
    def __init__(self):
        self.path = Path()
        self.mv2png = Mv2Png()
    # フォルダ選択ダイアログ
    def onClickFolderRef(self , pathEntry: Entry, initialdir):
        self.path.selectFolder(initialdir)
        pathEntry.configure(state="normal")
        pathEntry.delete(0, "end")
        pathEntry.insert(0, self.path.folderPath)
        pathEntry.configure(state="readonly")
    # ファイル選択ダイアログ
    def onClickFileRef(self , pathEntry: Entry, filetypes, initialdir):
        self.path.selectFile(filetypes, initialdir)
        pathEntry.configure(state="normal")
        pathEntry.delete(0, "end")
        pathEntry.insert(0, self.path.filePath)
        pathEntry.configure(state="readonly")
    # 変換ボタン
    def onClickConvert(self):
        self.mv2png.convert(self.path)
    # アプリ終了
    def shutDown(self, root: tkinter.Tk):
        root.destroy()
                