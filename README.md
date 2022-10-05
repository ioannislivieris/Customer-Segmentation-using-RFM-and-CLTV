# Customer Segmentation using RFM and CLTV
<br />
<br />

## Table of Contents
---

- [Data](#data)
- [Customer Segmentation based on Recency, Frequency & Monetary Value (RFM) metrics](#customer-segmentation-based-on-recency-frequency--monetary-value-rfm-metrics)
    - [Scope of RFM analysis](#scope-of-rfm-analysis)
- [Customer Life Time Value](#customer-life-time-value)
    - [Business problems addressed by CLTV](#business-problems-addressed-by-cltv)
    - [CLTV Statistics](#cltv-statistics)
- [Requirements](#requirements)
- [Contact](#contact)


<br />
<br />

## Data
---

This Online Retail II data set contains all the transactions occurring for a UK-based and registered, non-store online retail between 01/12/2009 and 09/12/2011. The company mainly sells unique all-occasion gift-ware. Many customers of the company are wholesalers.

- **Invoice:** Invoice number. Nominal. A 6-digit integral number uniquely assigned to each transaction. If this code starts with the letter ‘c’, it indicates a cancellation.

- **StockCode:** Product (item) code. Nominal. A 5-digit integral number uniquely assigned to each distinct product.

- **Description:** Product (item) name.

- **Quantity:** The quantities of each product (item) per transaction.

- **InvoiceDate:** Invice date and time. Numeric. The day and time when a transaction was generated.

- **UnitPrice:** Unit price. Numeric. Product price per unit in sterling.

- **CustomerID:** Customer number. Nominal. A 5-digit integral number uniquely assigned to each customer.

- **Country:** Country name. Nominal. The name of the country where a customer resides.


Link: ``https://archive.ics.uci.edu/ml/datasets/Online+Retail+II``

<br />
<br />

## Customer Segmentation based on Recency, Frequency & Monetary Value (RFM) metrics
---

Nowadays, never techniques have come up in the market for segmenting customers and also Customer segmentation very important to make a decision, what action needed to increase revenue, build a good relationship with the customer and optimize sales, for a business. 

The main focus of this blog would be to show how we can segment customers into different clusters using the K-means algorithm. But, first I would be doing RFM analysis to get the desired values and those features will be used as an input in K-means, to determine similarity. K-Means uses Euclidean distance as a distance metric to calculate the distance between the data points.


### Scope of RFM analysis

RFM analysis allows you to segment customers by the frequency and value of purchases and identify those customers who spend the most money.

* Recency — how long it’s been since a customer bought something from us
* Frequency — how often a customer buys from us
* Monetary value — the total value of purchases a customer has made

<br />
<br />


## Customer Life Time Value
---

In marketing, customer lifetime value (CLV or often CLTV), lifetime customer value (LCV), or life-time value (LTV) is a prognostication of the net profit contributed to the whole future relationship with a customer. The prediction model can have varying levels of sophistication and accuracy, ranging from a crude heuristic to the use of complex predictive analytics techniques.


### Business problems addressed by CLTV

- How to Identify the most profitable customers?
- How can a company offer the best and make the most ?
- How to segment profitable customers?
- How much budget need to spend to acquire customers?


### CLTV Statistics

- A 5% increase on the Retention Rate results in a 25% increase in profits.
- Acquiring a new customer is 5 to 25 times more expensive than retaining an existing one. 
- The probability of retaining an existing customer is between 60% — 70%. 
- Existing customers spend on average 67% more than new customers. 
- 75% of companies consider CLTV an important concept for their organization. 

<br />
<br />

## Requirements
---

- python>=3.7
- matplotlib==3.5.1
- numpy==1.21.5
- scipy==1.7.3
- pandas==1.3.5
- scikit-learn==1.0.2
- seaborn==0.11.0
- lifetimes==0.11.3


<br />
<br />

## Contact
---

Ioannis E. Livieris (livieris@gmail.com)