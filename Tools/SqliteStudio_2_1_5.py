#!/usr/bin/python
# -*- coding: UTF-8 -*-
import zipfile
import sys
import os

#使用python 库
def run():
    tmpZipFilePath=os.getcwd()+"/Tools/sqlitestudio-2.1.5/sqlitestudio-2.1.5.exe.zip"
    tmpZipFilePath=tmpZipFilePath.replace('\\','/')
    # print(tmpZipFilePath)
    tmpTargetDirPath=os.path.splitext(tmpZipFilePath)[0]
    if os.path.isdir(tmpTargetDirPath)==False:
        # 先解压
        print(u"第一次打开，先解压\n")
        tmpZipFile=zipfile.ZipFile(tmpZipFilePath)
        print(tmpZipFile.namelist())


        tmpTargetDirPath=os.path.splitext(tmpZipFilePath)[0]
        os.mkdir(tmpTargetDirPath)
            

        for tmpOneName in tmpZipFile.namelist():
            tmpZipFile.extract(tmpOneName,tmpTargetDirPath)
        tmpZipFile.close()
        print(u"解压完成\n")
    
    # 直接打开
    tmpExePath=os.getcwd()+"/Tools/sqlitestudio-2.1.5/sqlitestudio-2.1.5.exe/sqlitestudio-2.1.5.exe"
    print(tmpExePath)
    os.system(tmpExePath)

if __name__=="__main__":
    run()