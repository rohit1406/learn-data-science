from text_mining import plot_domain_rawdata_with_wc_to_file

output_relative_path = 'introduction/images/'
field_domain = 'Data Science' # This is the field domain we are working with
data_science_wiki_url = 'https://en.wikipedia.org/wiki/Data_science'

plot_domain_rawdata_with_wc_to_file(data_science_wiki_url, field_domain, output_relative_path)