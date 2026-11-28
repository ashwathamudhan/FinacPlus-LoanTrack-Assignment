# Stage 1: Prepare database initialization scripts
FROM postgres:16-alpine AS builder

WORKDIR /build

COPY migrations/*.sql ./migrations/
COPY seed.sql ./999_seed.sql


# Stage 2: PostgreSQL runtime
FROM postgres:16-alpine AS runtime

COPY --from=builder --chown=postgres:postgres \
    /build/migrations/ /docker-entrypoint-initdb.d/

COPY --from=builder --chown=postgres:postgres \
    /build/999_seed.sql /docker-entrypoint-initdb.d/999_seed.sql

USER postgres

EXPOSE 5432

HEALTHCHECK --interval=10s --timeout=5s --start-period=30s --retries=5 \
    CMD pg_isready -h 127.0.0.1 -U "$POSTGRES_USER" -d "$POSTGRES_DB" || exit 1