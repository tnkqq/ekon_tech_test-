# ekon_tech_test-
## Тестовое задание для "ЭКОН Технологии"

---
### Start API
#### 1. With docker
```
  docker-compose up
```
#### 2. Local 
  ```
    pip install -r src/rquirements.txt
  ```
  ```
    cd src/
  ```
  ```
    uvicorn app:app --reload
  ```
---
### Run tests 

```
  pip install -r src/rquirements.txt
```

```
  pytest -vv
```

Для изменения тестового набора данных обновить data / InitTestData: [`customer_test_data`, `trafic_test_data`].

---

