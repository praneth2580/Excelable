import os
import gui

excel_files = []

def fetch_excel():
    start_path = '.' # current directory
    for path,dirs,files in os.walk(start_path):
        for filename in files:
            filename = os.path.join(path,filename);
            if (filename.__contains__('.xlsx')):
                excel_files.append(filename)
            # print(os.path.join(path,filename))

def main():
    fetch_excel()
    app = gui.App(files=excel_files)
    app.mainloop()

if __name__ == '__main__':
    main()
    print(excel_files)