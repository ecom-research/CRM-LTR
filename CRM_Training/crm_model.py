#Model implementation borrowed from https://github.com/gvishal/rank_text_cnn

import keras
from keras import backend as K
from keras import optimizers, regularizers
from keras.layers import Dense, Dropout
from keras.layers import Input, Embedding
from keras.layers import Conv1D, GlobalMaxPooling1D, MaxPooling1D
from keras.layers.merge import Concatenate, Dot
from keras.layers import Multiply 
from keras.models import Sequential, Model

def counterfactual_risk_loss(weights):
    """
    Parameters
    ----------
    weights: np.array
    """
    
    def compute_loss(y_true, y_pred):
        """
        Parameters
        ---------
        y_true: np.array
            Actions taken by the system
        y_pred: np.array
            Softmax probability vector coming from the model
        """
   
        y_pred_prob = y_true*y_pred + (1-y_true)*(1-y_pred)
        loss = K.mean(weights * y_pred_prob)
        return loss

    return compute_loss

def crm_model(max_ques_len, max_ans_len, embedding, addit_feat_len, no_conv_filters=100, dropout_rate = 0.5):
    
    print('Model parameters are: ')
    print('Question length: {}, Answer length {}:, Embedding shape: {}, Additional features length: {}, Num conv filters: {}'.format(max_ques_len, max_ans_len, embedding.shape, addit_feat_len, no_conv_filters))
  
    #Question layers
    input_q = Input(shape=(max_ques_len,), name='ques_input')
    
    #Load embedding values from corpus here.
    embed_q = Embedding(input_dim=embedding.shape[0], output_dim=embedding.shape[1],
                        input_length=max_ques_len,
                        weights=[embedding], trainable=False)(input_q)
    
    conv_q = Conv1D(filters=no_conv_filters, kernel_size=5, strides=1, padding='same',
                    kernel_initializer='glorot_normal',
                    activation='relu',
                    kernel_regularizer=regularizers.l2(1e-3),
                    name='ques_conv')(embed_q)
   
    pool_q = GlobalMaxPooling1D(name='ques_pool')(conv_q)

    # Answer Layers
    input_a = Input(shape=(max_ans_len,))
    
    embed_a = Embedding(input_dim=embedding.shape[0], output_dim=embedding.shape[1],
                        input_length=max_ans_len,
                        weights=[embedding], trainable=False)(input_a)
    conv_a = Conv1D(filters=no_conv_filters, kernel_size=5, strides=1, padding='same',
                    kernel_initializer='glorot_normal',
                    activation='relu',
                    kernel_regularizer=regularizers.l2(1e-3))(embed_a) 
    pool_a = GlobalMaxPooling1D()(conv_a)

    # matrix M (similarity layer)
    x_a = Dense(no_conv_filters, use_bias=False, 
                kernel_initializer='glorot_normal',
                kernel_regularizer=regularizers.l2(1e-2))(pool_a)
    sim = Dot(axes=-1)([pool_q, x_a])

    # Additional features input
    input_addn_feat = Input(shape=(addit_feat_len, ), name='input_addn_feat')
    
    # Combine Question, Similarity score, Answer pooled outputs and additional input features
    join_layer = keras.layers.concatenate([pool_q, sim, pool_a,
                                            input_addn_feat])

    hidden_units = no_conv_filters + 1 + no_conv_filters + addit_feat_len
    hidden_layer = Dense(hidden_units,
                         kernel_initializer='glorot_normal',
                         kernel_regularizer=regularizers.l2(1e-1),
                         activation = 'relu')(join_layer)
    hidden_layer = Dropout(dropout_rate)(hidden_layer)

    # Final output layer
    softmax = Dense(1, activation = 'sigmoid')(hidden_layer)

    # Input to pass control propensity weights into the loss function
    input_weights = Input(shape=(1, ), name = 'input_weights')
    
    model = Model(inputs=[input_q, input_a, input_addn_feat, input_weights], outputs=softmax)
    print(model.summary())

    adam = optimizers.Adam(lr = 0.00001, beta_2=0.99999)    
    model.compile(optimizer=adam,
                  loss=counterfactual_risk_loss(input_weights))

    return model
