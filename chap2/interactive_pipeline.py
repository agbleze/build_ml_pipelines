

import tensorflow as tf
from tfx.orchestration.experimental.interactive.interactive_context import InteractiveContext
from tfx.components import StatisticsGen
#%%
context = InteractiveContext()

statistics_gen = StatisticsGen(examples=example_gen.output['examples'])
context.run(statistics_gen)

# inspect features of dataset
context.show(statistics_gen.outputs['statistics'])

# show artifacts
for artifact in statistics_gen.outputs['statistics'].get():
    print(artifact.uri)


# basic apache beam data pipeline
import apache_beam as beam

with beam.Pipeline() as p:
    lines = p | beam.io.ReadFromText(input_file)
    


