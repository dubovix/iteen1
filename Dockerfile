  mailpit:
    container_name: iteen1.mailpit
    environment:
      MP_SMTP_AUTH_ALLOW_INSECURE: "1"  # require EMAIL_USE_TLS=False
      MP_SMTP_AUTH: "${EMAIL_HOST_USER}:${EMAIL_HOST_PASSWORD}"
      MP_UI_AUTH: "${EMAIL_HOST_USER}:${EMAIL_HOST_PASSWORD}"
    healthcheck:
      interval: 60s
      retries: 4
      start_period: 30s
      test: [ "CMD-SHELL", 'wget -q -S -T 4 -O - --header "Authorization: Basic $(echo -n "${EMAIL_HOST_USER}:${EMAIL_HOST_PASSWORD}" | base64 -w 0)" http://localhost:8025/api/v1/info 2>&1 | grep -q "Uptime"' ]
      timeout: 5s
    hostname: mailpit
    image: axllent/mailpit:v1.15
    networks:
      - back_net
    ports:
      - "127.0.0.1:1025:1025"  # SMTP
      - "127.0.0.1:8025:8025"  # WEB UI