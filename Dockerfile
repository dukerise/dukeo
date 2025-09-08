# Builder
FROM python:3.12-alpine AS builder
WORKDIR /app
RUN apk add --no-cache git
COPY pyproject.toml README.md .
RUN pip install poetry && \
    poetry export -f requirements.txt --output requirements.txt --without-hashes

# Runtime
FROM python:3.12-alpine
WORKDIR /app
RUN adduser -S dukeo
COPY --from=builder /app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . ./
RUN chown -R dukeo:dukeo /app
USER dukeo
CMD ["python", "-m", "dukeo.main"]
EXPOSE 8000

