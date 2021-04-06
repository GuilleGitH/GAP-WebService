from data_transformers.trasformer_for_format import trasformer
from data_transformers.mariana_transformer import mariana_trasformer
from data_transformers.serviverde_transformer import serviverde_trasformer

trans = trasformer()

mariana_trans = mariana_trasformer()
trans.tranformer_templete('data/mariana_merge.csv', 'data/procesado_mariana.csv', mariana_trans)

serviverde_trans = serviverde_trasformer()
trans.tranformer_templete('data/serviverde_merge.csv', 'data/procesado_serviverde.csv', serviverde_trans)

trans.merge_two_csv('data/procesado_mariana.csv', 'data/procesado_serviverde.csv', 'data/final_data.csv')