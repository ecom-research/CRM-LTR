# Learning to Rank E-Commerce Products from Logged Data

This repository hosts the experimental code used in SIGIR 2019 paper "Learning to Rank E-Commerce Products from Logged Data".
The links for accessing the commercial dataset will be uploaded here soon.

crm_training.ipynb: Jupyter notebook with code for training CRM model.
model.py: Keras implementation of CNN for short text pairs as well as counterfactual risk loss function.
evaluation_metrics.py: contains function get_trec_eval_metrics(). This function creates submission file for trec_eval (https://trec.nist.gov/trec_eval/), stores it in trec_eval folder and runs evaluation. 
utils.py: contains function batch_gen() used to generate batches at training time

For any questions, you can report issue here.
