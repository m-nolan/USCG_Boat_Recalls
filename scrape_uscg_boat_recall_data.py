import pandas as pd
from tqdm import tqdm

HEADER_ROW_IDX = 0
TABLE_IDX = 4
PAGE_URL_TEMPLATE = "https://uscgboating.org/content/recalls.php?pageNum_allRecalls={page_idx:n}&totalRows_allRecalls=1639"
N_PAGES = 66
CSV_FILE_NAME = r'./uscg_boat_recalls.csv' # write locally

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

def write_table_to_csv( df, file_name=CSV_FILE_NAME ):
    print('writing table to csv file...')
    df.to_csv(file_name,index=False)

def main():
    recall_df = gather_recall_table()
    write_table_to_csv(recall_df)
    print('DONE.')

if __name__ == "__main__":
    main()