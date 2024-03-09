import pandas as pd

df = pd.read_csv("Song.csv")

def main():

    # artist_streams()
      mean_sales()
      median_sales()
      title_count()
      top_artists()
      filt_artist()
    #   make_group() didn't work with the dataset

def artist_streams():
        artist_mask = df["Artist"] == 'The Beatles'
        print(df[artist_mask])
      #   this was used as the test run to see if things worked

def mean_sales():
     print('')
     print('The sale average for this data set is:')
     print(df['Sales'].mean())
#      used 'Sales' and mean() to manipulate the data

def median_sales():
     print('')
     print('The sale median for this data set is:')
     print(df['Sales'].median())

     

def title_count():
      print('')
      print('Some songs are top songs of multiple years.\n Here are the top 25 songs that were repeated:')
      print(df["Title"].value_counts().head(25))
      # The list is very long, so only the top 25 are returned by
      # utilizing the head() method

def top_artists():
      print('')
      print('The most reaccuring artists (top 10):')
      print(df['Artist'].value_counts().head(10))
      # basically the same thing as the top songs in
      # title_count()

def make_group():
      print('')
      artist_group = df.groupby(['Artist'])
      print(artist_group.get_group['Madonna'])
      

def filt_artist():
      print('')
      print('All of the songs from the top artist, Madonna:')
      filt = df['Artist'] == 'Madonna'
      print(df.loc[filt])
      # used loc to located the filter that I had set, which is Madonna
if __name__ == "__main__":
    main()



