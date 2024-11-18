# ekon_tech_test-
## Тестовое задание для "ЭКОН Технологии"

#### *GET* trafic/ -> sum(trafic)
```
  - customer
  - after
  - before
  - ip
  ```
  
#### *POST* trafic/ -> trafic schemas
  ```
  - customer_id *
  - ip *
  - date
  ```


#### *GET* customers/ -> [customers]


#### *POST* customers/ -> id
```
  - name *
```

---
### Start API
#### 1. With docker
```
  docker-compose up
```
#### 2. Local 
  ```
    python3 -m venv venv 
  ```
  ```
    source venv/bin/activate 
  ```
  ```
    pip install -r src/rquirements.txt
  ```
  ```
    cd src/
  ```
  ```
    uvicorn app:app --reload
  ```

#### http://localhost/docs

---
### Run tests 
```
  python3 -m venv venv 
```
```
  source venv/bin/activate 
```
```
  pip install -r src/rquirements.txt
```

```
  pytest -vv
```

Для изменения тестового набора данных обновить data / InitTestData: [`customer_test_data`, `trafic_test_data`].

---

