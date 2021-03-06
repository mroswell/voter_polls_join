voter_poll_join
=================

Join a voter record with the appropriate precinct poll location.

### Documentation

1. Clone this voter_poll_join repo.
   ```
   $ git clone git@github.com:mroswell/voter_poll_join.git
   ```

2. Ensure that your comma-separated voter and poll files match the format of the sample CSV files ([voter_file.csv](https://github.com/mroswell/voter_poll_join/raw/master/voter_file.csv "voter_file.csv")  and [precinct_polling_list.csv](https://github.com/mroswell/voter_poll_join/raw/master/precinct_polling_list.csv "precinct_polling_list.csv")). Note: nearly any prefix before the "-" in the 'Precinct ID' and 'Precinct' fields could work, as long as there is a 'state' field in the voter file, and a 'State/ZIP' field in the poll file. The number of digits in the zip code (in either file) does not matter.

3. Ensure that you have Python 2.7.x installed.
    ```
    $ python --version
    ```
    If it is not already installed, find the download here:
    https://www.python.org/download/

4. Optionally: run this command in your repo directory to ensure that you have local disk space available for the output files. (Substitute the names of your two input files)
   ```
   $ python checkspace.py INPUT_VOTERFILE.csv INPUT_POLLFILE.csv
   ```
   If you run:
   ```
   $ python checkspace.py
   ```
   without any filename arguments, it's equivalent to:
   ```
   $ python checkspace.py voter_file.csv precinct_polling_list.csv
   ```

5. Install csvkit
    ```
    $ pip install csvkit
    ```
If pip is not already installed, follow the installation documentation here:
https://pip.pypa.io/en/latest/installing.html

    If you are a Windows user, [see these important instructions](https://github.com/mroswell/voter_poll_join/blob/master/windows_users.md "Windows User Instructions").

6. Run the voter_poll_join.py program with three filename arguments, as follows:

    ```
    $ python voter_poll_join.py INPUT_VOTERFILE.csv INPUT_POLLFILE.csv OUTPUT_FILE.csv
    ```
    Note that the two INPUT CSV files must already exist (per step 2 above). If you run:

    ```
    $ python voter_poll_join.py
    ```
    without any arguments, it will join the sample files. This is equivalent to the following:
    ```
   $ python voter_poll_join.py voter_file.csv precinct_polling_list.csv voter_poll_joined.csv
    ```

The result will be three new files, located by default in the same directory as your cloned repo:
 - parsed_voter_file.csv
 - parsed_precinct_polling_list.csv
 - __voter_poll_joined.csv__ (or the path/filename you specified as your OUTPUT_FILE.csv); This file is your final result (unless you're on Windows).

If you're on Windows, continue with [these steps](https://github.com/mroswell/voter_poll_join/blob/master/windows_users.md "Windows User Instructions").


### Note
To facilitate placement on GitHub, the [voter_file.csv](https://github.com/mroswell/voter_poll_join/raw/master/voter_file.csv "voter_file.csv")  and [precinct_polling_list.csv](https://github.com/mroswell/voter_poll_join/raw/master/precinct_polling_list.csv "precinct_polling_list.csv") line ends were changed to unix style via the dos2unix utility.
http://sourceforge.net/projects/dos2unix/

