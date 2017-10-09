FROM busybox:latest
COPY echo.sh /echo.sh
RUN chmod +x /echo.sh
ENTRYPOINT ["/echo.sh"]
CMD ["echo:v0.1"]
