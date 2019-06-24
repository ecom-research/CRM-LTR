<h1>Mercateo Dataset: E-commerce dataset for LTR</h1>

Mecateo Dataset contains queries from real users, actions taken by the policy running on the system, probability of these actions and feedback of users on those actions. Most queries included in this dataset are those which were really challenging for our current ranking algorithm. It can be accessed via following links:<br />
<ul>

<li><i>Embeddings:</i> https://s3.eu-central-1.amazonaws.com/ltr-log-dataset/embeddings.7z</li>

Our clients (sellers) have proprietary rights on the product title and description available on our platform. So, raw text can not be published in Mercateo dataset. Therefore, we train GloVe model on the corpus comprising of queries and product titles to learn word embeddings. We publish these 100- dimensional word embeddings. We think they will be useful for further research since most neural information retrieval models can be trained from word embeddings.
This zip file contains <i>embeddings.npy</i>, which is the embedding matrix, with each row represnting 100-dimensional word vector.


<li><i>Embeddings_Index_files:</i> https://ltr-log-dataset.s3.eu-central-1.amazonaws.com/Embeddings_Index_files.7z</li>
This zip file has 10 files containing indices which maps words ( of queries and product title) to their emeddings in the embedding matrix. Each row in these files is aligned with respective entry in tran, dev, test and log files.
<br />

<ul>
  <li>Queries_{train|dev|test}.npy</i> files contain numpy arrays of query word indices used for lookup in embedding matrix. Most LTR neural networks require the length of query and document be fixed for all samples. Since number of words in queries and products varies a lot, we set query length to 40 and length of product title to 48. We do padding with randomly generated vector for texts with lower length and cut-off texts of higher length. <br /><br /></li>
  <li>Products_{train|dev|test}.npy</i> files are numpy arrays of the title of the product returned by the system as a response to the query. Similar to query it contains integer values representing the position of GloVe vector in word-embedding matrix. Product title was also padded with 1738783 values.<br /><br /></li>
  
  <li>{click|order}_logs_queries.npy</i> files are numpy arrays of embedding indices of the queries in {click|order} logs. <br /><br /></li>

<li>{click|order}_logs_products.npy</i> files are numpy arrays of embedding indices of the title of the product in {click|order} logs. <br /><br /></li>
</ul></li>


<li><i>Supervised_ClicksNRR_files:</i> https://ltr-log-dataset.s3.eu-central-1.amazonaws.com/Supervised_ClickNRR_files.7z</li>

This zip file contains train, dev, test sets with Normalized Relevance Rates (NRR) for clicks on products, i.e. supervisory labels by aggregating log data (see paper for details).
Each file has three columns:
<ul>
<li>qid: Unique identifier of user query.</li>
<li>addn_feat: Additional features corresponding to the product returned by the system. Float values separated by comma stored as string.</li>
<li>click_NRR: Click Normalized Relevance Rates (NRR)</li>
</ul>  
<br />

<li><i>Supervised_OrdersNRR_files:</i>https://ltr-log-dataset.s3.eu-central-1.amazonaws.com/Supervised_OrderNRR_files.7z</li>

This zip file contains train, dev, test sets for with Normalized Relevance Rates (NRR) for orders of products, i.e. supervisory labels by aggregating log data (see paper for details).
Each file has three columns:
<ul>
<li>qid: Unique identifier of user query.</li>
<li>addn_feat: Additional features corresponding to the product returned by the system. Float values separated by comma stored as string.</li>
<li>order_NRR: Order Normalized Relevance Rates (NRR)</li>
</ul>  

<br />
<li><i>LambdaMART_files:</i>https://ltr-log-dataset.s3.eu-central-1.amazonaws.com/LambdaMART_files.7z</li>
It contains files in SVMLight format, as required by RankLib Tool ( https://sourceforge.net/p/lemur/wiki/RankLib/). These files are provided for ease of reproducing the results. 
<br />
<br />
<li><i>logs:</i>https://ltr-log-dataset.s3.eu-central-1.amazonaws.com/logs.7z</li>
It contains two files, click_logs and order_logs. It has following columns:<br />
<ul>
<li>control_policy: control policy probability of taking the action</li>
<li>loss: observed loss for action selected by the system</li>
<li>action: action sampled from the control policy</li>
<li>qid: Unique identifier of user query.</li>
<li>addn_feat: Additional features corresponding to the product returned by the system. Float values separated by comma stored as string.</li>
</ul>
</ul> 
