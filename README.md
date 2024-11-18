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
```bash
  docker-compose up
```
#### 2. Local 
  ```bash
    python3 -m venv venv 
  ```
  ```bash
    source venv/bin/activate 
  ```
  ```bash
    pip install -r src/rquirements.txt
  ```
  ```bash
    cd src/
  ```
  ```bash
    uvicorn app:app --reload
  ```

#### http://localhost/docs

---
### Run tests 
```bash
  python3 -m venv venv 
```
```bash
  source venv/bin/activate 
```
```bash
  pip install -r src/rquirements.txt
```

```bash
  pytest -vv
```

Для изменения тестового набора данных обновить data / InitTestData: [`customer_test_data`, `trafic_test_data`].

---

