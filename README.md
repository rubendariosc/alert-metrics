# Alert Metrics

## Dataflow
### dataflow_job
```current_num_vcpus``` **GAUGE** INT64<br>
La cantidad de CPU virtuales que usa actualmente este trabajo de Dataflow. Esta es la cantidad actual de trabajadores multiplicada por la cantidad de CPU virtuales por trabajador.
<br><br>
```system_lag``` **GAUGE** INT64<br>
La duración máxima actual que un dato ha estado procesando o esperando ser procesado, en segundos.
<br><br>
```disk_space_capacity``` **GAUGE** INT64<br>
La cantidad de disco persistente que se asigna actualmente a todos los trabajadores asociados con este trabajo de Dataflow.
<br><br>
```memory_capacity``` **GAUGE** INT64<br>
La cantidad de memoria que se asigna actualmente a todos los trabajadores asociados con este trabajo de Dataflow.
<br><br>
```per_stage_system_lag``` **GAUGE** INT64 - La duración máxima actual que un elemento de datos ha estado procesando o esperando procesarse en segundos, por etapa de canalización.
<br><br>

## Pub/Sub
### pubsub_subscription
```num_undelivered_messages``` **GAUGE** INT64<br>
Número de mensajes no reconocidos (también conocidos como mensajes atrasados) en una suscripción.
<br><br>
```num_outstanding_messages``` **GAUGE** INT64<br>
Número de mensajes entregados al punto final de envío de una suscripción, pero aún no reconocidos.
<br><br>
```send_messages_count``` **DELTA** INT64<br>
Recuento acumulado de mensajes enviados por Cloud Pub / Sub a los clientes suscriptores, agrupados por tipo de entrega.
<br><br>

### pubsub_topic
```num_unacked_messages_by_region``` **GAUGE** INT64<br>
Número de mensajes no reconocidos en un tema, desglosados ​​por región de la nube.
<br><br>
```byte_cost``` **DELTA** INT64<br>
Costo de operaciones, medido en bytes. Se utiliza para medir la utilización de las cuotas.
<br><br>
```send_message_operation_count``` **DELTA** INT64<br>
Recuento acumulado de operaciones de publicación de mensajes, agrupadas por resultado. Para obtener una definición de las operaciones de mensajes, consulte la suscripción a la métrica de Cloud Pub / Sub / mod_ack_deadline_message_operation_count.
<br><br>

## BigQuery
### bigquery_dataset
```uploaded_bytes``` **DELTA** INT64<br>
Bytes cargados
<br><br>

### bigquery_project