import pyzipper

def compress_file_with_password(file_path, password):
    # read the file contents
    with open(file_path, 'rb') as f:
        data = f.read()
    # create a new zip file with the given name
    with pyzipper.AESZipFile(file_path + '.zip', 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zip_file:
        # set password for the zip file
        zip_file.setpassword(password.encode('utf-8'))
        # write the file to the zip file
        zip_file.writestr(file_path, data)

if __name__ == '__main__':
    # specify the file path and password
    compress_file_with_password('08.파일 압축 프로그램\압축.txt', '1234')
