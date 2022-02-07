import sys, glob, os

# Get the directory name ie darwin for mac
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
    # getting the homedirectory/ home path for this operating system
else:
    hdir = os.environ['HOME']
# homedirectory variable assigned to operating system environemnt of home enviornement
# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')
print(pattern)
#print(glob.glob(pattern))
files = glob.glob(pattern)
for file in files:
    print(file)
    filesize = os.path.getsize(file)
    print(filesize)

# TODO: Use the glob.glob() function to obtain the list of filenames and joining files * means all files- glob is matching file names based on pattern -matching- finding file names and looking at the operating systems
#get me all the files matching in this users home directory

path1 = '/Users/getintotech/PycharmProjects/Excerise10/ex10_starter.py'
size = os.path.getsize(path1)
print(path1,"Size (In Bytes):",size)

path2 = '/Users/getintotech/PycharmProjects/Excerise11/ex10_starter.py'
#size = os.path.getsize(path2)
print(path2,"Size (In Bytes):",size)

# TODO: use os.path.getsize to find each file's size


# TODO: Add a test to only display files that are not zero length
path = '/ex10_starter.py'
basename = os.path.basename(path)
print(basename)


# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()

