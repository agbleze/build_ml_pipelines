
#%%
import tensorflow as tf
import string

with tf.io.TFRecordWriter("test.tfrecord") as w:
    w.write(b"Firts record")
    w.write(b"Second record")
    
for record in tf.data.TFRecordDataset("test.tfrecord"):
    print(record)

#%%    
tf.Tensor(b'Frist record', shape=(), dtype=string)
tf.Tensor(b'Second record', shape=(), dtype=string)


#%%  ingestng local data files
import os 
from tfx.components import CsvExampleGen
from tfx.orchestration.experimental.interactive.interactive_context import InteractiveContext


#%%
base_dir = os.getcwd()
data_dir = ""
#os.pardir
#examples = external_input()
example_gen = CsvExampleGen(input_base=data_dir)
context = InteractiveContext()
context.run(example_gen)

