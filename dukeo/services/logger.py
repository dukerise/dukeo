# dukeo/services/logger.py
import structlog
import logging

# 1. Configuriamo lo “stream” di logging (JSON per Prometheus / ELK)
structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer(),
    ]
)

# 2. E’ l’oggetto che i moduli importeranno
log = structlog.get_logger()

# 3. Evitiamo che Uvicorn stampi log inutili sullo standard output
logging.getLogger("uvicorn.access").handlers = []

