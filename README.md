# Learning to Rank E-Commerce Products from Logged Data

This repository hosts the experimental code used in SIGIR 2019 paper "Learning to Rank E-Commerce Products from Logged Data".

<i>crm_training.ipynb</i>: Jupyter notebook with code for training CRM model.<br />
<i>model.py</i>: Keras implementation of CNN for short text pairs as well as counterfactual risk loss function.<br />
<i>evaluation_metrics.py</i>: contains function get_trec_eval_metrics(). This function creates submission file for trec_eval (https://trec.nist.gov/trec_eval/), stores it in trec_eval folder and runs evaluation.<br />
<i>utils.py</i>: contains function batch_gen() used to generate batches at training time.<br />

Datasets can be accessed via following links:<br />
<i>Click logs:</i> s3://ltr-log-dataset/click_logs.7z<br />
<i>Order logs:</i> s3://ltr-log-dataset/order_logs.7z<br />
<i>Embeddings:</i> s3://ltr-log-dataset/embeddings.7z<br />

Each of the datasets contains files of three types. *Queries_{train|dev|test}.npy* files contain numpy arrays of query word indices used for lookup in embedding matrix. User query contains one or multiple search words. Words are integer values, that represent the position of GloVe vector in word-embedding matrix. Although original queries have various length (see column length of query), we padded each query with value 1738783, which is the position of randomly generated vector in embedding matrix (model requires queries of equal length).<br /> Similarly *products_{train|dev|test}.npy* files are numpy arrays of the title of the product returned by the system as a response to the query. Similar to query it contains integer values representing the position of GloVe vector in word-embedding matrix. Product title was also padded with 1738783 values.<br />

**Note**: Due to privacy reasons we are not allowed to publish the raw text of queries and product titles. As many of the neural information retrieval models use word embeddings for training, we publish our own 100-dimensional embeddings. They were obtained by applying GloVe model  to the corpus formed by the queries and product titles.<br />

*Click_rel_{dev|test}.csv* contain three columns:<br />
qid: Unique identifier of user query. Consecutive integer values starting with 0.<br />
addn_feat: Additional features corresponding to the product returned by the system. Float values separated by comma stored as string.<br />
relevance: click or order binary relevance indicator<br />

*Click_rel_train.csv* does not contain relevance column, but instead contains following additional columns:<br />
control_policy: control policy probability of taking the action<br />
loss: observed loss for action selected by the system<br />
action: action sampled from the control policy<br />

For more information about the dataset please refere to the paper.
For any questions, you can report issue here.<br /><br />
