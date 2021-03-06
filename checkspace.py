#!/usr/bin/env python
import ctypes
import os
import platform
import sys

def get_free_space_bytes(folder):
    """ Return folder/drive free space (in bytes)
    """
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value
    else:
        st = os.statvfs(folder)
#        return st.f_bavail * st.f_frsize/1024/1024 # division if we wanted results in MB
        return st.f_bavail * st.f_frsize



def process(input_voter_file, input_poll_file):
    BOLD = '\033[1m'
    END = '\033[0m'

    input_files_size = int((os.path.getsize(input_poll_file) + os.path.getsize(input_voter_file)))
    estimated_parsed_output_files_size = int(input_files_size * 1.19)
    estimated_output_files_size = int(input_files_size * 2.4)
    free_space = get_free_space_bytes('/')

    # BOLD/END strategy doesn't work on Windows
    if platform.system() == 'Windows':
        bold_input_files_size = str(input_files_size)
        bold_estimated_output_files_size = str(estimated_output_files_size)
        bold_estimated_parsed_output_files_size = str(estimated_parsed_output_files_size)
        bold_freespace = free_space
    else:
        bold_input_files_size = BOLD + str(int(input_files_size)) + END
        bold_estimated_parsed_output_files_size = BOLD + str(estimated_parsed_output_files_size) + END
        bold_estimated_output_files_size = BOLD + str(estimated_output_files_size) + END
        bold_freespace = BOLD + str(free_space) + END


    print "------------------------"
    print "SUMMARY"
    print "voter_poll_join.py will require approximately {} bytes of additional storage".format(bold_estimated_output_files_size)
    print "Space left on local drive: {} bytes".format(bold_freespace)
    print "------------------------"
    print "DETAIL"
    print "Combined input filesize: {} bytes".format(bold_input_files_size)
    print "Approximate added space required for 2 parsed output files"
    print "      (i.e. if result file is placed on an external drive): {} bytes".format(bold_estimated_parsed_output_files_size)
    print "Approximate added space required for 3 output files:"
    print "          (parsed output files + final result file): {} bytes".format(bold_estimated_output_files_size)
    print "Space left on local drive: {} bytes".format(bold_freespace)
    print "------------------------"

def main():
    if len(sys.argv) == 3:
        input_voter_file = sys.argv[1]
        input_poll_file = sys.argv[2]
        process(input_voter_file, input_poll_file)
    elif len(sys.argv) == 1: # default to sample input files
        input_voter_file = 'voter_file.csv'
        input_poll_file = 'precinct_polling_list.csv'
        process(input_voter_file, input_poll_file)
    else:
        print("Please provide 2 filename arguments:")
        print("python checkspace.py INPUT_VOTERFILE.csv INPUT_POLLFILE.csv ")

if __name__ == "__main__":
  main()
