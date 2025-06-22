import os # to handle file paths
import requests # to make HTTP requests
from html.parser import HTMLParser # built-in HTML parser
import nlp_rake # for keyword extraction
import matplotlib.pyplot as plt # for visualization
from wordcloud import WordCloud # another way to visualize word frequencies


# Inheriting from HTMLParser: collecting all the text from inside HTML tags except script and style tags
class MyHTMLParser(HTMLParser):
    script = False
    res = ""
    def handle_starttag(self, tag, attrs):
        if tag.lower() in ['script', 'style']:
            self.script = True
    def handle_endtag(self, tag):
        if tag.lower() in ['script', 'style']:
            self.script = False
    def handle_data(self, data):
        if str.strip(data)=="" or self.script:
            return
        self.res += ' '+data.replace('[ edit ]','')

# Plotting the simple distribution of the keywords based on their relevance
def plot(pair_list):
    k, v = zip(*pair_list)
    plt.bar(k, v)
    plt.xticks(range(len(k)), k, rotation='vertical')
    plt.show()

# Plotting with wordcloud: uses the frequencies of the keywords to create a word cloud
def plot_with_frequencies_wc(res):
    wc = WordCloud(width=800, height=600, background_color='white')
    plt.figure(figsize=(15, 7))
    wc.generate_from_frequencies({k:v for k,v in res}).to_file('introduction/images/ds_wc.png')

# Plotting with raw text using wordcloud: generates the frequencies of the words and uses them to plot
def plot_with_rawtext_wc(text, field_domain, relative_path):
    wc = WordCloud(width=800, height=600, background_color='white')
    plt.figure(figsize=(15, 7))
    relattive_file_path = os.path.join(relative_path, field_domain+ '_with_rawtext_wc.png')
    wc.generate(text).to_file(relattive_file_path)
    print(f'File saved to {os.getcwd()}/{relattive_file_path}')

def plot_domain_rawdata_with_wc_to_file(url, field_domain, output_relative_path):

    # Step1: Getting the data
    text = requests.get(url).content.decode('utf-8')

    # Step2: Transforming the data - converting the data that will be suitable for processing
    parser = MyHTMLParser()
    parser.feed(text)
    text = parser.res

    # Step3: Processing the data for getting Insights
    # Extracting the keywords from the text and see which keywords are more meaningful
    extractor = nlp_rake.Rake(max_words=2, min_freq=3, min_chars=5)
    res = extractor.apply(text)

    # Step4: Visualizing the results
    #plot(res) # This will generate a simple bar chart of the keywords and their relevance
    #plot_with_frequencies_wc(res) # This will generate a word cloud based on the frequencies of the keywords and save it to a file
    plot_with_rawtext_wc(text, field_domain, output_relative_path) # This will generate a word cloud based on the raw text and save it to a file