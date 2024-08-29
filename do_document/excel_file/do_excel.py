# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
# 导入xlrd模块
import xlrd,os


class DoExcel():
    def __init__(self,filename=r"./test01.xlsx"):
        self.book = xlrd.open_workbook(filename)
        self.sheet = self.book.sheet_names()        # 格式：['Sheet1']
        print(f"sheet 列表：{self.sheet}")

    def get_sheet(self, index=0):
        """
        通过索引获取指定  sheet页
        :param index:
        :return:
        """
        sheet_name = self.sheet[index]
        print(f"sheet >>>：\n{sheet_name}")
        return sheet_name

    def get_row_col(self,index=0):
        """
        获取指定sheet页中的行数和列数
        :param index:
        :return:
        """
        nrows = self.book.sheet_by_index(index).nrows
        ncols = self.book.sheet_by_index(index).ncols
        print(f"行数：{nrows}")
        print(f"列数：{ncols}")
        return nrows,ncols

    # 遍历所有行的内容
    def get_all_rows(self):
        for i in range(self.book.nsheets):
            sheet_name = self.sheet[i]
            sheet = self.book.sheet_by_name(sheet_name)
            for row in range(sheet.nrows):
                print(f"{row + 1}行内容：{sheet.row_values(row)}")

    # 遍历所有单元格内容
    def get_all_cell(self):
        for i in range(self.book.nsheets):
            sheet_name = self.sheet[i]
            sheet = self.book.sheet_by_name(sheet_name)
            for row in range(sheet.nrows):
                for col in range(sheet.ncols):
                    print(f"第{row + 1}行第{col + 1}列内容：{sheet.cell_value(row, col)}")

    # 修改文件拓展名
    def change_file_suffix(self,filename = r"./test11.xls",suffix=".xlsx"):
        """
        修改文件拓展名
        :param filename:源文件名
        :param suffix:新文件拓展名。默认为：.xlsx
        :return:
        """
        old_suffix = os.path.splitext(filename)[1]
        new_filename = filename.replace(old_suffix,suffix)
        os.rename(filename,new_filename)


if __name__ == '__main__':
    do_excel = DoExcel()
    do_excel.change_file_suffix()
