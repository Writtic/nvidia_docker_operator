nvidia_docker_operator
======================
Custom operator and hook for `nvidia-docker` on `Airflow 1.9.0`.

Requirement
-----------

```
pip install docker
```

> Warning: DO NOT INSTALL `apache-airflow[docker]` which install `docker-py 1.10.6` package. This operator and hook based on `docker 2.7.0` package. (a.k.a docker sdk for python)

