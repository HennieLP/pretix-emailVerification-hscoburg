FROM --platform=linux/amd64 pretix/standalone:stable

USER root
COPY pretix-emailChecker /pretix-emailChecker
RUN chown -R pretixuser:pretixuser /pretix-emailChecker && \
    sudo -u pretixuser pip3 install /pretix-emailChecker

USER pretixuser
