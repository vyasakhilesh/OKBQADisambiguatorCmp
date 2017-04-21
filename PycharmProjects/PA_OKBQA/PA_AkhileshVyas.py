#!/usr/bin/env python
import sys
import argparse
import json
import subprocess
import os


def curl_command_func(input_Data, webService_Url):
    tmp_data = "'data=" + input_Data + "'"
    curl_Command = str("curl -G --data-urlencode" + " " + tmp_data + " " + webService_Url)
    try:
        tmp_str = subprocess.check_output(str(curl_Command), shell = True)
        print tmp_str
    except:
        print ('Error :Command error')


def urlvalidator():
    return None

def inputdatafileparsing(input_File_Path):
    if os.path.exists(input_File_Path):
        with open(input_File_Path, 'r') as input_file:
            try:
                tmp_input_Data = json.JSONEncoder().encode(json.load(input_file))
                input_file.close()
                return tmp_input_Data
            except IOError:
                print "Error :Input file read or open error "
                sys.exit()
            except:
                print "Error :Input file json error "
                sys.exit()
    else:
        print "Error :File path does not exist"
        sys.exit()

def main():
    webService_Url = None
    input_Data = None

    parser = argparse.ArgumentParser(description='-----------Pass Input Data and WebServiceUrl.----------')

    parser.add_argument('-d', '--dataInput', dest='Input_Data', type=str, help='Sample input for command', required=False, default = None)
    parser.add_argument('-f', '--dataFile', dest='Input_Data_File', type=str, help='Sample input from file for command', required=False, default = None)
    parser.add_argument('-w', '--wsUrl', dest='WebService_Url', type=str, help='Web Service Url', required=True, default = None)
    args = parser.parse_args()




    if(None != args.WebService_Url):
        webService_Url = args.WebService_Url
    else:
        print ""

    if(None != args.Input_Data):
        input_Data = args.Input_Data
    elif(None != args.Input_Data_File):
        input_Data = inputdatafileparsing(args.Input_Data_File)
    else:
        print "Error :Input Data is Missing: Please provide data either by file or through command console"
        sys. exit()

    #print input_Data, webService_Url
    curl_command_func(input_Data, webService_Url)


if __name__ == "__main__":
    main()

