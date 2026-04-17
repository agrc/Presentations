# pandas: Getting Cuddly With Your Data

Want to take your data munging, analysis, and sharing to the next level? Come get hands-on with the pandas library for python. You'll get experience loading, querying, analyzing, and reshaping data. And who needs desktop GIS when you've got the ArcGIS API for Python and geopandas libraries to perform your GIS analysis in code? This is a great class to learn how to use your python skills to create powerful, repeatable spatial and non-spatial data analyses that can be run anywhere you can run python: locally, on a server, or in the cloud.

## Main Benefits

- Powerful analysis tools
- Repeatable and scriptable processes
- Powerful GIS integrations
- Quick in-memory operations


## Exercise Ideas

- Dataset: parks_local
- groupby: total acreage per city/county
- Join: which city/county has the highest percentage of park area?

## Pre-class Prep

- Laptop with conda and VS Code installed
  - ArcGIS Pro
  - Miniconda
  

## Outline from Gemini

This 4-hour workshop is designed to transition GIS professionals from traditional row-based iteration (cursors) to the high-performance, vectorized world of **pandas*- and **GeoPandas**.

---

## Workshop Overview: Pandas for GIS Professionals

**Duration:*- 4 Hours
**Prerequisites:*- Basic Python knowledge (variables, lists, functions) and familiarity with tabular data structures.

---

### Hour 1: Foundations & The Vectorized Mindset

The goal of this hour is to break the habit of "looping" through rows and understand how pandas handles data in memory.

- **Installation and Setup**- conda, pip, jupyter notebooks
  - conda install python=3.13 -c defaults
  - pip install geopandas jupyterlab arcgis sqlalchemy psycopg2
- **Loading Data:*- Using `pd.read_csv()` and `pd.read_excel()` with a focus on handling messy GIS exports (skipping headers, defining dtypes).
  - Example: load recreation.parks from opensgid
- **The DataFrame Anatomy:*- Understanding Series vs. DataFrames and how they relate to Attribute Tables.
- **Vectorization vs. Iteration:**
- Why we avoid `for row in dataframe`.
- **Unary & Binary Operations:*- Applying math and logic across entire columns instantly.
- *Exercise:- Convert a column of "Feet" to "Meters" using a single operation instead of a loop.


- **Indexing & Selection:*- Using `.loc` and `.iloc` to slice data (the "Select by Attribute" of pandas).

---

### Hour 2: Data Cleaning & Grouped Analysis

GIS data is notoriously "dirty." This session focuses on preparing data for analysis and performing aggregate statistics.

- **Data Quality Control:**
- Handling Nulls: `dropna()` vs. `fillna()`.
- String manipulation: Using `.str` accessors to clean up inconsistent naming (e.g., "Main St" vs "Main Street").


- **The "Split-Apply-Combine" Pattern:**
- Using `.groupby()` to summarize data (e.g., total area by land-use zone).
- Common aggregations: `sum()`, `mean()`, `count()`, and `nunique()`.


- **Reshaping Data:**
- **Pivoting:*- Moving from "long" to "wide" formats for reporting.
- **Melting:*- Preparing wide spreadsheets for time-series analysis.



---

### Hour 3: Merging & Geometric Integration

This hour bridges the gap between standalone spreadsheets and spatial datasets.

- **Combining Datasets:**
- **Appends:*- Using `pd.concat()` to stack similar tables (e.g., monthly inspection logs).
- **Joins:*- Using `pd.merge()` to perform inner, left, and outer joins (The "Add Join" equivalent).


- **Introduction to GeoPandas:**
- The `GeoDataFrame` and the `geometry` column.
- Reading Shapefiles and GeoJSONs with `gpd.read_file()`.


- **Spatial Operations:**
- Coordinate Reference System (CRS) management: `.to_crs()`.
- Basic spatial joins: Finding which points fall within which polygons using `gpd.sjoin()`.



---

### Hour 4: The ArcGIS API for Python & Advanced Analysis

In the final hour, we bring pandas into the Esri ecosystem for professional workflows.

- **The Spatially Enabled DataFrame (SeDF):**
- How the ArcGIS API for Python extends pandas.
- Reading Feature Layers directly from ArcGIS Online/Enterprise using `from_layer`.


- **Visualizing Data:**
- Creating quick "Heat Maps" or "Classified" maps directly in a Jupyter Notebook using `df.spatial.plot()`.


- **Exporting Results:**
- Writing back to Feature Classes, Excel, or CSV.


- **Capstone Challenge:**
- A 30-minute mini-project: Load a CSV of "Crime Incidents," clean the dates, group by "Crime Type," join it to a "Neighborhood" shapefile, and map the results.



---

### Key Takeaways for Students

- **Performance:*- Pandas is  to  faster than `arcpy.da.SearchCursor` for table manipulation.
- **Portability:*- These skills translate to data science, machine learning, and web development.
- **Reproducibility:*- Replace manual "Excel cleanup" with a script that runs the same way every time.

**Would you like me to draft a specific "Cheat Sheet" of pandas commands matched to their equivalent ArcGIS Pro tool names?**