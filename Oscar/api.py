import deakin 
import sys 
import os 
import pandas as pd 
import argparse


parser = argparse.ArgumentParser(description='''down load datasets from https://data.melbourne.vic.gov.au/''')
parser.add_argument('-n', type=str, help="Like search query function, typing a keyword")
parser.add_argument('-filter',type=int, help='0:search dataset, 1: inspect popular datasets, 2: download type_I, 3: download type_II')
parser.add_argument('-top',type=int, help='top #datasets')

args = parser.parse_args()

#download_type_I: downloading all datasets based on input
table, client= deakin.top_table() #init object 


if args.filter == 0:
    data_table = deakin.data_inspect(keywords=args.n,client = client)
    print(data_table)
    print('\n\n********Note********')
    print('''We encourage users to check dataset according to the link of each data.
There are many detailed descriptions on the official website of city of melbourne.''')


if args.filter == 1:
    table, client= deakin.top_table(args.top)
    print(table)

if args.filter == 2:
    pref_path = os.getcwd()+'/Datasets'
    result  =client.get(args.n,limit=5000)
    name = client.get_metadata(args.n)['name']+'.csv'
    results_df = pd.DataFrame.from_records(result)
    results_df = results_df.iloc[:,:-1]
    try:
        os.makedirs(pref_path)
    except OSError:
        pass
    else:
        print ("Successfully created the directory %s" % path)

    results_df.to_csv(os.path.join(pref_path,name),index=False)
    print("Successfully save in directory %s" %os.path.join(pref_path,name))
    


    




