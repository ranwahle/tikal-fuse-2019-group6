#!/usr/bin/env bash
celery -A experiments worker --loglevel=info
