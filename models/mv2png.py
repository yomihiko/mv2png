import os
from tkinter import messagebox
import cv2
from models.fileSelectBox import Path

class Mv2Png:
    def __init__(self):
        a = ""

    def convert(self, path: Path):
        # MP4ファイル読み込み
        mp4FilePath = path.filePath.strip()
        # MP4ファイルのパスが空の場合はエラー
        if not mp4FilePath:
            messagebox.showerror('エラー', 'MP4ファイルが指定されていません。')
            return
        # MP4ファイルが存在しない場合はエラー
        if not os.path.exists(mp4FilePath):
            messagebox.showerror('エラー', 'MP4ファイルが存在しません。')
            return
        cap = cv2.VideoCapture(mp4FilePath)

        # 保存先フォルダ読み込み
        saveFolderPath = path.folderPath.strip()
        # 保存先フォルダが空の場合はエラー
        if not saveFolderPath:
            messagebox.showerror('エラー', '出力先フォルダが指定されていません。')
            return
        # 保存先フォルダが存在しない場合はエラー
        if not os.path.exists(saveFolderPath):
            messagebox.showerror('エラー', '出力先フォルダが存在しません。')
            return

        # MP4のファイル名の実を取得して、出力する画像のファイル名に使用する
        mp4FileName = os.path.splitext(os.path.basename(mp4FilePath))[0]

        count = 0
        result = False
        while True:
            ret, frame = cap.read()
            if ret == True:
                count += 1
                # 画像を生成
                try:
                    result = cv2.imwrite(saveFolderPath + '/{:s}_{:05d}.png'.format(mp4FileName, count), frame)
                except cv2.error as e:
                    messagebox.showerror('エラー', 'PNGファイル出力が失敗しました。\n{e}')
                    return
            else:
                break
        
        if result:
            messagebox.showinfo('出力完了', 'PNGファイルを出力しました。')
        else:
            messagebox.showerror('エラー', 'PNGファイル出力が失敗しました。')