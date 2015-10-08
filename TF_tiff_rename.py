# TF_tiff_rename.py

'''
This general script renames freshly downloaded T.F. TIFF files. This 
script was written to aid a National Park Service project I'm currently
working on (from 21 Sept 2015 to present).
'''

# grab the operating system library
import os


# create function that renames freshly downloaded TF tiffs
def rename():
    folder = "c:/XXX/XXX/XXX"
    files = os.listdir(folder)

    n = 22 # <------- !! check that this is the next number in the sequence !!
    
    for filename in files:
        if "PUHEfire" not in filename:
            new_name1 = "PUHEfire - TF-00" + str(n) + ".tif"
            new_name2 = "PUHEfire - TF-0" + str(n) + ".tif"
            new_name3 = "PUHEfire - TF-" + str(n) + ".tif"

            if n < 10:
                print "new file name = %s" % new_name1
                os.rename(os.path.join(folder,filename),os.path.join(folder,new_name1))                
            elif n >= 10 and n <100:
                print "new file name = %s" % new_name2
                os.rename(os.path.join(folder,filename),os.path.join(folder,new_name2))
            else:
                print "new file name = %s" % new_name3
                os.rename(os.path.join(folder,filename),os.path.join(folder,new_name3))
            n += 1
            

# run functions
rename()

print "*** --- Script Complete --- ***\n"
