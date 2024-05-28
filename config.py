mail = Mailpit(
    email_port=env.str("EMAIL_PORT"),
    email_host=env.str("EMAIL_HOST"),
    email_use_tls=env.str("EMAIL_USE_TLS"),
    email_host_user=env.str("EMAIL_HOST_USER"),
    email_host_password=env.str("EMAIL_HOST_PASSWORD"),
    default_from_email=env.str("DEFAULT_FROM_EMAIL"),
),
)