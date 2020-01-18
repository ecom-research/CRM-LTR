<h1>Mend Your Learning Approach, Not the Data for Ranking E-Commerce Products</h1>

This repository contains code and the Commercial Dataset needed for reproducing the results presented in the following paper: 
<a href="https://arxiv.org/pdf/1907.10409.pdf">Counterfactual Learning from Logs for Ranking of E-Commerce Products</a>.

Note: Updates to the repository coming soon.


<h3>Commercial Dataset: E-commerce dataset for LTR</h3>
The dataset and its description can be found <a href="Mercateo Dataset Description.md">here</a>.

<h3>Neural network architecture of S-CNN</h3>
We selected a simple yet powerful CNN model proposed by Severyn et.al [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.723.6492&rep=rep1&type=pdf] for empirical evaluation of our CRM approach. We refer to this model as S-CNN in the paper. The figure below depicts the architecture of the neural network. This figure is taken from the paper of Severyn et.al. The implementation in Keras was adapted from https://github.com/gvishal/rank_text_cnn. 

![Deep learning architecture for reranking short text pairs](https://pangolulu.github.io/assets/img/dl-ir/sigir_2015.png)

<h3>Evaluation</h3>
<li>For evaluation we use the standard tool used by TREC community for evaluating ad-hoc retrieval tasks <i>trec_eval</i>. The latest version of this tool can be found <a href="https://github.com/usnistgov/trec_eval">here</a>. </li>
<li>evaluation_metrics.py: contains function get_trec_eval_metrics(). This function returns evaluation results using the evaluation tool <i>trec_eval.</li></i>

<h3>Reproducing the results</h3>
First install Jupyter Notebook using following command: (For details, click <a href="https://jupyter.readthedocs.io/en/latest/install.html">here</a>)
<pre> pip3 install jupyter </pre>

If you are not familiar with running notebook, click <a href="https://jupyter.readthedocs.io/en/latest/running.html">here</a>.

Download the treac_eval tool and Mercateo Dataset.
<ul>
  <li>CRM_Training
    <ul>
      <li>crm_training_clicks.ipynb: Run this jupyter notebook for training CRM model from AtB click logs [Reproducing results of Table 2 of the paper].</li>
      <li>crm_training_orders.ipynb: Run this jupyter notebook for training CRM model from order logs [Reproducing results of Table 3 of paper].</li>
      <li>crm_model.py: Keras implementation of CNN for short text pairs with counterfactual risk minimization (CRM) loss function.</li>
    </ul></li>
  <li>Cross_Entropy_Training
    <ul> 
      <li> cross_entropy_training_clicks.ipnyb: Run this jupyter notebook for training CNN model with cross entropy loss [Reproducing results of Table 2 of paper].</li>
      <li>cross_entropy_training_orders.ipynb: Run this jupyter notebook for training CNN model with cross entropy loss [Reproducing results of Table 3 of paper].</li>
      <li>model_cross_entropy.py: Keras implementation of CNN for short text pairs with cross-entropy loss.</li>
    </ul></li>
</ul>  
<ul>
    <li>LambdaMART Training
    <ul>  
      <li>Download the binary file of RankLib tool from <a href="https://sourceforge.net/projects/lemur/files/lemur/RankLib-2.1/">here</a>. </li>
      <li> We used latest binary 'RankLib-2.1-patched.jar' for our experiments. </li>
      <li> Train LambdaMART model, for Graded Order Labels [Table 3], by running this command: 
      <br />
    <pre> java -jar RankLib-2.1-patched.jar -train LambdaMART_files/New_Graded_Order_TrainFile.csv 
  -test LambdaMART_files/New_Graded_Order_TestFile.csv -validate LambdaMART_files/
  New_Graded_Order_DevFile.csv -ranker 6 -metric2t NDCG@10 -metric2T NDCG@10 
  -save Model_LMART_Graded_Orders.txt </pre>
  </li>
  <li> In order to evaluate the saved model on other metrics {NDCG@5,P@5,P@10,RR,MAP}, run this command:
      <br />
    <pre> java -jar RankLib-2.1-patched.jar -load Model_LMART_Graded_Orders.txt -test
    LambdaMART_files/New_Graded_Order_DevFile.csv -metric2T NDCG@5 </pre>
  </li>
      </ul> 
    <ul>
      <li>Affect of DNN architecture
    <ul>  
      <li> For reproducing the results in Table 4 of the paper, refer to 
         <a href="https://github.com/NTMC-Community/MatchZoo/tree/master">MatchZoo</a>. </li>
      <li> MatchZoo has comprehensive documentation on the dependencies and how to run the models.</li>
      <li> For a fair comparison with S-CNN model, we modified the models in MatchZoo and added a fully connected layer before the last layer. This layer is added so that we can utilize the dense features.   </li>
  </li>
    
</ul>    
</ul>

<h3>Dependencies</h3>

<ul>
<li>python 2.7 or higher</li>
<li>numpy</li>
<li>keras</li>
<li>trec_eval</li>
</ul>

For more information about the dataset and model please refer to the paper.
For any questions/bugs, you can report issue here.
 <br /><br />
