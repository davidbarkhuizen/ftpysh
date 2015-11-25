2015 david barkhuizen

import ftplib
import argparse

# -------------------------

parser = argparse.ArgumentParser(prog='ftpysh = python ftp push')

parser.add_argument("file")

parser.add_argument("server")
parser.add_argument("user")
parser.add_argument("password")
parser.add_argument("destination_root")

args = parser.parse_args()

# -------------------------

session = ftplib.FTP(args.server, args.user, args.password)

file = open(args.file,'rb')

file_cut = args.file[args.file.rfind('/'):] if args.file.find('/') != -1 else args.file
session.storbinary('STOR ' + args.destination_root + '/' + file_cut, file)
file.close()

session.quit()



