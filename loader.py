
import os
import pandas

_HOME = os.path.abspath( __file__ ) 
_HOME = os.path.dirname( _HOME )
_DATA = os.path.join( _HOME, 'data' )

def load_s2():
    '''
    outputs pandas dataframe of loaded file
        data/science.add9330_data_s2.csv
    '''
    path = os.path.join(_DATA, 'science.add9330_data_s2.csv')
    df = pandas.read_csv(path)
    return df

def load_s3():
    '''
    outputs pandas dataframe of loaded file
        data/science.add9330_data_s3.csv
    '''
    path = os.path.join(_DATA, 'science.add9330_data_s3.csv')
    df = pandas.read_csv(path)
    return df

def load_s4():
    '''
    outputs pandas dataframe of loaded file
        data/science.add9330_data_s4.csv
    '''
    path = os.path.join(_DATA, 'science.add9330_data_s4.csv')
    df = pandas.read_csv(path)
    return df

def load_s1_adj_all_all():
    '''
    outputs pandas dataframe of loaded file
        data/Supplementary-Data-S1/all-all_connectivity_matrix.csv
    '''
    path = os.path.join(_DATA, 'Supplementary-Data-S1')
    path = os.path.join(path, 'all-all_connectivity_matrix.csv')
    
    df = pandas.read_csv(path, index_col=0)
    df.index = df.index.astype(str)
    return df
#

def load_s1_adj_all_all_nx():
    '''
    outputs networkx Graph of loaded file 
        data/Supplementary-Data-S1/all-all_connectivity_matrix.csv
    
    loaded via the function load_s1_adj_all_all().
    
    TODO: does not work. Seems the index 
    and column labels don't match...?
    '''
    import networkx
    df = load_s1_adj_all_all()
    graph = networkx.from_pandas_adjacency(df)
    return graph

if __name__=="__main__":
    '''
    Run to verify files can be loaded (errors will 
    be thrown otherwise)
    '''
    for f in [load_s2, load_s3, load_s4, load_s1_adj_all_all]:
        df_temp = f()
        print(f.__name__, 'can successfully load.')
