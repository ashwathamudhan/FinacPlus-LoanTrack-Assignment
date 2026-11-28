# Stage 1: Prepare frontend files
FROM nginx:1.28-alpine AS builder

WORKDIR /build

COPY index.html style.css script.js ./


# Stage 2: Nginx runtime
FROM nginx:1.28-alpine AS runtime

COPY --from=builder /build/ /usr/share/nginx/html/

COPY nginx.conf /etc/nginx/conf.d/default.conf

RUN sed -i '/^user /d' /etc/nginx/nginx.conf && \
    sed -i 's|^[[:space:]]*pid[[:space:]].*;|pid /tmp/nginx.pid;|' /etc/nginx/nginx.conf && \
    chown -R nginx:nginx /var/cache/nginx /usr/share/nginx/html

USER nginx

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD wget -q -O /dev/null http://127.0.0.1:8080/healthz || exit 1

CMD ["nginx", "-g", "daemon off;"]