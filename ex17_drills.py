from sys import argv
from os.path import exists

script, source_file, dest_file = argv

if exists(source_file) == True:
    if exists(dest_file) == True:
        print "The destination file already exist. Press Ctrl-C (^C) to abort the operation or RETURN to overwrite"
        raw_input()
    print "The file is %d bytes long" % len(open(source_file).read())
    open(dest_file, 'w').write(open(source_file).read())
    print "File copied"
else:
    print "The source file doesn't exist. Please specify a valid source file"
# open(source_file).close()
# open(dest_file).close()

# from sys import argv;script, source_file, dest_file = argv; open(dest_file, 'w').write(open(source_file).read());open(dest_file).close();open(source_file).close()
