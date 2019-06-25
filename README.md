<h1>Counterfactual Learning from Logs for Improved Ranking of E-Commerce Products</h1>

This repository hosts the experimental code used in CIKM 2019 paper "Counterfactual Learning from Logs for Improved Ranking of E-Commerce Products". [CURRENTLY UNDER REVIEW]

<h3>Reproducing the results</h3>
<ul>
  <li>CRM_Training
    <ul>
      <li>crm_training_clicks.ipynb: Run this jupyter notebook for training CRM model from click logs [Reproducing results of Table 3, 4, 5 of paper].</li>
      <li>crm_training_orders.ipynb: Run this jupyter notebook for training CRM model from order logs [Reproducing results of Table 6 of paper].</li>
      <li>crm_model.py: Keras implementation of CNN for short text pairs with counterfactual risk minimization (CRM) loss function.</li>
    </ul></li>
  <li>Cross_Entropy_Training
    <ul> 
      <li> cross_entropy_training_clicks.ipnyb: Run this jupyter notebook for training CNN model with cross entropy loss [Reproducing results of Table 3, 4, 5 of paper].</li>
      <li>cross_entropy_training_orders.ipynb: Run this jupyter notebook for training CNN model with cross entropy loss [Reproducing results of Table 6 of paper].</li>
      <li>model_cross_entropy.py: Keras implementation of CNN for short text pairs with cross-entropy loss.</li>
    </ul></li>
</ul>  
<ul>
    <li>LambdaMART Training
    <ul>  
      <li>Download the binary file of RankLib tool from <a href="https://sourceforge.net/projects/lemur/files/lemur/RankLib-2.1/">here</a>. </li>
      <li> We used latest binary 'RankLib-2.1-patched.jar' for our experiments. </li>
      <li> Train LambdaMART model, for Graded Order Labels [Table 6], by running this command: 
      <br />
    <pre>
  java -jar RankLib-2.1-patched.jar -train ~/LambdaMART_files/New_Graded_Order_TrainFile.csv 
  -test ~/LambdaMART_files/New_Graded_Order_TestFile.csv -validate ~/LambdaMART_files/
  New_Graded_Order_DevFile.csv -ranker 6 -metric2t NDCG@10 -metric2T NDCG@10 
  -save ~/Model_LMART_Graded_Orders.txt 
    </pre>
  </li>
  <li> In order to evaluate the saved model on other metrics {NDCG@5,P@5,P@10,RR,MAP}, run this command:
      <br />
    <pre>
    java -jar RankLib-2.1-patched.jar-load ~/Model_LMART_Graded_Orders.txt -test
    ~/LambdaMART_files/New_Graded_Order_DevFile.csv -metric2T NDCG@5
     </pre>
  </li>
    
    
</ul>

</i>
<h3>Mercateo Dataset: E-commerce dataset for LTR</h3>
The dataset and its description can be found <a href="Mercateo Dataset Description.md">here</a>.

<h3>Neural network architecture</h3>
We selected a simple yet powerful CNN model proposed by Severyn et.al [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.723.6492&rep=rep1&type=pdf] for empirical evaluation of our CRM approach. The figure below depicts the architecture of the neural network. This figure is taken from the paper of Severyn et.al. The implementation in Keras was adapted from https://github.com/gvishal/rank_text_cnn. 

![Deep learning architecture for reranking short text pairs](https://pangolulu.github.io/assets/img/dl-ir/sigir_2015.png)

<h3>Evaluation</h3>
For evaluation we use the standard tool used by TREC community for evaluating ad-hoc retrieval tasks <i>trec_eval</i>. The latest version of this tool can be found <a href="https://github.com/usnistgov/trec_eval">here</a>. 
<li>evaluation_metrics.py: contains function get_trec_eval_metrics(). This function returns evaluation results using the evaluation tool <i>trec_eval.</li></i>

<h3>Depdendencies</h3>

<ul>
<li>python 2.7 or higher</li>
<li>numpy</li>
<li>keras</li>
<li>trec_eval</li>
</ul>

For more information about the dataset and model please refer to the paper.
For any questions, you can report issue here.<br /><br />
