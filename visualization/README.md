## Description
Couple of programs related to Data Science & **Data Visualization** topic. A visualization can help you identify all kinds of interesting parts of your data such as spikes, outliers, groupings, tendencies, and more, that can help you understand the story your data is trying to tell. Prior to visualizing your data, you need to ensure that it has been cleaned and prepared. After that, you can start deciding how best to present the data. In this part we will learn how to create interesting visualizations all around the concept of quantity using **line charts, scatterplots, bar plots**, data distribution using **Histograms and Density plots**, proportions using **pie charts, donut charts and waffle charts, Scatter plots, line charts, Facet grids, Dual-line plots**.

## List of Programs
### 1. Visualizing Quantity: with Birds dataset   
[This program](./vis_quantity.py) demonstrates the usage Matplotlib library to **observe** the data of the birds from [birds.csv](../data/birds.csv) file. It plots basic line plots, line plots with labelling on x, y coordinates, scatter chart to find outliners and to filter those outlines from the observation.  
<Img width="200" src="./output/quantity-visualization/lc-birds-wingspan-basic.png">
<Img width="200" src="./output/quantity-visualization/lc-birds-wingspan-with-labels.png">
<Img width="200" src="./output/quantity-visualization/sc-birds-wingspan-with-highlighting-outliners.png">
<Img width="200" src="./output/quantity-visualization/sc-birds-wingspan-with-filtered-outliners.png">  

#### **Exploring the bar chart (showing grouping of data)**:  
It plots the bar chart based on the number of birds based on category.  
<Img width="300" src="./output/quantity-visualization/bc-birds-category.png">
<Img width="300" src="./output/quantity-visualization/bc-birds-category-vertical-sorted.png">  

#### **Comparing Data**:  
Compare Max Length of a bird in each category and superimpose min, max length data per category.  
<Img width="300" src="./output/quantity-visualization/comparing-maxlength-per-category.png">
<Img width="300" src="./output/quantity-visualization/comparing-min-maxlength-per-category.png">  


### 2. Visualizing Distribution: Exploring the birds dataset
[This program](./vis_distribution.py) demonstrates the another way to dig into data by it's distribution i.e. how the data is organized along an axis.  

#### General Distribution of **max length per bird order** is demonstrated in below **scatter plot**.  
<Img width="300" src="./output/distribution/sc-dis-order-maxlen.png">  

#### Following **Histogram** shows the distribution of max body mass.  
Below are the comparison images:  
<Img width="250" src="./output/distribution/hist-dis-maxbodymass.png">
<Img width="250" src="./output/distribution/hist-dis-maxbodymass-b20.png">
<Img width="250" src="./output/distribution/hist-dis-maxbodymass-b30.png">
<Img width="250" src="./output/distribution/hist-dis-maxbodymass-below60-b40.png">
<Img width="250" src="./output/distribution/hist-dis-full-below60-b40.png">

#### Comparison: **MaxBodyMass vs MaxLength**  
<Img width="300" src="./output/distribution/hist-maxbodymass-vs-maxlength.png">

#### **Distribution according to textual data**:  
Digging into conservation information such as genus, species, family as well as conservation status.  
**Conservation Status vs MinWingspan**:  
<Img width="300" src="./output/distribution/hist-conservationstatus-vs-minwingspan.png">  


### 3. Density plot: with birds dataset
To show smoother density chart, use density plot. [This Program](./vis_distribution_density.py) show how to draw density plots.   

#### Density plot of **MinWingspan and MaxBodyMass** is as below.  
Below are the comparison images:  
<Img width="300" src='./output/distribution/dp-dist-minwingspan.png'>
<Img width="300" src='./output/distribution/dp-dist-maxbodymass.png'>
<Img width="300" src='./output/distribution/dp-dist-maxbodymass-nososmooth.png'>

#### Density plot of **MaxBodyMass per bird Order**:  

<Img width="300" src='./output/distribution/dp-dist-maxbodymass-per-order.png'>

#### **Map several fields** (MaxLength, MinLength of a bird) in a single chart:  

<Img width="300" src='./output/distribution/dp-dist-map-several-fields.png'>


### 4. Visualize Proportions: with Mushrooms dataset
[This program](./vis_proportion.py) demonstrates the analysis and visualization of [mushrooms data](../data/mushrooms.csv). First, you need to group your data into categories and then decide which is the best way to display the data - pie, donut, or waffle.    
#### **Mushrooms population** is shown with below **pie chart**. 
<Img width="300" src="./output/proportion/pro-pie-mushrooms-population.png">   

#### **Mushrooms Habitat** is shown with below **donut chart**.  
<Img width="300" src="./output/proportion/pro-donut-mushrooms-habitat.png">  

#### **Mushrooms cap colors** is displayed with below **Waffle chart**
<Img widht="300" src="./output/proportion/pro-waffle-mushrooms-capcolors.png">  


### 5. Visualizing Relationships: All About Honey
[This program](./vis_relationships.py) shows the relationship between various factors of [data of honey production in US](../data/honey.csv).

#### Relationship between the Price per pound and it's US state of origin
Below are the comparison images:  
<Img width="300" src="./output/relationships/rel-sp-ppl-vs-state.png">
<Img width="300" src="./output/relationships/rel-sp-ppl-vs-state-colored.png">
<Img width="300" src="./output/relationships/rel-sp-ppl-vs-state-sized.png">


#### Relationship between Price per pount and totalProduction over the years
Below are the comparison images:  
<Img width="300" src="./output/relationships/rel-lc-progression-ppp-year.png">
<Img width="300" src="./output/relationships/rel-lc-progression-honeyprod-year.png">


#### Yield Per Colonies and Number of Colonies over the years
<Img src="./output/relationships/comparison-ypc-noc-overyears.png">

#### Dual-line plot
<Img src="./output/relationships/dual-line-plot.png">    


### 6. Dangerous Liaisons data visualization project
[Project Link](./sample-network-app/README.md)  


## 🌟 Developer
Name: Rohit Shamrao Muneshwar  
Email: rohit.muneshwar1406@gmail.com  
LinkedIn Profile: [Click Here](https://www.linkedin.com/in/rohit-muneshwar-a9079258/)  
Other Github repositories: [Click Here](https://github.com/rohit1406?tab=repositories)  

---