# Alert Metrics

## Dataflow
### dataflow_job
```current_num_vcpus``` GAUGE INT64 - La cantidad de CPU virtuales que usa actualmente este trabajo de Dataflow. Esta es la cantidad actual de trabajadores multiplicada por la cantidad de CPU virtuales por trabajador.<br>
```system_lag``` GAUGE INT64 - La duración máxima actual que un dato ha estado procesando o esperando ser procesado, en segundos.<br>
```disk_space_capacity``` GAUGE INT64 - La cantidad de disco persistente que se asigna actualmente a todos los trabajadores asociados con este trabajo de Dataflow.
<br>
```memory_capacity``` GAUGE INT64 - La cantidad de memoria que se asigna actualmente a todos los trabajadores asociados con este trabajo de Dataflow.
<br>
```per_stage_system_lag``` GAUGE INT64 - La duración máxima actual que un elemento de datos ha estado procesando o esperando procesarse en segundos, por etapa de canalización.
<br>

## Pub/Sub
### pubsub_subscription

### pubsub_topic
