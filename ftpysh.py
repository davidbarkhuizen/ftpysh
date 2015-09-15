import ftplib
import argparse

# -------------------------

parser = argparse.ArgumentParser()

parser.add_argument("server")
parser.add_argument("user")
parser.add_argument("password")
parser.add_argument("file")
parser.add_argument("destination_root")

args = parser.parse_args()

# -------------------------

session = ftplib.FTP(args.server, args.user, args.password)

file = open(args.file,'rb')
session.storbinary('STOR ' + args.destination_root + '/' + args.file, file)
file.close()

session.quit()



