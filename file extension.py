import pathlib
file=input('the Filename:')
file_extension = pathlib.Path(file).suffix
print('The extension of the file is :',file_extension)