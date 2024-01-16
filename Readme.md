# Fastapi boilerplate

### Before start

1. Rename .env.example to .env
2. Run

```
npm install -g yarn
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

### Migration

```
alembic revision --autogenerate -m "init"
alembic upgrade head
```

### Seeder User For Login
```
py database\seeder.py
```

### Rollback Migration

```
alembic downgrade base

```

### Run Application Production

```
uvicorn main:app --port 5000

```

### Unit Test

```
pytest tests -v

```
