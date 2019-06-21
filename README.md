<h1>Learning to Rank E-Commerce Products from Logged Data</h1>

This repository hosts the experimental code used in SIGIR 2019 paper "Learning to Rank E-Commerce Products from Logged Data".

<h3>Repository structure</h3>
<ul>
  <li>CRM_model
    <ul>
      <li>crm_training.ipynb: Jupyter notebook with code for training CRM model.</li>
      <li>model.py: Keras implementation of CNN for short text pairs as well as counterfactual risk loss function.</li>
    </ul></li>
  <li>baseline_model
    <ul>  
      <li>model_cross_entropy.py: Keras implementation of CNN for short text pairs with cross-entropy loss. This model was used as a baseline.</li>
    </ul></li>
  <li>utils
    <ul>
      <li>utils.py: contains function batch_gen() used to generate batches at training time.</li>
      <li>evaluation_metrics.py: contains function get_trec_eval_metrics(). This function creates submission file for trec_eval (https://trec.nist.gov/trec_eval/), stores it in trec_eval folder and runs evaluation.</li>
    </ul></li>
</ul>

<h3>E-commerce logs datasets for query-document text pairs</h3>
Datasets can be accessed via following links:<br />
<ul>
<li><i>Click logs:</i> https://s3.eu-central-1.amazonaws.com/ltr-log-dataset/click_logs.7z</li>
<li><i>Order logs:</i> https://s3.eu-central-1.amazonaws.com/ltr-log-dataset/order_logs.7z</li>
<li><i>Aggregated train datasets for supervised loss functions:</i> https://s3.eu-central-1.amazonaws.com/ltr-log-dataset/train_supervised.7z</li>
<li><i>Embeddings:</i> https://s3.eu-central-1.amazonaws.com/ltr-log-dataset/embeddings.7z</li>
</ul>  

Each dataset folder contains 3 types of files, with 3 files for each type (9 files in total), e.g. click logs contain following files
<ul>
  <li>click_rel_dev.csv</li>
  <li>click_rel_test.csv</li>
  <li>click_rel_train.csv</li>
  <li>products_dev.npy</li>
  <li>products_test.npy</li>
  <li>products_train.npy</li>
  <li>queries_dev.npy</li>
  <li>queries_test.npy</li>
  <li>queries_test.npy</li>
</ul>

<h4>Dataset description</h4>
<br />
*Queries_{train|dev|test}.npy* files contain numpy arrays of query word indices used for lookup in embedding matrix. User query contains one or multiple search words. Words are integer values, that represent the position of GloVe vector in word-embedding matrix. Although original queries have various length (see column length of query), we padded each query with value 1738783, which is the position of randomly generated vector in embedding matrix (model requires queries of equal length).<br />
*Products_{train|dev|test}.npy* files are numpy arrays of the title of the product returned by the system as a response to the query. Similar to query it contains integer values representing the position of GloVe vector in word-embedding matrix. Product title was also padded with 1738783 values.<br />
 
**Note**: Due to privacy reasons we are not allowed to publish the raw text of queries and product titles. As many of the neural information retrieval models use word embeddings for training, we publish our own 100-dimensional embeddings. They were obtained by applying GloVe model  to the corpus formed by the queries and product titles.<br />

*Click_rel_{dev|test}.csv* contains three columns:<br />
<ul>
<li>qid: Unique identifier of user query. Consecutive integer values starting with 0.</li>
<li>addn_feat: Additional features corresponding to the product returned by the system. Float values separated by comma stored as string.</li>
<li>relevance: click or order binary relevance indicator</li>
</ul>  

*Click_rel_train.csv* does not contain relevance column, but instead contains following additional columns:<br />
<ul>
<li>control_policy: control policy probability of taking the action</li>
<li>loss: observed loss for action selected by the system</li>
<li>action: action sampled from the control policy</li>
</ul>

<h3>Neural network architecture</h3>
The architecture of the neural network for estimating relevance of text pairs, that we use in our experiments was introduced in http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.723.6492&rep=rep1&type=pdf. The figure below depicts this architecture. The implementation in Keras was adapted from https://github.com/gvishal/rank_text_cnn. 

![Deep learning architecture for reranking short text pairs](https://pangolulu.github.io/assets/img/dl-ir/sigir_2015.png)

<h3>Depdendencies</h3>

<ul>
<li>python 2.7+</li>
<li>numpy</li>
<li>keras</li>
</ul>

For more information about the dataset and model please refer to the paper.
For any questions, you can report issue here.<br /><br />
