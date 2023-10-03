spark-submit --master yarn --deploy-mode cluster \
--py-files spapp_lib.zip \
--files conf/spapp.conf,conf/spark.conf,log4j.properties \
spapp_main.py qa 2023-09-28