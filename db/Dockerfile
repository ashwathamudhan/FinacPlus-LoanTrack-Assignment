
FROM postgres:16-alpine

COPY migrations/*.sql /docker-entrypoint-initdb.d/

COPY seed.sql /docker-entrypoint-initdb.d/999_seed.sql

EXPOSE 5432

HEALTHCHECK --interval=10s --timeout=5s --start-period=30s --retries=5 \
    CMD pg_isready -h 127.0.0.1 -U "$POSTGRES_USER" -d "$POSTGRES_DB" || exit 1
