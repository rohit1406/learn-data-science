from text_mining import plot_domain_rawdata_with_wc_to_file

output_relative_path = 'introduction/images/'
field_domain = 'Machine Learning' # This is the field domain we are working with
data_science_wiki_url = 'https://en.wikipedia.org/wiki/Machine_learning'

plot_domain_rawdata_with_wc_to_file(data_science_wiki_url, field_domain, output_relative_path)