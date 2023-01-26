import numpy as np
import pandas as pd
from tqdm import tqdm

HEADER_ROW_IDX = 0
TABLE_IDX = 4
PAGE_URL_TEMPLATE = "https://uscgboating.org/content/recalls.php?pageNum_allRecalls={page_idx:n}&totalRows_allRecalls=1639"
RECALL_URL_TEMPLATE = "https://uscgboating.org/content/recalls-details.php?id={recall_num:s}"
N_PAGES = 66
CSV_FILE_NAME = r'./uscg_boat_recalls.csv' # write locally
EXT_FILE_NAME = r'./uscg_boat_recalls_ext.csv'

def scrape_table_page( page_url, header_row_idx=HEADER_ROW_IDX, table_idx=TABLE_IDX ):
    return pd.read_html(page_url,header=header_row_idx)[table_idx]

def gather_recall_table( page_url_template=PAGE_URL_TEMPLATE, n_pages=N_PAGES ):
    print('downloading USCG recall data...')
    boat_recall_df = pd.DataFrame()
    for page_idx in tqdm(range(n_pages)):
        page_url = page_url_template.format(page_idx=page_idx)
        page_table = scrape_table_page(page_url=page_url)
        boat_recall_df = pd.concat([boat_recall_df,page_table],axis=0,ignore_index=True)
    return boat_recall_df

def extend_recall_table( recall_df, recall_url_template=RECALL_URL_TEMPLATE ):
    print('downloading extended data...')
    ext_boat_recall_df = pd.DataFrame()
    for recall_num in tqdm(recall_df['Number'].values):
        recall_url = recall_url_template.format(recall_num=recall_num)
        recall_url_df = pd.read_html(recall_url)[0]
        recall_data_array = np.concatenate([recall_url_df.values[1:,0:2],recall_url_df.values[1:,3:5]],axis=0)
        recall_data_array = recall_data_array[~pd.isnull(recall_data_array[:,0]),]
        recall_data_dict = {v[0].replace(':',''): v[1] for v in recall_data_array}
        recall_df_row = pd.DataFrame(recall_data_dict,index=[0])
        ext_boat_recall_df = pd.concat([ext_boat_recall_df,recall_df_row],axis=0)
    return ext_boat_recall_df

def write_table_to_csv( df, file_name=CSV_FILE_NAME ):
    print('writing table to csv file...')
    df.to_csv(file_name,index=False)

def main():
    recall_df = gather_recall_table()
    ext_recall_df = extend_recall_table(recall_df)
    write_table_to_csv(recall_df)
    write_table_to_csv(ext_recall_df,file_name=EXT_FILE_NAME)
    print('DONE.')

if __name__ == "__main__":
    main()